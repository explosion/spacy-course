---
type: slides
---

# Word vectors y similitud semántica

Notes: En esta lección vas a aprender a usar spaCy para predecir qué tan
similares son documentos, spans o tokens entre sí.

También aprenderás cómo usar
<abbr title="Los word vectors son palabras o frases vinculadas a vectores de números reales mediante diferentes métodos. En español también se conocen como vectores de palabras.">word
vectors</abbr> y cómo aprovecharlos en tu aplicación de NLP.

---

# Prediciendo similitud semántica

- `spaCy` puede comparar dos objetos y predecir similitud
- `Doc.similarity()`, `Span.similarity()` y `Token.similarity()`
- Toma otro objeto y devuelve un puntaje de similitud (del `0` al `1`)
- **Importante:** necesita el modelo que tiene los word vectors incluidos, por
  ejemplo:
  - ✅ `en_core_web_md` (modelo mediano en inglés)
  - ✅ `es_core_news_md` (modelo mediano en español)
  - ✅ `es_core_news_lg` (modelo grande en español)
  - 🚫 **NO** `en_core_web_sm` o `es_core_news_sm`(modelos pequeños)

Notes: spaCy puede comparar dos objetos y predecir qué tan similares son - por
ejemplo, documentos, spans o tokens.

Los objetos `Doc`, `Token` y `Span` tienen un método `.similarity` que recibe
otro objeto y devuelve un número de punto flotante entre 0 y 1 indicando qué
tan similares son.

Algo muy importante: Para poder usar similitud necesitas un modelo
más grande de spaCy que incluya los word vectors.

