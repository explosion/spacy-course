---
title: 'Capítulo 2: Análisis de datos a gran escala con spaCy'
description:
  'En este capítulo usarás tus nuevas habilidades para extraer información
  específica de grandes volúmenes de texto. Aprenderás a sacarle el mayor
  provecho a las estructuras de datos de spaCy y cómo combinar los enfoques
  estadísticos y basados en reglas de manera efectiva para el análisis de texto.'
prev: /chapter1
next: /chapter3
type: chapter
id: 2
---

<exercise id="1" title="Estructuras de datos (1)" type="slides">

<slides source="chapter2_01_data-structures-1">
</slides>

</exercise>

<exercise id="2" title="De strings a hashes">

### Parte 1

- Busca el string "cat" en `nlp.vocab.strings` para obtener el hash.
- Busca el hash para obtener el string.

<codeblock id="02_02_01">

- Puedes usar el string store en `nlp.vocab.strings` como un diccionario de
  Python normal. Por ejemplo, `nlp.vocab.strings["unicornio"]` devolverá el hash y
  buscar el hash devolverá el string `"unicornio"`.

</codeblock>

### Parte 2

- Busca el label del string "PER" en `nlp.vocab.strings` para obtener el
  hash.
- Busca el hash para obtener el string.

<codeblock id="02_02_02">

- Puedes usar el string store en `nlp.vocab.strings` como un diccionario de
  Python normal. Por ejemplo, `nlp.vocab.strings["unicornio"]` devolverá el hash y
  buscar el hash devolverá el string `"unicornio"`.

</codeblock>

</exercise>

<exercise id="3" title="Vocabulario, hashes y lexemas">

¿Porqué devuelve un error este código?

```python
from spacy.lang.es import Spanish
from spacy.lang.de import German

# Crea un objeto nlp de español y uno de alemán
nlp = Spanish()
nlp_de = German()

# Obtén el ID para el string "Bowie"
bowie_id = nlp.vocab.strings["Bowie"]
print(bowie_id)

# Busca el ID de "Bowie" en el vocabulario
print(nlp_de.vocab.strings[bowie_id])
```

<choice>

<opt correct="true" text='El string <code>"Bowie"</code> no está en el vocabulario alemán, así que el hash no puede ser resuelto en el string store.'>

Los hashes no pueden ser revertidos. Para prevenir este problema añade la
palabra al nuevo vocabulario. Para hacer esto, procesa el texto, busca el
string, o usa el mismo vocabulario para resolver el hash de regreso a string.

</opt>

<opt text='<code>"Bowie"</code> no es una palabra normal en los diccionarios de español o de alemán así que no puede ser convertida a un hash.'>

Cualquier string puede ser convertido a un hash.

</opt>

<opt text="<code>nlp_de</code> no es un nombre válido. El vocabulario solo puede ser compartido si los objetos <code>nlp</code> tienen el mismo nombre.">

El nombre de variable `nlp` es solo una convención. Si el código usara el nombre
de variable `nlp` en vez de `nlp_de` se sobrescribiría el objeto `nlp`
existente, incluyendo el vocabulario.

</opt>

</choice>

</exercise>

<exercise id="4" title="Estructuras de datos (2)" type="slides">

<slides source="chapter2_02_data-structures-2">
</slides>

</exercise>

<exercise id="5" title="Creando un Doc">

¡Creemos algunos objetos `Doc` desde cero!

### Parte 1

- Importa el `Doc` desde `spacy.tokens`.
- Crea un `Doc` a partir de `words` y `spaces`. ¡No te olvides de pasar el
  vocabulario!

<codeblock id="02_05_01">

La clase `Doc` recibe 3 argumentos: el vocabulario compartido (generalmente
`nlp.vocab`), una lista de `words` y una lista de `spaces`, ( valores
booleanos que indican si una palabra está seguida de un espacio o no).

</codeblock>

### Parte 2

- Importa el `Doc` desde `spacy.tokens`.
- Crea un `Doc` a partir de `words` y `spaces`. ¡No te olvides de pasar el
  vocabulario!

<codeblock id="02_05_02">

Mira cada palabra en el texto deseado y revisa si está seguido por un espacio.
Si lo está, el valor del espacio debería ser `True`. Si no, debería ser `False`.

</codeblock>

### Parte 3

- Importa el `Doc` desde `spacy.tokens`.
- Completa los `words` y los `spaces` para que coincidan con el texto deseado y
  crea un `doc`.

<codeblock id="02_05_03">

Presta atención a los tokens individuales. Para ver cómo se tokeniza un string
normalmente en spaCy puedes probarlo e imprimir los tokens de
`nlp("¡¿En serio?!")`.

</codeblock>

</exercise>

<exercise id="6" title="Docs, spans y entidades desde cero">

En este ejercicio crearás los objetos `Doc` y `Span` manualmente y actualizarás
las entidades nombradas - igual que lo hace spaCy detrás de cámaras. Un
objeto `nlp` compartido ya fue creado.

