---
type: slides
---

# Modelos Estadísticos

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

Los modelos estadísticos le permiten a spaCy hacer predicciones dentro del contexto. Esto normalmente incluye las part-of speech tags, dependencias sintácticas y entidades nombradas.

Los modelos son entrenados con <abbr title="también conocido como conjunto de datos"> datasets </abbr> de textos de ejemplo anotados.

Los modelos pueden ser actualizados con más ejemplos para afinar sus predicciones - por ejemplo, para que se desempeñe mejor con tus datos específicos.

---

# Paquetes de modelos

<img src="/package.png" alt="A package with the label en_core_web_sm" width="30%" align="right" />

```bash
$ python -m spacy download en_core_web_sm
```

```python
import spacy

nlp = spacy.load("en_core_web_sm")
```

- Parámetros binarios
- Vocabulario
- Metadata (lenguaje, pipeline)

Notes: spaCy provee varios paquetes de modelos pre-entrenados que puedes descargar usando el comando `spacy download`. Por ejemplo, el paquete "en_core_web_sm" es un modelo pequeño de inglés que provee soporte para todas las capacidades centrales y está entrenado usando texto de la web.

El método `spacy.load` carga el paquete de modelo por su nombre y devuelve un objeto `nlp`.

El paquete provee los <abbr title="en inglés, en un contexto de Machine Leraning, conocidos como binary weights">parámetros binarios</abbr> que le permiten a spaCy hacer predicciones.

También incluye el vocabulario y la metadata para que spaCy sepa cuál clase de lenguaje usar y cómo configurar el pipeline de procesamiento.

---

# Prediciendo Part-of-speech Tags

```python
import spacy

# Carga el modelo pequeño de inglés
nlp = spacy.load("en_core_web_sm")

# Procesa un texto
doc = nlp("She ate the pizza")

# Itera sobre los tokens
for token in doc:
    # Imprime en pantalla el texto y el part-of-speech tag predicho
    print(token.text, token.pos_)
```

```out
She PRON
ate VERB
the DET
pizza NOUN
```

Notes: Revisemos las predicciones del modelo. En este ejemplo estamos usando spaCy para predecir part-of-speech tags, los tipos de palabras en el contexto.

Primero, cargamos el modelo pequeño de inglés y recibimos un objeto `nlp`.

Siguiente, procesamos el texto "She ate the pizza".

Para cada token en el Doc podemos imprimir en pantalla el texto y el part-of-speech tag predicho usando el atributo `.pos_`.

En spaCy, los atributos que devuelven un string usualmente terminan con un guión bajo (`_`). mientras que atributos sin un guión bajo devuelven un valor ID de tipo integer.

Aquí el modelo predijo correctamente "ate" como el verbo y "pizza" como el sustantivo.

---

# Prediciendo dependencias sintácticas

```python
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)
```

```out
She PRON nsubj ate
ate VERB ROOT ate
the DET det pizza
pizza NOUN dobj ate
```

Notes: Además de los part-of-speech tags, también podemos predecir las relaciones entre las palabras. Por ejemplo, si una palabra es el sujeto o el objeto de una oración.

El atributo `.dep_` devuelve el dependency label predicho.

El atributo `.head` devuelve el token <abbr title="en inglés head">cabeza</abbr> sintáctico. Otra forma de pensarlo es como el token padre (superordinado) al que esta palabra está atada.

---

# Esquema de Dependency label

<img src="/dep_example.png" alt="Visualization of the dependency graph for 'She ate the pizza'" />

| Label     | Descripción             | Ejemplo |
| --------- | ----------------------- | ------- |
| **nsubj** | sujeto nominal          | She     |
| **dobj**  | objeto directo          | pizza   |
| **det**   | determinante (artículo) | the     |

Notes: spaCy usa un esquema de labels estándar para describir dependencias sintácticas. Aquí verás un ejemplo de algunas <abbr title="en español se conocen como etiquetas, pero para mantener la diferenciación entre label y tag, las usamos en inglés">labels</abbr> comúnes:

El pronombre "She" es un sujeto nominal unido al verbo - en este caso, a "ate".

El sustantivo "pizza" es un objeto directo unido al verbo "ate". Está siendo comido ("eaten") por el sujeto "she".

El determinante "the", también conocido como artículo, está unido al sustantivo "pizza".

---

# Prediciendo entidades nombradas

<img src="/ner_example.png" alt="Visualization of the named entities in 'Apple is looking at buying U.K. startup for $1 billion'" width="80%" />

```python
# Procesa un texto
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

# Itera sobre las entidades predichas
for ent in doc.ents:
    # Imprime en pantalla el texto y el label del la entidad
    print(ent.text, ent.label_)
```

```out
Apple ORG
U.K. GPE
$1 billion MONEY
```

Notes: Las entidades nombradas son "objetos de la vida real" que tienen un nombre asignado. Por ejemplo, una persona, una organización o un país.

La propiedad `doc.ents` te permite acceder a las entidades nombradas predichas por el modelo.

Devuelve un iterador de objetos `Span`, así que podemos imprimir en pantalla el texto y el label de la entidad usando el atributo `.label_`.

En este caso, el modelo predijo correctamente "Apple" como una organización, "U.K." como una entidad geopolítica y "\$1 billion" como dinero.

---

# Tip: el método spacy.explain

Obtén definiciones rápidas de los tags y labels más comunes.

```python
spacy.explain("GPE")
```

```out
'Countries, cities, states'
```

```python
spacy.explain("NNP")
```

```out
'noun, proper singular'
```

```python
spacy.explain("dobj")
```

```out
'direct object'
```

Notes: Un tip rápido: Para obtener definiciones de los tags y labels más comunes puedes usar la función asistente `spacy.explain`.

Por ejemplo, "GPE" para entidad geopolítica no es necesariamente intuitivo, pero `spacy.explain` puede decirte que se refiere a países, ciudades y estados.

Lo mismo funciona para part-of-speech tags y dependency labels.

---

# ¡Practiquemos!

Notes: Ahora es tu turno. Exploremos los modelos estadísticos de spaCy y sus predicciones.
