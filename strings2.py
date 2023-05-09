#1
greet = "Happy birthday! "
print(greet * 3)

#2
word = str(input("Enter any word: "))
word_back = word[::-1]
print(f"Here is you word backwards '{word_back}'.")

#3
name = str(input("What is your name, dear User: "))
print(f"Hello, {name[::-1]}!")

#4
str_w = str(input("Enter any word that has more than 5 letters: "))
print(f"This is your word withot first and last 2 letters: {str_w[2:-2]}")

#5
word_1 = str(input("Enter the first word: "))
word_2 = str(input("Enter the second word: "))
print(f"{word_1[::-1]} {word_2[::-1]}")

#6
first_w = "HELLO"
second_w = "you"
print(first_w[0:3] + second_w + first_w[-2:])

#7
string = '1234567890'
print(f"+{string[0:3]} {string[3:6]}-{string[-4:]}")

#8
the_word = str(input("Enter any word here: "))
print(f"{'*' * (len(the_word)+2)}\n*{the_word}*\n{'*' * (len(the_word)+2)}")

