---
type: slides
---

# Extension attributes

Notes: In this lesson, you'll learn how to add custom attributes to the `Doc`,
`Token` and `Span` objects to store custom data.

---

# Setting custom attributes

- Add custom metadata to documents, tokens and spans
- Accessible via the `._` property

```python
doc._.title = "My document"
token._.is_color = True
span._.has_color = False
```

- Registered on the global `Doc`, `Token` or `Span` using the `set_extension`
  method

```python
# Import global classes
from spacy.tokens import Doc, Token, Span

# Set extensions on the Doc, Token and Span
Doc.set_extension("title", default=None)
Token.set_extension("is_color", default=False)
Span.set_extension("has_color", default=False)
```

Notes: Custom attributes let you add any metadata to docs, tokens and spans. The
data can be added once, or it can be computed dynamically.

Custom attributes are available via the `._` (dot underscore) property. This
makes it clear that they were added by the user, and not built into spaCy, like
`token.text`.

Attributes need to be registered on the global `Doc`, `Token` and `Span` classes
you can import from `spacy.tokens`. You've already worked with those in the
previous chapters. To register a custom attribute on the `Doc`, `Token` and
`Span`, you can use the `set_extension` method.

The first argument is the attribute name. Keyword arguments let you define how
the value should be computed. In this case, it has a default value and can be
overwritten.

---

# Extension attribute types

1. Attribute extensions
2. Property extensions
3. Method extensions

Notes: There are three types of extensions: attribute extensions, property
extensions and method extensions.

---

# Attribute extensions

- Set a default value that can be overwritten

```python
from spacy.tokens import Token

# Set extension on the Token with default value
Token.set_extension("is_color", default=False)

doc = nlp("The sky is blue.")

# Overwrite extension attribute value
doc[3]._.is_color = True
```

Notes: Attribute extensions set a default value that can be overwritten.

For example, a custom `is_color` attribute on the token that defaults to
`False`.

On individual tokens, its value can be changed by overwriting it – in this case,
True for the token "blue".

---

# Property extensions (1)

- Define a getter and an optional setter function
- Getter only called when you _retrieve_ the attribute value

```python
from spacy.tokens import Token

# Define getter function
def get_is_color(token):
    colors = ["red", "yellow", "blue"]
    return token.text in colors

# Set extension on the Token with getter
Token.set_extension("is_color", getter=get_is_color)

doc = nlp("The sky is blue.")
print(doc[3]._.is_color, "-", doc[3].text)
```

```out
True - blue
```

Notes: Property extensions work like properties in Python: they can define a
getter function and an optional setter.

The getter function is only called when you retrieve the attribute. This lets
you compute the value dynamically, and even take other custom attributes into
account.

Getter functions take one argument: the object, in this case, the token. In this
example, the function returns whether the token text is in our list of colors.

We can then provide the function via the `getter` keyword argument when we
register the extension.

The token "blue" now returns `True` for `._.is_color`.

---

# Property extensions (2)

- `Span` extensions should almost always use a getter

```python
from spacy.tokens import Span

# Define getter function
def get_has_color(span):
    colors = ["red", "yellow", "blue"]
    return any(token.text in colors for token in span)

# Set extension on the Span with getter
Span.set_extension("has_color", getter=get_has_color)

doc = nlp("The sky is blue.")
print(doc[1:4]._.has_color, "-", doc[1:4].text)
print(doc[0:2]._.has_color, "-", doc[0:2].text)
```

```out
True - sky is blue
False - The sky
```

Notes: If you want to set extension attributes on a span, you almost always want
to use a property extension with a getter. Otherwise, you'd have to update
_every possible span ever_ by hand to set all the values.

In this example, the `get_has_color` function takes the span and returns whether
the text of any of the tokens is in the list of colors.

After we've processed the doc, we can check different slices of the doc and the
custom `._.has_color` property returns whether the span contains a color token
or not.

---

# Method extensions

- Assign a **function** that becomes available as an object method
- Lets you pass **arguments** to the extension function

```python
from spacy.tokens import Doc

# Define method with arguments
def has_token(doc, token_text):
    in_doc = token_text in [token.text for token in doc]
    return in_doc

# Set extension on the Doc with method
Doc.set_extension("has_token", method=has_token)

doc = nlp("The sky is blue.")
print(doc._.has_token("blue"), "- blue")
print(doc._.has_token("cloud"), "- cloud")
```

```out
True - blue
False - cloud
```

Notes: Method extensions make the extension attribute a callable method.

You can then pass one or more arguments to it, and compute attribute values
dynamically – for example, based on a certain argument or setting.

In this example, the method function checks whether the doc contains a token
with a given text. The first argument of the method is always the object itself
– in this case, the doc. It's passed in automatically when the method is called.
All other function arguments will be arguments on the method extension. In this
case, `token_text`.

Here, the custom `._.has_token` method returns `True` for the word "blue" and
`False` for the word "cloud".

---

# Let's practice!

Notes: Now it's your turn. Let's add some custom extensions!
