---
type: slides
---

# Combinando modelos y reglas

Notes: Combinar modelos estadísticos con sistemas basados en reglas es uno de los trucos más poderosos que tienes en tu caja de herramientas de NLP.

En esta lección veremos cómo hacerlo con spaCy.

---

# Predicciones estadísticas vs. reglas

|                              | **Modelos estadísticos**                                                 | **Sistemas basados en reglas**   |
| ---------------------------- | ------------------------------------------------------------------------ | -------------------------------- |
| **Casos**                    | la aplicación necesita _generalizar_ basada en ejemplos                  |                                  |
| **Ejemplos de la vida real** | nombres de productos, nombres de personas, relaciones de sujeto/objeto   |                                  |
| **Características de spaCy** | entity recognizer, dependency parser, part-of-speech tagger              |                                  |

Notes: Los modelos estadísticos son útiles si tu aplicación necesita poder generalizar basada en pocos ejemplos.

Por ejemplo, detectar nombres de productos o personas normalmente se beneficia de un modelo estadístico. En vez de proveer una lista de todos los nombres de personas, tu aplicación debería poder predecir si un span de tokens es un nombre de persona. Del mismo modo, puedes predecir dependency labels para encontrar relaciones de sujeto/objeto.

Para hacer esto, usarías el entity recognizer, el dependency parser o el part-of-speech tagger de spaCy.

---

# Predicciones estadísticas vs. reglas

|                              | **Modelos estadísticos**                                                 | **Sistemas basados en reglas**   |
| ---------------------------- | ------------------------------------------------------------------------ | -------------------------------- |
| **Casos**                    | la aplicación necesita _generalizar_ basada en ejemplos                  | diccionario con número infinito de casos                              |
| **Ejemplos de la vida real** | nombres de productos, nombres de personas, relaciones de sujeto/objeto   | países del mundo, ciudades, nombres de drogas, razas de perros                                 |
| **Características de spaCy** | entity recognizer, dependency parser, part-of-speech tagger              | tokenizer `Matcher`, `PhraseMatcher`                                |

Notes: Los enfoques basados en reglas son muy útiles si hay un número más o menos finito de casos que quieres encontrar. Por ejemplo, todos los países o ciudades del mundo, nombres de drogas o inclusive razas de perros.

En spaCy puedes lograr esto con una regla de tokenización a la medida, así como el matcher y el <abbr title="El matcher de frases. Para revisar qué es el matcher, vuelve a la lección anterior.">phrase matcher</abbr>.

---

# Resumen: Encontrando patrones basados en reglas

```python
# Inicializa con el vocabulario compartido
from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)

# Los patrones son listas de diccionarios que describen los tokens
pattern = [{'LEMMA': 'love', 'POS': 'VERB'}, {'LOWER': 'cats'}]
matcher.add('LOVE_CATS', None, pattern)

# Los operadores pueden especificar que tan seguido puede ser buscado un token
pattern = [{'TEXT': 'very', 'OP': '+'}, {'TEXT': 'happy'}]
matcher.add('VERY_HAPPY', None, pattern)

# Llamar al matcher sobre un doc devuelve una lista de tuples con (match_id, inicio, final)
doc = nlp("I love cats and I'm very very happy")
matches = matcher(doc)
```

Notes: En el capítulo anterior aprendiste a usar el matcher basado en reglas de spaCy para encontrar patrones complejos en tus textos. Aquí está un resumen corto.

El matcher se inicializa con el vocabulario compartido - usualmente `nlp.vocab`.

Los patrones son listad de diccionarios y cada diccionario describe un token y sus atributos. Los patrones pueden ser añadidos usando el método `matcher.add`.

Los operadores te permiten especificar que tan a menudo buscar un token. Por ejemplo, "+" te deja buscar una o más veces.

Llamando a un matcher sobre el objeto doc devolverá una lista de los resultados. Cada resultado es un tuple que contiene un ID y el índice de inicio y final del token en el documento.

---

# Añadiendo predicciones estadísticas

```python
matcher = Matcher(nlp.vocab)
matcher.add('DOG', None, [{'LOWER': 'golden'}, {'LOWER': 'retriever'}])
doc = nlp("I have a Golden Retriever")

for match_id, start, end in matcher(doc):
    span = doc[start:end]
    print('Matched span:', span.text)
    # Obtén el token raíz del span y el token raíz central (head)
    print('Root token:', span.root.text)
    print('Root head token:', span.root.head.text)
    # Obtén el token anterior y su POS tag
    print('Previous token:', doc[start - 1].text, doc[start - 1].pos_)
```

```out
Matched span: Golden Retriever
Root token: Retriever
Root head token: have
Previous token: a DET
```

Notes: Aquí tenemos un ejemplo de una regla para el matcher que encuentra "golden retriever.

Si iteramos sobre los resultados devueltos por el matcher podemos obtener el match ID y el índice de inicio y final del span encontrado. Entonces podemos averiguar más sobre él. Los objetos `Span` nos dan acceso al documento original y a todos los otros atributos del token y características lingüísticas predichas por el modelo.

Por ejemplo, podemos obtener el token raíz del span. Si el span contiene más de un token, este token será el que determina la categoría de la frase. Por ejemplo, la raíz de "Golden Retriever" es "Retriever". También podemos encontrar el token cabeza de la raíz. Esto es el "padre" sintáctico que gobierna la frase - en este caso, el verbo "have".

Finalmente, podemos obtener el token anterior y sus atributos. En este caso, es el determinante, el artículo "a".

---

# Encontrando frases eficientemente "phrase matching" (1)

- `PhraseMatcher` como las expresiones regulares o una búsqueda de palabras claves - pero con acceso a los tokens!
- Toma al objeto `Doc` como patrones
- Mucho más eficiente y rápido que el `Matcher`
- Excelente para encontrar listas largas de palabras

Notes: El phrase matcher es otra herramienta útil para encontrar secuencias de palabras en tus datos.

Hace una búsqueda de <abbr title=" en español palabras clave">keyword</abbr> en el documento pero en vez de encontrar únicamente strings, te da acceso directo a los tokens en contexto.

Toma los objetos `Doc` como patrones.

También es muy rápido.

Esto hace que sea muy útil para encontrar diccionarios grandes y listas de palabras en grandes volúmenes de texto.

---

# Encontrando frases eficientemente "phrase matching" (2)

```python
from spacy.matcher import PhraseMatcher

matcher = PhraseMatcher(nlp.vocab)

pattern = nlp("Golden Retriever")
matcher.add('DOG', None, pattern)
doc = nlp("I have a Golden Retriever")

# Itera sobre los resultados
for match_id, start, end in matcher(doc):
    # Obtén el span resultante
    span = doc[start:end]
    print('Matched span:', span.text)
```

```out
Matched span: Golden Retriever
```

Notes: Aquí tenemos un ejemplo.

El phrase matcher puede ser importado desde `spacy.matcher` y sigue a la misma API que el matcher normal.

En vez de pasarle una lista de diccionarios, le pasamos un objeto `Doc` como el patrón que debe encontrar.

Entonces podemos iterar sobre los resultados en el texto, lo que nos da un match ID y el inicio y final del resultado. Esto nos permite crear un objeto `Span` para los tokens resultantes "Golden Retriever" para analizarlos en su contexto.

---

# ¡Practiquemos!

Notes: Probemos algunas de las nuevas técnicas para combinar reglas con modelos estadísticos.
