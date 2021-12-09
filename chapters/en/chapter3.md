---
title: 'Chapter 3: Processing Pipelines'
description:
  "This chapter will show you everything you need to know about spaCy's
  processing pipeline. You'll learn what goes on under the hood when you process
  a text, how to write your own components and add them to the pipeline, and how
  to use custom attributes to add your own metadata to the documents, spans and
  tokens."
prev: /chapter2
next: /chapter4
type: chapter
id: 3
---

<exercise id="1" title="Processing pipelines" type="slides">

<slides source="chapter3_01_processing-pipelines" start="23:36" end="26:12">
</slides>

</exercise>

<exercise id="2" title="What happens when you call nlp?">

What does spaCy do when you call `nlp` on a string of text?

```python
doc = nlp("This is a sentence.")
```

<choice>

<opt text="Run the tagger, parser and entity recognizer and then the tokenizer.">

The tokenizer is always run _before_ all other pipeline components, because it
transforms a string of text into a `Doc` object. The pipeline also doesn't have
to consist of the tagger, parser and entity recognizer.

</opt>

<opt text="Tokenize the text and apply each pipeline component in order." correct="true">

The tokenizer turns a string of text into a `Doc` object. spaCy then applies
every component in the pipeline on document, in order.

</opt>

<opt text="Connect to the spaCy server to compute the result and return it.">

spaCy computes everything on the machine and doesn't need to connect to any
server.

</opt>

<opt text="Initialize the language, add the pipeline and load in the binary model weights.">

When you call `spacy.load()` to load a pipeline, spaCy will initialize the
language, add the pipeline and load in the binary model weights. When you _call_
the `nlp` object on a text, the pipeline is already loaded.

</opt>

</exercise>

<exercise id="3" title="Inspecting the pipeline">

Let's inspect the small English pipeline!

- Load the `en_core_web_sm` pipeline and create the `nlp` object.
- Print the names of the pipeline components using `nlp.pipe_names`.
- Print the full pipeline of `(name, component)` tuples using `nlp.pipeline`.

<codeblock id="03_03">

The list of component names is available as the `nlp.pipe_names` attribute. The
full pipeline consisting of `(name, component)` tuples is available as
`nlp.pipeline`.

</codeblock>

</exercise>

<exercise id="4" title="Custom pipeline components" type="slides">

<slides source="chapter3_02_custom-pipeline-components" start="26:235" end="29:05">
</slides>

</exercise>

<exercise id="5" title="Use cases for custom components">

Which of these problems can be solved by custom pipeline components? Choose all
that apply!

1. Updating the trained pipelines and improving their predictions
2. Computing your own values based on tokens and their attributes
3. Adding named entities, for example based on a dictionary
4. Implementing support for an additional language

<choice>

<opt text="1 and 2.">

Custom components can only modify the `Doc` and can't be used to update weights
of other components directly.

</opt>

<opt text="1 and 3.">

Custom components can only modify the `Doc` and can't be used to update weights
of other components directly.

</opt>

<opt text="1 and 4.">

Custom components can only modify the `Doc` and can't be used to update weights
of other components directly. They're also added to the pipeline after the
language class is already initialized and after tokenization, so they're not
suitable to add new languages.

</opt>

<opt text="2 and 3." correct="true">

Custom components are great for adding custom values to documents, tokens and
spans, and customizing the `doc.ents`.

</opt>

<opt text="2 and 4.">

Custom components are added to the pipeline after the language class is already
initialized and after tokenization, so they're not suitable to add new
languages.

</opt>

<opt text="3 and 4.">

Custom components are added to the pipeline after the language class is already
initialized and after tokenization, so they're not suitable to add new
languages.

</opt>

</choice>

</exercise>

<exercise id="6" title="Simple components">

The example shows a custom component that prints the number of tokens in a
document. Can you complete it?

- Complete the component function with the `doc`'s length.
- Add the `"length_component"` to the existing pipeline as the **first**
  component.
- Try out the new pipeline and process any text with the `nlp` object – for
  example "This is a sentence.".

