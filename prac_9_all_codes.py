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

#Question 6: Function for List Processing
def process_list(lst):
    print("Sum =", sum(lst))
    print("Largest=", max(lst))

list1 = [10,20,30]
list2 = [5,15,25,35]

process_list(list1)
process_list(list2)

#Question 7: Recursive Function - Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

num = 5
print("Factorial =", factorial(num))
#Loop-Based Approach
fact = 1
for i in range(1,6):
    fact *= i

print("Factorial =", fact)


    
