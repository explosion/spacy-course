---
type: slides
---

# Combining predictions and rules

Notes: Combining predictions from statistical models with rule-based systems is
one of the most powerful tricks you should have in your NLP toolbox.

In this lesson, we'll take a look at how to do it with spaCy.

---

# Statistical predictions vs. rules

|                         | **Statistical models**                                      | **Rule-based systems**            |
| ----------------------- | ----------------------------------------------------------- | --------------------------------- |
| **Use cases**           | application needs to _generalize_ based on examples         | ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀ |
| **Real-world examples** | product names, person names, subject/object relationships   |                                   |
| **spaCy features**      | entity recognizer, dependency parser, part-of-speech tagger |                                   |

Notes: Statistical models are useful if your application needs to be able to
generalize based on a few examples.

For instance, detecting product or person names usually benefits from a trained
model. Instead of providing a list of all person names ever, your application
will be able to predict whether a span of tokens is a person name. Similarly,
you can predict dependency labels to find subject/object relationships.

To do this, you would use spaCy's entity recognizer, dependency parser or
part-of-speech tagger.

---

# Statistical predictions vs. rules

|                         | **Statistical models**                                      | **Rule-based systems**                                 |
| ----------------------- | ----------------------------------------------------------- | ------------------------------------------------------ |
| **Use cases**           | application needs to _generalize_ based on examples         | dictionary with finite number of examples              |
| **Real-world examples** | product names, person names, subject/object relationships   | countries of the world, cities, drug names, dog breeds |
| **spaCy features**      | entity recognizer, dependency parser, part-of-speech tagger | tokenizer, `Matcher`, `PhraseMatcher`                  |

Notes: Rule-based approaches on the other hand come in handy if there's a more
or less finite number of instances you want to find. For example, all countries
or cities of the world, drug names or even dog breeds.

In spaCy, you can achieve this with custom tokenization rules, as well as the
matcher and phrase matcher.

---

# Recap: Rule-based Matching

```python
# Initialize with the shared vocab
from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)

# Patterns are lists of dictionaries describing the tokens
pattern = [{"LEMMA": "love", "POS": "VERB"}, {"LOWER": "cats"}]
matcher.add("LOVE_CATS", [pattern])

# Operators can specify how often a token should be matched
pattern = [{"TEXT": "very", "OP": "+"}, {"TEXT": "happy"}]
matcher.add("VERY_HAPPY", [pattern])

# Calling matcher on doc returns list of (match_id, start, end) tuples
doc = nlp("I love cats and I'm very very happy")
matches = matcher(doc)
```

Notes: In the last chapter, you learned how to use spaCy's rule-based matcher to
find complex patterns in your texts. Here's a quick recap.

The matcher is initialized with the shared vocabulary – usually `nlp.vocab`.

Patterns are lists of dictionaries, and each dictionary describes one token and
its attributes. Patterns can be added to the matcher using the `matcher.add`
method.

Operators let you specify how often to match a token. For example, "+" will
match one or more times.

Calling the matcher on a doc object will return a list of the matches. Each
match is a tuple consisting of an ID, and the start and end token index in the
document.

---

# Adding statistical predictions

```python
matcher = Matcher(nlp.vocab)
matcher.add("DOG", [[{"LOWER": "golden"}, {"LOWER": "retriever"}]])
doc = nlp("I have a Golden Retriever")

for match_id, start, end in matcher(doc):
    span = doc[start:end]
    print("Matched span:", span.text)
    # Get the span's root token and root head token
    print("Root token:", span.root.text)
    print("Root head token:", span.root.head.text)
    # Get the previous token and its POS tag
    print("Previous token:", doc[start - 1].text, doc[start - 1].pos_)
```

```out
Matched span: Golden Retriever
Root token: Retriever
Root head token: have
Previous token: a DET
```

Notes: Here's an example of a matcher rule for "golden retriever".

If we iterate over the matches returned by the matcher, we can get the match ID
and the start and end index of the matched span. We can then find out more about
it. `Span` objects give us access to the original document and all other token
attributes and linguistic features predicted by a model.

For example, we can get the span's root token. If the span consists of more than
one token, this will be the token that decides the category of the phrase. For
example, the root of "Golden Retriever" is "Retriever". We can also find the
head token of the root. This is the syntactic "parent" that governs the phrase –
in this case, the verb "have".

Finally, we can look at the previous token and its attributes. In this case,
it's a determiner, the article "a".

---

# Efficient phrase matching (1)

- `PhraseMatcher` like regular expressions or keyword search – but with access
  to the tokens!
- Takes `Doc` object as patterns
- More efficient and faster than the `Matcher`
- Great for matching large word lists

Notes: The phrase matcher is another helpful tool to find sequences of words in
your data.

It performs a keyword search on the document, but instead of only finding
strings, it gives you direct access to the tokens in context.

It takes `Doc` objects as patterns.

It's also really fast.

This makes it very useful for matching large dictionaries and word lists on
large volumes of text.

---

# Efficient phrase matching (2)

```python
from spacy.matcher import PhraseMatcher

matcher = PhraseMatcher(nlp.vocab)

pattern = nlp("Golden Retriever")
matcher.add("DOG", [pattern])
doc = nlp("I have a Golden Retriever")

# Iterate over the matches
for match_id, start, end in matcher(doc):
    # Get the matched span
    span = doc[start:end]
    print("Matched span:", span.text)
```

```out
Matched span: Golden Retriever
```

Notes: Here's an example.

The phrase matcher can be imported from `spacy.matcher` and follows the same API
as the regular matcher.

Instead of a list of dictionaries, we pass in a `Doc` object as the pattern.

We can then iterate over the matches in the text, which gives us the match ID,
and the start and end of the match. This lets us create a `Span` object for the
matched tokens "Golden Retriever" to analyze it in context.

---

# Let's practice!

Notes: Let's try out some of the new techniques for combining rules with
predictions.
