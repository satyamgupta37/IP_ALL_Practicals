try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    print(a / b)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid numbers.")

except TypeError:
    print("Error: Invalid data type.")

except Exception:
    print("Something went wrong.")
    
    
