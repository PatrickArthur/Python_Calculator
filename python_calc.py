#Calculator in Python#

import math
print(" Weclome to Patrick Arthur's Calculator: V1")
print("     A) Add")
print("     B) Sub")
print("     C) Mul")
print("     D) Div")
choice = raw_input("Pick your choice: ")
if choice == "A":
   print("add numbers!")
   x= input("First Number: ")
   y= input("Second Number: ")
   print("Your answer is: "+str(x+y))
   raw_input("Press <ENTER> to exit")
if choice == "B":
    print("subtract numbers!")
    x= input("First Number: ")
    y= input("Second Number: ")
    print("Your answer is: "+str(x-y))
    raw_input("Press <ENTER> to exit")
if choice == "C":
    print("multiply numbers!")
    x= input("First Number: ")
    y= input("Second Number: ")
    print("Your answer is: "+str(x*y))
    raw_input("Press <ENTER> to exit")
if choice == "D":
    print("divide numbers!")
    x= input("First Number: ")
    y= input("Second Number: ")
    print("Your answer is: "+str(x/y))
    raw_input("Press <ENTER> to exit")
