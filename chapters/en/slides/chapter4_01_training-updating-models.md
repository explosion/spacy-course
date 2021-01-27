---
type: slides
---

# Training and updating models

Notes: Welcome to the final chapter, which is about one of the most exciting
aspects of modern NLP: training your own models!

In this lesson, you'll learn about training and updating spaCy's neural network
models and the data you need for it – focusing specifically on the named entity
recognizer.

---

# Why updating the model?

- Better results on your specific domain
- Learn classification schemes specifically for your problem
- Essential for text classification
- Very useful for named entity recognition
- Less critical for part-of-speech tagging and dependency parsing

Notes: Before we get starting with explaining _how_, it's worth taking a second
to ask ourselves: Why would we want to update the model with our own examples?
Why can't we just rely on pre-trained models?

Statistical models make predictions based on the examples they were trained on.

You can usually make the model more accurate by showing it examples from your
domain.

You often also want to predict categories specific to your problem, so the model
needs to learn about them.

This is essential for text classification, very useful for entity recognition
and a little less critical for tagging and parsing.

---

# How training works (1)

1. **Initialize** the model weights randomly with `nlp.initialize`
2. **Predict** a few examples with the current weights by calling `nlp.update`
3. **Compare** prediction with true labels
4. **Calculate** how to change weights to improve predictions
5. **Update** weights slightly
6. Go back to 2.

Notes: spaCy supports updating existing models with more examples, and training
new models.

If we're not starting with a pre-trained model, we first initialize the weights
randomly.

Next, we call `nlp.update`, which predicts a batch of examples with the current
weights.

The model then checks the predictions against the correct answers, and decides
how to change the weights to achieve better predictions next time.

Finally, we make a small correction to the current weights and move on to the
next batch of examples.

We continue calling `nlp.update` for each batch of examples in the data.

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
("iPhone X is coming", {"entities": [(0, 8, "GADGET")]})
```

- Texts with no entities are also important

```python
("I need a new phone! Any tips?", {"entities": []})
```

- **Goal:** teach the model to generalize

Notes: Let's look at an example for a specific component: the entity recognizer.

The entity recognizer takes a document and predicts phrases and their labels.
This means that the training data needs to include texts, the entities they
contain, and the entity labels.

Entities can't overlap, so each token can only be part of one entity.

Because the entity recognizer predicts entities _in context_, it also needs to
be trained on entities _and_ their surrounding context.

The easiest way to do this is to show the model a text and a list of character
offsets. For example, "iPhone X" is a gadget, starts at character 0 and ends at
character 8.

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
be texts and named entities we want to recognize, or tokens and their correct
part-of-speech tags.

To update an existing model, we can start with a few hundred to a few thousand
examples.

To train a new category we may need up to a million.

spaCy's pre-trained English models for instance were trained on 2 million words
labelled with part-of-speech tags, dependencies and named entities.

Training data is usually created by humans who assign labels to texts.

This is a lot of work, but can be semi-automated – for example, using spaCy's
`Matcher`.

---

# Let's practice!

Notes: Now it's time to get started and prepare the training data. Let's look at
some examples and create a small dataset for a new entity type.
