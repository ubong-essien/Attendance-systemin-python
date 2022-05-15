#fill a formm to create class
import os

import string    
import random # define the random module  
S = 5  # number of characters in the string.  

def connect():
    import mysql.connector
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="face_recognition_db"
    )  
    return mydb

def insert_class(Class_Name,Class_date,Lecturer_Name, Class_Status, Venue,Class_folder):
    mydb = connect()
    #print("insert class data")
    create_class_query = "INSERT INTO class_tb (id,Class_Name,Class_date,Lecturer_Name,Class_Status,Venue,Class_folder) VALUES (%s, %s,%s,%s, %s, %s,%s)";
    val = ("", Class_Name,Class_date,Lecturer_Name, Class_Status, Venue,Class_folder)
    #print(create_attendance_query)
    cursor = mydb.cursor()
    cursor.execute(create_class_query,val)
    mydb.commit()
#     rowid = cursor.lastrowid
#     return rowid
    

    
    
    
    
# call random.choices() string module to find the string in Uppercase + numeric data.  
ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    



Class_Name = "Seminar In computer Science "
Class_date ="2022-05-11"
Lecturer_Name="Dr Godwin Ansa"
Venue = "Department of Computer Science"
Class_Status = 1




#fetch the active class from the database 




# Directory
created_folder = Class_Name.replace(" ", "_") + Class_date + "_" + ran

 
# Parent Directory path
parent_dir = "C:\\Users\\UBONG\\Desktop\\python\\img\\"
  
# Path
path = os.path.join(parent_dir, created_folder)
 #create directory
os.mkdir(path)
  
isdir = os.path.isdir(path) 
if isdir == True:
    detected_folder = "detected_" + created_folder
    detected_path = os.path.join(path, detected_folder)
    os.mkdir(detected_path)
    
    
#insert data into db
insert_class(Class_Name,Class_date,Lecturer_Name, Class_Status, Venue, created_folder)



print("Class created successfully!")
#after creating the class details locally,uploade to the arduino so tthat it understandss the image path to store captured images.

#from details created in above,create folder to store faces from camera for detection