---
type: slides
---

## Great job for finishing this crash course!

You are ready to explore other courses or chapters on the website. Good for you!

Notes: Let's do a quick summary about what we have learned.

---

##  if-else clause

if-else enables branching of code logic. You can follow different branches when appropriate conditions satisfy.

```python
# determine whether a year has 366 days or 365 days.
if year%400 == 0:
    return 366
else:
    if year%4 == 0 and year%100 == 0:
        return 365
    elif year%4 == 0:
        return 366
    else:
        return 365
```

---

##  for loop and while loop

for loop and while loop allows you to do one thing repeatedly in a concise syntax. 

```python
YEARS = [2018, 2015, 2012, 2000]

for year in YEARS:
    if year%400 == 0:
        print(366)
    else:
        if year%4 == 0 and year%100 == 0:
            print(365)
        elif year%4 == 0:
            print(366)
        else:
            print(365)

```
---

## Let's write some functions

A function helps you wrap a block of code for reusage in the future.

```python
def leapYear(year):
    if year%400 == 0:
        return True
    else:
        if year%4 == 0 and year%100 == 0:
            return False
        elif year%4 == 0:
            return True
        else:
            return False

for year in [2018, 2015, 2012, 2000]:
    if leapYear(year):
        print(year, " is a leap year.")
    else:
        print(year, "is not a leap year.)
```
---

## Practice makes perfect. Some advices for your future Python learning here.

1. [StackOverflow](https://www.stackoverflow.com) and [Google](https://www.google.com) are always your best friends.
2. Consult Python official [documents](https://docs.python.org/3/) if you are confused.
3. Write some codes and try yourself. You will remember forever.

Notes: Now Let's practice what we have learned with a small project.