---
type: slides
---

# Creating a training corpus

Notes: TODO

---

# Training vs. evaluation data

- **Training data:** used to update the model
- **Evaluation data:**
  - data the model hasn't seen during training
  - used to calculate how accurate model is
  - should be representative of the data the model will see at runtime

Notes: When training your model, it's important to know how it's doing and
whether it's learning the right thing. This is done by comparing the model's
predictions on examples it _hasn't_ seen during training to answers we already
know. So in addition to the training data, you also need evaluation data, also
called development data.

The evaluation data is used to calculate how accurate your model is. For
example, an accuracy score of 90% means that the model predicted 90% of the
evaluation examples correctly.

This also means that the evaluation data needs to be representative of the data
your model will see at runtime. Otherwise, the accuracy score will be
meaningless, because it won't tell you how good your model _really_ is.

---

# Generating a training corpus (1)

```python
import spacy

nlp = spacy.blank("en")

# Create a Doc with entity spans
doc1 = nlp("iPhone X is coming")
doc1.ents = [Span(doc1, 0, 1, label="GADGET")]
# Create another doc without entity spans
doc2 = nlp("I need a new phone! Any tips?")

docs = [doc1, doc2]  # and so on...
```

Notes: spaCy can be updated from data in the same format it creates: `Doc`
objects. You already learned all about creating `Doc` and `Span` objects in
chapter 2.

In this example, we're creating two `Doc` objects for our corpus: one that
contains an entity and another one that doesn't contain any entities. To set the
entities on the `Doc`, we can write add a `Span` to the `doc.ents`.

Of course, you'll need a lot more examples to effectively train your model to
generalize and predict similar entities in context. Depending on the task, you
usually want at least a few hundred to a few thousand representative examples.

---

# Generating a training corpus (2)

- split data into two portions:
  - **training data:** used to update the model
  - **development data:** used to evaluate the model

```python
random.shuffle(docs)
train_docs = docs[:len(docs) // 2)]
dev_docs = docs[len(docs) // 2):]
```

Notes: As I mentioned earlier, we don't just need data to train the model. We
also want to evaluate its accuracy on examples it hasn't seen during training.
This is usually done by shuffling and splitting your data in two: one portion
for training and one for evaluation. Here, we're using a simple 50/50 split.

---

# Generating a training corpus (3)

- `DocBin`: container to efficiently store and save `Doc` objects
- can be saved to a binary file
- binary files are used for training

```python
# Create and save a collection of training docs
train_docbin = DocBin(docs=train_docs)
train_docbin.to_disk("./train.spacy")
# Create and save a collection of evaluation docs
dev_docbin = DocBin(docs=dev_docs)
dev_docbin.to_disk("./dev.spacy")
```

Notes: You typically want to store your training and development data as files
on disk so you can load them into spaCy's training process.

The `DocBin` is a container for efficiently storing and serializing `Doc`
objects. You can instantiate it with a list of `Doc` objects and call its
`to_disk` method to save it to a binary file. We typically use the file
extension `.spacy` for these files.

Compared to other binary serializatipn protocols like `pickle`, the `DocBin` is
faster and produces smaller file sizes because it only stores the shared
vocabulary once. You can read more about how it works in the
[documentation](https://spacy.io/api/docbin).

---

# Tip: Converting your data

- `spacy convert` lets you convert corpora in common formats
- supports `.conll`, `.conllu`, `.iob` and spaCy's old JSON format

```bash
$ python -m spacy convert ./train.gold.conll ./corpus
```

Notes: In some cases, you might already have training and development data in a
common format – for example, CoNLL or IOB. spaCy's `convert` command
automatically converts these files into spaCy's binary format. It also converts
JSON files in the old format used by spaCy v2.

---

# Let's practice!

Notes: Now it's time to get started and prepare the training corpus. Let's look
at some examples and create a small dataset for a new entity type.
