---
type: slides
---

# Introduction to spaCy

Notes: Hi, I'm Ines! I'm one of the core developers of spaCy, a popular library
for advanced Natural Language Processing in Python.

In this lesson, we'll take a look at the most important concepts of spaCy and
how to get started.

---

# The nlp object

```python
# Import spaCy
import spacy

# Create a blank English nlp object
nlp = spacy.blank("en")
```

- contains the processing pipeline
- includes language-specific rules for tokenization etc.

Notes: At the center of spaCy is the object containing the processing pipeline.
We usually call this variable "nlp".

For example, to create an English `nlp` object, you can import the `spacy` and
use the `spacy.blank` method to create a blank English pipeline. You can use the
`nlp` object like a function to analyze text.

It contains all the different components in the pipeline.

It also includes language-specific rules used for tokenizing the text into words
and punctuation. spaCy supports a variety of languages.

---

# The Doc object

```python
# Created by processing a string of text with the nlp object
doc = nlp("Hello world!")

# Iterate over tokens in a Doc
for token in doc:
    print(token.text)
```

```out
Hello
world
!
```

Notes: When you process a text with the `nlp` object, spaCy creates a `Doc`
object – short for "document". The Doc lets you access information about the
text in a structured way, and no information is lost.

The Doc behaves like a normal Python sequence by the way and lets you iterate
over its tokens, or get a token by its index. But more on that later!

---

# The Token object

<img src="/doc.png" alt="Illustration of a Doc object containing four tokens" width="50%" />

```python
doc = nlp("Hello world!")

# Index into the Doc to get a single Token
token = doc[1]

# Get the token text via the .text attribute
print(token.text)
```

```out
world
```

Notes: `Token` objects represent the tokens in a document – for example, a word
or a punctuation character.

To get a token at a specific position, you can index into the doc.

`Token` objects also provide various attributes that let you access more
information about the tokens. For example, the `.text` attribute returns the
verbatim token text.

---

# The Span object

<img src="/doc_span.png" width="50%" alt="Illustration of a Doc object containing four tokens and three of them wrapped in a Span" />

```python
doc = nlp("Hello world!")

# A slice from the Doc is a Span object
span = doc[1:3]

# Get the span text via the .text attribute
print(span.text)
```

```out
world!
```

Notes: A `Span` object is a slice of the document consisting of one or more
tokens. It's only a view of the `Doc` and doesn't contain any data itself.

To create a span, you can use Python's slice notation. For example, `1:3` will
create a slice starting from the token at position 1, up to – but not including!
– the token at position 3.

---

# Lexical Attributes

```python
doc = nlp("It costs $5.")
```

```python
print("Index:   ", [token.i for token in doc])
print("Text:    ", [token.text for token in doc])

print("is_alpha:", [token.is_alpha for token in doc])
print("is_punct:", [token.is_punct for token in doc])
print("like_num:", [token.like_num for token in doc])
```

```out
Index:    [0, 1, 2, 3, 4]
Text:     ['It', 'costs', '$', '5', '.']

is_alpha: [True, True, False, False, False]
is_punct: [False, False, False, False, True]
like_num: [False, False, False, True, False]
```

Notes: Here you can see some of the available token attributes:

`i` is the index of the token within the parent document.

`text` returns the token text.

`is_alpha`, `is_punct` and `like_num` return boolean values indicating whether
the token consists of alphabetic characters, whether it's punctuation or whether
it _resembles_ a number. For example, a token "10" – one, zero – or the word
"ten" – T, E, N.

These attributes are also called lexical attributes: they refer to the entry in
the vocabulary and don't depend on the token's context.

---

# Let's practice!

Notes: Let's see this in action and process your first text with spaCy.
