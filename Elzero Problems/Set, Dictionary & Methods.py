# -----------------Assignment #1-----------------
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = list(set(my_list))
print(unique_list)
print(type(unique_list))
print(unique_list[:-1])

print("-" * 50)

# -----------------Assignment #2-----------------
nums = {1, 2, 3}
letters = {"A", "B", "C"}
print(nums.union(letters))
print(nums | letters)
nums.update(letters)
print(nums)
nums = {*nums, *letters}
print(nums)

print("-" * 50)

# -----------------Assignment #3-----------------
my_set = {1, 2, 3}
print(my_set)
my_set.clear()
print(my_set)
my_set.add("A")
my_set.add("B")
print(my_set)
my_set.discard("C")

print("-" * 50)

# -----------------Assignment #4-----------------
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_two.issuperset(set_one))
print(set_one.issubset(set_two))

print("-" * 50)

# -----------------Assignment #5-----------------
Skills = {
    "HTML": "90%",
    "CSS": "80%",
    "Python": "30%"
}
print(f"HTML progress is {Skills['HTML']}")
print(f"CSS progress is {Skills['CSS']}")
print(f"Python progress is {Skills['Python']}")
Skills.update({"AI": "20%"})
print(f"AI progress is {Skills['AI']}")
print(Skills)

print("-" * 50)
