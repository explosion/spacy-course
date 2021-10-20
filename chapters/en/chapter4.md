---
title: 'Chapter 4: Training a neural network model'
description:
  "In this chapter, you'll learn how to update spaCy's statistical models to
  customize them for your use case – for example, to predict a new entity type
  in online comments. You'll write your own training loop from scratch, and
  understand the basics of how training works, along with tips and tricks that
  can make your custom NLP projects more successful."
prev: /chapter3
next: null
type: chapter
id: 4
---

<exercise id="1" title="Training and updating models" type="slides">

<slides source="chapter4_01_training-updating-models">
</slides>

</exercise>

<exercise id="2" title="Purpose of training">

While spaCy comes with a range of trained pipelines to predict linguistic
annotations, you almost _always_ want to fine-tune them with more examples. You
can do this by training them with more labelled data.

What does training **not** help with?

<choice>

<opt text="Improve model accuracy on your data.">

If a trained pipeline doesn't perform well on your data, training it with more
examples is often a good solution.

</opt>

<opt text="Learn new classification schemes.">

You can use training to teach the model new labels, entity types or other
classification schemes.

</opt>

<opt text="Discover patterns in unlabelled data." correct="true">

spaCy's components are supervised models for text annotations, meaning they can
only learn to reproduce examples, not guess new labels from raw text.

</opt>

</choice>

</exercise>

<exercise id="3" title="Creating a training corpus" type="slides">

<slides source="chapter4_02_training-corpus">
</slides>

</exercise>

<exercise id="4" title="Evaluation data">

To train a model, you typically need training data _and_ a development for for
evaluation. What is this evaluation data used for?

<choice>

<opt text="Provide more training examples as a fallback if the training data isn't enough.">

During training, the model will only be updated from the training data. The
development data is used to check the model's predictions on unseen data and
calculate the accuracy score.

</opt>

<opt text="Check predictions on unseen examples and calculate the accuracy score." correct="true">

...

</opt>

</choice>

</exercise>

<exercise id="5" title="Creating training data (1)">

spaCy's rule-based `Matcher` is a great way to quickly create training data for
named entity models. A list of sentences is available as the variable `TEXTS`.
You can print it to inspect it. We want to find all mentions of different iPhone
models, so we can create training data to teach a model to recognize them as
`"GADGET"`.

- Write a pattern for two tokens whose lowercase forms match `"iphone"` and
  `"x"`.
- Write a pattern for two tokens: one token whose lowercase form matches
  `"iphone"` and a digit.

<codeblock id="04_05">

- To match the lowercase form of a token, you can use the `"LOWER"` attribute.
  For example: `{"LOWER": "apple"}`.
- To find a digit token, you can use the `"IS_DIGIT"` flag. For example:
  `{"IS_DIGIT": True}`.

</codeblock>

</exercise>

<exercise id="5" title="Creating training data (2)">

After creating the data for our corpus, we need to save it out to a `.spacy`
file. The code from the previous example is already available.

- Instantiate the `DocBin` with the list of `docs`.
- Save the `DocBin` to a file called `train.spacy`.

<codeblock id="04_06">

- You can initialize the `DocBin` with a list of docs by passing them in as the
  keyword argument `docs`.
- The `DocBin`'s `to_disk` method takes one argument: the path of the file to
  save the binary data to. Make sure to use the file extension `.spacy`.

</codeblock>

</exercise>

<exercise id="6" title="Configuring and running the training" type="slides">

<slides source="chapter4_03_running-training">
</slides>

</exercise>

<exercise id="7" title="The training config">

TODO (multiple choice)

</exercise>

<exercise id="8" title="Generating a config file">

