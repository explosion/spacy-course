# while exercise

# Let's do a countdown
counter = 10

while counter > 0:
    print("Counting down: ", counter)
    counter = counter - 1

# If you double a number every round, when will you obtain a value larger than 1000?

start = 1

while start < 1000:
    print(start)
    start = start * 2

print(start)

# Now you try. Can you guess what the following code does? Change the value of number and examine  your discovery.

number = 1024

while number != 1:
    if number % 2 == 0:
        number = number // 2
    elif number % 2 == 1:
        number = number*3 + 1
    print(number)