- Importa las clases `Doc` y `Span` desde `spacy.tokens`.
- Usa la clase `Doc` directamente para crear un `doc` a partir de palabras y
  espacios.
- Crea un `Span` para "David Bowie" desde el `doc` y asígnalo al label
  `"PER"`.
- Sobrescribe los `doc.ents` con una lista de una entidad, el `Span` "David
  Bowie".

<codeblock id="02_06">

- El `Doc` es inicializado con tres argumentos: el vocabulario compartido, e.g.
  `nlp.vocab`, una lista de palabras y una lista de valores booleanos que
  indican si una palabra está seguida por un espacio.
- La clase `Span` recibe cuatro argumentos: el `doc` de referencia, el índice de
  inicio del token, el índice del final del token y un label opcional.
- La propiedad `doc.ents` es escribible así que puedes asignarle cualquier
  iterable que consista de objetos `Span`.

</codeblock>

</exercise>

<exercise id="7" title="Buenas prácticas de las estructuras de datos">

El código en este ejemplo está intentando analizar un texto y recoger todos los
nombres propios que están seguidos por un verbo.

```python
import spacy

nlp = spacy.load("es_core_news_sm")
doc = nlp("Por Berlín fluye el río Esprea.")

# Obtén todos los tokens y los part-of-speech tags
token_texts = [token.text for token in doc]
pos_tags = [token.pos_ for token in doc]

for index, pos in enumerate(pos_tags):
    # Revisa si el token actual es un nombre propio
    if pos == "PROPN":
        # Revisa si el token siguiente es un verbo
        if pos_tags[index + 1] == "VERB":
            result = token_texts[index]
            print("Encontré un nombre propio antes de un verbo:", result)
```

### Parte 1

¿Por qué está mal este código?

<choice>

<opt text="El token <code>result</code> debería ser convertido de regreso a un objeto <code>Token</code>. Esto te permite reutilizarlo en spaCy.">

No debería ser necesario convertir strings de regreso a objetos `Token`.
Deberías evitar convertir tokens a strings si todavía necesitas acceder a sus
atributos y relaciones.

</opt>

<opt correct="true" text="Únicamente usa listas de strings en vez de los atributos nativos de los tokens. Esto es normalmente menos eficiente y no puede expresar relaciones complejas.">

Siempre convierte los resultados a strings lo más tarde posible e intenta usar
los atributos nativos de los tokens para mantener la consistencia.

</opt>

<opt text='<code>pos_</code> es el atributo equivocado para extraer nombres propios. Debería usar <code>tag_</code> y los labels <code>"NNP"</code> y <code>"NNS"</code> en su lugar.'>

El atributo `.pos_` devuelve el part-of-speech tag grueso y `PROPN` es el tag
correcto para revisar los nombres propios.

</opt>

</choice>

### Parte 2

- Reescribe el código y usa los atributos nativos de los tokens en vez de listas
  de `token_texts` y `pos_tags`.
- Has un loop sobre cada `token` en el `doc` y revisa el atributo `token.pos_`.
- Usa `doc[token.i + 1]` para revisar el token siguiente y su atributo `.pos_`.
- Si encuentras un nombre propio antes de un verbo imprime en pantalla su
  `token.text`.

<codeblock id="02_07">

- Quita los `token_texts` y `pos_tags` – ¡No necesitamos compilar listas de
  strings por adelantado!
- En vez de iterar sobre los `pos_tags`, has un loop sobre cada `token` en el
  `doc` y revisa el atributo `token.pos_`.
- Para chequear si el próximo token es un verbo, mira el
  `doc[token.i + 1].pos_`.

</codeblock>

</exercise>

<exercise id="8" title="Word vectors y similitud semántica" type="slides">

<slides source="chapter2_03_word-vectors-similarity">
</slides>

</exercise>

<exercise id="9" title="Inspeccionando los word vectors">

