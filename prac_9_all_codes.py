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

#Question 4: Default and Keyword Arguments
def student(name, age=18):
    print("Name:",name)
    print("Age:",age)
student("Rahul")
student(age=20, name="Priya")

#Question 5: Bulit-in Functions Exploration
numbers = [10,20,30,40,50]
text = "Python"
print("Length of list:", len(numbers))
print("Length of string:", len(text))
print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
total=0
for n in numbers:
    total +=n
print("Minimum Sum:", total)

    