The [`init config` command](https://spacy.io/api/cli#init-config) auto-generates
a config file for training with the default settings. We want to train a named
entity recognizer, so we'll generate a config file for one pipeline component,
`ner`. Because we're executing the command in a Jupyter environment in this
course, we're using the prefix `!`. If you're running the command in your local
terminal, you can leave this out.

### Part 1

- Use spaCy's `init config` command to auto-generate a config. We're setting the
  output file to `-` to print the generated config to the terminal so we can
  look at it.
- Use the `--pipeline` argument to specify one pipeline component, `ner`.

<codeblock id="04_08_01"></codeblock>

### Part 2

- Use spaCy's `init config` command to auto-generate a config.
- Save the config to a file `config.cfg`.
- Use the `--pipeline` argument to specify one pipeline component, `ner`.

<codeblock id="04_08_02">

- The `spacy init-config` command lets you specify the path to the output file
  as its first argument.
- Config files should have the file extension `.cfg`.

</codeblock>

</exercise>

<exercise id="9" title="Using the training CLI">

Let's use the config file generated in the previous exercise and the training
corpus we've created to train a named entity recognizer!

The [`train`](https://spacy.io/api/cli#train) command lets you train a model
from a training config file. A file `config.cfg` is already available in the
current working directory, as well as a file `train.spacy` containing the
training examples, and a file `dev.spacy` containing the evaluation examples.
Because we're executing the command in a Jupyter environment in this course,
we're using the prefix `!`. If you're running the command in your local
terminal, you can leave this out.

- Call the `train` command with the `config.cfg`.
- Save the trained pipeline to a directory `output`.
- Pass in the `train.spacy` and `dev.spacy` paths.

<codeblock id="04_09">

- The first argument of the `spacy train` command is the path to the config
  file.

</codeblock>

</exercise>

<exercise id="10" title="Exploring the model">

Let's see how the model performs on unseen data! To speed things up a little, we
already ran a trained pipeline for the label `"GADGET"` over some text. Here are
some of the results:

| Text                                                                                                              | Entities               |
| ----------------------------------------------------------------------------------------------------------------- | ---------------------- |
| Apple is slowing down the iPhone 8 and iPhone X - how to stop it                                                  | `(iPhone 8, iPhone X)` |
| I finally understand what the iPhone X 'notch' is for                                                             | `(iPhone X,)`          |
| Everything you need to know about the Samsung Galaxy S9                                                           | `(Samsung Galaxy,)`    |
| Looking to compare iPad models? Here’s how the 2018 lineup stacks up                                              | `(iPad,)`              |
| The iPhone 8 and iPhone 8 Plus are smartphones designed, developed, and marketed by Apple                         | `(iPhone 8, iPhone 8)` |
| what is the cheapest ipad, especially ipad pro???                                                                 | `(ipad, ipad)`         |
| Samsung Galaxy is a series of mobile computing devices designed, manufactured and marketed by Samsung Electronics | `(Samsung Galaxy,)`    |

Out of all the entities in the texts, **how many did the model get correct**?
Keep in mind that incomplete entity spans count as mistakes, too! Tip: Count the
number of entities that the model _should_ have predicted. Then count the number
of entities it _actually_ predicted correctly and divide it by the number of
total correct entities.

<choice>

<opt text="45%">

Try counting the number of correctly predicted entities and divide it by the
number of total correct entities the model _should_ have predicted.

</opt>

<opt text="60%">

Try counting the number of correctly predicted entities and divide it by the
number of total correct entities the model _should_ have predicted.

</opt>

<opt text="70%" correct="true">

On our test data, the model achieved an accuracy of 70%.

</opt>

<opt text="90%">

Try counting the number of correctly predicted entities and divide it by the
number of total correct entities the model _should_ have predicted.

</opt>

</choice>

</exercise>

<exercise id="11" title="Training best practices" type="slides">

<slides source="chapter4_04_training-best-practices" start="42:36" end="44:55">
</slides>

</exercise>

<exercise id="10" title="Good data vs. bad data">

Here's an excerpt from a training set that labels the entity type
`TOURIST_DESTINATION` in traveler reviews.

```python
doc1 = nlp("i went to amsterdem last year and the canals were beautiful")
doc1.ents = [Span(doc1, 3, 4, label="TOURIST_DESTINATION")]

doc2 = nlp("You should visit Paris once, but the Eiffel Tower is kinda boring")
doc2.ents = [Span(doc2, 3, 4, label="TOURIST_DESTINATION")]

doc3 = nlp("There's also a Paris in Arkansas, lol")
doc3.ents = []

doc4 = nlp("Berlin is perfect for summer holiday: great nightlife and cheap beer!")
doc4.ents = [Span(doc4, 0, 1, label="TOURIST_DESTINATION")]
```

### Part 1

Why is this data and label scheme problematic?

<choice>

<opt text="Whether a place is a tourist destination is a subjective judgement and not a definitive category. It will be very difficult for the entity recognizer to learn." correct="true">

A much better approach would be to only label `"GPE"` (geopolitical entity) or
`"LOCATION"` and then use a rule-based system to determine whether the entity is
a tourist destination in this context. For example, you could resolve the
entities types back to a knowledge base or look them up in a travel wiki.

</opt>

<opt text="Paris should also be labelled as tourist destinations for consistency. Otherwise, the model will be confused.">

While it's possible that Paris, AK is also a tourist attraction, this only
highlights how subjective the label scheme is and how difficult it will be to
decide whether the label applies or not. As a result, this distinction will also
be very difficult to learn for the entity recognizer.

</opt>

<opt text="Rare out-of-vocabulary words like the misspelled 'amsterdem' shouldn't be labelled as entities.">

Even very uncommon words or misspellings can be labelled as entities. In fact,
being able to predict categories in misspelled text based on the context is one
of the big advantages of statistical named entity recognition.

</opt>

</choice>

### Part 2

- Rewrite the `doc.ents` to only use spans of the the label `"GPE"` (cities,
  states, countries) instead of `"TOURIST_DESTINATION"`.
- Don't forget to add spans for the `"GPE"` entities that weren't labeled in the
  old data.

<codeblock id="04_11">

- For the spans that are already labelled, you'll only need to change the label
  name from `"TOURIST_DESTINATION"` to `"GPE"`.
- One text includes a city and a state that aren't labeled yet. To add the
  entity spans, count the tokens to find out where the entity span starts and
  where it ends. Keep in mind that the last token index is _exclusive_! Then add
  a new `Span` to the `doc.ents`.

</codeblock>

</exercise>

<exercise id="12" title="Training multiple labels">

Here's a small sample of a dataset created to train a new entity type
`"WEBSITE"`. The original dataset contains a few thousand sentences. In this
exercise, you'll be doing the labeling by hand. In real life, you probably want
to automate this and use an annotation tool – for example,
[Brat](http://brat.nlplab.org/), a popular open-source solution, or
[Prodigy](https://prodi.gy), our own annotation tool that integrates with spaCy.

### Part 1

- Complete the entity offsets for the `"WEBSITE"` entities in the data. Feel
  free to use `len(doc1)` etc. if you don't want to count the tokens.

<codeblock id="04_12_01">

- Keep in mind that the end token of a span is exclusive. So an entity that
  starts at token 2 and ends at token 3 will have a start of `2` and an end of
  `3`.

</codeblock>

### Part 2

A model was trained with the data you just labelled, plus a few thousand similar
examples. After training, it's doing great on `"WEBSITE"`, but doesn't recognize
`"PERSON"` anymore. Why could this be happening?

<choice>

<opt text='It’s very difficult for the model to learn about different categories like <code>"PERSON"</code> and <code>"WEBSITE"</code>.'>

It's definitely possible for a model to learn about very different categories.
For example, spaCy's pre-trained English models can recognize persons, but also
organizations or percentages.

</opt>

<opt text='The training data included no examples of <code>"PERSON"</code>, so the model learned that this label is incorrect.' correct="true">

If `"PERSON"` entities occur in the training data but aren't labelled, the model
will learn that they shouldn't be predicted. Similarly, if an existing entity
type isn't present in the training data, the model may \"forget\" and stop
predicting it.

</opt>

<opt text="The hyperparameters need to be retuned so that both entity types can be recognized.">

While the hyperparameters can influence a model's accuracy, they're likely not
the problem here.

</opt>

</choice>

### Part 3

- Update the training data to include annotations for the `"PERSON"` entities
  "PewDiePie" and "Alexis Ohanian".

<codeblock id="04_12_02">

- To add more entities, add another `Span` to the `doc.ents`.
- - Keep in mind that the end token of a span is exclusive. So an entity that
    starts at token 2 and ends at token 3 will have a start of `2` and an end of
    `3`.

</codeblock>

</exercise>

<exercise id="13" title="Wrapping up" type="slides">

<slides source="chapter4_05_wrapping-up" start="45:01" end="47:195">
</slides>

</exercise>
