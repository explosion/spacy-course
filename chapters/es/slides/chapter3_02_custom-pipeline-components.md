---
type: slides
---

# Componentes personalizados del pipeline

Notes: Ahora que sabes cómo funciona el pipeline de spaCy exploremos otra característica muy poderosa: los componentes personalizados para el pipeline.

Los componentes personalizados del pipeline te permiten añadir tu propia función al pipeline de spaCy que se ejecuta cuando llamas al objeto `nlp` sobre un texto - por ejemplo, para modificar el doc y añadirle más datos.

---

# ¿Porqué tener componentes personalizados?

<img src="/pipeline.png" alt="Illustration of the spaCy pipeline" width="90%" />

- Haz que una función se ejecute automáticamente cuando llamas al objeto `nlp`
- Añade tus propios metadatos a los documentos y a los tokens
- Actualiza atributos incluidos como los `doc.ents`

Notes: Después de que el texto es convertido en tokens y un objeto `Doc` ha sido creado, los componentes del pipeline se aplican en orden. spaCy ofrece soporte para un rango de componentes incluidos, pero también te permite definir los tuyos.

Los componentes personalizados se ejecutan automáticamente cuando llamas al objeto `nlp` sobre un texto.

Son especialmente útiles para añadir tus propios metadatos a los documentos y a los tokens.

También puedes usarlos para actualizar los atributos incluidos, como los spans de las entidades nombradas.

---

# Anatomía de un componente (1)

- Funciones que toman un  `doc`, lo modifican y lo devuelven
- Pueden ser añadidos usando el método `nlp.add_pipe`

```python
def custom_component(doc):
    # Haz algo con el doc aquí
    return doc

nlp.add_pipe(custom_component)
```

Notes: Fundamentalmente, un componente del pipeline es una función o un <abbr title="Algo que puede ser llamado o ejecutado, así como una función o una clase.">callable</abbr> que toma a un doc, lo modifica y lo devuelve para que pueda ser procesado por el próximo componente en el pipeline.

Los componentes pueden ser añadidos al pipeline usando el método `nlp.add_pipe`. Éste toma al menos un argumento: la función del componente.

---

# Anatomía de un componente (2)

```python
def custom_component(doc):
    # Haz algo con el doc aquí
    return doc

nlp.add_pipe(custom_component)
```

| Argumento | Descripción          | Ejemplo                                   |
| -------- | -------------------- | ----------------------------------------- |
| `last`   | Si es `True`, lo pone de último  | `nlp.add_pipe(component, last=True)`      |
| `first`  | Si es `True`, lo pone primero | `nlp.add_pipe(component, first=True)`     |
| `before` | Lo añade antes del componente | `nlp.add_pipe(component, before="ner")`   |
| `after`  | Lo añade después del componente  | `nlp.add_pipe(component, after="tagger")` |

Notes: Para especificar _dónde_ añadir el componente en el pipeline, puedes usar uno de los siguientes argumentos keyword:

Si haces que el valor de `last` sea `True`, se añadirá el componente en el último lugar del pipeline. Este es el comportamiento por defecto.

Si haces que el valor de `first` sea `True`, se añadirá en el primer lugar del pipeline justo después del tokenizer.

Los argumentos `before` y `after` te permiten definir el nombre de un componente existente al que le puedes añadir el nuevo componente antes o después. Por ejemplo, `before="ner"` añadirá el nuevo componente antes del named entity recognizer.

Sin embargo, el otro componente al que se le añadirá un nuevo componente antes o después tiene que existir. Si no, spaCy arrojará un error.

---

# Ejemplo: un componente simple (1)

```python
# Crea el objeto nlp
nlp = spacy.load("es_core_news_sm")

# Define un componente personalizado
def custom_component(doc):
    # Imprime la longitud del doc en pantalla
    print("longitud del Doc:", len(doc))
    # Devuelve el objeto doc
    return doc

# Añade el componente al primer lugar del pipeline
nlp.add_pipe(custom_component, first=True)

# Imprime los nombres de los componentes del pipeline
print("Pipeline:", nlp.pipe_names)
```

```out
Pipeline: ['custom_component', 'tagger', 'parser', 'ner']
```

Notes: Aquí tenemos un ejemplo de un componente simple del pipeline.

Comenzamos con el modelo pequeño de español.

Luego definimos el componente - una función que toma un objeto `Doc` y luego lo devuelve.

Hagamos algo simple e imprimamos en pantalla la longitud del documento que pasa por el pipeline.

¡No olvides devolver el doc para que pueda ser procesado por el próximo componente en el pipeline! El doc creado por el tokenizer pasa por todos los componentes, así que es importante que todos devuelvan el doc modificado.

Ahora podemos añadir el componente al pipeline. Vamos a añadirlo en el primer lugar, justo después del tokenizer. Lo hacemos definiendo `first=True`.

Cuando imprimimos en pantalla los nombres de los componentes el nuevo aparece al principio. Esto significa que será aplicado cuando procesemos un doc.

---

# Ejemplo: un componente simple (2)

```python
# Crea el objeto nlp
nlp = spacy.load("es_core_news_sm")

# Define un componente personalizado
def custom_component(doc):

    # Imprime la longitud del doc en pantalla
    print("longitud del Doc:", len(doc))

    # Devuelve el objeto doc
    return doc

# Añade el componente al primer lugar del pipeline
nlp.add_pipe(custom_component, first=True)

# Procesa un texto
doc = nlp("¡Hola Mundo!")
```

```out
longitud del Doc: 4
```

Notes: Ahora, cuando procesamos un texto usando el objeto `nlp`, el componente personalizado será aplicado al doc y la longitud del documento será impresa en pantalla.

---

# ¡Practiquemos!

Notes: ¡Es hora de llevar esto a la práctica y escribir tu primer componente para el pipeline!
