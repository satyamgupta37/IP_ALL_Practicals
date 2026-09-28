#Question no:1
student={"Name":"Rahul","Age":20,"Marks":85}

print("Student Dictionary:")
print(student)

print("\nType of student:", type(student))

#Accessing values using keys
#(key-value Mapping)

print("\nkey-value Mapping:")
print("Name ->", student["Name"])
print("Age ->", student["Age"])
print("Marks ->", student["Marks"])

#Question no:3
student={"Name":"Rahul","Age":20,"Marks":85}
print("Original Dictionary:")
print(student)
#Adding a new key-value pair
student["City"] = "Mumbai"
#Updating an existing value
student["Marks"]=90
#Display the updated dictionary
print("\nUpdated Dictionary:")
print(student)
