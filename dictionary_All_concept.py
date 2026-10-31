dict={
    "Name":"Satyam Gupta",
    "Roll no":"26302A0058",
    "Course":"FYBSC-IT",
    "College Name":"Vidyalankar School of Information Technology"
    }
print(dict)

#displaying all dictionary values.
print(dict["Name"])
print(dict["Roll no"])
print(dict["Course"])
print(dict["College Name"])

#updating dictinary
dict["City"] = "Mumbai"
print(dict)

#Updating using built-in function.
dict.update({"age":18})
print(dict)

#displaying dictionary all keys,values and items.
print("Dictionary Keys:", dict.keys())
print("Dictionary Values:", dict.values())
print("Dictionary Items:", dict.items())

#Output
"""
{'Name': 'Satyam Gupta', 'Roll no': '26302A0058', 'Course': 'FYBSC-IT', 'College Name': 'Vidyalankar School of Information Technology'}
Satyam Gupta
26302A0058
FYBSC-IT
Vidyalankar School of Information Technology
{'Name': 'Satyam Gupta', 'Roll no': '26302A0058', 'Course': 'FYBSC-IT', 'College Name': 'Vidyalankar School of Information Technology', 'City': 'Mumbai'}
{'Name': 'Satyam Gupta', 'Roll no': '26302A0058', 'Course': 'FYBSC-IT', 'College Name': 'Vidyalankar School of Information Technology', 'City': 'Mumbai', 'age': 18}
Dictionary Keys: dict_keys(['Name', 'Roll no', 'Course', 'College Name', 'City', 'age'])
Dictionary Values: dict_values(['Satyam Gupta', '26302A0058', 'FYBSC-IT', 'Vidyalankar School of Information Technology', 'Mumbai', 18])
Dictionary Items: dict_items([('Name', 'Satyam Gupta'), ('Roll no', '26302A0058'), ('Course', 'FYBSC-IT'), ('College Name', 'Vidyalankar School of Information Technology'), ('City', 'Mumbai'), ('age', 18)])
"""
