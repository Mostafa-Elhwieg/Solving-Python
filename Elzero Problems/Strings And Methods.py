print("-" * 50)
# -----------------Assignment #1-----------------
Name = "mostafa"
age = 20
country = "Egypt"
print(f"""\"Hello '{Name}', How You Doing \\ \"\"\" Your Age Is \"{age}\"\" + And Your Country Is: {country}""")
print("-" * 50)

# -----------------Assignment #2-----------------
print(f"""\"Hello '{Name}', How You Doing \\\n \"\"\" Your Age Is \"{age}\"\" +\n And Your Country Is: {country}""")
print("-" * 50)

# -----------------Assignment #3-----------------
Name = "Elzero"
print("Second Letter is: \"" + Name[1] + "\"")
print("Third Letter is: \"" + Name[2] + "\"")
print("Last Letter is: \"" + Name[-1] + "\"")
print("-" * 50)

# -----------------Assignment #4-----------------
print("\"" + Name[1:4] + "\"")
print("\"" + Name[::2] + "\"")
print("\"" + Name[-2::-2] + "\"")
print("-" * 50)
# -----------------Assignment #5-----------------
name = "#@#@Elzero#@#@"
print(name.strip("#@"))
print("-" * 50)

# -----------------Assignment #6-----------------
num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"
print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))
print("-" * 50)

# -----------------Assignment #7-----------------
name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))
print("-" * 50)

# -----------------Assignment #8-----------------
name_one = "OSamA"
name_two = "osaMA"
print(name_one.swapcase())
print(name_two.swapcase())
print("-" * 50)

# -----------------Assignment #9-----------------
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))
print("-" * 50)

# -----------------Assignment #10-----------------
name = "Elzero"
print(name.find("z"))
print("-" * 50)

# -----------------Assignment #11-----------------
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3", "Love", 1))
print("-" * 50)

# -----------------Assignment #12-----------------
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3", "Love"))
print("-" * 50)

# -----------------Assignment #13-----------------
name = "Mostafa"
age = 20
country = "Egypt"
print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")
print("-" * 50)
