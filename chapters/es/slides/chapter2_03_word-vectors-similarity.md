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
  - ✅ `en_core_web_md` (modelo mediano)
  - ✅ `es_core_news_md` (modelo mediano español)
  - ✅ `en_core_web_lg` (modelo grande)
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
0.9771402664001864
```

```python
# Compara dos tokens
doc = nlp("Me gusta la pizza y la pasta")
token1 = doc[3]
token2 = doc[6]
print(token1.similarity(token2))
```

```out
0.7795312
```

Notes: Aquí tenemos un ejemplo. Digamos que queremos determinar si dos
documentos son similares.

Primero, cargamos el modelo de español mediano "es_core_news_md".

Después podemos crear dos objetos doc y usar el método `similarity` del primer
doc para compararlo con el segundo.

Aquí tenemos un puntaje de similitud alto de 0.97 para "Me gusta la comida rápida" y "Me gusta la pizza".

Lo mismo funciona para los tokens.

De acuerdo con los word vectors, los tokens "pizza" y "pasta" son medianamente
parecidos y reciben un puntaje de 0.78.

---

# Ejemplos de similitud (2)

```python
# Compara un documento con un token
doc = nlp("Me gusta la pizza")
token = nlp("jabón")[0]

print(doc.similarity(token))
```

```out
0.4755507088511145
```

```python
# Compara un span con un documento
span = nlp("Me gusta la pizza y la pasta")[2:7]
doc = nlp("McDonalds vende hamburguesas")

print(span.similarity(doc))
```

```out
0.6243837841459509
```

Notes: También puedes usar los métodos `similarity` para comparar diferentes
tipos de objetos.

Por ejemplo, un documento y un token.

Aquí el puntaje de similitud es bastante bajo y los dos objetos se consideran
bastante diferentes.

Aquí tenemos otro ejemplo que compara un span - "la pizza y la pasta" – a un
documento sobre McDonalds.

El puntaje que obtuvimos aquí es de 0.62, así que determinamos que son
medianamente similares.

---

# ¿Cómo predice spaCy la similitud?

- La similitud se determina usando **word vectors**
- Representaciones multidimensionales de significados de palabras
- Generado usando un algoritmo como
  [Word2Vec](https://en.wikipedia.org/wiki/Word2vec) y mucho texto
- Puede añadirse a los modelos estadísticos de spaCy
- Por defecto: similitud coseno, pero puede cambiarse por otra medida de semejanza
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
vectores, pero esto puede cambiarse si es necesario.

Los vectores para objetos que consisten de varios tokens, como el Doc y el Span
tienen por defecto el valor promedio de los vectores de sus tokens.

Es por esto que normalmente puedes obtener más valor con las frases más cortas, ya que contienen menos palabras irrelevantes.

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
[-0.162944,   0.042666,   0.405069,
 -0.884944,   0.13951 ,   1.37826 ,
 -0.807906,  -0.432592,  -0.747897,  
  0.953742,   0.90389 ,  -0.514217,
  0.360039,  -0.409261,   1.11574 ,
 -0.407411,   0.118361,  -0.426352,
 -0.315689,   0.027726,   0.79418 ,
 -0.99135 ,   0.147428,   0.36956 ,
  0.547555,  -0.023946,  -2.024585,
 -0.122916,   0.406145,   0.911639,
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
doc2 = nlp("Odio a los gatos")

print(doc1.similarity(doc2))
```

```out
0.9073441516522552
```

Notes: Predecir similitud puede ser muy útil para muchos tipos de aplicaciones.
Por ejemplo, para recomendarle al usuario textos parecidos basados en los que ya
ha leído. También puede ser útil para reportar contenido duplicado, como posts
en una plataforma en línea.

Sin embargo, es importante tener presente que no hay una definición objetiva de
lo que es similar y lo que no. Siempre depende del contexto y de lo que tu
aplicación tiene que hacer.

Aquí tenemos un ejemplo: los word vectors por defecto de spaCy le asignan un
puntaje de similitud muy alto a "Me gustan los gatos" y "Odio a los gatos". Esto tiene
sentido porque ambas frases expresan un sentimiento sobre los gatos. Pero en
otro contexto de aplicación estas frases pueden ser consideradas muy
_diferentes_, porque hablan sobre el sentimiento opuesto.

---

# ¡Practiquemos!

Notes: Ahora es tu turno. Probemos algunos de los word vectors de spaCy y
usémoslos para predecir similitudes.
