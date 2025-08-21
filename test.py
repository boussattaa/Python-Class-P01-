first_name = "alex"
last_name = "boussatta"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name}!") # Hello, Alex Boussatta!
print(full_name.title())
age = 28
print (f"{full_name} is {age} years old.") #age is 28
age = 28
print(f"{full_name} is {age:.1f} years old.") #age is 28.0
new_age = age + 1
print(f"{full_name} is {age} and will be {new_age} next year.") #age is 28 will be 29
