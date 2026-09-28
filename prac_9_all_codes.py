#Question 1: Defining and Calling User-Defined Functions
def display_message():
    print("Welcome to python Functions!")
display_message()

#Question 2: Functions with Parameters
def add(a ,b):
    print("Sum =", a+b)
add(10,20)
add(5,7)

#Question 3: Functions with Return Values
def square(num):
    return num*num

result = square(5)
print("Square =", result)
print("Square + 10=", result + 10)
    
