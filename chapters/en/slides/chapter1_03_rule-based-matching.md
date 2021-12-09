---
type: slides
---

# Rule-based matching

Notes: In this lesson, we'll take a look at spaCy's matcher, which lets you
write rules to find words and phrases in text.

---

# Why not just regular expressions?

- Match on `Doc` objects, not just strings
- Match on tokens and token attributes
- Use a model's predictions
- Example: "duck" (verb) vs. "duck" (noun)

Notes: Compared to regular expressions, the matcher works with `Doc` and `Token`
objects instead of only strings.

It's also more flexible: you can search for texts but also other lexical
attributes.

You can even write rules that use a model's predictions.

For example, find the word "duck" only if it's a verb, not a noun.

---

# Match patterns

- Lists of dictionaries, one per token

- Match exact token texts

```python
[{"TEXT": "iPhone"}, {"TEXT": "X"}]
```

- Match lexical attributes

```python
[{"LOWER": "iphone"}, {"LOWER": "x"}]
```

- Match any token attributes

```python
[{"LEMMA": "buy"}, {"POS": "NOUN"}]
```

Notes: Match patterns are lists of dictionaries. Each dictionary describes one
token. The keys are the names of token attributes, mapped to their expected
values.

In this example, we're looking for two tokens with the text "iPhone" and "X".

We can also match on other token attributes. Here, we're looking for two tokens
whose lowercase forms equal "iphone" and "x".

We can even write patterns using attributes predicted by a model. Here, we're
matching a token with the lemma "buy", plus a noun. The lemma is the base form,
so this pattern would match phrases like "buying milk" or "bought flowers".

---

# Using the Matcher (1)

```python
import spacy

# Import the Matcher
from spacy.matcher import Matcher

# Load a pipeline and create the nlp object
nlp = spacy.load("en_core_web_sm")

# Initialize the matcher with the shared vocab
matcher = Matcher(nlp.vocab)

# Add the pattern to the matcher
pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]
matcher.add("IPHONE_PATTERN", [pattern])

# Process some text
doc = nlp("Upcoming iPhone X release date leaked")

# Call the matcher on the doc
matches = matcher(doc)
```

Notes: To use a pattern, we first import the matcher from `spacy.matcher`.

We also load a pipeline and create the `nlp` object.

The matcher is initialized with the shared vocabulary, `nlp.vocab`. You'll learn
more about this later – for now, just remember to always pass it in.

The `matcher.add` method lets you add a pattern. The first argument is a unique
ID to identify which pattern was matched. The second argument is a list of
patterns.

To match the pattern on a text, we can call the matcher on any doc.

This will return the matches.

---

# Using the Matcher (2)

```python
# Call the matcher on the doc
doc = nlp("Upcoming iPhone X release date leaked")
matches = matcher(doc)

# Iterate over the matches
for match_id, start, end in matches:
    # Get the matched span
    matched_span = doc[start:end]
    print(matched_span.text)
```

```out
iPhone X
```

- `match_id`: hash value of the pattern name
- `start`: start index of matched span
- `end`: end index of matched span

Notes: When you call the matcher on a doc, it returns a list of tuples.

Each tuple consists of three values: the match ID, the start index and the end
index of the matched span.

This means we can iterate over the matches and create a `Span` object: a slice
of the doc at the start and end index.

---

# Matching lexical attributes

```python
pattern = [
    {"IS_DIGIT": True},
    {"LOWER": "fifa"},
    {"LOWER": "world"},
    {"LOWER": "cup"},
    {"IS_PUNCT": True}
]
```

```python
doc = nlp("2018 FIFA World Cup: France won!")
```

```out
2018 FIFA World Cup:
```

Notes: Here's an example of a more complex pattern using lexical attributes.

We're looking for five tokens:

A token consisting of only digits.

Three case-insensitive tokens for "fifa", "world" and "cup".

And a token that consists of punctuation.

The pattern matches the tokens "2018 FIFA World Cup:".

---

# Matching other token attributes

```python
pattern = [
    {"LEMMA": "love", "POS": "VERB"},
    {"POS": "NOUN"}
]
```

```python
doc = nlp("I loved dogs but now I love cats more.")
```

```out
loved dogs
love cats
```

Note: In this example, we're looking for two tokens:

A verb with the lemma "love", followed by a noun.

This pattern will match "loved dogs" and "love cats".

---

# Using operators and quantifiers (1)

```python
pattern = [
    {"LEMMA": "buy"},
    {"POS": "DET", "OP": "?"},  # optional: match 0 or 1 times
    {"POS": "NOUN"}
]
```

```python
doc = nlp("I bought a smartphone. Now I'm buying apps.")
```

```out
bought a smartphone
buying apps
```

Notes: Operators and quantifiers let you define how often a token should be
matched. They can be added using the "OP" key.

Here, the "?" operator makes the determiner token optional, so it will match a
token with the lemma "buy", an optional article and a noun.

---

# Using operators and quantifiers (2)

| Example       | Description                  |
| ------------- | ---------------------------- |
| `{"OP": "!"}` | Negation: match 0 times      |
| `{"OP": "?"}` | Optional: match 0 or 1 times |
| `{"OP": "+"}` | Match 1 or more times        |
| `{"OP": "*"}` | Match 0 or more times        |

Notes: "OP" can have one of four values:

An "!" negates the token, so it's matched 0 times.

A "?" makes the token optional, and matches it 0 or 1 times.

A "+" matches a token 1 or more times.

And finally, an "\*" matches 0 or more times.

Operators can make your patterns a lot more powerful, but they also add more
complexity – so use them wisely.

---

# Let's practice!

Notes: Token-based matching opens up a lot of new possibilities for information
extraction. So let's try it out and write some patterns!
