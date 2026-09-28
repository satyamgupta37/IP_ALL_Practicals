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