En este ejercicio usarás un [modelo de español](https://spacy.io/models/es) más
grande, que incluye al rededor de 20.000 word vectors. El modelo ya está
pre-instalado.

- Carga el modelo mediano `"es_core_news_md"` con word vectors.
- Imprime en pantalla el vector de `"banano"` usando el atributo
  `token.vector`.

<codeblock id="02_09">

- Para cargar el modelo estadístico llama a `spacy.load` con su nombre en
  string.
- Para acceder al token en el doc puedes usar su índice. Por ejemplo, `doc[4]`.

</codeblock>

</exercise>

<exercise id="10" title="Prediciendo similitudes">

En este ejercicio usarás el método `similarity` de spaCy para comparar objetos
`Doc`, `Token` y `Span` y obtener puntajes de similitud.

### Parte 1

- Usa el método `doc.similarity` para comparar el `doc1` con el `doc2` e imprime el
  resultado en pantalla.

<codeblock id="02_10_01">

- El método `doc.similarity` recibe un argumento: el otro objeto con el que debe
  comparar el objeto actual.

</codeblock>

### Parte 2

- Usa el método `token.similarity` para comparar el `token1` al `token2` e
  imprime el resultado en pantalla.

<codeblock id="02_10_02">

- El método `token.similarity` recibe un argumento: el otro objeto con el que
  debe comparar el objeto actual.

</codeblock>

### Parte 3

- Crea spans para "restaurante genial"/ "bar muy divertido".
- Usa `span.similarity` para compararlos e imprime el resultado en pantalla.

<codeblock id="02_10_03"></codeblock>

</exercise>

<exercise id="11" title="Combinando modelos y reglas" type="slides">

<slides source="chapter2_04_models-rules">
</slides>

</exercise>

<exercise id="12" title="Debugging de patrones (1)">

¿Por qué este patrón no encuentra los tokens "Silicon Valley" en el `doc`?

```python
pattern = [{"LOWER": "silicon"}, {"TEXT": " "}, {"LOWER": "valley"}]
```

```python
doc = nlp("¿Por qué Silicon Valley necesita miles de astrofísicos?")
```

<choice>

<opt text='Los tokens "Silicon" y "Valley" no están en minúsculas, así que el atributo <code>"LOWER"</code> no los encontrará.'>

El atributo `LOWER` en el patrón describe a los tokens que pueden ser
encontrados con el valor dado _en minúsculas_. Así, `{"LOWER": "valley"}`
encontrará tokens como "Valley", "VALLEY", "valley", etc.

</opt>

<opt correct="true" text='El tokenizer no crea tokens para los espacios únicos, así que no hay un token con el valor <code>" "</code> en la mitad.'>

El tokenizer se encarga de hacer las separaciones por los espacios en blanco y
cada diccionario en el patrón describe un token.

</opt>

<opt text='A los tokens les está faltando un operador <code>"OP"</code> para indicar que deberían ser encontrados una vez exactamente.'>

Por defecto, todos los tokens descritos por un patrón van a ser encontrados una
vez. Los operadores solo tienen que ser añadidos para cambiar este comportamiento -
por ejemplo, para encontrar cero o más veces.

</opt>

</choice>

</exercise>

<exercise id="13" title="Debugging de patrones (2)">

Los dos patrones en este ejercicio contienen errores y no van a tener los
resultados esperados. ¿Puedes arreglarlos? Si te atascas intenta imprimir en
pantalla los tokens en el `doc` para ver cómo se va a dividir el texto y ajusta
el patrón para que cada diccionario represente un token.

- Edita el `pattern1` para que encuentre correctamente todas las menciones de
  `"Bandai"`, sin importar si son minúsculas o mayúsculas, más un nombre propio
  con la primera letra en mayúscula.
- Edita el `pattern2` para que encuentre correctamente todas las menciones de
  `"Pac-Man"`, sin importar si son minúsculas o mayúsculas, más uno o dos nombres propios siguientes opcionales.

<codeblock id="02_13">

- Procesa los strings que deben ser encontrados con el objeto `nlp` - for
  ejemplo, `[token.text for token in nlp("Pac-Man Live")]`.
- Inspecciona los tokens y asegúrate de que cada diccionario en el patrón describa
  correctamente a un token.

</codeblock>

</exercise>

<exercise id="14" title="Encontrando frases eficientemente, 'phrase matching'">

A veces es más eficiente buscar los strings exactos en vez de escribir los
patrones describiendo los tokens individuales. Esto es especialmente cierto para
cosas que tienen categorías finitas - como todos los países del mundo. Aquí
tenemos una lista de países, así que usémoslos como base para nuestro script
para extraer información. La lista de nombres en strings está disponible en la
variable `COUNTRIES`.

- Importa el `PhraseMatcher` e inicialízalo con el `vocab` compartido como la variable
  `matcher`.
- Añade los patrones de frases y llama al matcher sobre el `doc`.

<codeblock id="02_14">

El `vocab` compartido está disponible como `nlp.vocab`.

</codeblock>

</exercise>

<exercise id="15" title="Extrayendo países y relaciones">

En el ejercicio anterior escribiste un script usando el `PhraseMatcher` de spaCy
para encontrar nombres de países en un texto. Usemos ese buscador de países en
un texto más largo. Analiza la sintaxis y actualiza las entidades del documento
con los países resultantes.

- Itera sobre los resultados y crea un `Span` con el label `"LOC"` (Nombres de ubicaciones definidas política o geográficamente).
- Sobrescribe las entidades en el `doc.ents` y añade el span resultante.
- Obtén el token cabeza de la raíz del span.
- Imprime en pantalla el texto del token cabeza y el span.

<codeblock id="02_15">

- Recuerda que el texto está disponible como la variable `text`.
- El token raíz del span está disponible como `span.root`. El token cabeza está
  disponible a través del atributo `token.head`.

</codeblock>

</exercise>
