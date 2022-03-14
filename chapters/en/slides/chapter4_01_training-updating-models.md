---
type: slides
---

# Training and updating models

Notes: Welcome to the final chapter, which is about one of the most exciting
aspects of modern NLP: training your own models!

In this lesson, you'll learn about training and updating spaCy's pipeline
components and their neural network models, and the data you need for it –
focusing specifically on the named entity recognizer.

---

# Why update the model?

- Better results on your specific domain
- Learn classification schemes specifically for your problem
- Essential for text classification
- Very useful for named entity recognition
- Less critical for part-of-speech tagging and dependency parsing

Notes: Before we get starting with explaining _how_, it's worth taking a second
to ask ourselves: Why would we want to update the model with our own examples?
Why can't we just rely on pre-trained pipelines?

Statistical models make predictions based on the examples they were trained on.

You can usually make the model more accurate by showing it examples from your
domain.

You often also want to predict categories specific to your problem, so the model
needs to learn about them.

This is essential for text classification, very useful for entity recognition
and a little less critical for tagging and parsing.

---

# How training works (1)

1. **Initialize** the model weights randomly
2. **Predict** a few examples with the current weights
3. **Compare** prediction with true labels
4. **Calculate** how to change weights to improve predictions
5. **Update** weights slightly
6. Go back to 2.

Notes: spaCy supports updating existing models with more examples, and training
new models. If we're not starting with a trained pipeline, we first initialize
the weights randomly.

Next, spaCy calls `nlp.update`, which predicts a batch of examples with the
current weights.

The model then checks the predictions against the correct answers, and decides
how to change the weights to achieve better predictions next time.

Finally, we make a small correction to the current weights and move on to the
next batch of examples.

spaCy then continues calling `nlp.update` for each batch of examples in the
data. During training, you usually want to make multiple passes over the data
and train until the model stops improving.

---

# How training works (2)

<img src="/training.png" alt="Diagram of the training process" />

- **Training data:** Examples and their annotations.
- **Text:** The input text the model should predict a label for.
- **Label:** The label the model should predict.
- **Gradient:** How to change the weights.

Notes: Here's an illustration showing the process.

The training data are the examples we want to update the model with.

The text should be a sentence, paragraph or longer document. For the best
results, it should be similar to what the model will see at runtime.

The label is what we want the model to predict. This can be a text category, or
an entity span and its type.

The gradient is how we should change the model to reduce the current error. It's
computed when we compare the predicted label to the true label.

After training, we can then save out an updated model and use it in our
application.

---

# Example: Training the entity recognizer

- The entity recognizer tags words and phrases in context
- Each token can only be part of one entity
- Examples need to come with context

```python
doc = nlp("iPhone X is coming")
doc.ents = [Span(doc, 0, 2, label="GADGET")]
```

- Texts with no entities are also important

```python
doc = nlp("I need a new phone! Any tips?")
doc.ents = []
```

- **Goal:** teach the model to generalize

Notes: Let's look at an example for a specific component: the entity recognizer.

The entity recognizer takes a document and predicts phrases and their labels _in
context_. This means that the training data needs to include texts, the entities
they contain, and the entity labels.

Entities can't overlap, so each token can only be part of one entity.

The easiest way to do this is to show the model a text and entity spans. spaCy
can be updated from regular `Doc` objects with entities annotated as the
`doc.ents`. For example, "iPhone X" is a gadget, starts at token 0 and ends at
token 1.

It's also very important for the model to learn words that _aren't_ entities.

In this case, the list of span annotations will be empty.

Our goal is to teach the model to recognize new entities in similar contexts,
even if they weren't in the training data.

---

# The training data

- Examples of what we want the model to predict in context
- Update an **existing model**: a few hundred to a few thousand examples
- Train a **new category**: a few thousand to a million examples
  - spaCy's English models: 2 million words
- Usually created manually by human annotators
- Can be semi-automated – for example, using spaCy's `Matcher`!

Notes: The training data tells the model what we want it to predict. This could
be texts and named entities we want to recognize, tokens and their correct
part-of-speech tags or anything else the model should predict.

To update an existing model, we can start with a few hundred to a few thousand
examples.

To train a new category we may need up to a million.

spaCy's trained English pipelines for instance were trained on 2 million words
labelled with part-of-speech tags, dependencies and named entities.

Training data is usually created by humans who assign labels to texts.

This is a lot of work, but can be semi-automated – for example, using spaCy's
`Matcher`.

---

# Training vs. evaluation data

- **Training data:** used to update the model
- **Evaluation data:**
  - data the model hasn't seen during training
  - used to calculate how accurate the model is
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
doc1.ents = [Span(doc1, 0, 2, label="GADGET")]
# Create another doc without entity spans
doc2 = nlp("I need a new phone! Any tips?")

docs = [doc1, doc2]  # and so on...
```

Notes: spaCy can be updated from data in the same format it creates: `Doc`
objects. You already learned all about creating `Doc` and `Span` objects in
chapter 2.

In this example, we're creating two `Doc` objects for our corpus: one that
contains an entity and another one that doesn't contain any entities. To set the
entities on the `Doc`, we can add a `Span` to the `doc.ents`.

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
train_docs = docs[:len(docs) // 2]
dev_docs = docs[len(docs) // 2:]
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

Compared to other binary serialization protocols like `pickle`, the `DocBin` is
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
