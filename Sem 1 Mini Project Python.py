import mysql.connector
import random

conn = mysql.connector.connect(
    host='localhost',
    username='root',
    password='sql123',
    database='aarush_events'
)

my_cursor = conn.cursor()

print("\n********************WELCOME TO AARUSH EVENTS PAGE***********************")

acc = input("\nDO YOU HAVE AN ACCOUNT WITH AARUSH (Y/N)")
em = []

if acc.lower() in ['y', 'yes']:
    email = input("\nENTER YOUR EMAIL ID:-")
    em.append(email)
    password = input("\nENTER YOUR PASSWORD:-")
    phone_number = int(input("\nENTER YOUR PHONE NUMBER:-"))
    otp = int(input("\nENTER OTP SENT TO YOUR PHONE AND EMAIL:-"))
   
    print("\n-------LOGIN SUCCESSFUL-------")

else:
    print("\n-------LET US CREATE YOUR AARUSH ACCOUNT-------")
    full_name = input("\nENTER YOUR FULL NAME:-")
    phone_number = int(input("\nENTER YOUR PHONE NUMBER:-"))
    city = input("\nENTER YOUR CITY NAME:-")
    state = input("\nENTER YOUR STATE:-")
    email = input("\nENTER YOUR EMAIL ID:-")
    em.append(email)
    password = input("\nENTER YOUR PASSWORD:-")
    print(f"\nOTP SENT TO YOUR PHONE AND EMAIL")
    otp = int(input("\nENTER THE OTP NO:-"))
    
    print("\n-------YOUR ACCOUNT IS CREATED SUCCESSFULLY-------")

print("\nTHESE ARE THE LATEST EVENTS----")
query1 = "SELECT events FROM events"
my_cursor.execute(query1)
for event in my_cursor:
    print(event)

names = []
selected_event = input("\nWHICH EVENT DO YOU WANT THE TICKET FOR:-")
num_tickets = int(input("\nENTER NUMBER OF TICKETS YOU WANT:-"))

for _ in range(num_tickets):
    attendee_name = input("\nENTER NAME:-")
    names.append(attendee_name)

venues, dates, timings, charges = [], [], [], []

query2 = "SELECT venue FROM events WHERE events = '{}'".format(selected_event)
my_cursor.execute(query2)
for venue in my_cursor:
    venues.append(venue)

query3 = "SELECT date FROM events WHERE events = '{}'".format(selected_event)
my_cursor.execute(query3)
for date in my_cursor:
    dates.append(date)

query4 = "SELECT timing FROM events WHERE events = '{}'".format(selected_event)
my_cursor.execute(query4)
for timing in my_cursor:
    timings.append(timing)

query5 = "SELECT charges*{} FROM events WHERE events = '{}'".format(num_tickets, selected_event)
my_cursor.execute(query5)
for charge in my_cursor:
    charges.append(charge)

seat_num = random.randint(1, 100)

print(f"YOU HAVE TO PAY {charges} RUPEES")
payment = input("TO PAY, ENTER (P):-")

print("\nYOUR TICKET IS HERE - ")

if num_tickets == 1:
    print(f"\nName = {names}          Event Name = {selected_event}      Venue = {venues}")
    print(f"Timing = {timings}        Date = {dates}             Charges = {charges}      ")
    print(f"Seat Number = {seat_num}")
    print(f"Your ticket has been sent to your email {em}")

if num_tickets > 1:
    print(f"\nName = {names}          Event Name = {selected_event}      Venue = {venues}")
    print(f"Timing = {timings}        Date = {dates}             Charges = {charges}      ")
    print(f"Seat Numbers = {seat_num} to {seat_num + (num_tickets - 1)}")
    print(f"Your ticket has been sent to your email {em}")

conn.close()
