---
type: slides
---

# Introducción a spaCy

Notes: ¡Hola, soy Ines! Soy una de las programadoras principales de spaCy, un paquete popular para hacer Procesamiento de Lenguaje Natural en Python.

En esta lección vamos a ver los conceptos más importantes de spaCy y cómo comenzar a usarlo.

---

# El objeto nlp

```python
# Importa la clase de lenguaje "Spanish"
from spacy.lang.es import Spanish

# Crea el objeto nlp
nlp = Spanish()
```

- contiene el pipeline de procesamiento
- incluye las reglas específicas de su lenguaje para tokenizar, etc.

Notes: En el centro de spaCy está el objeto que contiene el <abbr title="Un pipeline es una serie de acciones que se ejecutan en secuencia. Cada paso depende del anterior usando su resultado.">pipeline</abbr> de procesamiento. Normalmente llamamos "nlp" a esta variable.

Por ejemplo, para crear un objeto `nlp` de español puedes importar la clase de lenguaje `Spanish` de `spacy.lang.es` y crear un <abbr title="Es un ejemplar de una clase, a veces referido incorrectamente como instancia.">instance</abbr>. Puedes usar el objeto nlp como una función para analizar el texto.

Contiene todos los componentes diferentes de un pipeline.

También incluye las reglas específicas de su lenguaje usadas para convertir el texto en tokens con palabras y puntuación. spaCy ofrece soporte para varios lenguajes que están disponibles en `spacy.lang`.

---

# El objeto Doc

```python
# Creado procesando un string de texto con el objeto nlp
doc = nlp("¡Hola Mundo!")

# Itera sobre los tokens en un Doc
for token in doc:
    print(token.text)
```

```out
¡
Hola
Mundo
!
```

Notes: Cuando procesas un <abbr title="El tipo de dato de Python para texto.">string</abbr> de texto con el objeto `nlp`, spaCy crea un objeto `Doc` - de "documento". 
El Doc te permite acceder a la información sobre el texto en una forma estructurada y sin perder información.

El Doc se comporta como una secuencia normal de Python y te permite iterar sobre sus tokens u obtener un token con su índice. Más adelante hablaremos más de ello.

---

# El objeto Token

<img src="/doc.png" alt="Illustration of a Doc object containing four tokens" width="50%" />

```python
doc = nlp("¡Hola Mundo!")

# Usa el índice del Doc para obtener un solo Token
token = doc[2]

# Obtén el texto del token a través del atributo .text
print(token.text)
```

```out
Mundo
```

Notes: Los objetos `Token` representan a los tokens en un documento. Por ejemplo, una palabra o un signo de puntuación.

Para obtener el token en una posición específica puedes usar el índice del doc.

Los objetos `Token` también proveen varios atributos que te permiten acceder a más información sobre los tokens. Por ejemplo, el atributo `.text` devuelve el texto del token.

---

# El objeto Span

<img src="/doc_span.png" width="50%" alt="Illustration of a Doc object containing four tokens and three of them wrapped in a Span" />

```python
doc = nlp("¡Hola Mundo!")

# Un slice de un Doc en un objeto Span
span = doc[2:4]

# Obtén el texto del span a través del atributo .text
print(span.text)
```

```out
Mundo!
```

Notes: Un objeto `Span` es un <abbr title="Un slice es un subconjunto de elementos dentro de una secuencia de datos como una lista o un objeto Doc.">slice</abbr> de un documento compuesto por uno o más tokens. Es solo un <abbr title="En español: representación o vista.">view</abbr> de un `Doc` y no contiene los datos en sí.

Para crear un span puedes usar la notación de slice de Python. Por ejemplo, `2:4` crea un slice que comienza en el token en la posición 2 hasta - pero no incluyendo! - el token en la posición 4.

---

# Atributos léxicos

```python
doc = nlp("Eso cuesta €5.")
```

```python
print("Index:   ", [token.i for token in doc])
print("Text:    ", [token.text for token in doc])

print("is_alpha:", [token.is_alpha for token in doc])
print("is_punct:", [token.is_punct for token in doc])
print("like_num:", [token.like_num for token in doc])
```

```out
Index:    [0, 1, 2, 3, 4]
Text:     ['Eso', 'cuesta', '€', '5', '.']

is_alpha: [True, True, False, False, False]
is_punct: [False, False, False, False, True]
like_num: [False, False, False, True, False]
```

Notes: Aquí puedes ver algunos de los atributos disponibles de los tokens:

`i` es el índice del token dentro del documento padre.

`text` devuelve el texto del token.

`is_alpha`, `is_punct` y `like_num` devuelven valores booleanos que indican si un token está compuesto por caracteres alfabéticos, si es puntuación, o si _parece_ un número. Por ejemplo, el token "10" - uno, cero - o la palabra "diez" - D, I, E, Z.

Estos atributos también se llaman atributos léxicos: se refieren a una entrada en el vocabulario y no dependen del contexto del token.

---

# ¡Practiquemos!

Notes: Veamos todo esto en acción y procesemos tu primer texto con spaCy.
