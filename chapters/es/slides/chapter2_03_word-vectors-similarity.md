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

# Comparando similitud semántica

- `spaCy` puede comparar dos objetos y predecir similitud
- `Doc.similarity()`, `Span.similarity()` y `Token.similarity()`
- Toma otro objeto y devuelve un puntaje de similitud (del `0` al `1`)
- **Importante:** necesita el modelo que tiene los word vectors incluidos, por
  ejemplo:
  - ✅ `en_core_web_md` (modelo mediano)
  - ✅ `en_core_web_lg` (modelo grande)
  - 🚫 **NO** `en_core_web_sm` (modelo pequeño)

Notes: spaCy puede comparar dos objetos y predecir qué tan similares son - por
ejemplo, documentos, spans o tokens.

Los objetos `Doc`, `Token` y `Span` tienen un método `.similarity` que recibe
otro objeto y devuelve un número de punto flotante entre 0 y 1 - que indica qué
tan similares son.

Una cosa que es muy importante: Para poder usar similitud necesitas un modelo
más grande de spaCy que incluya los word vectors.

Por ejemplo, el modelo de inglés mediano o grande - pero _no_ el pequeño. Así
que si quieres usar los vectores usa uno de los modelos que terminan en "md" o
"lg". Puedes ver más detalles sobre esto en la
[documentación de los modelos](https://spacy.io/models).

---

# Ejemplos de similitud (1)

```python
# Carga uno de los modelos más grandes que contiene vectores
nlp = spacy.load('en_core_web_md')

# Compara dos documentos
doc1 = nlp("I like fast food")
doc2 = nlp("I like pizza")
print(doc1.similarity(doc2))
```

```out
0.8627204117787385
```

```python
# Compara dos tokens
doc = nlp("I like pizza and pasta")
token1 = doc[2]
token2 = doc[4]
print(token1.similarity(token2))
```

```out
0.7369546
```

Notes: Aquí tenemos un ejemplo. Digamos que queremos determinar si dos
documentos son similares.

Primero, cargamos el modelo de inglés mediano "en_core_web_md".

Después podemos crear dos objetos doc y usar el método `similarity` del primer
doc para compararlo con el segundo.

Aquí tenemos un puntaje de similitud relativamente alto de 0.86 para "I like
fast food" y "I like pizza".

Lo mismo funciona para los tokens.

De acuerdo con los word vectors, los tokens "pizza" y "pasta" son medianamente
parecidos y reciben un puntaje de 0.7.

---

# Ejemplos de similitud (2)

```python
# Compara un documento con un token
doc = nlp("I like pizza")
token = nlp("soap")[0]

print(doc.similarity(token))
```

```out
0.32531983166759537
```

```python
# Compara un span con un documento
span = nlp("I like pizza and pasta")[2:5]
doc = nlp("McDonalds sells burgers")

print(span.similarity(doc))
```

```out
0.619909235817623
```

Notes: También puedes usar los métodos `similarity` para comparar diferentes
tipos de objetos.

Por ejemplo, un documento y un token.

Aquí el puntaje de similitud es bastante bajo y los dos objetos se consideran
bastante diferentes.

Aquí tenemos otro ejemplo que compara un span - "pizza and pasta" – a un
documento sobre McDonalds.

El puntaje que devolvió aquí es de 0.61, así que determinamos que son
medianamente similares.

---

# ¿Cómo predice spaCy la similitud?

- La similitud se determina usando **word vectors**
- Representaciones multidimensionales de significados de palabras
- Generado usando un algoritmo como
  [Word2Vec](https://en.wikipedia.org/wiki/Word2vec) y mucho texto
- Puede añadirse a los modelos estadísticos de spaCy
- Por defecto: similitud coseno, pero puede ser ajustada
- Los vectores de los `Doc` y `Span` tienen por defecto el valor del promedio
  de los vectores de los tokens
- Las frases cortas son mejores que los documentos largos con muchas palabras
  irrelevantes

Notes: ¿Pero cómo hace esto spaCy detrás de cámaras?

La similitud se determina usando word vectors, que son representaciones
multidimensionales de los significados de las palabras.

Puedes que hayas escuchado sobre Word2Vec, que es un algoritmo que se usa
frecuentemente para entrenar vectores de palabras desde texto puro.

Los vectores se pueden añadir a los modelos estadísticos de spaCy.

Por defecto, la similitud que devuelve spaCy es una similitud coseno entre dos
vectores - pero esto puede ser ajustado si es necesario.

Los vectores para objetos que consisten de varios tokens, como el Doc y el Span
tienen por defecto el valor promedio de los vectores de sus tokens.

Es por esto que normalmente puedes obtener más valor con las frases más cortas
que contienen menos palabras irrelevantes.

---

# Word vectors en spaCy

```python
# Carga uno de los modelos más grandes que contiene vectores
nlp = spacy.load("en_core_web_md")

doc = nlp("I have a banana")
# Accede al vector a través del atributo token.vector
print(doc[3].vector)
```

```out
 [2.02280000e-01,  -7.66180009e-02,   3.70319992e-01,
  3.28450017e-02,  -4.19569999e-01,   7.20689967e-02,
 -3.74760002e-01,   5.74599989e-02,  -1.24009997e-02,
  5.29489994e-01,  -5.23800015e-01,  -1.97710007e-01,
 -3.41470003e-01,   5.33169985e-01,  -2.53309999e-02,
  1.73800007e-01,   1.67720005e-01,   8.39839995e-01,
  5.51070012e-02,   1.05470002e-01,   3.78719985e-01,
  2.42750004e-01,   1.47449998e-02,   5.59509993e-01,
  1.25210002e-01,  -6.75960004e-01,   3.58420014e-01,
 -4.00279984e-02,   9.59490016e-02,  -5.06900012e-01,
 -8.53179991e-02,   1.79800004e-01,   3.38669986e-01,
  ...
```

Notes: Para darte una idea de como se ven estos vectores aquí está un ejemplo.

Primero, cargamos el modelo mediano otra vez. Este contiene word vectors.

Después, podemos procesar un texto y buscar el vector de un token usando el
atributo `.vector`.

El resultado es un vector con 300 dimensiones de la palabra "banana".

---

# La similitud depende del contexto de la aplicación

- Útil para muchas aplicaciones: sistemas de recomendaciones, reportando
  duplicados, etc.
- No hay una definición objetiva de "similitud"
- Depende del contexto y de lo que la aplicación necesita hacer

```python
doc1 = nlp("I like cats")
doc2 = nlp("I hate cats")

print(doc1.similarity(doc2))
```

```out
0.9501447503553421
```

Notes: Predecir similitud puede ser muy útil para muchos tipos de aplicaciones.
Por ejemplo, para recomendarle al usuario textos parecidos basados en los que ya
ha leído. También puede ser útil para reportar contenido duplicado, como posts
en una plataforma en línea.

Sin embargo, es importante tener presente que no hay una definición objetiva de
lo que es similar y no que no. Siempre depende del contexto y de lo que tu
aplicación tiene que hacer.

Aquí tenemos un ejemplo: los word vectors por defecto de spaCy le asignan un
puntaje de similitud muy alto a "I like cats" y "I hate cats". Esto tiene
sentido porque ambas frases expresan un sentimiento sobre los gatos. Pero en
otro contexto de aplicación estas frases pueden ser consideradas muy
_diferentes_, porque hablan sobre el sentimiento opuesto.

---

# ¡Practiquemos!

Notes: Ahora es tu turno. Probemos algunos de los word vectors de spaCy y
usémoslos para predecir similitudes.
