from lookup import Lookup
from vehicle import *
import mysql.connector
from database_client import DatabaseClient
from vehicle import Vehicle
import customtkinter as ctk, tkinter as tk
from vehicle_creation import VehicleCreation
ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
db = DatabaseClient()

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resizable(False,False)
        self.title("Car Database")
        app = ctk.CTk()  # create CTk window like you do with the Tk window
        self.geometry("240x240")
        self.create_button = ctk.CTkButton(self, text="Create Vehicles", command=self.create_button_function)
        self.create_button.place(relx=0.2, rely=0.2, anchor=tk.NW)

        self.truncate_button = ctk.CTkButton(self, text="Destroy Vehicles", command=self.truncate_button_function)
        self.truncate_button.place(relx=0.2, rely=0.4, anchor=tk.NW)

        self.lookup_button = ctk.CTkButton(self, text="Vehicle Lookup", command=self.lookup_button_function)
        self.lookup_button.place(relx=0.2, rely=0.6, anchor=tk.NW)


    def create_button_function(self):
        v = VehicleCreation()
        v.create_vehicles()
    def truncate_button_function(self):
        db.truncate_vehicle_table()
        #Popup window asking for confirmation along with another window "Table Truncated"
    def lookup_button_function(self): #A window that displays vehicle information based on the property given
        window = Lookup() 
        window.mainloop() #Must disable button so only one lookup window can exist, unless you want to run multiple queries

        # Use CTkButton instead of tkinter Button
    
        

if __name__ == "__main__":
    app = App()
    app.mainloop()