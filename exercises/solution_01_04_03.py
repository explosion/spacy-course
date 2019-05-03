# Dictionary exercise

# build an empty dictionary like this

dictionaryA = dict()

# Or you can build a dictionary like the following. I built a dictionary called `AGES`. 
# This dictionary contains three objects. Each object is a pair like `name: age`. 

AGES = {"Amy": 7, "Bob": 10, "Claire": 9}

# check the dictionary `AGES` length

print(len(AGES))

# now check its type

print(type(AGES))

# What are the `keys` for the `AGES`?

print("The keys are: ", AGES.keys())

# How about the values? 

print("The values are: ", AGES.values())

# How to retrive the age of Amy? 

print("The Age of Amy is", AGES["Amy"])

# How about Bob?

print("The Age of Bob is", AGES["Bob"])

# Now let's add `David` to our dictionary.

AGES["David"] = 11

# Eason is 8 years old. Can you add him too?

AGES["Eason"] = 8

# Now, add one to the age of Claire.

AGES["Claire"] = AGES["Claire"] + 1

# What will happen if you want to index a dictionary like AGES[0]? try it yourself.

AGES[0] # will cause error.