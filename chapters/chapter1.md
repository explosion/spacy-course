---
title: 'Chapter 1: How to use this website and Python basics'
description:
  "This chapter will teach you what a lesson looks like on this website. It will also teach you some basic knowledge about a programming language called Python. All you need to do is some occasional clicking."
prev: /chapter1
next: /chapter1
type: chapter
id: 1
---

<exercise id="1" title="Start here" type="slides">

<slides source="chapter1_01_how_to_use_the_website">
</slides>

</exercise>

<exercise id="2" title="Use Python in this website">

Welcome to lesson two. In this lesson, you will run two lines of Python code and learn to use the interactive environment. The first lesson is as simple as $1+1=2$!

### Python is talkative!

You can change `Hello` to `Hi` and click `Run Code` again to see its effect.

<codeblock id="01_02_01">

</codeblock>

Note that everything you type beginning with a `#` will not have any effect in the input box. Feel free to comment what you do and make notes for yourself.

### Python is your calculator!

Let Python do some math for you.

In this part, if you click `Run Code` directly, the program will complain. you need to edit the last line of the code to make it runnable. 

<codeblock id="01_02_02">
</codeblock>

</exercise>

<exercise id="3" title="20-minute Python, variables and operators">

In Python, you can use variables to denote numbers so you can reuse those numbers again. For example, you have already seen that `greetings = "Hello!"` before. In this question, we are going to calculate the amount of money we need to pay for certain number of bananas.

### Price of bananas

- In this exercise, we buy 3 bananas for 1 dollar each. You need to replace the name `replaceMe` with something else to obtain the right answer.

<codeblock id="01_03_01">

</codeblock>

### More operators, please!

- In this example, let's learn some other operators. You will also see a new data type called `boolean`  .

<codeblock id="01_03_02">

</codeblock>

`+`, `-`, `*` and `/` are the four arithmetic operators. 

You can use `()` to change the order of operations.

the `True` and `False` value of a variable is called `boolean` as it represents whether something is true or not.

In Python, at this stage, you can freely add, divide, multiply or subtract numbers without worrying too much about how accuracy your result is. In the future, we will look into this issue when it is necessary.

</exercise>

<exercise id="4" title="20-minute Python, list, string and dictionary">

Things become more and more interesting! Now, let's see how to organize a bunch of things together into one object.

### Be listy!

You need to replace `replaceMe` to get the code work.

<codeblock id="01_04_01">

</codeblock>

### "There is no strings on me." -- Ultron.

A string is a collection of characters wrapped by double quote `"`. They can also be indexed and manipulated pretty freely.

<codeblock id="01_04_02">


</codeblock>

### Just like a hardcopy dictionary.

Dictionary is also very useful. When you look up a word in a dictionary, you search the word and find its definition and sample sentences. The word itself is like a `key` for you to locate what you want to find and the corresponding contents are like the `values`.

<codeblock id="01_04_03">


</codeblock>

A dictionary is different from list for several important reasons.

1. It is not ordered. You can't access elements in a dictionary by indexing it.
2. It is very fast to retrieve an element when the containers of objects get larger and larger.
3. A `dictionary` represents a `mapping` relationship between elements while a `list` usually doesn't.

</exercise>

<exercise id="5" title="20-minute Python, mini summary one" type="slides">

<slides source="chapter1_02_mini_summary_one">
</slides>

</exercise>

<exercise id="6" title="20-minute Python, mini test one, question one" type="choice">

Can you index a string of length 6 like `"Hello!"`?

<choice>
<opt correct="true" text="Yes">

Yes, we can.

</opt>
<opt  text="No">

Try again and try to index it :)

</opt>
</choice>

</exercise>

<!-- <exercise id="6-2" title="20-minute Python, mini test one, question two" type="choice">

Can you change a character of a string of length 6 like `"Hello!"` by indexing? for example, does the following code work?

```python

stringA = "Hello!"
stringA[0] = "S"
```

<choice>

<opt text="Yes">

Try it in an interactive session and see what error you get.

</opt>
<opt correct="true" text="No">

Right. A string in Python is immutable.

</opt>
</choice>

</exercise> -->

<exercise id="7" title="20-minute Python, if and else">

In this lesson, we will examine an important structure in Python and almost any other programming languages. Sometimes we want to check a condition then decide what to do next. The `if` and `else` clauses are designed for such situations.

Python uses the indentation mechanism to determine whether a part of code is a branch or secondary part of another part of code. This exercise will be the first time you see it. Don't worry. It is pretty intuitive.

<codeblock id="01_07">

</codeblock>

Notice the following details:

1. the `:` is after each condition assessment.
2. the indentation is four space `    `.
3. `in` is also a keyword in Python, it checks the membership of an element
4. pay attention to the logical operators like `or` and `and`. Use brackets when neccessary.
5. `%` is an interesting operator in Python. Can you guess what it does?

</exercise>

<exercise id="8" title="20-minute Python, loops">

Finally, we come to the loopy part! Loop is a very important concept in Python and almost all other programming languages. It enables the program to do things `repeatedly` or `iterate` over a `list` or any other `iterable` object. Things will become more clear when we dive into the code.

### `while` loop

<codeblock id="01_08_01">

</codeblock>

- Python checks a condition after the keyword `while`. If it is true, the block nested below it will run once then come back to check the condition agian.

- In this part, you saw a new operator `//`. It is slightly different from `/`. `//` will return an integer for sure. It is called `floor division`. Check more [here](https://python-reference.readthedocs.io/en/latest/docs/operators/floor_division.html)

### `for` loop

`for` loop is, in my opinion, more powerful and flexible than the `while` loop. It checks a limited `collection` of elements and perform operations.

In Python, a variable doesn't need to be `initialized`. It can appear *suddenly* anywhere in the code. This creates great convenience for small project. In the future, you may find it not so good :)

<codeblock id="01_08_02">

</codeblock>

We saw something new in this piece of code.

1. `range()` function. This is a builtin function in Python. It generates a list of numbers from a range, default starting value is `0`.
2. a dictionary has a method called `items()`. `AGES.items()` gives you a list of pairs so you can use a pair of variables to catch it like `name, age` pair.

</exercise>

<exercise id="9" title="20 minute Python, don't copy but write functions">

Great job so far! This is our last lesson before moving on to math. Let's write some functions!

When programming, we often do one operation repeatedly. A function will help you avoid writing or copy-pasting the same content again and again. 

We will learn two functions in this lesson.

1. `sayManyHis()`
2. `mean()`. 

<codeblock id="01_09">

</codeblock>

 We see something new in this lesson:

 1. `def`, short for `define`
 2. `return`, return the value of a function's result.

</exercise>

<exercise id="10" title="20-minute Python, mini summary two" type="slides">

<slides source="chapter1_03_mini_summary_two">
</slides>

</exercise>


<exercise id="11" title="20-minute Python, a mini project">

## Welcome to the last part of the crash course. In this part, we will work on a mini project about counting days in 12 months.


### How many days are there in a month?

In this part, build two dictionaries.

1. The first dictionary has month as key and  number of days in that month as corresponding value. It has 12 elements. TLet's assume February has 28 days.
2. The second dictionary has number of days as key and a `list` of months with that days as value. It has 3 elements.

<codeblock id="01_11_01">

</codeblock>

### Query the answer by writing functions.

In this part, write two functions to perform the query operation.

1. `sameDays()`, take two month names as input, test whether two months have the same number of days.
2. `otherMonths()`, take a month name as input, print all other months with the same number of days.

<codeblock id="01_11_02">

</codeblock>
Legend says you are a well-trained Python newbie now!
</exercise>
