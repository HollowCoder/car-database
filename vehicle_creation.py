import mysql.connector
import random as r
import vehicle, database_client as db
from vehicle import Vehicle
from lane import Lane
from read_text import open_file
#import g
class VehicleCreation:
    models = []
    colors = []
    vehicles = []
    models = open_file("models.txt")
    colors = open_file("colors.txt")

    #def add_vehicle(vehicle=vehicle, vehicles=[]):
        #vehicles.append(vehicle)

    def random_model(models=[]) -> str:
        """Given a list of models, returns a random car model.
        @param models: A list of models"""
        model = models[(r.randint(0, len(models) - 1))]
        return model

    def random_license_plate() -> str: #Implement different license plate standards?
        """Using the given plate standard, returns a license plate using random letters and numbers."""
        candidateChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        plate = "000-0000"
        licensePlate = ["0", "0", "0", "-", "0", "0", "0", "0"]

        for i, v in enumerate(licensePlate):
            if "-" in v:
                continue
            elif i in range(0, 3): #Inclusive to exclusive
                licensePlate[i] = candidateChars[r.randint(0, 25)]
                continue
            elif i in range(4, 8):
                licensePlate[i] = candidateChars[r.randint(26, len(candidateChars) - 1)]
        plate = ''.join(str(e) for e in licensePlate) #Converts lincense plate list to string
        #for av, bv in zip(plate, licensePlate):
        #    av += bv

        return plate

    def random_color(colors=[]) -> str:
        """Using the list of colors, returns a random color.
        @param colors: the list of colors"""
        color = colors[(r.randint(0, len(colors) - 1))]
        return color

    def max_speed(): #Haven't set this up yet
        speed = 0
        return speed

    for i in range(0, 1000):
        v = Vehicle(random_model(models), random_license_plate(), random_color(colors), max_speed())
        vehicles.append(v)
        print(f"Count {i} : {v.get_vehicle_model()} {v.get_vehicle_license_plate()} {v.get_color()}")
        try:
            #db.mydb
            db.vehicle_table(v)
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