<codeblock id="03_06">

- To get the length of a `Doc` object, you can call Python's built-in `len()`
  method on it.
- Use the `nlp.add_pipe` method to add the component to the pipeline. Remember
  to use the string name of the component and to set the `first` keyword
  argument to `True` to make sure it's added before all other components.
- To process a text, call the `nlp` object on it.

</codeblock>

</exercise>

<exercise id="7" title="Complex components">

In this exercise, you'll be writing a custom component that uses the
`PhraseMatcher` to find animal names in the document and adds the matched spans
to the `doc.ents`. A `PhraseMatcher` with the animal patterns has already been
created as the variable `matcher`.

- Define the custom component and apply the `matcher` to the `doc`.
- Create a `Span` for each match, assign the label ID for `"ANIMAL"` and
  overwrite the `doc.ents` with the new spans.
- Add the new component to the pipeline _after_ the `"ner"` component.
- Process the text and print the entity text and entity label for the entities
  in `doc.ents`.

<codeblock id="03_07">

- Remember that the matches are a list of `(match_id, start, end)` tuples.
- The `Span` class takes 4 arguments: the parent `doc`, the start index, the end
  index and the label.
- To add a component after another, use the `after` keyword argument on
  `nlp.add_pipe`. Remember to use the string name of the component to add it.

</codeblock>

</exercise>

<exercise id="8" title="Extension attributes" type="slides">

<slides source="chapter3_03_extension-attributes" start="29:16" end="32:23">
</slides>

</exercise>

<exercise id="9" title="Setting extension attributes (1)">

Let's practice setting some extension attributes.

### Step 1

- Use `Token.set_extension` to register `"is_country"` (default `False`).
- Update it for `"Spain"` and print it for all tokens.

<codeblock id="03_09_01">

Remember that extension attributes are available via the `._` property. For
example, `doc._.has_color`.

</codeblock>

### Step 2

- Use `Token.set_extension` to register `"reversed"` (getter function
  `get_reversed`).
- Print its value for each token.

<codeblock id="03_09_02">

Remember that extension attributes are available via the `._` property. For
example, `doc._.has_color`.

</codeblock>

</exercise>

<exercise id="10" title="Setting extension attributes (2)">

Let's try setting some more complex attributes using getters and method
extensions.

### Part 1

- Complete the `get_has_number` function .
- Use `Doc.set_extension` to register `"has_number"` (getter `get_has_number`)
  and print its value.

<codeblock id="03_10_01">

- Remember that extension attributes are available via the `._` property. For
  example, `doc._.has_color`.
- The `get_has_number` function should return whether any of the tokens in the
  `doc` return `True` for `token.like_num` (whether the token resembles a
  number).

</codeblock>

### Part 2

- Use `Span.set_extension` to register `"to_html"` (method `to_html`).
- Call it on `doc[0:2]` with the tag `"strong"`.

<codeblock id="03_10_02">

- Method extensions can take one or more arguments. For example:
  `doc._.some_method("argument")`.
- The first argument passed to the method is always the `Doc`, `Token` or `Span`
  object the method was called on.

</codeblock>

</exercise>

<exercise id="11" title="Entities and extensions">

In this exercise, you'll combine custom extension attributes with the
statistical predictions and create an attribute getter that returns a Wikipedia
search URL if the span is a person, organization, or location.

- Complete the `get_wikipedia_url` getter so it only returns the URL if the
  span's label is in the list of labels.
- Set the `Span` extension `"wikipedia_url"` using the getter
  `get_wikipedia_url`.
- Iterate over the entities in the `doc` and output their Wikipedia URL.

<codeblock id="03_11">

- To get the string label of a span, use the `span.label_` attribute. This is
  the label predicted by the entity recognizer if the span is an entity span.
- Remember that extension attributes are available via the `._` property. For
  example, `doc._.has_color`.

</codeblock>

</exercise>

<exercise id="12" title="Components with extensions">

Extension attributes are especially powerful if they're combined with custom
pipeline components. In this exercise, you'll write a pipeline component that
finds country names and a custom extension attribute that returns a country's
capital, if available.

