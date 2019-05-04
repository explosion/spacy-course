# function exercise

# a simplest function looks like this

def sayHi():
    print("Hi!")

# What this function does is simply printing `Hi!`. Let's pass an argument to the function so it can print `Hi!` for many times.

def sayManyHis(number):
    for time in range(number):
        print("Hi!")

# However, you can use a defined function in another function, too.

def sayManyHis2(number):
    for time in range(number):
        sayHi()

# Now, these functions can be called.

sayManyHis2(3)

# Define another function which calculates the average of all the numerical values in a list.
# We make use of the two functions you have already seen before: `sum()` and `len()`.

def mean(L):
    # L is a list
    return sum(L)/len(L)

listA = [2, 4, 6, 8]

print(mean(listA))