#Question no:1(Drone Battery Report)
def battery_report(battery):
    drop = (battery[0] - battery[-1]) / (len(battery) - 1)
    print("Average battery drop per hour:", drop)

    if drop > 5:
        print("Warning: Battery drop is above 5%")

battery = [92, 88, 84, 79, 73, 68]
battery_report(battery)

#Question no:2(Smart Hospital BMI Service)
def calculate_bmi(weight, height):
    bmi = weight / (height * height)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category

bmi, category = calculate_bmi(72, 1.75)
print("BMI:", round(bmi, 2))
print("Category:", category)

#Question no:3(Recursive Security PIN Sum)
def digit_sum(pin):
    if pin == 0:
        return 0
    return pin % 10 + digit_sum(pin // 10)

print(digit_sum(482931))

#Question no:4(Reusable Bill Function)
def bill_amount(price, discount, gst):
    amount = price - discount
    final_bill = amount + (amount * gst / 100)
    return final_bill

print(bill_amount(2500, 100, 18))

#Question no:5(AI Chat Text Sanitizer)
def sanitize(text):
    text = " ".join(text.split())
    text = text.lower()
    words = text.split()
    unique_words = list(dict.fromkeys(words))
    return " ".join(unique_words)

print(sanitize("Python   Makes   AI Easy"))

#Question no:6
def add(a, b):
    return a + b

print(add(5, 3))

#Question no:7
def greet(name="Student"):
    print("Hello", name)

greet()

#Question no:8(Factorial)
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(4))

#Question no:9
def add(a, b):
    return a + b

#Question no:10
def square(x):
    print(x * x)

square(5)