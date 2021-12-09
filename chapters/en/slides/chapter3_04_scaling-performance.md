---
type: slides
---

# Scaling and performance

Notes: In this lesson, I'll show you a few tips and tricks to make your spaCy
pipelines run as fast as possible, and process large volumes of text
efficiently.

---

# Processing large volumes of text

- Use `nlp.pipe` method
- Processes texts as a stream, yields `Doc` objects
- Much faster than calling `nlp` on each text

**BAD:**

```python
docs = [nlp(text) for text in LOTS_OF_TEXTS]
```

**GOOD:**

```python
docs = list(nlp.pipe(LOTS_OF_TEXTS))
```

Notes: If you need to process a lot of texts and create a lot of `Doc` objects
in a row, the `nlp.pipe` method can speed this up significantly.

It processes the texts as a stream and yields `Doc` objects.

It is much faster than just calling nlp on each text, because it batches up the
texts.

`nlp.pipe` is a generator that yields `Doc` objects, so in order to get a list
of docs, remember to call the `list` method around it.

---

# Passing in context (1)

- Setting `as_tuples=True` on `nlp.pipe` lets you pass in `(text, context)`
  tuples
- Yields `(doc, context)` tuples
- Useful for associating metadata with the `doc`

```python
data = [
    ("This is a text", {"id": 1, "page_number": 15}),
    ("And another text", {"id": 2, "page_number": 16}),
]

for doc, context in nlp.pipe(data, as_tuples=True):
    print(doc.text, context["page_number"])
```

```out
This is a text 15
And another text 16
```

Notes: `nlp.pipe` also supports passing in tuples of text / context if you set
`as_tuples` to `True`.

The method will then yield doc / context tuples.

This is useful for passing in additional metadata, like an ID associated with
the text, or a page number.

---

# Passing in context (2)

```python
from spacy.tokens import Doc

Doc.set_extension("id", default=None)
Doc.set_extension("page_number", default=None)

data = [
    ("This is a text", {"id": 1, "page_number": 15}),
    ("And another text", {"id": 2, "page_number": 16}),
]

for doc, context in nlp.pipe(data, as_tuples=True):
    doc._.id = context["id"]
    doc._.page_number = context["page_number"]
```

Notes: You can even add the context metadata to custom attributes.

In this example, we're registering two extensions, `id` and `page_number`, which
default to `None`.

After processing the text and passing through the context, we can overwrite the
doc extensions with our context metadata.

---

# Using only the tokenizer (1)

<img src="/pipeline.png" width="90%" alt="Illustration of the spaCy pipeline">

- don't run the whole pipeline!

Notes: Another common scenario: Sometimes you already have a model loaded to do
other processing, but you only need the tokenizer for one particular text.

Running the whole pipeline is unnecessarily slow, because you'll be getting a
bunch of predictions from the model that you don't need.

---

# Using only the tokenizer (2)

- Use `nlp.make_doc` to turn a text into a `Doc` object

**BAD:**

```python
doc = nlp("Hello world")
```

**GOOD:**

```python
doc = nlp.make_doc("Hello world!")
```

Notes: If you only need a tokenized `Doc` object, you can use the `nlp.make_doc`
method instead, which takes a text and returns a doc.

This is also how spaCy does it behind the scenes: `nlp.make_doc` turns the text
into a doc before the pipeline components are called.

---

# Disabling pipeline components

- Use `nlp.select_pipes` to temporarily disable one or more pipes

```python
# Disable tagger and parser
with nlp.select_pipes(disable=["tagger", "parser"]):
    # Process the text and print the entities
    doc = nlp(text)
    print(doc.ents)
```

- Restores them after the `with` block
- Only runs the remaining components

Notes: spaCy also allows you to temporarily disable pipeline components using
the `nlp.select_pipes` context manager.

It accepts the keyword arguments `enable` or `disable` that can define a list of
string names of the pipeline components to disable. For example, if you only
want to use the entity recognizer to process a document, you can temporarily
disable the tagger and parser.

After the `with` block, the disabled pipeline components are automatically
restored.

In the `with` block, spaCy will only run the remaining components.

---

# Let's practice!

Notes: Now it's your turn. Let's try out the new methods and optimize some code
to be faster and more efficient.
