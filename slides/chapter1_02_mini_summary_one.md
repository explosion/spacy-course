---
type: slides
---

## You did a wonderful job to reach your first milestone!


Notes: Let's go over the summaries so you will be well equipped for the mini quiz coming.

---

## What is Python?

- Python is a programming language. it runs on computer so you can tell the computer to do whatever you want it to do *exactly*. 
- As a `language`, Python has a set of syntax or rules that you must follow to correctly and efficiently tell what you want it to do.
- As a `programming language`, it enables you to do many things much faster than human. For example, mathematical calculation.

---

## What is a variable?

- To keep track of what you tell Python to memorize and manipulate, Python uses variables to denote them. Variables can't start with a digit but almost anything else.
- There are many basic types for variables, what we have seen includes:

1. numerical, like `3` and `1.5`
2. string, like `"Hello!"`
3. boolean, like `True` or `False`

---

## What are list and dictionary? What are their differences?

- A list is an `ordered` collection of objects. Its elements can be accessed by indexing. 
- A dictionary is an `unordered`collection of pairs. The first element of the pair is called the `key` and the second element is called `value`. The value can be queried through the `key`. 

Notes: Both data structures are builtin in Python. 

---

## Make sure you understand what the following snippet does. 

```python
ages = {"Amy": 7, "Bob": 10, "Claire": 9}

print(ages["Amy"] > ages["Bob"]) # true or false?

# Let's do a trick

indexByName = {"Amy": 0, "Bob": 1, "Claire": 2} 
# this gives you the location/index of the information in another data structure, here a list called `agesByIndex`.

agesByIndex = [7, 10, 9]

# Now, Amy's age can be accessed like this. Can you get it?

print(agesByIndex[indexByName["Amy"]])
```

```out
False

7
```

Notes: If you have difficulty guessing the results, open one interactive session in previous chapter, copy, paste and try it.



---

## Let's practice!

Notes: Now it's your turn!

---

## Aha, you find this page!

Notes: There are some contents that we have already used but not discussed yet. For example, functions. `print()` and `len()` are essentially built-in functions and we already used them a lot in previous exercises. Hang on there. We will look into them soon!