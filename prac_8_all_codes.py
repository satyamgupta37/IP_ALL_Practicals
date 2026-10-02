#Question no:1
#Create a student dictionary
student={"Name":"Rahul","Age":20,"Marks":85}
print("Student Dictionary:")
print(student)
print("Type:",type(student))
# Access values using keys
print("Name ->",student["Name"])
print("Age ->",student["Age"])
print("Marks ->",student["Marks"])
#Question no:2
#Access dictionary values using keys
student={"Name":"Rahul","Age":20,"Marks":85}
print(student)
print("Name:",student["Name"])
print("Age:",student["Age"])
print("Marks:",student["Marks"])
# Non-existing key gives KeyError
print("City:",student["City"])
#Question no:3
#Access existing keys using get()
student={"Name":"Rahul","Age":20,"Marks":85}
print(student.get("Name"))
print(student.get("Age"))
print(student.get("Marks"))
# get() returns None for a missing key
print(student.get("City"))
# Direct indexing accesses an existing value
print(student["Name"])
#Question no:4
#Create the original dictionary
student={"Name":"Rahul","Age":20,"Marks":85}
print(student)
# Add a new key-value pair
student["City"]="Mumbai"
# Update an existing value
student["Marks"]=90
print(student)
#Question no:5
#Create a student dictionary
student={"Name":"Rahul","Age":18,"Course":"BSc IT"}
# Remove using pop()
student.pop("Age")
print(student)
# Remove using del
del student["Course"]
print(student)
# Handle a missing key safely
try: student.pop("Marks")
except KeyError: print("Key does not exist")
#Question no:6
#Create a dictionary
student={"Name":"Rahul","Age":18,"Course":"BSc IT"}
# Iterate through keys
for key in student:
    print(key)
# Iterate through values
for value in student.values():
    print(value)
# Iterate through key-value pairs
for key,value in student.items():  
    print(key,":",value)
#Question no:7
#Create a dictionary
student={"Name":"Rahul","Age":18,"Course":"BSc IT"}
# Display all keys
print(student.keys())
# Display all values
print(student.values())
# Display all key-value pairs
print(student.items())
#Question no:8
#Count frequency of each character
text=input("Enter a string: ")
frequency={}
for char in text:
    if char in frequency: 
        frequency[char]+=1
    else:
         frequency[char]=1
print(frequency)
#Question no:9
#Create a nested dictionary
students={
    "Student 1": {
        "Name":"Rahul",
        "Age":18,
        "Course":"BSc IT"
    },
    "Student2": {
        "Name":"Amit",
        "Age":19,
        "Course":"BSc IT"
   }
}
# Access nested values
print(students["Student 1"]["Name"])
print(students["Student 2"]["Course"])
# Update a nested value
students["Student 1"]["Age"]=19
print(students["Student 1"])
#Question no:10
#Create two dictionaries
d1={"a":1}
d2={"b":2}
# Merge both dictionaries
merged=d1|d2
print("Merged Dictionary:",merged)
#Question no:11
#Create a dictionary
data={"apple":50,"banana":20,"mango":30}
# Sort dictionary by keys
sorted_keys=dict(sorted(data.items()))
print("By keys:",sorted_keys)
# Sort dictionary by values
sorted_values=dict(sorted(data.items(),key=lambda x:x[1]))
print("By values:",sorted_values)
#Question no:12
#Create inventory with product quantities
inventory={
    "Pen":10,
    "Notebook":20,
    "Pencil":15
}
# Add a new product
inventory["Pencil Box"]=5
# Update product stock
inventory["Pen"]=25
# Remove a product
del inventory["Pencil"]
# Display final inventory
print("Final Inventory:",inventory)
