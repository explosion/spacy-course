---
title: 'Chapter 2: Large-scale data analysis with spaCy'
description:
  "In this chapter, you'll use your new skills to extract specific information
  from large volumes of text. You'll learn how to make the most of spaCy's data
  structures, and how to effectively combine statistical and rule-based
  approaches for text analysis."
prev: /chapter1
next: /chapter3
type: chapter
id: 2
---

<exercise id="1" title="Data Structures (1)" type="slides">

<slides source="chapter2_01_data-structures-1" start="11:06" end="13:37">
</slides>

</exercise>

<exercise id="2" title="Strings to hashes">

### Part 1

- Look up the string "cat" in `nlp.vocab.strings` to get the hash.
- Look up the hash to get back the string.

<codeblock id="02_02_01">

- You can use the string store in `nlp.vocab.strings` like a regular Python
  dictionary. For example, `nlp.vocab.strings["unicorn"]` will return the hash,
  and looking up the hash again will return the string `"unicorn"`.

</codeblock>

### Part 2

- Look up the string label "PERSON" in `nlp.vocab.strings` to get the hash.
- Look up the hash to get back the string.

<codeblock id="02_02_02">

- You can use the string store in `nlp.vocab.strings` like a regular Python
  dictionary. For example, `nlp.vocab.strings["unicorn"]` will return the hash,
  and looking up the hash again will return the string `"unicorn"`.

</codeblock>

</exercise>

<exercise id="3" title="Vocab, hashes and lexemes">

Why does this code throw an error?

```python
import spacy

# Create an English and German nlp object
nlp = spacy.blank("en")
nlp_de = spacy.blank("de")

# Get the ID for the string 'Bowie'
bowie_id = nlp.vocab.strings["Bowie"]
print(bowie_id)

# Look up the ID for "Bowie" in the vocab
print(nlp_de.vocab.strings[bowie_id])
```

<choice>

<opt correct="true" text='The string <code>"Bowie"</code> isn’t in the German vocab, so the hash can’t be resolved in the string store.'>

Hashes can't be reversed. To prevent this problem, add the word to the new vocab
by processing a text or looking up the string, or use the same vocab to resolve
the hash back to a string.

</opt>

<opt text='<code>"Bowie"</code> is not a regular word in the English or German dictionary, so it can’t be hashed.'>

Any string can be converted to a hash.

</opt>

<opt text="<code>nlp_de</code> is not a valid name. The vocab can only be shared if the <code>nlp</code> objects have the same name.">

The variable name `nlp` is only a convention. If the code used the variable name
`nlp` instead of `nlp_de`, it'd overwrite the existing `nlp` object, including
the vocab.

</opt>

</choice>

</exercise>

<exercise id="4" title="Data Structures (2)" type="slides">

<slides source="chapter2_02_data-structures-2" start="13:475" end="15:47">
</slides>

</exercise>

<exercise id="5" title="Creating a Doc">

Let's create some `Doc` objects from scratch!

### Part 1

- Import the `Doc` from `spacy.tokens`.
- Create a `Doc` from the `words` and `spaces`. Don't forget to pass in the
  vocab!

<codeblock id="02_05_01">

The `Doc` class takes 3 arguments: the shared vocabulary, usually `nlp.vocab`, a
list of `words` and a list of `spaces`, boolean values, indicating whether the
word is followed by a space or not.

</codeblock>

### Part 2

- Import the `Doc` from `spacy.tokens`.
- Create a `Doc` from the `words` and `spaces`. Don't forget to pass in the
  vocab!

<codeblock id="02_05_02">

Look at each word in the desired text output and check if it's followed by a
space. If so, the spaces value should be `True`. If not, it should be `False`.

</codeblock>

### Part 3

- Import the `Doc` from `spacy.tokens`.
- Complete the `words` and `spaces` to match the desired text and create a
  `doc`.

<codeblock id="02_05_03">

Pay attention to the individual tokens. To see how spaCy usually tokenizes that
string, you can try it and print the tokens for `nlp("Oh, really?!")`.

</codeblock>

</exercise>

