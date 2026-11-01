# Tuple Operations in Python

# 1. Creating a Tuple
fruits = ("Apple", "Banana", "Mango", "Orange")
print("Original Tuple:", fruits)

# 2. Accessing Elements Using Index
print("First Element:", fruits[0])
print("Last Element:", fruits[-1])

# 3. Accessing Elements Using Loop
print("\nTuple Elements:")
for fruit in fruits:
    print(fruit)

# 4. Updating Tuple
# Tuple is immutable, so we cannot update directly.
# Convert tuple into list to update it.

temp = list(fruits)
temp[1] = "Grapes"
fruits = tuple(temp)
print("After Updating:", fruits)

# 5. Adding Elements
temp = list(fruits)
temp.append("Pineapple")
fruits = tuple(temp)
print("After Adding:", fruits)

# 6. Removing Elements
temp = list(fruits)
temp.remove("Mango")
fruits = tuple(temp)
print("After Removing:", fruits)

# 7. Tuple Built-in Functions
print("Length:", len(fruits))
print("Maximum:", max(fruits))
print("Minimum:", min(fruits))

# 8. Tuple Methods
numbers = (10, 20, 10, 30, 10, 40)
print("Count of 10:", numbers.count(10))
print("Index of 30:", numbers.index(30))