A phrase matcher with all countries is available as the variable `matcher`. A
dictionary of countries mapped to their capital cities is available as the
variable `CAPITALS`.

- Complete the `countries_component_function` and create a `Span` with the label
  `"GPE"` (geopolitical entity) for all matches.
- Add the component to the pipeline.
- Register the Span extension attribute `"capital"` with the getter
  `get_capital`.
- Process the text and print the entity text, entity label and entity capital
  for each entity span in `doc.ents`.

<codeblock id="03_12">

- The `Span` class takes four arguments: the `doc`, the `start` and `end` token
  index of the span and the `label`.
- Calling the `PhraseMatcher` on a `doc` returns a list of
  `(match_id, start, end)` tuples.
- To register a new extension attribute, use the `set_extension` method on the
  global class, e.g. `Doc`, `Token` or `Span`. To define a getter, use the
  `getter` keyword argument.
- Remember that extension attributes are available via the `._.` property. For
  example, `doc._.has_color`.

</codeblock>

</exercise>

<exercise id="13" title="Scaling and performance" type="slides">

<slides source="chapter3_04_scaling-performance" start="32:335" end="34:515">
</slides>

</exercise>

<exercise id="14" title="Processing streams">

In this exercise, you'll be using `nlp.pipe` for more efficient text processing.
The `nlp` object has already been created for you. A list of tweets about a
popular American fast food chain are available as the variable `TEXTS`.

### Part 1

- Rewrite the example to use `nlp.pipe`. Instead of iterating over the texts and
  processing them, iterate over the `doc` objects yielded by `nlp.pipe`.

<codeblock id="03_14_01">

- Using `nlp.pipe` lets you merge the first two lines of code into one.
- `nlp.pipe` takes the `TEXTS` and yields `doc` objects that you can loop over.

</codeblock>

### Part 2

- Rewrite the example to use `nlp.pipe`. Don't forget to call `list()` around
  the result to turn it into a list.

<codeblock id="03_14_02"></codeblock>

### Part 3

- Rewrite the example to use `nlp.pipe`. Don't forget to call `list()` around
  the result to turn it into a list.

<codeblock id="03_14_03"></codeblock>

</exercise>

<exercise id="15" title="Processing data with context">

In this exercise, you'll be using custom attributes to add author and book meta
information to quotes.

A list of `[text, context]` examples is available as the variable `DATA`. The
texts are quotes from famous books, and the contexts dictionaries with the keys
`"author"` and `"book"`.

- Use the `set_extension` method to register the custom attributes `"author"`
  and `"book"` on the `Doc`, which default to `None`.
- Process the `[text, context]` pairs in `DATA` using `nlp.pipe` with
  `as_tuples=True`.
- Overwrite the `doc._.book` and `doc._.author` with the respective info passed
  in as the context.

<codeblock id="03_15">

- The `Doc.set_extension` method takes two arguments: the string name of the
  attribute, and a keyword argument indicating the default, getter, setter or
  method. For example, `default=True`.
- If `as_tuples` is set to `True`, the `nlp.pipe` method takes a list of
  `(text, context)` tuples and yields `(doc, context)` tuples.

</codeblock>

</exercise>

<exercise id="16" title="Selective processing">

In this exercise, you'll use the `nlp.make_doc` and `nlp.select_pipes` methods
to only run selected components when processing a text.

### Part 1

- Rewrite the code to only tokenize the text using `nlp.make_doc`.

<codeblock id="03_16_01">

The `nlp.make_doc` method can be called on a text and returns a `Doc`, just like
the `nlp` object.

</codeblock>

### Part 2

- Disable the tagger and lemmatizer using the `nlp.select_pipes` method.
- Process the text and print all entities in the `doc`.

<codeblock id="03_16_02">

The `nlp.select_pipes` method accepts the keyword arguments `enable` or
`disable` that take a list of component names to enable or disable. For example,
`nlp.select_pipes(disable="ner")` will disable the named entity recognizer.

</codeblock>

</exercise>
