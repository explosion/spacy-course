---
type: slides
---

# Processing pipelines

Notes: Welcome back! This chapter is dedicated to processing pipelines: a series
of functions applied to a doc to add attributes like part-of-speech tags,
dependency labels or named entities.

In this lesson, you'll learn about the pipeline components provided by spaCy,
and what happens behind the scenes when you call nlp on a string of text.

---

# What happens when you call nlp?

<img src="/pipeline.png" alt="Illustration of the spaCy pipeline transforming a text into a processed Doc" width="90%" />

```python
doc = nlp("This is a sentence.")
```

Notes: You've already written this plenty of times by now: pass a string of text
to the `nlp` object, and receive a `Doc` object.

But what does the `nlp` object _actually_ do?

First, the tokenizer is applied to turn the string of text into a `Doc` object.
Next, a series of pipeline components is applied to the doc in order. In this
case, the tagger, then the parser, then the entity recognizer. Finally, the
processed doc is returned, so you can work with it.

---

# Built-in pipeline components

| Name        | Description             | Creates                                                   |
| ----------- | :---------------------- | :-------------------------------------------------------- |
| **tagger**  | Part-of-speech tagger   | `Token.tag`, `Token.pos`                                  |
| **parser**  | Dependency parser       | `Token.dep`, `Token.head`, `Doc.sents`, `Doc.noun_chunks` |
| **ner**     | Named entity recognizer | `Doc.ents`, `Token.ent_iob`, `Token.ent_type`             |
| **textcat** | Text classifier         | `Doc.cats`                                                |

Notes: spaCy ships with the following built-in pipeline components.

The part-of-speech tagger sets the `token.tag` and `token.pos` attributes.

The dependency parser adds the `token.dep` and `token.head` attributes and is
also responsible for detecting sentences and base noun phrases, also known as
noun chunks.

The named entity recognizer adds the detected entities to the `doc.ents`
property. It also sets entity type attributes on the tokens that indicate if a
token is part of an entity or not.

Finally, the text classifier sets category labels that apply to the whole text,
and adds them to the `doc.cats` property.

Because text categories are always very specific, the text classifier is not
included in any of the pre-trained models by default. But you can use it to
train your own system.

---

# Under the hood

<img src="/package_meta.png" alt="Illustration of a package labelled en_core_web_sm, folders and file and the meta.json" />

- Pipeline defined in model's `meta.json` in order
- Built-in components need binary data to make predictions

Notes: All models you can load into spaCy include several files and a
`meta.json`.

The meta defines things like the language and pipeline. This tells spaCy which
components to instantiate.

The built-in components that make predictions also need binary data. The data is
included in the model package and loaded into the component when you load the
model.

---

# Pipeline attributes

- `nlp.pipe_names`: list of pipeline component names

```python
print(nlp.pipe_names)
```

```out
['tagger', 'parser', 'ner']
```

- `nlp.pipeline`: list of `(name, component)` tuples

```python
print(nlp.pipeline)
```

```out
[('tagger', <spacy.pipeline.Tagger>),
 ('parser', <spacy.pipeline.DependencyParser>),
 ('ner', <spacy.pipeline.EntityRecognizer>)]
```

Notes: To see the names of the pipeline components present in the current nlp
object, you can use the `nlp.pipe_names` attribute.

For a list of component name and component function tuples, you can use the
`nlp.pipeline` attribute.

The component functions are the functions applied to the doc to process it and
set attributes – for example, part-of-speech tags or named entities.

---

# Let's practice!

Notes: Let's check out some spaCy pipelines and take a look under the hood!