<exercise id="6" title="Docs, spans and entities from scratch">

In this exercise, you'll create the `Doc` and `Span` objects manually, and
update the named entities – just like spaCy does behind the scenes. A shared
`nlp` object has already been created.

- Import the `Doc` and `Span` classes from `spacy.tokens`.
- Use the `Doc` class directly to create a `doc` from the words and spaces.
- Create a `Span` for "David Bowie" from the `doc` and assign it the label
  `"PERSON"`.
- Overwrite the `doc.ents` with a list of one entity, the "David Bowie" `span`.

<codeblock id="02_06">

- The `Doc` is initialized with three arguments: the shared vocab, e.g.
  `nlp.vocab`, a list of words and a list of boolean values indicating whether
  the word should be followed by a space.
- The `Span` class takes four arguments: the reference `doc`, the start token
  index, the end token index and an optional label.
- The `doc.ents` property is writable, so you can assign it any iterable
  consisting of `Span` objects.

</codeblock>

</exercise>

<exercise id="7" title="Data structures best practices">

The code in this example is trying to analyze a text and collect all proper
nouns that are followed by a verb.

```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Berlin looks like a nice city")

# Get all tokens and part-of-speech tags
token_texts = [token.text for token in doc]
pos_tags = [token.pos_ for token in doc]

for index, pos in enumerate(pos_tags):
    # Check if the current token is a proper noun
    if pos == "PROPN":
        # Check if the next token is a verb
        if pos_tags[index + 1] == "VERB":
            result = token_texts[index]
            print("Found proper noun before a verb:", result)
```

### Part 1

Why is the code bad?

<choice>

<opt text="The <code>result</code> token should be converted back to a <code>Token</code> object. This will let you reuse it in spaCy.">

It shouldn't be necessary to convert strings back to `Token` objects. Instead,
try to avoid converting tokens to strings if you still need to access their
attributes and relationships.

</opt>

<opt correct="true" text="It only uses lists of strings instead of native token attributes. This is often less efficient, and can't express complex relationships.">

Always convert the results to strings as late as possible, and try to use native
token attributes to keep things consistent.

</opt>

<opt text='<code>pos_</code> is the wrong attribute to use for extracting proper nouns. You should use <code>tag_</code> and the <code>"NNP"</code> and <code>"NNS"</code> labels instead.'>

The `.pos_` attribute returns the coarse-grained part-of-speech tag and
`"PROPN"` is the correct tag to check for proper nouns.

</opt>

</choice>

### Part 2

- Rewrite the code to use the native token attributes instead of lists of
  `token_texts` and `pos_tags`.
- Loop over each `token` in the `doc` and check the `token.pos_` attribute.
- Use `doc[token.i + 1]` to check for the next token and its `.pos_` attribute.
- If a proper noun before a verb is found, print its `token.text`.

<codeblock id="02_07">

- Remove the `token_texts` and `pos_tags` – we don't need to compile lists of
  strings upfront!
- Instead of iterating over the `pos_tags`, loop over each `token` in the `doc`
  and check the `token.pos_` attribute.
- To check if the next token is a verb, take a look at `doc[token.i + 1].pos_`.

</codeblock>

</exercise>

<exercise id="8" title="Word vectors and semantic similarity" type="slides">

<slides source="chapter2_03_word-vectors-similarity" start="15:58" end="19:47">
</slides>

</exercise>

<exercise id="9" title="Inspecting word vectors">

