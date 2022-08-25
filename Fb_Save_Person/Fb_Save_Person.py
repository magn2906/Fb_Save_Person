import pyrebase
from tkinter import *
from dotenv import load_dotenv
import os

load_dotenv()


# Firebase 'login' information
config = {
  "apiKey" : os.getenv("apiKey"),
  "authDomain" : os.getenv("authDomain"),
  "databaseURL": os.getenv("databaseURL"),
  "projectId" : os.getenv("projectId"),
  "storageBucket" : os.getenv("storageBucket"),
  "messagingSenderId" : os.getenv("messagingSenderId"),
  "appId" : os.getenv("appId"),
  "measurementId" : os.getenv("measurementId")
}


# Firebase and realtime db initialization
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Creating instance of a tkinter window
MainWindow = Tk()

# Methods / functions
def submit(name, age, occupation):
    data = {
        "Full Name": name, 
        "Age": age, 
        "Occupation": occupation
        }
    # Enter the submitted data to the database
    db.child("root").push(data)

    # Clear submition boxes
    tbx_Name.delete(0, END)
    tbx_Age.delete(0, END)
    tbx_Occupation.delete(0, END)
    
    # Update the status
    lbl_Status.configure(text="Status: " + name + " submitted")



# Creating elements
lbl_Name = Label(MainWindow, text="Name: ")
lbl_Age = Label(MainWindow, text="Age: ")
lbl_Occupation = Label(MainWindow, text="Occupation: ")

tbx_Name = Entry(MainWindow)
tbx_Age = Entry(MainWindow)
tbx_Occupation = Entry(MainWindow)

btn_Submit = Button(MainWindow, text="Submit", command=lambda: submit(tbx_Name.get(), tbx_Age.get(), tbx_Occupation.get()))

lbl_Status = Label(MainWindow, text="Status: ")


# Putting elements on grid
lbl_Name.grid(row=0, column=0, pady=5)
lbl_Age.grid(row=1, column=0, pady=5)
lbl_Occupation.grid(row=2, column=0, pady=5)

tbx_Name.grid(row=0, column=1, columnspan=2, pady=5)
tbx_Age.grid(row=1, column=1, columnspan=2, pady=5)
tbx_Occupation.grid(row=2, column=1, columnspan=2, pady=5)

btn_Submit.grid(row=4, column=1, pady=5)

lbl_Status.grid(row=5, column=0, columnspan=3, pady=5)


# looping the window
MainWindow.mainloop()

