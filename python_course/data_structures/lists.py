fruits = ["apple", "banana", "mango"]

print("full list:", fruits)
print("first fruit:", fruits[0])
print("number of fruits:", len(fruits))
 
fruits.append("orange")
print("after adding:",fruits)

fruits.remove("banana")
print("after removeing:",fruits)

print("looping through list:")
for fruit in fruits:
    print(fruit)

