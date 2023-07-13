# -----------------Assignment #1-----------------
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0])
print(friends[-5])
print(friends[-1])
print(friends[4])

print("-" * 50)

# -----------------Assignment #2-----------------
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[::2])
print(friends[1::2])

print("-" * 50)

# -----------------Assignment #3-----------------
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[1:4])
print(friends[-2:])

print("-" * 50)

# -----------------Assignment #4-----------------
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends[-2:] = ["Elzero", "Elzero"]
print(friends)

print("-" * 50)

# -----------------Assignment #5-----------------
friends = ["Osama", "Ahmed", "Sayed"]
friends.insert(0, "Nasser")
print(friends)
friends.append("Salem")
print(friends)

print("-" * 50)

# -----------------Assignment #6-----------------
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
friends[0:2] = []
print(friends)
friends.remove(friends[-1])
print(friends)

print("-" * 50)

# -----------------Assignment #7-----------------
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
friends.extend(employees)
friends.extend(school)
print(friends)

print("-" * 50)

# -----------------Assignment #8-----------------
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)

print("-" * 50)

# -----------------Assignment #9-----------------
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends))

print("-" * 50)

# -----------------Assignment #10-----------------
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web",]]
print(technologies[-1][0])
print(technologies[-1][-1])

print("-" * 50)

