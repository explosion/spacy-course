# This short algorithm represents a famous mathematical conjecture: Collatz Conjecture

number = 1024

while number != 1:
    if number % 2 == 0:
        number = number // 2
    elif number % 2 == 1:
        number = number*3 + 1
    print(number)

# https://en.wikipedia.org/wiki/Collatz_conjecture