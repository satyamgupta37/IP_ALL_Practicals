# List Operations in Python

# 1. Creating a List
fruits = ["Apple", "Banana", "Mango", "Orange"]
print("Original List:", fruits)

# 2. Accessing Elements Using Index
print("First Element:", fruits[0])
print("Last Element:", fruits[-1])

# 3. Updating Elements
fruits[1] = "Grapes"
print("After Updating:", fruits)

# 4. Accessing Elements Using Loop
print("\nList Elements:")
for fruit in fruits:
    print(fruit)

# 5. Updating Using Built-in Functions
# append() - Add an element at the end
fruits.append("Pineapple")
print("After Append:", fruits)

# insert() - Add an element at a specific index
fruits.insert(1, "Watermelon")
print("After Insert:", fruits)

# extend() - Add multiple elements
fruits.extend(["Papaya", "Kiwi"])
print("After Extend:", fruits)

# remove() - Remove a specific element
fruits.remove("Mango")
print("After Remove:", fruits)

# pop() - Remove an element using index
fruits.pop(0)
print("After Pop:", fruits)

# sort() - Arrange elements alphabetically
fruits.sort()
print("After Sort:", fruits)

# reverse() - Reverse the list
fruits.reverse()
print("After Reverse:", fruits)

# 6. Other Built-in Functions
print("Length:", len(fruits))
print("Maximum:", max(fruits))
print("Minimum:", min(fruits))
