from graphics import *
from vehicle import Vehicle
import time_counter

def main(vehicles=[]):

    win = GraphWin("Traffic", 1000, 1000)

    #c = Circle(Point(100,100), 10)
    #for i in vehicles:
    #    colors[i] = vehicles[i.get_color()]
    cars = []
    for j in range(0, len(vehicles), 100):
        for i in range(0, len(vehicles), 50): #Each row has the same colored cars
            r = Rectangle(Point(i, j), Point(i+50, j+100))
            cars.append(r)
    #t = Text(r.getP2(), v.get_vehicle_license_plate())
    #t.setSize(8)
            
    #t.draw(win)
            #r.setFill(vehicles[i].get_color())
            #r.draw(win)
    
    for i in range(0, len(cars)):
        cars[i].setFill(vehicles[i].get_color())
        #r.setFill(vehicles[i].get_color())
        cars[i].draw(win)
    #while win.isOpen():
    win.getMouse() # pause for click in window
    #r.draw(time_counter.display_time())

    win.close()
