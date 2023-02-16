import mysql.connector as connector
import json, os, re

from mysqlx import Session
from vehicle import Vehicle

if os.path.exists("config.json"):
    with open("config.json", "r") as f:
        configData = json.load(f)
else:
    configTemplate = {"host":"", "user":"", "password":"", "database":"",} #If the config file does not exist, it will be created allowing custom values to be passed through.
    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f)
    with open("config.json", "r") as f:
        configData = json.load(f)

#session = Session(config)

try:
    mydb = connector.connect( 
        host=configData["host"],
        user=configData["user"],
        password=configData["password"],
        database=configData["database"],
        )
except connector.Error as err:
    print("Something went wrong: {}".format(err))
    match err.errno:
        case 1045:  print("Check that your login info is correct")
        case 1049:  print("Check that your database name is correct")
        case 2005:  print("Check that your host name is correct")

#def connection():
    
#def create_db():

class DatabaseClient():

    def insert_vehicle_table(self, v=Vehicle): #Insert a vehicle into the table
        mycursor = mydb.cursor()
        sql = "INSERT INTO vehicles (model, license_plate, color, max_speed) VALUES (%s, %s, %s, %s)"
        val = (v.get_vehicle_model(), v.get_vehicle_license_plate(), v.get_color(), v.get_vehicle_max_speed())
        mycursor.execute(sql, val)
        mydb.commit()

    def truncate_vehicle_table(self): #Truncates the table of all vehicles
        mycursor = mydb.cursor()
        sql = "TRUNCATE TABLE vehicles"
        mycursor.execute(sql)
        mydb.commit()
        pass
    
    def lookup_vehicle_table(self, **kwargs):
        mycursor = mydb.cursor()
        model = kwargs.get('model')
        color = kwargs.get('color')
        sql = "SELECT * FROM vehicles WHERE model = %s AND color = %s"
        print(sql)
        tuple1 = (model, color)
        mycursor.execute(sql, tuple1)
        text = mycursor.fetchall()
        
        #print(session.exec(sql).fetchall())
        return text
        