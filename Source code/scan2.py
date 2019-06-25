from pymongo import MongoClient
import scan_modified as sm
import password_gui as pw
import serial
client= MongoClient('localhost:27017')
db= client.data
from Tkinter import *
root = Tk()
root.attributes('-fullscreen',True)
def quite():
     root.destroy()

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
     except Exception, e:
          print str(e)

def disp():
     try:
          itemdata= db.data.find()
          for i in itemdata:
               print(i)
     except Exception, e:
          print str(e)

def read():
     try:
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
     except Exception, e:
          print str(e)

def delete():
     try:
          criteria = input('\n Enter item barcode to delete\n')
          db.data.delete_many({"barcode":criteria})
          print ('\nDeletion successful\n')
     except Exception, e:
          print str(e)

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
     except Exception, e:
          print str(e)
     
def send_data(pincode):  
     if pincode == "110035" :
          ser.write('a'.encode())
          print('A')
     if pincode == "600002" :
          ser.write('b'.encode())
          print('B')
     if pincode == "400099" :
          ser.write('c'.encode())
          print('C')
     if pincode == "382110" :
          ser.write('d'.encode())
          print('D')

def main():

     root.title("") 
     ws = root.winfo_screenwidth() 
     hs = root.winfo_screenheight()
     x = (ws/2) + 20
     y = (hs/2) - (350)
     root.geometry('%dx%d+%d+%d' % (20, 350, x, y))
     root.configure(background = 'RoyalBlue4')
     root.geometry('500x500')
     #logo=tk.PhotoImage(file="insert.png")
     #w1=tk.Label(root,image=logo).pack(side="right")
     label = Label(root, text="Welcome to India Post", font=("Arial Bold", 24), fg = 'White', bg= 'Red')
     label.pack()
     label.place(x=490,y=10)
     Button1 = Button(root, text = '  Insert  ', font = ("Arial Bold", 20), bg = 'grey', fg = 'Blue', command = insert)
     Button1.pack(side="top", fill='none', expand=True, padx=8, pady=8)
     Button1.place(x=180,y=90)
     Button2 = Button(root, text = ' Display ',font = ("Arial Bold", 20), bg = 'grey', fg = 'Blue', command = disp)
     Button2.pack(side="top", expand=True, padx=8, pady=8)
     Button2.place(x=180,y=180)
     Button3 = Button(root, text = '   Read   ', font = ("Arial Bold", 20), bg = 'grey', fg = 'Blue', command = read)
     Button3.pack(side="top", fill='none', expand=True, padx=8, pady=8)
     Button3.place(x=180,y=270)
     Button4 = Button(root, text = '  Delete  ', font = ("Arial Bold", 20), bg = 'grey', fg = 'Blue', command = delete)
     Button4.pack(side="top", fill='none', expand=True, padx=8, pady=8)
     Button4.place(x=180,y=360)
     Button5 = Button(root, text = ' Update ', font = ("Arial Bold", 20), bg = 'grey', fg = 'Blue', command = update)
     Button5.pack(side="top", fill='none', expand=True, padx=8, pady=8)
     Button5.place(x=180,y=450)
     Button6 = Button(root, text = '   Quit   ', font = ("Arial Bold", 20), bg = 'grey', fg = 'Blue', command = quite)
     Button6.pack(side="top", fill='none', expand=True, padx=8, pady=8)
     Button6.place(x=180,y=540)
     root.mainloop()
#ser = serial.Serial('COM14',9600)
directory = "C://Program Files (x86)//ZBar//bin//zbarcam.exe"
print('befor main')
main()

