#Question no:1
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Simple print:")
print(name,age)
print("\n Formatted String:")
print(f"My name is {name} and I am {age} years old.")    

#Question no:2
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("Addition=",num1 + num2)
print("Subtraction=",num1-um2)
print("Multiplication=",num1*num2)
print("Division=",num1/num2)

#Without Type Conversion
a=input("Enter first number: ")
b=input("Enter second number: ")
print("Addition=",a+b)

#Question no:3
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

sum = num1+num2+num3
print("Sum is: ", sum)

avg = sum/3
print("Average is: ", avg)

x = num1+num2
exp = x+num3/2
print("Solution for Equation: ", exp)

#Question no:4

#Expression 1: 10 + 5*2 = 20
"""
    Multiplication has higher Precedence
"""
#Expression 2: (10+5)*2 = 30
"""
    Parenthesis have Highest precedence
"""
#Expression 3: 100/5 + 3*2 = 26
"""
    Multiplication adn Division haev equal precedence
"""

#Question no:5
salary_T = int(input("Enter salary(Basic): "))
salary = float(salary_T)
hra = salary*0.20
da = salary*0.10
total_Sal = salary + hra + da
print(f"{total_Sal} is your Net Salary")

#Question no:6

#Rectangle
rect_l = float(input("Enter Area of Rectangle: "))
rect_b = float(input("Enter Breadth of Rectangle: "))
area_R = rect_b * rect_l
peri_R = rect_l + rect_b
print(f"Area of rectangle is: {area_R}")
print(f"Perimeter of rectangle is: {peri_R}")

#Circle
import math
radius = float(input("Enter Radius of Circle: "))
circum = 2*math.pi*radius
print(f"Curcumference of Circle is: {circum}")

#Question no:7
km = float(input("Enter Distance in km: "))
cel = float(input("Enter Temperature in Celcius: "))
rupee = float(input("Enter Amount in ₹: "))
meters = km*1000;
fahren = (cel*9/5)+32
dollars = rupee*97
print("Meters: ", meters)
print("Temp. in Fahrenheit: ", fahren)
print("Rupee in Dollars: ", round(dollars, 2))

#Question no:8
a,b,c = map(int(input("Enter 3 numbers: "))).split()
print("Sum: ", a+b+c)
print("Product: ", a*b*c)
print(f"Numbers Entered are {a}, {b}, {c}")

#Question no:9

m1 = int(input("Enter marks for Subject 1: "))
m2 = int(input("Enter marks for Subject 2: "))
m3 = int(input("Enter marks for Subject 3: "))
marks = m1+m2+m3
avg = (m1 + m2 + m3)/3
print("P.S. Marks for each subject MUST be LESS THAN OR EQUAL TO 100")
if marks > 300:
    print("Invalid,  Max marks are 300.")
elif marks >= 260:
    print("Grade A")
elif marks >= 260 and marks <= 190:
    print("Grade B")
elif marks >= 190 and marks <= 100:
    print("Grade C")
else:
    print("Grade D")

#Question no:10
try: 
    z = int(input("Enter a number: "))
    v = int(input("Enter a number: "))
except ZeroDivisionError :
    print("ERR: Cannot Divide by 0")
try: 
    f = "10"
    n = 5
    print(f+n)
except TypeError:
    print("ERR: Not a Nummber. Hence no Addition")
    print(int(f)+n)
