#1
side = 55
area = side ** 2
print(f"If the side of a square equals {side} than its area equals {area}")

#2
num = 365
first_digit = num // 100
second_digit = (num // 10) % 10
third_digit = num % 10
sum = first_digit + second_digit + third_digit
print(f"The sum of the 3 digits of number {num} is {sum}")

#3
hour = 3
min =  55
sec = 4
total_sec = sec + min * 60 + hour * (60 ** 2)
print(f"3 hours 55 minutes and 4 seconds contains {total_sec} seconds")

#4
section_day_one = 120
section_day_two = section_day_one * 2 
print(f"If a lake's section overgrown with water lilies equales {section_day_one} on the first day and it duobles in size every day, than its size after one day will be equal {section_day_two}")




