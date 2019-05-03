# You find a bonus section! This is a gentle introduction to `%` and `==`

# In Python, `%` means to obtain the reminder of the division.

print(5%3) # expect 2

print(10%3) # expect 1

print(36%4) # expect 9

# `==` is different from `=`. For beginners, it is a common mistake to misuse them two. 
# `=` is `assign` operator, let the left-hand-side take the value of the right-hand-side.
# `==` is an evaluation. If the left-hand-side DOES equal to the right-hand-side, then it returns `True`

if 1 = 2:
    print("This line will not be printed.") # can you fix the syntax error

if 1 == 2:
    print("This line will never be printed for another reason")