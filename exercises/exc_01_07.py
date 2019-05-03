# if-else exercise

# which sentence will be printed here? Is the logic complete here?

if 3 < 5:
    print("3 is less than 5.")
else:
    print("3 is greater than 5.")

# What if there are three choices? 
# Try to change their ages so you may reproduce all three of the possible results.

Amy = 14
Betty = 11

if Amy > Betty:
    print("Amy is older than Betty.")
elif Amy < Betty:
    print("Amy is younger than Betty.")
else: 
    print("Amy and Betty are at the same age!")
    
# Try some other conditions 

ODDS = [1, 3, 5, 7, 9]

testNumber = 8

if testNumber in ODDS:
    print(testNumber, " doesn't belong to the odd number list.")
else:
    if testNumber%2 == 0:
        print("At least testNumber ", testNumber, " is an even number.")
    else:
        print("testNumber is ", testNumber)


# Combine conditions by logical operators.

testNumber2 = 11

if testNumber2 in ODDS or testNumber2 == 11:
    print("testNumber2 passed the test!")