---
type: slides
---

# Wrapping up

Notes: Congratulations – you've made it to the end of the course!

---

# Your new spaCy skills

- Extract **linguistic features**: part-of-speech tags, dependencies, named
  entities
- Work with trained **pipelines**
- Find words and phrases using `Matcher` and `PhraseMatcher` **match rules**
- Best practices for working with **data structures** `Doc`, `Token` `Span`,
  `Vocab`, `Lexeme`
- Find **semantic similarities** using **word vectors**
- Write custom **pipeline components** with **extension attributes**
- **Scale up** your spaCy pipelines and make them fast
- Create **training data** for spaCy's statistical models
- **Train and update** spaCy's neural network models with new data

Notes: Here's an overview of all the new skills you learned so far:

In the first chapter, you learned how to extract linguistic features like
part-of-speech tags, syntactic dependencies and named entities, and how to work
with trained pipelines.

You also learned to write powerful match patterns to extract words and phrases
using spaCy's matcher and phrase matcher.

Chapter 2 was all about information extraction, and you learned how to work with
the data structures, the `Doc`, `Token` and `Span`, as well as the `Vocab` and
lexical entries.

You also used spaCy to predict semantic similarities using word vectors.

In chapter 3, you got some more insights into spaCy's pipeline, and learned to
write your own custom pipeline components that modify the doc.

You also created your own custom extension attributes for docs, tokens and
spans, and learned about processing streams and making your pipeline faster.

Finally, in chapter 4, you learned about training and updating spaCy's
statistical models, specifically the entity recognizer.

You learned some useful tricks for how to create training data, and how to
design your label scheme to get the best results.

---

# More things to do with spaCy (1)

- [Training and updating](https://spacy.io/usage/training) other pipeline
  components
  - Part-of-speech tagger
  - Dependency parser
  - Text classifier

Notes: Of course, there's a lot more that spaCy can do that we didn't get to
cover in this course.

While we focused mostly on training the entity recognizer, you can also train
and update the other statistical pipeline components like the part-of-speech
tagger and dependency parser.

Another useful pipeline component is the text classifier, which can learn to
predict labels that apply to the whole text. It's not part of the pre-trained
models, but you can add it to an existing model and train it on your own data.

---

# More things to do with spaCy (2)

- [Customizing the tokenizer](https://spacy.io/usage/linguistic-features#tokenization)
  - Adding rules and exceptions to split text differently
- [Adding or improving support for other languages](https://spacy.io/usage/adding-languages)
  - 60+ languages currently
  - Lots of room for improvement and more languages
  - Allows training models for other languages

Notes: In this course, we basically accepted the default tokenization as it is.
But you don't have to!

spaCy lets you customize the rules used to determine where and how to split the
text.

You can also add and improve the support for other languages.

While spaCy already supports tokenization for many different languages, there's
still a lot of room for improvement.

Supporting tokenization for a new language is the first step towards being able
to train a statistical model.

---

# See the website for more info and documentation!

<img src="/website.png" alt="Laptop showing the spacy.io website" width="50%" />

👉 [spacy.io](https://spacy.io)

Notes: For more examples, tutorials and in-depth API documentation, check out
the spaCy website.

---

# Thanks and see you soon! 👋

Notes: Thanks so much for taking this course! I hope you had fun, and I'm
excited to hear about the cool things you end up building with spaCy.
