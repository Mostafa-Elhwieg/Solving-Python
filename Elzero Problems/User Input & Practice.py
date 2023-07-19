# -----------------Assignment #1-----------------
name = input("What's Your Name ?").strip().capitalize()
print(f"Hello {name} Happy To See You.")

print("-" * 50)

# -----------------Assignment #2-----------------
age = int(input("What's Your Age ?"))
print(f"Hello Your Age Is Under 16, Some Articles Is Not Suitable For You" if age < 16 else f"Hello Your Age Is {age}, All Articles Is Suitable For You")

print("-" * 50)

# -----------------Assignment #3-----------------
firstName = input("What's Your First Name ?").strip().capitalize()
secondName = input("What's Your Second Name ?").strip().capitalize()
print(f"Hello {firstName} {secondName:.1s}")

print("-" * 50)

# -----------------Assignment #4-----------------
email = input("What's Your Email ?").strip().lower()

print(f"Your name is {email[:email.index('@')].capitalize()}")
print(f"Email Service Provider is {email[email.index('@')+1:email.index('.')]}")
print(f"Top Level Domain is {email[email.index('.')+1:]}")
