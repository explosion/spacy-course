---
type: slides
---

# Estructuras de datos (1): Vocab, Lexemas y StringStore

Notes: ¡Hola de nuevo! Ahora que tienes experiencia real usando los objetos de
spaCy es hora de que aprendas más de lo que está sucediendo detrás de cámaras en spaCy.

En esta lección veremos el vocabulario compartido y la manera en la que spaCy
maneja los strings.

---

# Vocabulario compartido y string store (1)

- `Vocab`: guarda los datos compartidos a través de múltiples documentos
- Para usar menos memoria, spaCy codifica todos los strings a **valores hash**
- Los strings solo son guardados una vez en el `StringStore` via
  `nlp.vocab.strings`
- String store: un **lookup table** en ambas direcciones

```python
coffee_hash = nlp.vocab.strings["coffee"]
coffee_string = nlp.vocab.strings[coffee_hash]
```

- Los hashes no pueden ser revertidos - es por esto que debemos proveer el
  vocabulario compartido

```python
# Arroja un error si no hemos visto el string antes
string = nlp.vocab.strings[3197928453018144401]
```

Notes: spaCy guarda todos los datos en un vocabulario, el vocab.

Este incluye palabras, pero también los esquemas de labels para tags y
entidades.

Para usar menos memoria, todos los strings son codificados a hash IDs. Si una
palabra ocurre múltiples veces, no tenemos que guardarla cada vez.

En cambio, spaCy usa una función hash para generar un ID y guarda el string una
vez en el string store. El string store está disponible como `nlp.vocab.strings`

Es una <abbr title="En español: tabla de consulta, como un diccionario.">lookup table</abbr> que
funciona en ambas direcciones. Puedes buscar un string y obtener su hash, así
como puedes buscar un hash para obtener su valor string. Internamente spaCy solo
se comunica en hash IDs.

Los hash IDs no se pueden revertir. Si una palabra no está en el vocabulario no
hay forma de obtener su string. Es por esto que siempre tenemos que pasar el
vocabulario compartido.

---

# Vocabulario compartido y string store (2)

- Busca el string y el hash en `nlp.vocab.strings`

```python
doc = nlp("I love coffee")
print("hash value:", nlp.vocab.strings['coffee'])
print("string value:", nlp.vocab.strings[3197928453018144401])
```

```out
hash value: 3197928453018144401
string value: coffee
```

- El `doc` también expone su vocabulario y sus strings

```python
doc = nlp("I love coffee")
print("hash value:", doc.vocab.strings["coffee"])
```

```out
hash value: 3197928453018144401
```

Notes: Para obtener el hash de un string podemos buscarlo en
`nlp.vocab.strings`.

Para obtener el string que representa a un hash podemos buscar con el hash.

Un objeto `Doc` también expone su vocabulario y strings.

---

# Lexemas: entradas en el vocabulario

- Un objeto `Lexeme` es una entrada en el vocabulario

```python
doc = nlp("I love coffee")
lexeme = nlp.vocab["coffee"]

# Imprime en pantalla los atributos léxicos
print(lexeme.text, lexeme.orth, lexeme.is_alpha)
```

```out
coffee 3197928453018144401 True
```

- Contiene la información sobre una palabra, **independiente del contexto**
  - Texto de la palabra: `lexeme.text` y `lexeme.orth` (el hash)
  - Atributos léxicos como `lexeme.is_alpha`
  - **No** part-of-speech tags, dependencies o entity labels dependedientes del
    contexto.

Notes: Los lexemas son entradas en el vocabulario independientes del contexto.

Puedes obtener un lexema buscando un string o un hash ID en el vocabulario.

Los lexemas exponen atributos, al igual que los tokens.

Ellos contienen información sobre una palabra independiente del contexto, como
el texto o si la palabra está compuesta por caracteres alfanuméricos.

Los lexemas no tienen part-of-speech tags, dependencies o entity labels. Esos
dependen del contexto.

---

# Vocabulario, hashes y lexemas

<img src="/vocab_stringstore.png" width="70%" alt="Illustration of the words 'I', 'love' and 'coffee' across the Doc, Vocab and StringStore" />

Notes: Aquí tenemos un ejemplo.

El `Doc` contiene palabras en contexto - en este caso, los tokens "I", "love" y
"coffee" con sus part-of-speech tags y dependencies.

Cada token se refiere a un lexema, que conoce el hash ID de la palabra. Para
obtener la representación en string de la palabra, spaCy busca el hash en el
string store.

---

# ¡Practiquemos!

Notes: Todo esto suena un poco abstracto - así que exploremos el vocabulario y
el string store en la práctica.
