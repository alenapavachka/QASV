#1
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))
print(f"Here is the sum of your  numbers: {num1 + num2 + num3}")

#2
num = int(input("Enter any integer number: "))
print(f"{num - 1} is less by one than your number and {num + 1} is greater by one than your number")

#3
catheti_one = int(input("Enter the length of the first cathethi of a right triangle: "))
catheti_two = int(input("Enter the length of the second cathethi of the same triangle: "))
print(f"The area of this triangle equals {0.5 * catheti_one * catheti_two}")

#4 
name  = input("What is your name? ")
age =  int(input("How old are you? "))
print(f"{name}, your age {age} is the best!")

#5
number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))
print(f"{number_1} + {number_2} = {number_1 + number_2}\n{number_1} - {number_2} = {number_1 -number_2}\n{number_1} * {number_2} = {number_1 * number_2}\n{number_1} / {number_2} = {number_1 / number_2}")

#6
two_digit_number  = int(input("Enter any positive two-digit number: " ))
print(f"The sum of your number's ({two_digit_number})  digits is {two_digit_number // 10 + two_digit_number % 10}")

#7
fahrenheits = int(input("Enter the temperature in Fahrenheits: "))
print(f"Yuor enetered temperature in Celsius is {(fahrenheits - 32) * 5 / 9}")

#8
price_after_discount = round((float(input("Enter the final price of your perchace (after the discount): "))), 2)
discount=int(input("Ener the discount here: "))
original_price = round((price_after_discount / (1- (discount/100))), 2)
print(f"Original price of your purchace was {original_price}")




