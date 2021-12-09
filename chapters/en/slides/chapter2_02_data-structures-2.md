---
type: slides
---

# Data Structures (2): Doc, Span and Token

Notes: Now that you know all about the vocabulary and string store, we can take
a look at the most important data structure: the `Doc`, and its views `Token`
and `Span`.

---

# The Doc object

```python
# Create an nlp object
import spacy
nlp = spacy.blank("en")

# Import the Doc class
from spacy.tokens import Doc

# The words and spaces to create the doc from
words = ["Hello", "world", "!"]
spaces = [True, False, False]

# Create a doc manually
doc = Doc(nlp.vocab, words=words, spaces=spaces)
```

Notes: The `Doc` is one of the central data structures in spaCy. It's created
automatically when you process a text with the `nlp` object. But you can also
instantiate the class manually.

After creating the `nlp` object, we can import the `Doc` class from
`spacy.tokens`.

Here we're creating a doc from three words. The spaces are a list of boolean
values indicating whether the word is followed by a space. Every token includes
that information – even the last one!

The `Doc` class takes three arguments: the shared vocab, the words and the
spaces.

---

# The Span object (1)

<img src="/span_indices.png" width="65%" alt="Illustration of a Span object within a Doc with token indices" />

Notes: A `Span` is a slice of a doc consisting of one or more tokens. The `Span`
takes at least three arguments: the doc it refers to, and the start and end
index of the span. Remember that the end index is exclusive!

---

# The Span object (2)

```python
# Import the Doc and Span classes
from spacy.tokens import Doc, Span

# The words and spaces to create the doc from
words = ["Hello", "world", "!"]
spaces = [True, False, False]

# Create a doc manually
doc = Doc(nlp.vocab, words=words, spaces=spaces)

# Create a span manually
span = Span(doc, 0, 2)

# Create a span with a label
span_with_label = Span(doc, 0, 2, label="GREETING")

# Add span to the doc.ents
doc.ents = [span_with_label]
```

Notes: To create a `Span` manually, we can also import the class from
`spacy.tokens`. We can then instantiate it with the doc and the span's start and
end index, and an optional label argument.

The `doc.ents` are writable, so we can add entities manually by overwriting it
with a list of spans.

---

# Best practices

- `Doc` and `Span` are very powerful and hold references and relationships of
  words and sentences
  - **Convert result to strings as late as possible**
  - **Use token attributes if available** – for example, `token.i` for the token
    index
- Don't forget to pass in the shared `vocab`

Notes: A few tips and tricks before we get started:

The `Doc` and `Span` are very powerful and optimized for performance. They give
you access to all references and relationships of the words and sentences.

If your application needs to output strings, make sure to convert the doc as
late as possible. If you do it too early, you'll lose all relationships between
the tokens.

To keep things consistent, try to use built-in token attributes wherever
possible. For example, `token.i` for the token index.

Also, don't forget to always pass in the shared vocab!

---

# Let's practice!

Notes: Now let's try this out and create some docs and spans from scratch.
