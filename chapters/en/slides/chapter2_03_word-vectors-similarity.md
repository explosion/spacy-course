---
type: slides
---

# Word vectors and semantic similarity

Notes: In this lesson, you'll learn how to use spaCy to predict how similar
documents, spans or tokens are to each other.

You'll also learn how to use word vectors and how to take advantage of them in
your NLP application.

---

# Comparing semantic similarity

- `spaCy` can compare two objects and predict similarity
- `Doc.similarity()`, `Span.similarity()` and `Token.similarity()`
- Take another object and return a similarity score (`0` to `1`)
- **Important:** needs a pipeline that has word vectors included, for example:
  - ✅ `en_core_web_md` (medium)
  - ✅ `en_core_web_lg` (large)
  - 🚫 **NOT** `en_core_web_sm` (small)

Notes: spaCy can compare two objects and predict how similar they are – for
example, documents, spans or single tokens.

The `Doc`, `Token` and `Span` objects have a `.similarity` method that takes
another object and returns a floating point number between 0 and 1, indicating
how similar they are.

One thing that's very important: In order to use similarity, you need a larger
spaCy pipeline that has word vectors included.

For example, the medium or large English pipeline – but _not_ the small one. So
if you want to use vectors, always go with a pipeline that ends in "md" or "lg".
You can find more details on this in the
[documentation](https://spacy.io/models).

---

# Similarity examples (1)

```python
# Load a larger pipeline with vectors
nlp = spacy.load("en_core_web_md")

# Compare two documents
doc1 = nlp("I like fast food")
doc2 = nlp("I like pizza")
print(doc1.similarity(doc2))
```

```out
0.8627204117787385
```

```python
# Compare two tokens
doc = nlp("I like pizza and pasta")
token1 = doc[2]
token2 = doc[4]
print(token1.similarity(token2))
```

```out
0.7369546
```

Notes: Here's an example. Let's say we want to find out whether two documents
are similar.

First, we load the medium English pipeline, "en_core_web_md".

We can then create two doc objects and use the first doc's `similarity` method
to compare it to the second.

Here, a fairly high similarity score of 0.86 is predicted for "I like fast food"
and "I like pizza".

The same works for tokens.

According to the word vectors, the tokens "pizza" and "pasta" are kind of
similar, and receive a score of 0.7.

---

# Similarity examples (2)

```python
# Compare a document with a token
doc = nlp("I like pizza")
token = nlp("soap")[0]

print(doc.similarity(token))
```

```out
0.32531983166759537
```

```python
# Compare a span with a document
span = nlp("I like pizza and pasta")[2:5]
doc = nlp("McDonalds sells burgers")

print(span.similarity(doc))
```

```out
0.619909235817623
```

Notes: You can also use the `similarity` methods to compare different types of
objects.

For example, a document and a token.

Here, the similarity score is pretty low and the two objects are considered
fairly dissimilar.

Here's another example comparing a span – "pizza and pasta" – to a document
about McDonalds.

The score returned here is 0.61, so it's determined to be kind of similar.

---

# How does spaCy predict similarity?

- Similarity is determined using **word vectors**
- Multi-dimensional meaning representations of words
- Generated using an algorithm like
  [Word2Vec](https://en.wikipedia.org/wiki/Word2vec) and lots of text
- Can be added to spaCy's pipelines
- Default: cosine similarity, but can be adjusted
- `Doc` and `Span` vectors default to average of token vectors
- Short phrases are better than long documents with many irrelevant words

Notes: But how does spaCy do this under the hood?

Similarity is determined using word vectors, multi-dimensional representations
of meanings of words.

You might have heard of Word2Vec, which is an algorithm that's often used to
train word vectors from raw text.

Vectors can be added to spaCy's pipelines.

By default, the similarity returned by spaCy is the cosine similarity between
two vectors – but this can be adjusted if necessary.

Vectors for objects consisting of several tokens, like the `Doc` and `Span`,
default to the average of their token vectors.

That's also why you usually get more value out of shorter phrases with fewer
irrelevant words.

---

# Word vectors in spaCy

```python
# Load a larger pipeline with vectors
nlp = spacy.load("en_core_web_md")

doc = nlp("I have a banana")
# Access the vector via the token.vector attribute
print(doc[3].vector)
```

```out
 [2.02280000e-01,  -7.66180009e-02,   3.70319992e-01,
  3.28450017e-02,  -4.19569999e-01,   7.20689967e-02,
 -3.74760002e-01,   5.74599989e-02,  -1.24009997e-02,
  5.29489994e-01,  -5.23800015e-01,  -1.97710007e-01,
 -3.41470003e-01,   5.33169985e-01,  -2.53309999e-02,
  1.73800007e-01,   1.67720005e-01,   8.39839995e-01,
  5.51070012e-02,   1.05470002e-01,   3.78719985e-01,
  2.42750004e-01,   1.47449998e-02,   5.59509993e-01,
  1.25210002e-01,  -6.75960004e-01,   3.58420014e-01,
 -4.00279984e-02,   9.59490016e-02,  -5.06900012e-01,
 -8.53179991e-02,   1.79800004e-01,   3.38669986e-01,
  ...
```

Notes: To give you an idea of what those vectors look like, here's an example.

First, we load the medium pipeline again, which ships with word vectors.

Next, we can process a text and look up a token's vector using the `.vector`
attribute.

The result is a 300-dimensional vector of the word "banana".

---

# Similarity depends on the application context

- Useful for many applications: recommendation systems, flagging duplicates etc.
- There's no objective definition of "similarity"
- Depends on the context and what application needs to do

```python
doc1 = nlp("I like cats")
doc2 = nlp("I hate cats")

print(doc1.similarity(doc2))
```

```out
0.9501447503553421
```

Notes: Predicting similarity can be useful for many types of applications. For
example, to recommend a user similar texts based on the ones they have read. It
can also be helpful to flag duplicate content, like posts on an online platform.

However, it's important to keep in mind that there's no objective definition of
what's similar and what isn't. It always depends on the context and what your
application needs to do.

Here's an example: spaCy's default word vectors assign a very high similarity
score to "I like cats" and "I hate cats". This makes sense, because both texts
express sentiment about cats. But in a different application context, you might
want to consider the phrases as very _dissimilar_, because they talk about
opposite sentiments.

---

# Let's practice!

Notes: Now it's your turn. Let's try out some of spaCy's word vectors and use
them to predict similarities.
