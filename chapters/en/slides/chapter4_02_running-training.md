---
type: slides
---

# Configuring and running the training

Notes: Now that you've learned how to create training data, let's take a look at
training your pipeline and configuring the training. In this lesson, you'll
learn all about spaCy's training config system, how to generate your own
training config, how to use the CLI to train a model and how to explore your
trained pipeline afterwards.

---

# The training config (1)

- **single source of truth** for all settings
- typically called `config.cfg`
- defines how to initialize the `nlp` object
- includes all settings about the pipeline components and their model
  implementations
- configures the training process and hyperparameters
- makes your training more reproducible

Notes: spaCy uses a config file, usually called `config.cfg`, as the "single
source of truth" for all settings. The config file defines how to initialize the
`nlp` object, which pipeline components to add and how their internal model
implementations should be configured. It also includes all settings for the
training process and how to load the data, including hyperparameters.

Instead of providing lots of arguments on the command line or having to remember
to define every single setting in code, you only need to pass your config file
to spaCy's training command.

Config files also help with reproducibility: you'll have all settings in one
place and always know how your pipeline was trained. You can even check your
config file into a Git repo to version it and share it with others so they can
train the same pipeline with the same settings.

---

# The training config (2)

```ini
[nlp]
lang = "en"
pipeline = ["tok2vec", "ner"]
batch_size = 1000

[nlp.tokenizer]
@tokenizers = "spacy.Tokenizer.v1"

[components]

[components.ner]
factory = "ner"

[components.ner.model]
@architectures = "spacy.TransitionBasedParser.v2"
hidden_width = 64
# And so on...
```

Notes: Here's an excerpt from a config file used to train a pipeline with a
named entity recognizer. The config is grouped into sections, and nested
sections are defined using a dot. For example, `[components.ner.model]` defines
the settings for the named entity recognizer's model implementation.

Config files can also reference Python functions using the `@` notation. For
example, the tokenizer defines a registered tokenizer function. You can use this
to customize different parts of the `nlp` object and training – from plugging in
your own tokenizer, all the way to implementing your own model architectures.
But let's not worry about this for now – what you'll learn in this chapter will
simply use the defaults spaCy provides out-of-the-box!

---

# Generating a config

