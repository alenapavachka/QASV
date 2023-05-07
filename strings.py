#1
poem = '''to be
or not be
that is the qustion '''
print(poem)

#2
season = "spring"
print(len(season))

#3
string = str(input("Enter your text here: "))
n = string[-1]
print(f"Here is the last letter of the entered text: {n}")

#4
first_name = str(input("Enter your first name: "))
last_name = str(input("Enter your last name: "))
full_name  = first_name + " " + last_name
print(f"Your full name is {full_name}")

#5
name = str(input("Enter your name: "))
print(f"{name}, your name has {len(name)} letters.")
print(f"{name}, your name starts with letter '{name[0]}'.")
print(f"{name}, your name ends with letter '{name[-1]}'.")
