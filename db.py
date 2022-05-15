import mysql.connector 


def connect():
    
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="face_recognition_db"
    )  
    
   # print(mydb)
    return mydb
def getactive_class():
    mydb = connect()
    cursor = mydb.cursor()
    select_class_query = "SELECT * FROM class_tb WHERE Class_Status = 1"
    cursor.execute(select_class_query)
    classdatas = cursor.fetchall()
    return classdatas[0][0]


def check_duplicate_attendance(regno,session,semester):
    mydb = connect()
    cursor = mydb.cursor()
    select_attendance_query = "SELECT * FROM attendance_tb WHERE RegNo LIKE %s AND Ses = %s AND Sem = %s"
    att_val= [regno,session,semester]
    cursor.execute(select_attendance_query,att_val)
    r = cursor.fetchall()
    #print(r)
    att_row = cursor.rowcount
   # print(att_row)
    return cursor.rowcount


def get_stud_details(regno):
   # print(regno)
    mydb = connect()
    cursor = mydb.cursor()
    select_stud_query = "SELECT * FROM students_tb WHERE RegNo LIKE %s"
    vals= [regno]
    #print(select_stud_query)
    cursor.execute(select_stud_query,vals)
    stud_datas = cursor.fetchall()
    return stud_datas
        
def insert(reg,ses,sem):
    mydb = connect()
    import datetime
    current_time = datetime.datetime.now()
    classid = getactive_class()
    num = check_duplicate_attendance(reg,ses,sem)
    #print(num)
    if num > 0:
        print("Attendance Already taken!")
    else:
        print("insert new data")
        create_attendance_query = "INSERT INTO attendance_tb (id,RegNo,Class_id,logged_date,Ses,Sem) VALUES (%s, %s,%s,%s, %s, %s)";
        val = ("", reg,classid,current_time, ses, sem)
        #print(create_attendance_query)
        cursor = mydb.cursor()
        cursor.execute(create_attendance_query,val)
        mydb.commit()
        print("Attendance Taken Successfully!!")


# regno = 'AK19_PHS_MSC_001'      
# session = 11
# semester = 1
# num = check_duplicate_attendance(regno,session,semester)
# #print(num)
# if num > 0:
#     print("Attendance Already taken!")
# else:
#     print("insert new data")