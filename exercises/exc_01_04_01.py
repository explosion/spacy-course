# Get to know list

# A list is an ORDERED structure of a bunch of other objects. Let's take a look.

FRUIT = ["apple", "banana", "orange"]

# Now, the variable FRUIT represents a `list` of three different kinds of fruits. Let's check the first one. When you want to index a list to get the `nth` object, use `[index]` to select. You will see that `print()` can print several objects at the same time.

print("You get a(an)", FRUIT[1])

# Oops! It looks like we get a `banana` rather than an `apple`. The thing is that python indexing starts with 0, rather than 1. So in order to get the first element, set index to be 0.

print("You get a(an)", FRUIT[0])

# Here you go, you get an apple.

# Let's create another list of odd numbers which are smaller than 10

ODDS = [1, 3, 5, 7, 9]

# Let's check the length of this list by wrapping it around the `len()` function. We will learn more about functions very soon.

print("The length is ", len(ODDS))

# How about the summation of those numbers?, the function you need is called `sum()`

print("Sum of all the numbers is ", replaceMe)

# Can a list contain different types of objects? Can you create a list like [1, "One"]?

# Can you create an empty list []? What is the length of it?
