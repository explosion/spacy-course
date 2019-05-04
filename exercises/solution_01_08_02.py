# for loop exercise

# Let's print all the even numbers smaller than or equal to 10.

for num in range(10):
    if num%2 == 0:
        print(num, "is even.")

# Weird. There is no `10` in the output. It is your turn to find out why.

# The range() function takes one argument as the cap of a range. It has some other usages and we will encounter it in the future.

# How about iterate another `iterable`

AGES = {"Amy":10, "Bob":11, "Chris":14}

for age in AGES.keys():
    print(age, ":", AGES[age])

# A very common usage of `for` loop is to generate a list like this:

ODDS = [odd for odd in range(1,10,2)]
# Can you figure out how this works?  
# Can you guess what the `2` does in the `range()` 
print(ODDS) 

# Print the name and age pair.

for name, age in AGES.items():
    print(name, " is ", age, " years old.")