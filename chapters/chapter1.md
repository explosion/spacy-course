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

- In this example, let's exame some other operators. You will also see a new type called `boolean` variables.

<codeblock id="01_03_02">

Creating a slice of a `Doc` works just like creating a slice of a list in Python
using the `:` notation. Remember that the last token index is _exclusive_ – for
example, `0:4` describes the tokens 0 _up to_ token 4, but not including
token 4.

</codeblock>

</exercise>

<exercise id="4" title="20-minute Python, list, string and dictionary">

In this example, you'll use spaCy's `Doc` and `Token` objects, and lexical
attributes to find percentages in a text. You'll be looking for two subsequent
tokens: a number and a percent sign.

- Use the `like_num` token attribute to check whether a token in the `doc`
  resembles a number.
- Get the token _following_ the current token in the document. The index of the
  next token in the `doc` is `token.i + 1`.
- Check whether the next token's `text` attribute is a percent sign "%".

<codeblock id="01_04">

To get the token at a certain index, you can index into the `doc`. For example,
`doc[5]` is the token at index 5.

</codeblock>

</exercise>

<exercise id="5" title="20-minute Python, mini summary one" type="slides">

<slides source="chapter1_02_statistical-models">
</slides>

</exercise>

<exercise id="6" title="20-minute Python, mini test one" type="choice">

What's **not** included in a model package that you can load into spaCy?

<choice>
<opt text="A meta file including the language, pipeline and license.">

All models include a `meta.json` that defines the language to initialize, the
pipeline component names to load as well as general meta information like the
model name, version, license, data sources, author and accuracy figures (if
available).

</opt>
<opt text="Binary weights to make statistical predictions.">

To predict linguistic annotations like part-of-speech tags, dependency labels or
named entities, models include binary weights.

</opt>
<opt correct="true" text="The labelled data that the model was trained on.">

Statistical models allow you to generalize based on a set of training examples.
Once they're trained, they use binary weights to make predictions. That's why
it's not necessary to ship them with their training data.

</opt>
<opt text="Strings of the model's vocabulary and their hashes.">

Model packages include a `strings.json` that stores the entries in the model's
vocabulary and the mapping to hashes. This allows spaCy to only communicate in
hashes and look up the corresponding string if needed.

</opt>
</choice>

</exercise>

<exercise id="7" title="20-minute Python, if and else">

The models we're using in this course are already pre-installed. For more
details on spaCy's statistical models and how to install them on your machine,
see [the documentation](https://spacy.io/usage/models).

- Use `spacy.load` to load the small English model `'en_core_web_sm'`.
- Process the text and print the document text.

<codeblock id="01_07">

To load a model, call `spacy.load` on its string name. Model names differ
depending on the language and the data they were trained on – so make sure to
use the correct name.

</codeblock>

</exercise>

<exercise id="8" title="20-minute Python, loops">

You'll now get to try one of spaCy's pre-trained model packages and see its
predictions in action. Feel free to try it out on your own text! To find out
what a tag or label means, you can call `spacy.explain` in the. For example:
`spacy.explain('PROPN')` or `spacy.explain('GPE')`.

### Part 1

- Process the text with the `nlp` object and create a `doc`.
- For each token, print the token text, the token's `.pos_` (part-of-speech tag)
  and the token's `.dep_` (dependency label).

<codeblock id="01_08_01">

To create a `doc`, call the `nlp` object on a string of text. Remember that you
need to use the token attribute names with an underscore to get the string
values.

</codeblock>

### Part 2

- Process the text and create a `doc` object.
- Iterate over the `doc.ents` and print the entity text and `label_` attribute.

<codeblock id="01_08_02">

To create a `doc`, call the `nlp` object on a string of text. Remember that you
need to use the token attribute names with an underscore to get the string
values.

</codeblock>

</exercise>

<exercise id="9" title="20 minute Python, don't copy but write functions">

Models are statistical and not _always_ right. Whether their predictions are
correct depends on the training data and the text you're processing. Let's take
a look at an example.

- Process the text with the `nlp` object.
- Iterate over the entities and print the entity text and label.
- Looks like the model didn't predict "iPhone X". Create a span for those tokens
  manually.

<codeblock id="01_09">

- To create a `doc`, call the `nlp` object on the text. Named entities are
  available as the `doc.ents` property.
- The easiest way to create a `Span` object is to use the slice notation – for
  example `doc[5:10]` for the token at position 5 _up to_ position 10. Remember
  that the last token index is exclusive.

</codeblock>

</exercise>

<exercise id="10" title="20-minute Python, mini summary two" type="slides">

<slides source="chapter1_03_rule-based-matching">
</slides>

</exercise>

<exercise id="11" title="20-minute Python, mini test two" type="choice">

Let's try spaCy's rule-based `Matcher`. You'll be using the example from the
previous exercise and write a pattern that can match the phrase "iPhone X" in
the text.

- Import the `Matcher` from `spacy.matcher`.
- Initialize it with the `nlp` object's shared `vocab`.
- Create a pattern that matches the `'TEXT'` values of two tokens: `"iPhone"`
  and `"X"`.
- Use the `matcher.add` method to add the pattern to the matcher.
- Call the matcher on the `doc` and store the result in the variable `matches`.
- Iterate over the matches and get the matched span from the `start` to the
  `end` index.

<codeblock id="01_11">

- The shared vocabulary is available as the `nlp.vocab` attribute.
- A pattern is a list of dictionaries keyed by the attribute names. For example,
  `[{'TEXT': 'Hello'}]` will match one token whose exact text is "Hello".
- The `start` and `end` values of each match describe the start and end index of
  the matched span. To get the span, you can create a slice of the `doc` using
  the given start and end.

</codeblock>

</exercise>

<exercise id="12" title="20-minute Python, a comprehensive summary">

In this exercise, you'll practice writing more complex match patterns using
different token attributes and operators.

### Part 1

- Write **one** pattern that only matches mentions of the _full_ iOS versions:
  "iOS 7", "iOS 11" and "iOS 10".

<codeblock id="01_12_01">

- To match a token with an exact text, you can use the `TEXT` attribute. For
  example, `{'TEXT': 'Apple'}` will match tokens with the exact text "Apple".
- To match a number token, you can use the `IS_DIGIT` attribute, which will only
  return `True` for tokens consisting of only digits.

</codeblock>

### Part 2

- Write **one** pattern that only matches forms of "download" (tokens with the
  lemma "download"), followed by a token with the part-of-speech tag `'PROPN'`
  (proper noun).

<codeblock id="01_12_02">

- To specify a lemma, you can use the `'LEMMA'` attribute in the token pattern.
  For example, `{'LEMMA': 'be'}` will match tokens like "is", "was" or "being".
- To find proper nouns, you want to match all tokens whose `POS` value equals
  `'PROPN'`.

</codeblock>

### Part 3

- Write **one** pattern that matches adjectives (`'ADJ'`) followed by one or two
  `'NOUN'`s (one noun and one optional noun).

<codeblock id="01_12_03">

- To find adjectives, look for tokens whose `'POS'` value equals `'ADJ'`. For
  nouns, look for `'NOUN'`.
- Operators can be added via the `'OP'` key. For example, `'OP': '?'` to match
  zero or one time.

</codeblock>

</exercise>
