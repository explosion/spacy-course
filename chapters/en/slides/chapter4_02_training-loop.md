---
type: slides
---

# The training loop

Notes: While some other libraries give you one method that takes care of
training a model, spaCy gives you full control over the training loop.

---

# The steps of a training loop

1. **Loop** for a number of times.
2. **Shuffle** the training data.
3. **Divide** the data into batches.
4. **Update** the model for each batch.
5. **Save** the updated model.

Notes: The training loop is a series of steps that's performed to train or
update a model.

We usually need to perform it several times, for multiple iterations, so that
the model can learn from it effectively. If we want to train for 10 iterations,
we need to loop 10 times.

To prevent the model from getting stuck in a suboptimal solution, we randomly
shuffle the data for each iteration. This is a very common strategy when doing
stochastic gradient descent.

Next, we divide the training data into batches of several examples, also known
as minibatching. This increases the reliability of the gradient estimates.

Finally, we update the model for each batch, and start the loop again until
we've reached the last iteration.

We can then save the model to a directory and use it in spaCy.

---

# Recap: How training works

<img src="/training.png" alt="Diagram of the training process" />

- **Training data:** Examples and their annotations.
- **Text:** The input text the model should predict a label for.
- **Label:** The label the model should predict.
- **Gradient:** How to change the weights.

Notes: To recap:

The training data are the examples we want to update the model with.

The text should be a sentence, paragraph or longer document. For the best
results, it should be similar to what the model will see at runtime.

The label is what we want the model to predict. This can be a text category, or
an entity span and its type.

The gradient is how we should change the model to reduce the current error. It's
computed when we compare the predicted label to the true label.

---

# Example loop

```python
TRAINING_DATA = [
    ("How to preorder the iPhone X", {"entities": [(20, 28, "GADGET")]})
    # And many more examples...
]
```

```python
# Loop for 10 iterations
for i in range(10):
    # Shuffle the training data
    random.shuffle(TRAINING_DATA)
    # Create batches and iterate over them
    for batch in spacy.util.minibatch(TRAINING_DATA):
        # Split the batch in texts and annotations
        texts = [text for text, annotation in batch]
        annotations = [annotation for text, annotation in batch]
        # Update the model
        nlp.update(texts, annotations)

# Save the model
nlp.to_disk(path_to_model)
```

Notes: Here's an example.

Let's imagine we have a list of training examples consisting of texts and entity
annotations.

We want to loop for 10 iterations, so we're iterating over a `range` of 10.

Next, we use the `random` module to randomly shuffle the training data.

We then use spaCy's `minibatch` utility function to divide the examples into
batches.

For each batch, we get the texts and annotations and call the `nlp.update`
method to update the model.

Finally, we call the `nlp.to_disk` method to save the trained model to a
directory.

---

# Updating an existing model

- Improve the predictions on new data
- Especially useful to improve existing categories, like `"PERSON"`
- Also possible to add new categories
- Be careful and make sure the model doesn't "forget" the old ones

Notes: spaCy lets you update an existing pre-trained model with more data – for
example, to improve its predictions on different texts.

This is especially useful if you want to improve categories the model already
knows, like "person" or "organization".

You can also update a model to add new categories.

Just make sure to always update it with examples of the new category _and_
examples of the other categories it previously predicted correctly. Otherwise
improving the new category might hurt the other categories.

---

# Setting up a new pipeline from scratch

```python
# Start with blank English model
nlp = spacy.blank("en")
# Create blank entity recognizer and add it to the pipeline
nlp.add_pipe("ner")
# Add a new label
ner.add_label("GADGET")

# Start the training
nlp.initialize()
# Train for 10 iterations
for itn in range(10):
    random.shuffle(examples)
    # Divide examples into batches
    for batch in spacy.util.minibatch(examples, size=2):
        texts = [text for text, annotation in batch]
        annotations = [annotation for text, annotation in batch]
        # Update the model
        nlp.update(texts, annotations)
```

Notes: In this example, we start off with a blank English model using the
`spacy.blank` method. The blank model doesn't have any pipeline components, only
the language data and tokenization rules.

We then create a blank entity recognizer and add it to the pipeline.

Using the `add_label` method, we can add new string labels to the model.

We can now call `nlp.initialize` to initialize the model with random
weights.

To get better accuracy, we want to loop over the examples more than once and
randomly shuffle the data on each iteration.

On each iteration, we divide the examples into batches using spaCy's `minibatch`
utility function. Each example consists of a text and its annotations.

Finally, we update the model with the texts and annotations and continue the
loop.

---

# Let's practice!

Notes: Time to practice! Now that you've seen the training loop, let's use the
data created in the previous exercise to update a model.
