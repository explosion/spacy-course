---
type: slides
---

# Modelos estadísticos

Notes: ¡Ahora vamos a añadir más poder al objeto `nlp`!

En esta lección aprenderás sobre los modelos estadísticos de spaCy.

---

# ¿Qué son los pipelines entrenados?

- Le permiten a spaCy predecir atributos lingüísticos _en contexto_
  - Etiquetado gramatical
  - Dependencias sintácticas
  - Entidades nombradas
- Entrenados con textos de ejemplo anotados
- Pueden ser actualizados con más ejemplos para afinar las predicciones

Notes: Algunas de las cosas más interesantes que puedes analizar son específicas
al contexto: por ejemplo, si una palabra es un verbo o si un span de texto es
el nombre de una persona.

Los componentes de los pipelines entrenados tienen modelos estadísticos que le
permiten a spaCy hacer predicciones en contexto. Esto normalmente incluye el
etiquetado gramatical, dependencias sintácticas y entidades nombradas.

Los pipelines son entrenados con <abbr title="También conocidos como conjuntos de datos.">datasets</abbr> de textos de ejemplo anotados.

Los pipelines pueden ser actualizados con más ejemplos para afinar sus
predicciones - por ejemplo, para que se desempeñe mejor en tus datos
específicos.

---

# Paquetes de pipelines

<img src="/package_es.png" alt="Un paquete con la etiqueta es_core_news_sm" width="30%" align="right" />

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
- Archivo de configuración

Notes: spaCy provee varios paquetes de pipelines pre-entrenados que puedes
descargar usando el comando `spacy download`. Por ejemplo, el paquete
"es_core_news_sm" es un pipeline pequeño de español que provee soporte para
todas las capacidades centrales y está entrenado usando textos de internet.

El método `spacy.load` carga el paquete del pipeline por su nombre y devuelve
un objeto `nlp`.

El paquete provee los <abbr title="En un contexto de Machine Learning, son conocidos como `binary weights` en inglés.">parámetros binarios</abbr> que le permiten a spaCy hacer predicciones.

También incluye el vocabulario y los metadatos acerca del pipeline y el archivo
de configuración utilizado para entrenarlo. El paquete le dice a spaCy cuál
clase de lenguaje usar y cómo configurar el pipeline de procesamiento.

---

# Predicción de etiquetas gramaticales

```python
import spacy

# Carga el pipeline pequeño de español
nlp = spacy.load("es_core_news_sm")

# Procesa un texto
doc = nlp("Ella comió pizza")

# Itera sobre los tokens
for token in doc:
    # Imprime en pantalla el texto y la etiqueta gramatical predicha
    print(token.text, token.pos_)
```

```out
Ella PRON
comió VERB
pizza NOUN
```

Notes: Revisemos las predicciones del modelo. En este ejemplo estamos usando
spaCy para predecir etiquetas gramaticales, es decir, los tipos de palabras en
contexto.

Primero, cargamos el modelo pequeño de español y recibimos un objeto `nlp`.

Luego, procesamos el texto "Ella comió pizza".

Por cada token en el doc, podemos imprimir en pantalla el texto y la etiqueta
gramatical predicha usando el atributo `.pos_`.

En spaCy, los atributos que devuelven un string normalmente terminan con un
guion bajo (`_`). mientras que atributos sin un guion bajo devuelven un valor ID de tipo <abbr title="En inglés: integer, un número entero sin parte decimal.">entero</abbr>.

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

Notes: Además de las etiquetas gramaticales, también podemos predecir las
relaciones entre las palabras. Por ejemplo, si una palabra es el sujeto o el
objeto de una oración.

El atributo `.dep_` devuelve la etiqueta de la dependencia sintáctica predicha.

El atributo `.head` devuelve el token de la
<abbr title="En inglés: head.">cabeza</abbr> de la dependencia sintáctica. Otra
forma de concebirlo es como el token "padre" al que esta palabra está atada.

---

# Esquema del etiquetado de dependencias sintácticas

<img src="/dep_example_es.png" alt="Visualización de un gráfico de dependencias sintácticas dependency para 'Ella comió la pizza'" />

| Label     | Descripción             | Ejemplo |
| --------- | ----------------------- | ------- |
| **nsubj** | sujeto nominal          | Ella    |
| **obj**   | objeto                  | pizza   |

Notes: spaCy usa un esquema de etiquetas estándar para describir dependencias
sintácticas. Aquí verás un ejemplo de algunas etiquetas comunes:

El pronombre "Ella" es un sujeto nominal unido al verbo - en este caso, a
"comió".

El sustantivo "pizza" es un objeto unido al verbo "comió". Este objeto está
siendo comido por el sujeto "ella".

---

# Prediciendo entidades nombradas

<img src="/ner_example_es.png" alt="Visualización de las entidades nombradas en 'Apple es la marca que más satisfacción genera en EE.UU.; pero el iPhone, fue superado por el Galaxy Note 9'" width="80%" />

```python
# Procesa un texto
doc = nlp(
    "Apple es la marca que más satisfacción genera en EE.UU., "
    "pero el iPhone, fue superado por el Galaxy Note 9"
)

# Itera sobre las entidades predichas
for ent in doc.ents:
    # Imprime en pantalla el texto y la etiqueta de la entidad
    print(ent.text, ent.label_)
```

```out
Apple ORG
EE.UU LOC
iPhone MISC
Galaxy Note 9 MISC
```

Notes: Las entidades nombradas son "objetos de la vida real" que tienen un
nombre asignado. Por ejemplo, una persona, una organización o un país.

La propiedad `doc.ents` te permite acceder a las entidades nombradas predichas
por el modelo de reconocimiento de entidades.

La propiedad `doc.ents` devuelve un iterador de objetos `Span`, así que podemos
imprimir en pantalla el texto y la etiqueta de la entidad usando el atributo
`.label_`.

En este caso, el modelo predijo correctamente "Apple" como una organización,
"EE.UU" como un lugar, "iPhone" y "Galaxy Note 9" con la categoría miscelanea.

---

# Tip: el método spacy.explain

Obtén definiciones rápidas de las etiquetas más comunes.

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

Notes: Un tip rápido: Para obtener definiciones de las etiquetas más
comunes puedes usar la función asistente `spacy.explain`.

Por ejemplo, "LOC" para lugar no es necesariamente intuitivo, pero
`spacy.explain` puede decirte que se refiere a ubicaciones naturales no
geopolíticas como cordilleras o cuerpos de agua.

De igual manera funciona para el etiquetado gramatical y de dependencias
sintácticas.

---

# ¡Practiquemos!

Notes: Ahora es tu turno. Exploremos los modelos estadísticos de spaCy y sus predicciones.
