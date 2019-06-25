from pymongo import MongoClient
import scan_modified as sm
import serial
client= MongoClient('localhost:27017')
db= client.data
from tkinter import *

root = Tk()
root.title("")
root.configure(background = 'grey')
root.geometry('400x400')
label = Label(root, text="Welcome to Indian Post", font=("Arial Bold", 24), fg = 'Red', bg= 'grey')
label.pack()

def insert():
     try:
          barcode = input('Enter barcode: ')
          weight = input('Enter weight of the item: ')
          height = input('enter height: ')
          length = input('enter length: ')
          breadth = input('enter breadth: ')
          pin = input('enter pincode: ')
          db.data.insert_one(
          {
          "barcode":barcode,
          "weight":weight,
          "height":height,
          "length":length,
          "breadth":breadth,
          "pincode":pin
          })
          print ('\n Inserted data successfully\n')
     except Exception(e):
          print(str(e))

def disp():
     try:
          itemdata= db.data.find()
          for i in itemdata:
               print(i)
     except Exception(e):
          print (str(e))

def read():
     try:
          #bar=raw_input('enter the barcode: ')
          bar = sm._return_barcode(directory)
          itemdata = db.data.find({"barcode":bar})
          pincode = db.data.find({"barcode":bar},{"pincode":1})
          #pincode = db.data.find({"pincode: { "barcode":bar }"})
          print ('\nItem Data :\n')
          for i in itemdata:
               print( i)
          for j in pincode:
               pincode = j['pincode']
          send_data(pincode)
     except Exception(e):
          print (str(e))

def delete():
     try:
          criteria = input('\n Enter item barcode to delete\n')
          db.data.delete_many({"barcode":criteria})
          print ('\nDeletion successful\n')
     except Exception(e):
          print (str(e))

def update():
     try:
          criteria = input('\nenter barcode to update\n')
          wt= input('\n Enter weight to update\n')
          db.data.update_one(
               {
               "barcode":criteria},
               {
               "$set":{
               "weight":wt
               }
               }
               )
          print ("\n REcords updated succesfully\n")
     except Exception(e):
          print (str(e))
     
def send_data(pincode):	
     if pincode>"600000" and pincode<"620000" :
          ser.write('a'.encode())
          print('A')
     if pincode>"382000" and pincode<"390000" :
          ser.write('s'.encode())
          print('S')
     if pincode>"100000" and pincode<"120000" :
          ser.write('d'.encode())
          print('D')
     if pincode>"250000" and pincode<"270000" :
          ser.write('f'.encode())
          print('F')

def main():
     Button1 = Button(text = 'Insert', font = ("Arial Bold", 20), bg = 'orange', fg = 'Blue', command = insert)
     Button1.pack(side="top", fill='both', expand=True, padx=4, pady=4)
     Button2 = Button(text = 'Update',font = ("Arial Bold", 20), bg = 'orange', fg = 'Blue', command = disp)
     Button2.pack(side="top", fill='both', expand=True, padx=4, pady=4)
     Button3 = Button(text = 'Read', font = ("Arial Bold", 20), bg = 'orange', fg = 'Blue', command = read)
     Button3.pack(side="top", fill='both', expand=True, padx=4, pady=4)
     Button4 = Button(text = 'Delete', font = ("Arial Bold", 20), bg = 'orange', fg = 'Blue', command = delete)
     Button4.pack(side="top", fill='both', expand=True, padx=4, pady=4)
     Button5 = Button(text = 'Display', font = ("Arial Bold", 20), bg = 'orange', fg = 'Blue', command = update)
     Button5.pack(side="top", fill='both', expand=True, padx=4, pady=4)

#ser = serial.Serial('COM14',9600)
directory = "C://Program Files (x86)//ZBar//bin//zbarcam.exe"

main()


