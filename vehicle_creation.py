import mysql.connector
import random as r
import vehicle
from database_client import DatabaseClient
from vehicle import Vehicle
#from lane import Lane
from read_text import open_file
#import g
db = DatabaseClient()
class VehicleCreation:
    
    def __init__(self):
        self.models = open_file("models.txt")
        self.colors = open_file("colors.txt")
    #def add_vehicle(vehicle=vehicle, vehicles=[]):
        #vehicles.append(vehicle)
    
    def create_vehicles(self):
        """ models = []
        colors = []
        vehicles = []
        models = open_file("models.txt")
        colors = open_file("colors.txt") """
        for i in range(0, 1000):
            v = Vehicle(Vehicle.random_model(self.models), Vehicle.random_license_plate(), Vehicle.random_color(self.colors), Vehicle.max_speed())
            print(f"Count {i} : {v.get_vehicle_model()} {v.get_vehicle_license_plate()} {v.get_color()}")
            try:
                db.insert_vehicle_table(v)
            except mysql.connector.Error as err:
                print("An exception occured: {}".format(err))

    #lane_1 = Lane()
    #lane_2 = Lane()
    #lane_3 = Lane()
    #lanes = [lane_1, lane_2, lane_3]

    #for lane, vehicle in zip(lanes, vehicles):
        #lane.enqueue(vehicle.get_vehicle_model())

    #for lane in lanes:
        #lane.display()
        #print(lane.size())
    #g.main(vehicles)