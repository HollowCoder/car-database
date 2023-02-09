import mysql.connector as connector
import json, os
from vehicle import Vehicle


if os.path.exists("config.json"):
    with open("config.json", "r") as f:
        configData = json.load(f)

mydb = connector.connect(
    host=configData["host"],
    user=configData["user"],
    password=configData["password"],
    database=configData["database"],
)

#def connection():
    
    

    
    
    

#def create_db():
    

def vehicle_table(v=Vehicle):
    #connection()
    mycursor = mydb.cursor()
    sql = "INSERT INTO vehicles (model, license_plate, color, max_speed) VALUES (%s, %s, %s, %s)"
    val = (v.get_vehicle_model(), v.get_vehicle_license_plate(), v.get_color(), v.get_vehicle_max_speed())
    mycursor.execute(sql, val)
    mydb.commit()
    