# -----------------Assignment #1-----------------
name = "Mostafa",
print(name)
print(type(name))

print("-" * 50)

# -----------------Assignment #2-----------------
friends = ("Osama", "Ahmed", "Sayed")
friendsTwo = list(friends)
friendsTwo[0] = "Elzero"
friends = tuple(friendsTwo)

print(friends)
print(type(friends))
print(len(friends))

print("-" * 50)

# -----------------Assignment #3-----------------
nums = (1, 2, 3)
letters = ("A", "B", "C")
newTuple = nums + letters
print(newTuple)
print(len(newTuple))

print("-" * 50)

# -----------------Assignment #4-----------------
my_tuple = (1, 2, 3, 4)

a, b, _, c = my_tuple
print(a, b, c, sep="\n")

print("-" * 50)
