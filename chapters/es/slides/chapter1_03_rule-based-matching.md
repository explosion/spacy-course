---
type: slides
---

# Encontrando patrones basados en reglas

Notes: En esta lección veremos el matcher de spaCy, que te permite escribir
reglas para encontrar palabras y frases en el texto.

---

# ¿Por qué no simplemente expresiones regulares?

- Matching en objetos `Doc`, no solamente en strings
- Matching en tokens y atributos de tokens
- Usa las predicciones del modelo
- Ejemplo: "araña" (verbo) vs. "araña" (sustantivo)

Notes: Comparándolo con las expresiones regulares, el matcher funciona con
objetos `Doc` y `Token`, en vez de únicamente strings.

También es más flexible: puedes buscar textos, pero también otros atributos
léxicos.

Inclusive puedes escribir reglas que usen las predicciones del modelo.

Por ejemplo, encontrar la palabra "araña" únicamente si es un verbo y no un
sustantivo.

---

# Match patterns

- Listas de diccionarios, uno por token

- Encuentra por textos exactos de tokens

```python
[{"TEXT": "iPhone"}, {"TEXT": "X"}]
```

- Encuentra por atributos léxicos

```python
[{"LOWER": "iphone"}, {"LOWER": "x"}]
```

- Encuentra por cualquier atributo del token

```python
[{"LEMMA": "comprar"}, {"POS": "NOUN"}]
```

Notes: Los match patterns son listas de diccionarios. Cada diccionario describe
un token. Los keys son los nombres de los atributos del token, mapeados a sus
valores esperados.

En este ejemplo, estamos buscando dos token con el texto "iPhone" y "X".

También podemos usar otros atributos de los tokens para encontrar lo que
buscamos. Aquí estamos buscando dos tokens que en minúsculas son iguales a
"iphone" y "x".

También podemos escribir patrones que usen los atributos predichos por el
modelo. Aquí estamos buscando un token con el lemma "comprar", más un sustantivo. El
lemma es la forma básica, así que este patrón encontraría frases como "comprando
leche" o "compré flores".

---

# Usando el Matcher (1)

```python
import spacy

# Importa el Matcher
from spacy.matcher import Matcher

# Carga el modelo y crea un objeto nlp
nlp = spacy.load("es_core_news_sm")

# Inicializa el matcher con el vocabulario compartido
matcher = Matcher(nlp.vocab)

# Añade el patrón al matcher
pattern = [{"TEXT": "adidas"}, {"TEXT": "ZX"}]
matcher.add("ADIDAS_PATTERN", None, pattern)

# Procesa un texto
doc = nlp("Nuevos diseños de zapatillas en la colección adidas ZX")

# Llama al matcher sobre el doc
matches = matcher(doc)
```

Notes: Para usar el patrón primero importamos el matcher desde `spacy.matcher`.

También cargamos el modelo y creamos un objeto `nlp`.

El matcher es inicializado con el vocabulario compartido, `nlp.vocab`.
Aprenderás más sobre esto más adelante - por ahora solo recuerda pasarlo.

El método `matcher.add` te permite añadir un patrón. El primer argumento es un
ID único para identificar el patrón que fue buscado. El segundo argumento es un
callback opcional, no necesitamos uno aquí, así que lo ponemos como `None`. El
tercer argumento es el patrón.

Para encontrar el patrón en un texto, podemos llamar el matcher sobre cualquier
doc.

Esto devolverá los resultados.

---

# Usando el Matcher (2)

```python
# Llama al matcher sobre el doc
doc = nlp("Nuevos diseños de zapatillas en la colección adidas ZX")
matches = matcher(doc)

# Itera sobre los resultados
for match_id, start, end in matches:
    # Obtén el span resultante
    matched_span = doc[start:end]
    print(matched_span.text)
```

```out
adidas ZX
```

- `match_id`: valor hash del nombre del patrón
- `start`: índice de inicio del span resultante
- `end`: índice del final del span resultante

Notes: Cuando llamas el matcher sobre un doc, este devuelve una lista de <abbr title="En español: tuplas, un tuple es un tipo de dato que contiene una secuencia fija de ítems, como una lista, pero que no se puede modificar.">tuples</abbr>.

Cada tuple consiste de tres valores: el ID del resultado, el índice de inicio y
el índice del final del span resultante.

Esto significa que podemos iterar sobre los resultados y crear un objeto `Span`:
un slice del doc que comienza en el índice de inicio y termina en el índice del
final.

---

# Encontrando por atributos léxicos

```python
pattern = [
    {"IS_DIGIT": True},
    {"LOWER": "copa"},
    {"LOWER": "mundial"},
    {"LOWER": "fifa"},
    {"IS_PUNCT": True}
]
```

```python
doc = nlp("2014 Copa Mundial FIFA: Alemania ganó!")
```

```out
2014 Copa Mundial FIFA:
```

Notes: Aquí tenemos un ejemplo de un patrón más complejo usando atributos
léxicos.

Estamos buscando cinco tokens:

Un token compuesto únicamente por dígitos.

Tres tokens insensibles a mayúsculas/minúsculas para "copa", "mundial" y "fifa".

Un token que está compuesto por puntuación.

El patrón encuentra los tokens "2014 Copa Mundial FIFA:".

---

# Encontrando por otros atributos del token

```python
pattern = [
    {"LEMMA": "gustar", "POS": "VERB"},
    {"POS": "VERB"}
]
```

```python
doc = nlp("Me gustaba correr pero ahora me gusta nadar.")
```

```out
gustaba correr
gusta nadar
```

Notes: En este ejemplo estamos buscando dos tokens:

Un verbo con el lemma "gustar", seguido por un verbo.

Este patrón encontrará "gustaba correr" y "gusta nadar".

---

# Usando operadores y cuantificadores (1)

```python
pattern = [
    {"LEMMA": "comprar"},
    {"POS": "DET", "OP": "?"},  # opcional: encuentra 0 o 1 veces
    {"POS": "NOUN"}
]
```

```python
doc = nlp("Me compré un smartphone. Ahora le estoy comprando aplicaciones.")
```

```out
compré un smartphone
comprando aplicaciones
```

Notes: Operadores y cuantificadores te permiten definir con qué frecuencia un
token debe ser encontrado. Pueden ser añadidos con el key "OP".

Aquí, el operador "?" hace que el token determinante sea opcional, así que
encontrará un token con el lemma "comprar", un artículo opcional y un sustantivo.

---

# Usando operadores y cuantificadores (2)

| Ejemplo       | Descripción                     |
| ------------- | ------------------------------- |
| `{"OP": "!"}` | Negación: encuentra 0 veces     |
| `{"OP": "?"}` | Opcional: encuentra 0 o 1 veces |
| `{"OP": "+"}` | Encuentra 1 o más veces         |
| `{"OP": "*"}` | Encuentra 0 o más veces         |

Notes: "OP" puede tener uno de cuatro valores:

Un "!" niega el token, así que es encontrado 0 veces.

Un "?" hace que el token sea opcional y es encontrado 0 o 1 veces.

Un "+" encuentra el token 1 o más veces.

Finalmente, un "\*" encuentra 0 o más veces.

Los operadores pueden hacer que tus patrones sean mucho más poderosos, pero
también pueden añadir más complejidad, así que úsalos sabiamente.

---

# ¡Practiquemos!

Notes: Encontrar usando patrones basados en tokens abre muchas posibilidades
nuevas para extraer información. ¡Así que probémoslo y escribamos algunos
patrones!
