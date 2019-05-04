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

Welcome to lesson two. In this lesson, you will run two lines of Python code and learn to use the interactive environment.

### Python is talkative. It replies you whenever you allow it to `print` something.

In this example, don't change anything, just click the `Run Code` button below to run the two lines of code. For the first time you run a code block, it will take some time to initialize the background services. Great thanks to `binder` to make such services possible and free.

You may also notice that there are three buttons `Show hints`, `Show solutions` and `Reset` below. If there are hints available, clicking `Show hints` will give you some hints. Clicking `Show solutions` will show you the solution while `Reset` will just remove all your editing.

- Let Python say *Hello*.

Note that everything you type beginning with a `#` will not have any effect in the input box. Feel free to comment what you do and make notes for yourself.

<codeblock id="01_02_01">
</codeblock>

### Python is your calculator!

- Let Python do some math for you.

In this part, if you click `Run Code` directly, the program will complain. you need to edit the last line of the code to make it runnable. 

<codeblock id="01_02_02">
</codeblock>

</exercise>

<exercise id="3" title="20-minute Python, variables and operators">

In Python, you can use variables to denote numbers so you can reuse those numbers again. For example, you have already seen that `greetings = "Hello!"` before. In this question, we are going to calculate the amount of money we need to pay for certain number of bananas.

### Bananas

- In this exercise, we buy 3 bananas for 1 dollar each. You need to replace the name `replaceMe` with something else to obtain the right answer.

<codeblock id="01_03_01">

</codeblock>

### Other operators

- In this example, let's learn some other operators. You will also see a new data type called `boolean`  .

<codeblock id="01_03_02">

`+`, `-`, `*` and `/` are the four arithmetic operators. 

You can use `()` to change the order of operations.

the `True` and `False` value of a variable is called `boolean` as it represents whether something is true or not.

In Python, at this stage, you can freely add, divide, multiply or subtract numbers without worrying too much about how accuracy your result is. In the future, we will look into this issue when it is necessary.

</codeblock>

</exercise>

<exercise id="4" title="20-minute Python, list, string and dictionary">

Things become more and more interesting! Now, let's see how to organize a bunch of things together into one object. We are going to look at the data type called `list` first. You need to replace `replaceMe` to get the last line of code work.

<codeblock id="01_04_01">

</codeblock>

Now, let's take a look at `string`. A string is simple what you see wrapped by double quote `"`. They can also be indexed and manipulated pretty freely.

<codeblock id="01_04_02">


</codeblock>

Dictionary is also very useful. When you look up a word in a dictionary, you search the word and find its definition and sample sentences. The word itself is like a `key` for you to locate what you want to find and the corresponding contents are like the `values`.

<codeblock id="01_04_03">


</codeblock>

A dictionary is different from list for several important reasons.

1. It is not ordered. You can't access elements in a dictionary by indexing it.
2. It is very fast to retrieve an element. This may not be clear now.
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

In this lesson, we will examine an important structure in Python and almost any other programming languages. Sometimes we want to check a condition then decide what to do. The `if` and `else` clauses are designed for such jobs.

Note Python uses the indentation mechanism to determine whether a part of code is a branch or secondary part of another part of code. This exercise will be the first time you see it. Don't worry. It is pretty intuitive.

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

Python checks a condition after the keyword `while`. If it is true, the block nested below it will run once then come back to check the condition agian.

</codeblock>

In this part, you saw a new operator `//`. It is slightly different from `/`. `//` will return an integer for sure. It is called `floor division`. Check more [here](https://python-reference.readthedocs.io/en/latest/docs/operators/floor_division.html)

### `for` loop

`for` loop is, in my opinion, more powerful and flexible than the `while` loop. It checks a limited `collection` of elements and perform operations.
<codeblock id="01_08_02">

As you may notice, in Python, a variable doesn't need to be `initialized`. It can appear *suddenly* anywhere in the code. This creates great convenience for small project. In the future, you may find it not so good :)

We saw something new in this piece of code.

1. `range()` function. This is a builtin function in Python. It generates a list of numbers from a range, default starting value is `0`.
2. a dictionary has a method called `items()`. `AGES.items()` gives you a list of pairs so you can use a pair of variables to catch it like `name, age` pair.

</codeblock>


</exercise>

<exercise id="9" title="20 minute Python, don't copy but write functions">

Great job so far! This is our last lesson before moving on to math. Let's write some functions!
<codeblock id="01_09">

In programming, we often do one operation repeatedly. A function will help you avoid writing or copy-pasting the same content again and again. 

We will learn two functions in this lesson.

1. `sayManyHis()`
2. `mean()`. 

 We see something new in this lesson:

 1. `def`, short for `define`
 2. `return`, return the value of a function's result.

</codeblock>

</exercise>

<exercise id="10" title="20-minute Python, mini summary two" type="slides">

<slides source="chapter1_03_mini_summary_two">
</slides>

</exercise>


<exercise id="11" title="20-minute Python, a mini project">

## Welcome to the 

### Days in a month

<codeblock id="01_11_01">
In this part, build two dictionaries.

The first dictionary has month as key and  number of days in that month as corresponding value. It has 12 elements. TLet's assume February has 28 days.

The second dictionary has number of days as key and a `list` of months with that days as value. It has 3 elements.
</codeblock>

### Query 

<codeblock id="01_11_02">

In this part, write two functions to perform the query operation.

1. `sameDays()`, take two month names as input, test whether two months have the same number of days.
2. `otherMonths()`, take a month name as input, print all other months with the same number of days.

</codeblock>

</exercise>