Por ejemplo, el modelo de inglés mediano o grande - pero _no_ el pequeño. Así
que si quieres usar los vectores usa uno de los modelos que terminan en "md" o
"lg". Puedes ver más detalles sobre esto en la
[documentación de los modelos](https://spacy.io/models).

---

# Ejemplos de similitud (1)

```python
# Carga uno de los modelos más grandes que contiene vectores
nlp = spacy.load("es_core_news_md")

# Compara dos documentos
doc1 = nlp("Me gusta la comida rápida")
doc2 = nlp("Me gusta la pizza")
print(doc1.similarity(doc2))
```

```out
0.9513663710080219
```

```python
# Compara dos tokens
doc = nlp("Me gustan la pizza y las hamburguesas")
token1 = doc[3]
token2 = doc[6]
print(token1.similarity(token2))
```

```out
0.6704209
```

Notes: Aquí tenemos un ejemplo. Digamos que queremos determinar si dos
documentos son similares.

Primero, cargamos el modelo de español mediano "es_core_news_md".

Después podemos crear dos objetos doc y usar el método `similarity` del primer
doc para compararlo con el segundo.

Aquí tenemos un puntaje de similitud alto de 0.95 para "Me gusta la comida
rápida" y "Me gusta la pizza".

Lo mismo funciona para los tokens.

De acuerdo con los word vectors, los tokens "pizza" y "hamburguesa" son
medianamente parecidos y reciben un puntaje de 0.67.

---

# Ejemplos de similitud (2)

```python
# Compara un documento con un token
doc = nlp("Me gusta la pizza")
token = nlp("jabón")[0]

print(doc.similarity(token))
```

```out
0.13637736545255463
```

```python
# Compara un span con un documento
span = nlp("Me gustan los perros calientes")[3:5]
doc = nlp("McDonalds vende hamburguesas")

print(span.similarity(doc))
```

```out
0.44930617034116915
```

Notes: También puedes usar los métodos `similarity` para comparar diferentes
tipos de objetos.

Por ejemplo, un documento y un token.

Aquí el puntaje de similitud es bastante bajo y los dos objetos se consideran
bastante diferentes.

Aquí tenemos otro ejemplo que compara un span - "perros calientes" – a un
documento sobre McDonalds.

El puntaje que obtuvimos aquí es de 0.44, así que determinamos que son
medianamente similares según el modelo.

---

# ¿Cómo predice spaCy la similitud?

- La similitud se determina usando **word vectors**
- Representaciones multidimensionales de significados de palabras
- Generado usando un algoritmo como
  [Word2Vec](https://en.wikipedia.org/wiki/Word2vec) y muchos textos
- Puede añadirse a los modelos estadísticos de spaCy
- Por defecto: similitud coseno, pero puede cambiarse por otra medida de
  semejanza
- Los vectores de los `Doc` y `Span` tienen por defecto el valor del promedio
  de los vectores de los tokens
- Las frases cortas son mejores que los documentos largos con muchas palabras
  irrelevantes

Notes: ¿Pero cómo hace esto spaCy detrás de las cámaras?

La similitud se determina usando word vectors, que son representaciones
multidimensionales de los significados de las palabras.

Puede que hayas escuchado sobre Word2Vec, que es un algoritmo que se usa
frecuentemente para entrenar vectores de palabras desde texto puro.

Los vectores se pueden añadir a los modelos estadísticos de spaCy.

Por defecto, la similitud que devuelve spaCy es una similitud coseno entre dos
vectores, pero esto puede cambiarse si es necesario.

Los vectores para objetos que consisten de varios tokens, como el Doc y el Span
tienen por defecto el valor promedio de los vectores de sus tokens.

Es por esto que normalmente puedes obtener más valor con las frases más cortas,
ya que contienen menos palabras irrelevantes.

---

# Word vectors en spaCy

```python
# Carga uno de los modelos más grandes que contiene vectores
nlp = spacy.load("es_core_news_md")

doc = nlp("Tengo una manzana")
# Accede al vector a través del atributo token.vector
print(doc[2].vector)
```

```out
[-0.5813     0.03749    0.6693    2.796    -0.02335   0.39145
  0.5510     0.259      2.625     3.193    -0.4927    0.084971
  0.08304   -1.178     -0.1118    0.05210  -0.56      0.2155
 -1.524     -1.976     -1.669    -0.8539    0.8901   -0.99332
  1.713     -1.749     -1.553     0.4498    0.7688    1.298 
  0.09468   -0.0784     1.184    -1.530    -0.4466    1.3727
  1.223     -1.496      0.7591    0.7092    1.496     0.56073
 -1.601     -0.9133    -2.058     1.120    -0.8625    0.76231
  0.6092    -1.093     -2.022    -1.232     0.2491    0.95122
 -1.097     -0.8304    -1.491    -0.7970   -0.2383    0.10205
 ...
```

Notes: Aquí hay un ejemplo para darte una idea de cómo se ven estos vectores.

Primero, cargamos el modelo mediano otra vez. Este contiene word vectors.

Después, podemos procesar un texto y buscar el vector de un token usando el
atributo `.vector`.

El resultado es un vector con 300 dimensiones de la palabra "manzana".

---

# La similitud depende del contexto de la aplicación

- Útil para muchas aplicaciones: sistemas de recomendaciones, reporte
  de duplicados, etc.
- No hay una definición objetiva de "similitud"
- Depende del contexto y de lo que la aplicación necesita hacer

```python
doc1 = nlp("Me gustan los gatos")
doc2 = nlp("Me desagradan los gatos")

print(doc1.similarity(doc2))
```

```out
0.9709654355279296
```

Notes: Predecir similitud puede ser muy útil para muchos tipos de aplicaciones.
Por ejemplo, para recomendarle al usuario textos parecidos basados en los que
ya ha leído. También puede ser útil para reportar contenido duplicado, como
posts en una plataforma en línea.

Sin embargo, es importante tener presente que no hay una definición objetiva de
lo que es similar y lo que no. Siempre depende del contexto y de lo que tu
aplicación tiene que hacer.

Aquí tenemos un ejemplo: los word vectors por defecto de spaCy le asignan un
puntaje de similitud muy alto a "Me gustan los gatos" y "Me desagradan los
gatos". Esto tiene sentido porque ambas frases expresan un sentimiento sobre
los gatos. Pero en otro contexto de aplicación estas frases pueden ser
consideradas muy _diferentes_, porque hablan sobre el sentimiento opuesto.

---

# ¡Practiquemos!

Notes: Ahora es tu turno. Probemos algunos de los word vectors de spaCy y
usémoslos para predecir similitudes.
