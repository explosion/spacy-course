---
type: slides
---

# Modelos estadísticos

Notes: ¡Ahora vamos a añadir más poder al objeto `nlp`!

En esta lección aprenderás sobre los modelos estadísticos de spaCy.

---

# Qué son los modelos estadísticos?

- Le permiten a spaCy predecir atributos lingüísticos _en contexto_
  - Part-of-speech tags
  - Dependencias sintácticas
  - Entidades nombradas
- Entrenados con textos de ejemplo anotados
- Pueden ser actualizados con más ejemplos para afinar las predicciones

Notes: Algunas de las cosas más interesantes que puedes analizar son específicas al contexto: por ejemplo, si una palabra es un verbo o si un span de texto es el nombre de una persona.

Los modelos estadísticos le permiten a spaCy hacer predicciones dentro del contexto. Esto normalmente incluye las part-of-speech tags, dependencias sintácticas y entidades nombradas.

Los modelos son entrenados con <abbr title="También conocido como conjunto de datos.">datasets</abbr> de textos de ejemplo anotados.

Los modelos pueden ser actualizados con más ejemplos para afinar sus predicciones - por ejemplo, para que se desempeñe mejor con tus datos específicos.

---

# Paquetes de modelos

<img src="/package_es.png" alt="A package with the label en_core_web_sm" width="30%" align="right" />

```bash
$ python -m spacy download es_core_news_sm
```

```python
import spacy

nlp = spacy.load("es_core_news_sm")
```

- Parámetros binarios
- Vocabulario
- Metadata (lenguaje, pipeline)

Notes: spaCy provee varios paquetes de modelos pre-entrenados que puedes descargar usando el comando `spacy download`. Por ejemplo, el paquete "en_core_web_sm" es un modelo pequeño de inglés que provee soporte para todas las capacidades centrales y está entrenado usando texto de la web.

El método `spacy.load` carga el paquete de modelo por su nombre y devuelve un objeto `nlp`.

El paquete provee los <abbr title="En inglés: en un contexto de Machine Learning, conocidos como binary weights.">parámetros binarios</abbr> que le permiten a spaCy hacer predicciones.

También incluye el vocabulario y la metadata para que spaCy sepa cuál clase de lenguaje usar y cómo configurar el pipeline de procesamiento.

---

# Prediciendo part-of-speech tags

```python
import spacy

# Carga el modelo pequeño de español
nlp = spacy.load("es_core_news_sm")

# Procesa un texto
doc = nlp("Ella comió pizza")

# Itera sobre los tokens
for token in doc:
    # Imprime en pantalla el texto y el part-of-speech tag predicho
    print(token.text, token.pos_)
```

```out
Ella PRON
comió VERB
pizza NOUN
```

Notes: Revisemos las predicciones del modelo. En este ejemplo estamos usando spaCy para predecir part-of-speech tags, los tipos de palabras en el contexto.

Primero, cargamos el modelo pequeño de inglés y recibimos un objeto `nlp`.

Luego, procesamos el texto "Ella comió pizza".

Para cada token en el Doc podemos imprimir en pantalla el texto y el part-of-speech tag predicho usando el atributo `.pos_`.

En spaCy, los atributos que devuelven un string normalmente terminan con un guión bajo (`_`). mientras que atributos sin un guión bajo devuelven un valor ID de tipo <abbr title="En inglés: integer, un número entero sin parte decimal.">entero</abbr>.

Aquí el modelo predijo correctamente "comió" como el verbo y "pizza" como el sustantivo.

---

# Prediciendo dependencias sintácticas

```python
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)
```

```out
Ella PRON nsubj comió
comió VERB ROOT comió
pizza NOUN obj comió
```

Notes: Además de los part-of-speech tags, también podemos predecir las relaciones entre las palabras. Por ejemplo, si una palabra es el sujeto o el objeto de una oración.

El atributo `.dep_` devuelve el dependency label predicho.

El atributo `.head` devuelve el token <abbr title="En inglés: head.">cabeza</abbr> sintáctico. Otra forma de pensarlo es como el token padre al que esta palabra está atada.

---

# Esquema de dependency label

<img src="/dep_example_es.png" alt="Visualization of the dependency graph for 'Ella comió la pizza'" />

| Label     | Descripción             | Ejemplo |
| --------- | ----------------------- | ------- |
| **nsubj** | sujeto nominal          | Ella    |
| **obj**   | objeto                  | pizza   |

Notes: spaCy usa un esquema de <abbr title="En español se conocen como etiquetas, pero para mantener la diferenciación entre label y tag, las usamos en inglés.">labels</abbr> estándar para describir dependencias sintácticas. Aquí verás un ejemplo de algunas labels comunes:

El pronombre "Ella" es un sujeto nominal unido al verbo - en este caso, a "comió".

El sustantivo "pizza" es un objeto unido al verbo "comió". Está siendo comido por el sujeto "ella".

---

# Prediciendo entidades nombradas

<img src="/ner_example_es.png" alt="Visualization of the named entities in 'Apple es la marca que más satisfacción genera en EE.UU.; pero el iPhone, fue superado por el Galaxy Note 9'" width="80%" />

```python
# Procesa un texto
doc = nlp(
    "Apple es la marca que más satisfacción genera en EE.UU., "
    "pero el iPhone, fue superado por el Galaxy Note 9"
)

# Itera sobre las entidades predichas
for ent in doc.ents:
    # Imprime en pantalla el texto y el label de la entidad
    print(ent.text, ent.label_)
```

```out
Apple ORG
EE.UU LOC
iPhone MISC
Galaxy Note 9 MISC
```

Notes: Las entidades nombradas son "objetos de la vida real" que tienen un nombre asignado. Por ejemplo, una persona, una organización o un país.

La propiedad `doc.ents` te permite acceder a las entidades nombradas predichas por el modelo.

Devuelve un iterador de objetos `Span`, así que podemos imprimir en pantalla el texto y el label de la entidad usando el atributo `.label_`.

En este caso, el modelo predijo correctamente "Apple" como una organización, "EE.UU" como un lugar, "iPhone" y "Galaxy Note 9" con la categoría miscelanea.

---

# Tip: el método spacy.explain

Obtén definiciones rápidas de los tags y labels más comunes.

```python
spacy.explain("LOC")
```

```out
'Name of politically or geographically defined location'
```

```python
spacy.explain("NNP")
```

```out
'noun, proper singular'
```

```python
spacy.explain("MISC")
```

```out
'Miscellaneous entities, e.g. events, nationalities, products or works of art'
```

Notes: Un tip rápido: Para obtener definiciones de los tags y labels más comunes puedes usar la función asistente `spacy.explain`.

Por ejemplo, "LOC" para lugar no es necesariamente intuitivo, pero `spacy.explain` puede decirte que se refiere a nombres de ubicaciones definidas política o geográficamente.

Lo mismo funciona para part-of-speech tags y dependency labels.

---

# ¡Practiquemos!

Notes: Ahora es tu turno. Exploremos los modelos estadísticos de spaCy y sus predicciones.
