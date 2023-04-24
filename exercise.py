#original code
cash = int(input("How much money do you have?: "))
age = int(input("Add your age: "))

if cash < 5 and age <21:
    print("You need more money and you are too young for this Club...")
elif cash >= 5:
    print("You have enough money for a ticket.")
    if age >= 21:
        print("And your age is OK. Welcome to the Club!")
    elif age < 21: 
        print("But you are too young for this Club , see u later.")  
else:
    print("No money, no honey buddy!" )
print("Please start over if you need too.")


#rewritten/shortened
print("Welcome!") if int(input("What's your entrance ticket budget in cash: "))>=5 and int(input("How old are you: "))>=21 else print("We will be glad to see you again  when you are 21 or older and have 5$.")
