#1. Opening a File
file = open("sample.txt", "r")
print("File opened successfully")
file.close()

#2. Reading a File
file = open("sample.txt", "r")
data = file.read()
print("File Content:")
print(data)
file.close()

#3. Writing into a File
file = open("sample.txt", "w")
file.write("Hello World\n")
file.write("Welcome to Python Programming")
print("Data written successfully")
file.close()

#4. Appending Data to a File
file = open("sample.txt", "a")
file.write("\nThis is Python File Handling")
print("Data appended successfully")
file.close()