- spaCy can auto-generate a default config file for you
- interactive [quickstart widget](https://spacy.io/usage/training#quickstart) in
  the docs
- [`init config`](https://spacy.io/api/cli#init-config) command on the CLI

```bash
$ python -m spacy init config ./config.cfg --lang en --pipeline ner
```

- `init config`: the command to run
- `config.cfg`: output path for the generated config
- `--lang`: language class of the pipeline, e.g. `en` for English
- `--pipeline`: comma-separated names of components to include

Notes: Of course, you don't have to write the config files by hand, and in a lot
of cases, you won't even need to customize it at all. spaCy can auto-generate a
config file for you.

The quickstart widget in the documentation lets you generate a config
interactively by selecting the language and pipeline components you need, as
well as optional hardware and optimization settings.

Alternatively, you can also use spaCy's built-in `init config` command. It takes
the output file as the first argument. We usually call this file `config.cfg`.
The argument `--lang` defines the language class that should be used for the
pipeline, for example, `en` for English. The `--pipeline` argument lets you
specify one or more comma-separated pipeline components to include. In this
example, we're creating a config with one pipeline component, the named entity
recognizer.

---

# Training a pipeline (1)

- all you need is the `config.cfg` and the training and development data
- config settings can be overwritten on the command line

```bash
$ python -m spacy train ./config.cfg --output ./output --paths.train train.spacy --paths.dev dev.spacy
```

- `train`: the command to run
- `config.cfg`: the path to the config file
- `--output`: the path to the output directory to save the trained pipeline
- `--paths.train`: override with path to the training data
- `--paths.dev`: override with path to the evaluation data

Notes: To train a pipeline, all you need is the config file and the training and
development data. These are the `.spacy` files you already worked with in the
previous exercises.

The first argument of `spacy train` is the path to the config file. The
`--output` argument lets you specify a directory for saving the final trained
pipeline.

You can also override different config settings on the command line. In this
case, we override `paths.train` using the path to the `train.spacy` file and
`paths.dev` using the `dev.spacy` file.

---

# Training a pipeline (2)

```
============================ Training pipeline ============================
ℹ Pipeline: ['tok2vec', 'ner']
ℹ Initial learn rate: 0.001

E    #       LOSS TOK2VEC  LOSS NER  ENTS_F  ENTS_P  ENTS_R  SCORE
---  ------  ------------  --------  ------  ------  ------  ------
  0       0          0.00     26.50    0.73    0.39    5.43    0.01
  0     200         33.58    847.68   10.88   44.44    6.20    0.11
  1     400         70.88    267.65   33.50   45.95   26.36    0.33
  2     600         67.56    156.63   45.32   62.16   35.66    0.45
  3     800        138.28    134.12   48.17   74.19   35.66    0.48
  4    1000        177.95    109.77   51.43   66.67   41.86    0.51
  6    1200         94.95     52.13   54.63   67.82   45.74    0.55
  8    1400        126.85     66.19   56.00   65.62   48.84    0.56
 10    1600         38.34     24.16   51.96   70.67   41.09    0.52
 13    1800        105.14     23.23   56.88   69.66   48.06    0.57

✔ Saved pipeline to output directory
/path/to/output/model-last
```

Notes: Here's an example of the output you'll see during and after training. You
might remember from earlier in this chapter that you usually want to make
several passes over the data during training. Each pass over the data is also
called an "epoch". This is shown in the first column of the table.

Within each epoch, spaCy outputs the accuracy scores every 200 examples. These
are the steps shown in the second column. You can change the frequency in the
config. Each line shows the loss and calculated accuracy score at this point
during training.

The most interesting score to keep an eye on is the combined score in the last
column. It reflects how accurately your model predicted the correct answers in
the evaluation data.

The training runs until the model stops improving and exits automatically.

---

# Loading a trained pipeline

- output after training is a regular loadable spaCy pipeline
  - `model-last`: last trained pipeline
  - `model-best`: best trained pipeline
- load it with `spacy.load`

```python
import spacy

nlp = spacy.load("/path/to/output/model-best")
doc = nlp("iPhone 11 vs iPhone 8: What's the difference?")
print(doc.ents)
```

Notes: The pipeline saved after training is a regular loadable spaCy pipeline –
just like the trained pipelines provided by spaCy, for example `en_core_web_sm`.
At the end, the last trained pipeline and the pipeline with the best score is
saved to the output directory.

You can load your trained pipeline by passing the path to `spacy.load`. You can
then use it to process and analyze text.

---

# Tip: Packaging your pipeline

<!-- TODO: illustration of pipeline packages, similar to earlier chapters? -->

- [`spacy package`](https://spacy.io/api/cli#package): create an installable
  Python package containing your pipeline
- easy to version and deploy

```bash
$ python -m spacy package /path/to/output/model-best ./packages --name my_pipeline --version 1.0.0
```

```bash
$ cd ./packages/en_my_pipeline-1.0.0
$ pip install dist/en_my_pipeline-1.0.0.tar.gz
```

Load and use the pipeline after installation:

```python
nlp = spacy.load("en_my_pipeline")
```

Notes: To make it easy to deploy your pipelines, spaCy provides a handy command
to package them as Python packages. The `spacy package` command takes the path
to your exported pipeline and an output directory. It then generates a Python
package containing your pipeline. The Python package is a `.tar.gz` file and can
be installed into your environment.

You can also provide an optional name and version on the command. This lets you
manage multiple different versions of a pipeline, for example, if you decide to
customize your pipeline later or train it with more data.

The package behaves just like any other Python package. After installation, you
can load your pipeline using its name. Note that spaCy will automatically add
the language code to the name. So your pipeline `my_pipeline` will become
`en_my_pipeline`.

---

# Let's practice!

Notes: Let's get to work and train your first pipeline! You'll practice
generating a config for a named entity recognizer and training a pipeline using
the data you worked on in the previous exercises.
