# Advanced NLP with spaCy course

The front-end is powered by [Gatsby](#) and [Reveal.js](#) and the back-end code
execution uses [Binder](https://mybinder.org) 💖

## Features

- Supports slides, interactive code exercises and multiple-choice questions.
- Uses the `localStorage` to keep track of which exercises were already (marked
  as) completed.

## How it works

When building the site, Gatsby will look for `.py` files and make their contents
available to query via GraphQL. This lets us use the raw code within the app.
Under the hood, the app uses [Binder](https://mybinder.org) to serve up an image
with the packages dependencies, including the spaCy models. By calling into
[JupyterLab](https://jupyterlab.readthedocs.io/en/stable/), we can then execute
code using the active kernel. This lets you edit the code in the browser and see
the live results.

To validate the code when the user hits "Submit", I'm currently using a slightly
hacky trick. Since the Python code is sent back to the kernel as a string, we
can manipulate it and add tests – for example, exercise `exc_01_02_01.py` will
be validated using `test_01_02_01.py` (if available). The user code and test are
combined using a string template. At the moment, the `testTemplate` in the
`meta.json` looks like this:

```python
from wasabi import Printer
__msg__ = Printer()
__solution__ = """${solution}"""
${solution}

${test}
test()
```

If present, `${solution}` will be replaced with the string value of the
submitted user code. In this case, we're inserting it twice: once as a string so
we can check whether the submission includes something, and once as the code, so
we can actually run it and check the objects it creates. Finally, `${test}` is
replaced by the contents of the test file. I'm also making
[`wasabi`](https://github.com/ines/wasabi)'s printer available as `__msg__`, so
we can easily print pretty messages.

A test file could then look like this:

```python
def test():
    assert "spacy.load" in __solution__, "Are you calling spacy.load?"
    assert nlp.meta["lang"] == "en", "Are you loading the correct model?"
    assert nlp.meta["name"] == "core_web_sm", "Are you loading the correct model?"
    assert "nlp(text)" in __solution__, "Are you processing the text correctly?"
    assert "print(doc.text)" in __solution__, "Are you printing the Doc's text?"

    __msg__.good(
        "Well done! Now that you've practiced loading models, let's look at "
        "some of their predictions."
    )
```

With this approach, it's not _always_ possible to validate the input perfectly –
there are too many options and we want to avoid false positives. Because the
tests only raise `AssertionError`s, they can also potentially leak the correct
answers in the traceback.

## Usage & API

I mostly built this project for my own course, but it should be very easy to
fork and adapt. I made sure to strictly separate the content and the app
functionality and source. So if you want to fork the repo and create your own
course, you should only have to edit the chapters, exercises and `meta.json`,
update the visual assets in `/static` and optionally adjust the theme colours.
In theory, it should even work for languages other than Python – but I haven't
tested this yet.

### Directory Structure

```yaml
├── chapters             # chapters, one Markdown file per chapter
├── exercises            # code files, tests and assets for exercises
├── public               # compiled site
├── slides               # slides, one Markdown file per presentation
├── src                  # Gatsby/React source, independent from content
├── static               # static assets like images, available in slides/chapters
├── meta.json            # course metadata
└── theme.sass           # UI theme colors and settings
```

### Custom Elements

When using custom elements, make sure to place a newline between the
opening/closing tags and the children. Otherwise, Markdown content may not
render correctly.

#### `<exercise>`

Container of a single exercise.

| Argument     | Type            | Description                                                    |
| ------------ | --------------- | -------------------------------------------------------------- |
| `id`         | number / string | Unique exercise ID within chapter.                             |
| `title`      | string          | Exercise title.                                                |
| `type`       | string          | Optional type. `"slides"` makes container wider and adds icon. |
| **children** | -               | The contents of the exercise.                                  |

```markdown
<exercise id="1" title="Introduction to spaCy">

Content goes here...

</exercise>
```

#### `<codeblock>`

| Argument     | Type            | Description                                                                                  |
| ------------ | --------------- | -------------------------------------------------------------------------------------------- |
| `id`         | number / string | Unique identifier of the code exercise.                                                      |
| `source`     | string          | Name of the source file (without file extension). Defaults to `exc_${id}` if not set.        |
| `solution`   | string          | Name of the solution file (without file extension). Defaults to `solution_${id}` if not set. |
| `test`       | string          | Name of the test file (without file extension). Defaults to `test_${id}` if not set.         |
| **children** | string          | Optional hints displayed when the user clicks "Show hint".                                   |

```markdown
<codeblock id="02_03">

This is a hint!

</codeblock>
```

#### `<slides>`

Container to display slides interactively using Reveal.js and a Markdown file.

| Argument | Type   | Description                                   |
| -------- | ------ | --------------------------------------------- |
| `source` | string | Name of slides file (without file extension). |

```markdown
<slides source="chapter1_01_introduction-to-spacy">
</slides>
```

#### `<choice>`

Container for multiple-choice question.

| Argument     | Type  | Description                              |
| ------------ | ----- | ---------------------------------------- |
| **children** | nodes | Only `<opt>` components for the options. |

```markdown
<choice>

<opt text="Option one">You have selected option one! This is not good.</opt>
<opt text="Option two" correct="true">Yay! </opt>

</choice>
```

#### `<opt>`

A multiple-choice option.

| Argument     | Type   | Description                                                                                    |
| ------------ | ------ | ---------------------------------------------------------------------------------------------- |
| `text`       | string | The option text to be displayed. Supports inline HTML.                                         |
| `correct`    | string | `"true"` if the option is the correct answer.                                                  |
| **children** | string | The text to be displayed if the option is selected (explaining why it's correct or incorrect). |

### File formats

#### Chapters

Chapters are placed in [`/chapters`](/chapters) and are Markdown files
consisting of `<exercise>` components. They'll be turned into pages, e.g.
`/chapter1`. In their frontmatter block at the top of the file, they need to
specify `type: chapter`, as well as the following meta:

```yaml
---
title: The chapter title
description: The chapter description
prev: /chapter1 # exact path to previous chapter or null to not show a link
next: /chapter3 # exact path to next chapter or null to not show a link
id: 2 # unique identifier for chapter
type: chapter # important: this creates a standalone page from the chapter
---

```

#### Slides

Slides are placed in [`/slides`](/slides) and are markdown files consisting of
slide content, separated by `---`. They need to specify the following
frontmatter block at the top of the file:

```yaml
---
type: slides
---

```

The **first and last slide** use a special layout and will display the headline
in the center of the slide. **Speaker notes** (in this case, the script) can be
added at the end of a slide, prefixed by `Notes:`. They'll then be shown on the
right next to the slides. Here's an example slides file:

```markdown
---
type: slide
---

# Processing pipelines

Notes: This is a slide deck about processing pipelines.

---

# Next slide

- Some bullet points here
- And another bullet point

<img src="image.jpg" alt="An image located in /static" />>
```

## Roadmap and todos
