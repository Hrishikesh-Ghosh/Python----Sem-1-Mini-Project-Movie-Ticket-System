import mysql.connector
import random

conn = mysql.connector.connect(host='localhost', username='root',password='sql123', database='carnival_cinima')
my_cursor = conn.cursor()

print("\n********************WELCOME TO CARNIVAL TICKET SYSTEM***********************")

acc = input("\nDO YOU HAVE A ACCOUNT (Y/N)")
em = []
if acc=='y' or acc=='yes' or acc=='Y' or acc=='YES':
    email = input("\nENTER YOUR EMAIL ID:-")
    em.append(email)
    pas = input("\nENTER YOUR PASSWORD:-")
    otp = int(input("\nENTER A OTP CODE ON YOUR EMAIL AND PHONE NO:-"))
   
    print("\n-------LOGIN SUCCESSFUL-------")

else:
    nam = input("\nENTER YOUR FULL NAME:-")
    pn = int(input("\nENTER YOUR PHONE NO:-"))
    city = input("\nENTER YOUR CITY NAME:-")
    state = input("\nENTER YOUR STATE:-")
    em = input("\nENTER YOUR EMAIL ID:-")
    e.append(em)
    passw = input("\nENTER YOUR PASSWORD:-")
    print(f"\nOTP SEND TO {pn} AND {em}")
    ot = int(input("\nENTER THE OTP NO:-"))
    
    print("\n-------YOUR ACCOUNT IS CREATED SUCCESSFULLY-------")
print("\n THESE ARE THE LATEST MOVIES----")
query1 = "select movies from movies"
my_cursor.execute(query1)
for a in my_cursor:
    print(a)

name = []
mname = input("\n WHICH MOVIE YOU WANT TO WATCH :-")
tik = int(input("\n ENTER NUMBER OF TICKETS YOU WANT :-"))
for b in range(tik):
    nam = input("\nENTER NAME :-")
    name.append(nam)

hall = []
date = []
timing = []
charges = []
query2 = "select hall from movies where movies = '{}' ".format(mname)
my_cursor.execute(query2)
for c in my_cursor:
    hall.append(c)

query3 = "select date from movies where movies = '{}'".format(mname)
my_cursor.execute(query3)
for d in my_cursor:
    date.append(d)

query4  = "select timing from movies where movies = '{}'".format(mname)
my_cursor.execute(query4)
for e in my_cursor:
    timing.append(e)

query5 = "select charges*{} from movies where movies = '{}'".format(tik, mname)
my_cursor.execute(query5)
for f in my_cursor:
    charges.append(f)

seatnum = random.randint(1, 100)


print(f"YOU HAVE TO PAY {charges} RUPEES")
pay = input("TO PAY ENTER (P) :-")

print("\nyour ticket is here - ")

if tik==1:
    print(f"\nNAME = {name}          MOVIE NAME = {mname}      HALL = {hall}")
    print(f"TIMING = {timing}      DATE = {date}             CHARGES = {charges}      ")
    print(f"seat number = {seatnum}")
    print(f"your ticket has been send to your email {em}")

if tik>1:
    print(f"\nNAME = {name}          MOVIE NAME = {mname}      HALL = {hall}")
    print(f"TIMING = {timing}      DATE = {date}             CHARGES = {charges}      ")
    print(f"seat number = {seatnum} to {seatnum+(tik-1)}")
    print(f"your ticket has been send to your email {em}")



conn.close()
    





    