# -----------------Assignment #1-----------------
print(bool(100))
print(bool(58.22))
print(bool("Mostafa"))
print(bool(True))
print(bool([1, 2, 3, 4, 5]))
print(bool(False))
print(bool(0))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(""))
print(bool(''))

print("-" * 50)

# -----------------Assignment #2-----------------
html = 80
css = 60
javascript = 70

print(html > 50 and css > 50 and javascript > 50)

print("-" * 50)

# -----------------Assignment #3-----------------
num_one = 10
num_two = 20
num = 20
print(num > num_one or num > num_two)
print(num > num_one and num > num_two)

print("-" * 50)

# -----------------Assignment #4-----------------
num_one = 10
num_two = 20
result = num_one + num_two
print(result)
result **= 3
print(result)
result %= 26000
print(result)
result /= 5
print(result)
print(type(str(result)))
