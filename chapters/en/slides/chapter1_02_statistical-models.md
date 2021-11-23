---
type: slides
---

# Trained pipelines

Notes: Let's add some more power to the `nlp` object!

In this lesson, you'll learn about spaCy's trained pipelines.

---

# What are trained pipelines?

- Models that enable spaCy to predict linguistic attributes _in context_
  - Part-of-speech tags
  - Syntactic dependencies
  - Named entities
- Trained on labeled example texts
- Can be updated with more examples to fine-tune predictions

Notes: Some of the most interesting things you can analyze are context-specific:
for example, whether a word is a verb or whether a span of text is a person
name.

Trained pipeline components have statistical models that enable spaCy to make
predictions in context. This usually includes part-of speech tags, syntactic
dependencies and named entities.

Pipelines are trained on large datasets of labeled example texts.

They can be updated with more examples to fine-tune their predictions – for
example, to perform better on your specific data.

---

# Pipeline Packages

<img src="/package.png" alt="A package with the label en_core_web_sm" width="30%" align="right" />

```bash
$ python -m spacy download en_core_web_sm
```

```python
import spacy

nlp = spacy.load("en_core_web_sm")
```

- Binary weights
- Vocabulary
- Meta information
- Configuration file

Notes: spaCy provides a number of trained pipeline packages you can download
using the `spacy download` command. For example, the "en_core_web_sm" package is
a small English pipeline that supports all core capabilities and is trained on
web text.

The `spacy.load` method loads a pipeline package by name and returns an `nlp`
object.

The package provides the binary weights that enable spaCy to make predictions.

It also includes the vocabulary, meta information about the pipeline and the
configuration file used to train it. It tells spaCy which language class to use
and how to configure the processing pipeline.

---

# Predicting Part-of-speech Tags

```python
import spacy

# Load the small English pipeline
nlp = spacy.load("en_core_web_sm")

# Process a text
doc = nlp("She ate the pizza")

# Iterate over the tokens
for token in doc:
    # Print the text and the predicted part-of-speech tag
    print(token.text, token.pos_)
```

```out
She PRON
ate VERB
the DET
pizza NOUN
```

Notes: Let's take a look at the model's predictions. In this example, we're
using spaCy to predict part-of-speech tags, the word types in context.

First, we load the small English pipeline and receive an `nlp` object.

Next, we're processing the text "She ate the pizza".

For each token in the doc, we can print the text and the `.pos_` attribute, the
predicted part-of-speech tag.

In spaCy, attributes that return strings usually end with an underscore –
attributes without the underscore return an integer ID value.

Here, the model correctly predicted "ate" as a verb and "pizza" as a noun.

---

# Predicting Syntactic Dependencies

```python
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)
```

```out
She PRON nsubj ate
ate VERB ROOT ate
the DET det pizza
pizza NOUN dobj ate
```

Notes: In addition to the part-of-speech tags, we can also predict how the words
are related. For example, whether a word is the subject of the sentence or an
object.

The `.dep_` attribute returns the predicted dependency label.

The `.head` attribute returns the syntactic head token. You can also think of it
as the parent token this word is attached to.

---

# Dependency label scheme

<img src="/dep_example.png" alt="Visualization of the dependency graph for 'She ate the pizza'" />

| Label     | Description          | Example |
| --------- | -------------------- | ------- |
| **nsubj** | nominal subject      | She     |
| **dobj**  | direct object        | pizza   |
| **det**   | determiner (article) | the     |

Notes: To describe syntactic dependencies, spaCy uses a standardized label
scheme. Here's an example of some common labels:

The pronoun "She" is a nominal subject attached to the verb – in this case, to
"ate".

The noun "pizza" is a direct object attached to the verb "ate". It is eaten by
the subject, "she".

The determiner "the", also known as an article, is attached to the noun "pizza".

---

# Predicting Named Entities

<img src="/ner_example.png" alt="Visualization of the named entities in 'Apple is looking at buying U.K. startup for $1 billion'" width="80%" />

```python
# Process a text
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

# Iterate over the predicted entities
for ent in doc.ents:
    # Print the entity text and its label
    print(ent.text, ent.label_)
```

```out
Apple ORG
U.K. GPE
$1 billion MONEY
```

Notes: Named entities are "real world objects" that are assigned a name – for
example, a person, an organization or a country.

The `doc.ents` property lets you access the named entities predicted by the
named entity recognition model.

It returns an iterator of `Span` objects, so we can print the entity text and
the entity label using the `.label_` attribute.

In this case, the model is correctly predicting "Apple" as an organization,
"U.K." as a geopolitical entity and "\$1 billion" as money.

---

# Tip: the spacy.explain method

Get quick definitions of the most common tags and labels.

```python
spacy.explain("GPE")
```

```out
'Countries, cities, states'
```

```python
spacy.explain("NNP")
```

```out
'noun, proper singular'
```

```python
spacy.explain("dobj")
```

```out
'direct object'
```

Notes: A quick tip: To get definitions for the most common tags and labels, you
can use the `spacy.explain` helper function.

For example, "GPE" for geopolitical entity isn't exactly intuitive – but
`spacy.explain` can tell you that it refers to countries, cities and states.

The same works for part-of-speech tags and dependency labels.

---

# Let's practice!

Notes: Now it's your turn. Let's take a look at spaCy's trained pipelines and
their models' predictions.
