---
type: slides
---

# Pipelines de procesamiento

Notes: ¡Hola otra vez! Este capítulo está dedicado a los pipelines de
procesamiento: una serie de funciones que se aplican a un doc para añadir
atributos como part-of-speech tags, dependency labels o entidades nombradas.

En esta lección aprenderás sobre los componentes del pipeline proveído por spaCy
y qué sucede detrás de cámaras cuando llamas a un objeto `nlp` sobre un string
de texto.

---

# ¿Qué sucede cuando llamas al objeto nlp?

<img src="/pipeline.png" alt="Illustration of the spaCy pipeline transforming a text into a processed Doc" width="90%" />

```python
doc = nlp("Esto es una frase.")
```

Notes: Ya has escrito esto bastantes veces: le pasas un string de texto al
objeto `nlp` y recibes un objeto `Doc`.

Pero, ¿qué hace el objeto `nlp` _realmente_?

Primero, se aplica el tokenizer para convertir el string de texto a un objeto
`Doc` A continuación, una serie de componentes del pipeline se aplican al doc en
orden. En este caso, el tagger, luego el parser, luego el
<abbr title="Es el componente que identifica las entidades nombradas de un texto.">entity
recognizer</abbr> . Finalmente, el doc procesado es devuelto para que puedas
trabajar con él.

---

# Componentes incluidos en el pipeline

| Nombre      | Descripción             | Crea                                                      |
| ----------- | :---------------------- | :-------------------------------------------------------- |
| **tagger**  | Part-of-speech tagger   | `Token.tag`, `Token.pos`                                  |
| **parser**  | Dependency parser       | `Token.dep`, `Token.head`, `Doc.sents`, `Doc.noun_chunks` |
| **ner**     | Named entity recognizer | `Doc.ents`, `Token.ent_iob`, `Token.ent_type`             |
| **textcat** | Text classifier         | `Doc.cats`                                                |

Notes: spaCy viene con los siguientes componentes incluidos en su pipeline.

El part-of-speech tagger añade los atributos `token.tag` y `token.pos`.

El dependency parser añade los atributos `token.dep` y `token.head` y es
responsable de detectar frases y los
<abbr title="En español: frases nominales.">base noun phrases</abbr>, también
conocidos como "noun chunks".

El named entity recognizer añade las entidades detectadas a la propiedad
`doc.ents`. También escribe los atributos del tipo de entidad en los tokens, lo
que indica si un token es parte de una entidad o no.

Finalmente, el <abbr title="En español: clasificador de texto.">text classifier</abbr> escribe las labels de categoría que aplican a
todo el texto y las añade a la propiedad `doc.cats`.

Debido a que las categorías de texto son siempre muy específicas, el text
classifier no está incluido en los modelos pre-entrenados por defecto. Pero lo
puedes usar para entrenar tu propio sistema.

---

# Detrás de cámaras

<img src="/package_meta_es.png" alt="Illustration of a package labelled es_core_news_sm, folders and file and the meta.json" />

- El pipeline está definido en el `meta.json` del modelo en el orden específico
- Los componentes incluidos necesitan datos binarios para hacer predicciones

Notes: Todos los modelos que puedes cargar en spaCy incluyen varios archivos y
un `meta.json`.

El meta define cosas como el lenguaje y el pipeline. Esto le deja saber a spaCy
cuáles son los componentes a los que les debe hacer un instance.

Los componentes incluidos que hacen predicciones también necesitan datos
binarios. Los datos se incluyen en el paquete del modelo y se cargan al
componente cuando cargas el modelo.

---

# Atributos del pipeline

- `nlp.pipe_names`: una lista de nombres de componentes del pipeline

```python
print(nlp.pipe_names)
```

```out
['tagger', 'parser', 'ner']
```

- `nlp.pipeline`: una lista de tuples de `(name, component)`

```python
print(nlp.pipeline)
```

```out
[('tagger', <spacy.pipeline.Tagger>),
 ('parser', <spacy.pipeline.DependencyParser>),
 ('ner', <spacy.pipeline.EntityRecognizer>)]
```

Notes: Para ver los nombres de los componentes del pipeline que están en el
objeto `nlp` actual puedes usar el atributo `nlp.pipe_names`.

Para una lista de tuples con los nombres y funciones de cada componente usa el
atributo `nlp.pipeline`.

Las funciones de los componentes son aquellas funciones que se aplican al doc
para procesarlo y añadir atributos - por ejemplo, part-of-speech tags o
entidades nombradas.

---

# ¡Practiquemos!

Notes: ¡Exploremos algunos de los pipelines de spaCy y miremos detrás de
cámaras!
