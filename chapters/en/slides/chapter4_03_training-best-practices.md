---
type: slides
---

# Best practices for training spaCy models

Notes: When you start running your own experiments, you might find that a lot of
things just don't work the way you want them to. And that's okay.

Training models is an iterative process, and you have to try different things
until you find out what works best.

In this lesson, I'll be sharing some best practices and things to keep in mind
when training your own models.

Let's take a look at some of the problems you may come across.

---

# Problem 1: Models can "forget" things

- Existing model can overfit on new data
  - e.g.: if you only update it with `"WEBSITE"`, it can "unlearn" what a
    `"PERSON"` is
- Also known as "catastrophic forgetting" problem

Notes: Statistical models can learn lots of things – but they can also unlearn
them.

If you're updating an existing model with new data, especially new labels, it
can overfit and adjust _too much_ to the new examples.

For instance, if you're only updating it with examples of `"WEBSITE"`, it may
"forget" other labels it previously predicted correctly – like `"PERSON"`.

This is also known as the catastrophic forgetting problem.

---

# Solution 1: Mix in previously correct predictions

- For example, if you're training `"WEBSITE"`, also include examples of
  `"PERSON"`
- Run existing spaCy model over data and extract all other relevant entities

Note: To prevent this, make sure to always mix in examples of what the model
previously got correct.

If you're training a new category `"WEBSITE"`, also include examples of
`"PERSON"`.

spaCy can help you with this. You can create those additional examples by
running the existing model over data and extracting the entity spans you care
about.

You can then mix those examples in with your existing data and update the model
with annotations of all labels.

---

# Problem 2: Models can't learn everything

- spaCy's models make predictions based on **local context**
- Model can struggle to learn if decision is difficult to make based on context
- Label scheme needs to be consistent and not too specific
  - For example: `"CLOTHING"` is better than `"ADULT_CLOTHING"` and
    `"CHILDRENS_CLOTHING"`

Notes: Another common problem is that your model just won't learn what you want
it to.

spaCy's models make predictions based on the local context – for example, for
named entities, the surrounding words are most important.

If the decision is difficult to make based on the context, the model can
struggle to learn it.

The label scheme also needs to be consistent and not too specific.

For example, it may be very difficult to teach a model to predict whether
something is adult clothing or children's clothing based on the context.
However, just predicting the label "clothing" may work better.

---

# Solution 2: Plan your label scheme carefully

- Pick categories that are reflected in local context
- More generic is better than too specific
- Use rules to go from generic labels to specific categories

**BAD:**

```python
LABELS = ["ADULT_SHOES", "CHILDRENS_SHOES", "BANDS_I_LIKE"]
```

**GOOD:**

```python
LABELS = ["CLOTHING", "BAND"]
```

Notes: Before you start training and updating models, it's worth taking a step
back and planning your label scheme.

Try to pick categories that are reflected in the local context and make them
more generic if possible.

You can always add a rule-based system later to go from generic to specific.

Generic categories like "clothing" or "band" are both easier to label and easier
to learn.

---

# Let's practice!

Notes: Let's look at some of these problems in context and fix them!