In this exercise, you'll use a larger
[English pipeline](https://spacy.io/models/en), which includes around 20.000
word vectors. The pipeline package is already pre-installed.

- Load the medium `"en_core_web_md"` pipeline with word vectors.
- Print the vector for `"bananas"` using the `token.vector` attribute.

<codeblock id="02_09">

- To load a trained pipeline, call `spacy.load` with its string name.
- To access a token in a doc, you can index into it. For example, `doc[4]`.

</codeblock>

</exercise>

<exercise id="10" title="Comparing similarities">

In this exercise, you'll be using spaCy's `similarity` methods to compare `Doc`,
`Token` and `Span` objects and get similarity scores.

### Part 1

- Use the `doc.similarity` method to compare `doc1` to `doc2` and print the
  result.

<codeblock id="02_10_01">

The `doc.similarity` method takes one argument: the other object to compare the
current object to.

</codeblock>

### Part 2

- Use the `token.similarity` method to compare `token1` to `token2` and print
  the result.

<codeblock id="02_10_02">

- The `token.similarity` method takes one argument: the other object to compare
  the current object to.

</codeblock>

### Part 3

- Create spans for "great restaurant"/"really nice bar".
- Use `span.similarity` to compare them and print the result.

<codeblock id="02_10_03"></codeblock>

</exercise>

<exercise id="11" title="Combining predictions and rules" type="slides">

<slides source="chapter2_04_models-rules" start="19:58" end="23:25">
</slides>

</exercise>

<exercise id="12" title="Debugging patterns (1)">

Why does this pattern not match the tokens "Silicon Valley" in the `doc`?

```python
pattern = [{"LOWER": "silicon"}, {"TEXT": " "}, {"LOWER": "valley"}]
```

```python
doc = nlp("Can Silicon Valley workers rein in big tech from within?")
```

<choice>

<opt text='The tokens "Silicon" and "Valley" are not lowercase, so the <code>"LOWER"</code> attribute won’t match.'>

The `"LOWER"` attribute in the pattern describes tokens whose _lowercase form_
matches a given value. So `{"LOWER": "valley"}` will match tokens like "Valley",
"VALLEY", "valley" etc.

</opt>

<opt correct="true" text='The tokenizer doesn’t create tokens for single spaces, so there’s no token with the value <code>" "</code> in between.'>

The tokenizer already takes care of splitting off whitespace and each dictionary
in the pattern describes one token.

</opt>

<opt text='The tokens are missing an operator <code>"OP"</code> to indicate that they should be matched exactly once.'>

By default, all tokens described by a pattern will be matched exactly once.
Operators are only needed to change this behavior – for example, to match zero
or more times.

</opt>

</choice>

</exercise>

<exercise id="13" title="Debugging patterns (2)">

Both patterns in this exercise contain mistakes and won't match as expected. Can
you fix them? If you get stuck, try printing the tokens in the `doc` to see how
the text will be split and adjust the pattern so that each dictionary represents
one token.

- Edit `pattern1` so that it correctly matches all case-insensitive mentions of
  `"Amazon"` plus a title-cased proper noun.
- Edit `pattern2` so that it correctly matches all case-insensitive mentions of
  `"ad-free"`, plus the following noun.

<codeblock id="02_13">

- Try processing the strings that should be matched with the `nlp` object – for
  example `[token.text for token in nlp("ad-free viewing")]`.
- Inspect the tokens and make sure each dictionary in the pattern correctly
  describes one token.

</codeblock>

</exercise>

<exercise id="14" title="Efficient phrase matching">

Sometimes it's more efficient to match exact strings instead of writing patterns
describing the individual tokens. This is especially true for finite categories
of things – like all countries of the world. We already have a list of
countries, so let's use this as the basis of our information extraction script.
A list of string names is available as the variable `COUNTRIES`.

- Import the `PhraseMatcher` and initialize it with the shared `vocab` as the
  variable `matcher`.
- Add the phrase patterns and call the matcher on the `doc`.

<codeblock id="02_14">

The shared `vocab` is available as `nlp.vocab`.

</codeblock>

</exercise>

<exercise id="15" title="Extracting countries and relationships">

In the previous exercise, you wrote a script using spaCy's `PhraseMatcher` to
find country names in text. Let's use that country matcher on a longer text,
analyze the syntax and update the document's entities with the matched
countries.

- Iterate over the matches and create a `Span` with the label `"GPE"`
  (geopolitical entity).
- Overwrite the entities in `doc.ents` and add the matched span.
- Get the matched span's root head token.
- Print the text of the head token and the span.

<codeblock id="02_15">

- Remember that the text is available as the variable `text`.
- The span's root token is available as `span.root`. A token's head is available
  via the `token.head` attribute.

</codeblock>

</exercise>
