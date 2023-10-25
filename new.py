import module1
import math
module1.nameprint("Sam")
findmin = min(1,5,4,100)
findmax = max(1,5,4,100)

print(findmin)
print(findmax)


## Tuples 

sports = ("Basketball", "Football", "Cricket")
print(sports)

## Json 

import json

employeedata = '{"name": "Raad", "category": "Hardware Engineer", "company": "amd", "salary": "1000000$"}'
parsedData = json.loads(employeedata)
print(parsedData)

##ElseIF

import elseif

Dave = 54 
Kartik = 47 

elseif.agediff(Dave,Kartik)

##Typecasting 

a = 2.5897 

print(a)
print(type(a))
print(int(a))
print(type(int(a)))

##The __init__() function 

class studentid :
    def __init__(self, name,roll):
        self.name = name 
        self.roll = roll


s1 = studentid("Raad", 2003042)
print(s1.name)
print(s1.roll)

##Print Random Numbers 

import random

print(random.randrange(1,10000))
print(random.randrange(1,5))

##For loop 

favpersons = ["Rafid", "Shoikat", "Rabby"]

for i in favpersons: 
    print(i)

##Functions 

def counter():
    count = 1 
    count = count +1
    return count


print(counter()) 

##Python del 

def car(): 
        print("Raad is Awesome")

# del car()
car()

##This is all for Python Syntax Introduction. Code once accordingly and you'd be very familier with python language.


