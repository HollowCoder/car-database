import customtkinter as ctk, tkinter as tk
from database_client import DatabaseClient

db = DatabaseClient()

from read_text import open_file
models = open_file("models.txt")
colors = open_file("colors.txt")
class Lookup(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resizable(False,False)
        self.title("Lookup Vehicles")
        app = ctk.CTk()  # create CTk window like you do with the Tk window
        self.geometry("500x500")
        self.modelLabel = ctk.CTkLabel(self,text="Model")
        self.modelLabel.place(relx=0.1, rely=0.1, anchor=tk.NW)
        self.modelOptionMenu = ctk.CTkOptionMenu(self, values=models) #values should be a list of models from models.txt
        self.modelOptionMenu.place(relx=0.3, rely=0.1, anchor=tk.NW)
        self.colorLabel = ctk.CTkLabel(self,text="Color")
        self.colorLabel.place(relx=0.1, rely=0.2)
        self.colorOptionMenu = ctk.CTkOptionMenu(self, values=colors)
        self.colorOptionMenu.place(relx=0.3, rely=0.2, anchor=tk.NW)
        self.plateLabel = ctk.CTkLabel(self,text="Plate")
        self.plateLabel.place(relx=0.1, rely=0.3)
        self.plateEntry = ctk.CTkEntry(self, placeholder_text="123-ABCD")
        self.plateEntry.place(relx=0.3, rely=0.3)
        self.generateResultsButton = ctk.CTkButton(self, text="Generate Results", command=self.generateResults)
        self.generateResultsButton.place(relx=0.1, rely=0.4, anchor=tk.NW)
        self.displayBox = ctk.CTkTextbox(self, width=400, height=225)
        self.displayBox.place(relx=0.1, rely=0.5)
        
    def generateResults(self):
        self.displayBox.delete("0.0", "200.0")
        text = self.createText()
        print(text)
        #self.displayBox.insert("1.0", "Model License Plate Color")
        self.displayBox.insert("0.0", text)

    def createText(self):
        # .get() is used to get the value of the checkboxes and entryfields       
        model = self.modelOptionMenu.get()
        color = self.colorOptionMenu.get()
        plate = self.plateEntry.get()
        #text = model + color + plate
        text = db.lookup_vehicle_table(model=model, color=color, plate=plate)
        return text