#Question 1: Basic String Creation and Indexing
text = "Python"
print("String:", text)
print("First Character:", text[0])
print("Last Character:", text[-1])
print("Middle Character:",text[len(text)//2])

#Question 2: String Slicing Fundamentals
text = "Programming"
print("First 5 Characters:", text[:5])
print("Last 4 Characters:", text[-4:])
print("Substring (2 to 7):", text[2:8])

#Question 3: Advanced Slicing with Step
text = "Programming"
print("Alternate Characters:", text[::2])
print("Reverse String:", text[::-1])

#Question 4: String Immutability Demonstration
text = "Python"
# text[0] = "J" #TypeError
new_text = "J" + text[1:]
print(new_text)

#Question 5: Searching using in and not in
text = "Python Programming"
if "Python" in text:
    print("Substring Found")
else:
    print("Substring Not Found")
if "Java" not in text:
    print("Java is not present")

#Question 6: Using find() and index()
text = "Python Programming"
print(text.find("Programming"))
print(text.find("Java"))
print(text.index("Python"))

