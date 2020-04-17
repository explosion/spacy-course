---
title: 'Capítulo 1: Encontrando palabras, frases, nombres y conceptos'
description:
  'Este capítulo te introducirá en lo básico del procesamiento de texto con spaCy.
  Aprenderás sobre las estructuras de datos, cómo trabajar con modelos estadísticos
  y cómo usarlos para predecir características lingüísticas en tu texto.'

prev: null
next: /chapter2
type: chapter
id: 1
---

<exercise id="1" title="Introducción a spaCy" type="slides">

<slides source="chapter1_01_introduction-to-spacy">
</slides>

</exercise>

<exercise id="2" title="Empezando">

¡Empecemos y probemos spaCy! En este ejercicio vas a poder probar algunos de los 45+ [lenguajes disponibles](https://spacy.io/usage/models#languages).

### Parte 1: Inglés

- Importa la clase `English` de `spacy.lang.en` y crea el objeto `nlp`.
- Crea un `doc` e imprime en pantalla su texto.

<codeblock id="01_02_01">
</codeblock>

### Parte 2: Alemán

- Importa la clase `German` de `spacy.lang.de` y crea el objeto `nlp`.
- Crea un `doc` e imprime en pantalla su texto.

<codeblock id="01_02_02">
</codeblock>

### Parte 3: Español

- Importa la clase `Spanish` de `spacy.lang.es` y crea el objeto `nlp`.
- Crea un `doc` e imprime en pantalla su texto.

<codeblock id="01_02_03">
</codeblock>

</exercise>

<exercise id="3" title="Documentos, spans y tokens">

Cuando llamas `nlp` sobre un string, spaCy primero generas tokens del texto y crea un objeto de documento. En este ejercicio aprenderás más sobre el `Doc`, así como de sus <abbr title="en español representaciones">views</abbr> `Token` y `Span`.

### Paso 1

- Importa la clase de lenguaje `English` y crea el objeto `nlp`.
- Procesa el texto y genera un <abbr title="en español ejemplar, a veces referido incorrectamente como instancia">instance</abbr> de un objeto `Doc` en la variable `doc`.
- Selecciona el primer token de `Doc` e imprime en pantalla su `text`.

<codeblock id="01_03_01">

Puedes indexar a `Doc` de la misma manera en la que indexas en una lista de Python. Por ejemplo, `doc[4]` dará como resultado el token en el índice 4, que es el quinto token en el texto. Recuerda que en Python el primer índice es 0 y no 1.

</codeblock>

### Paso 2

- Importa la clase de lenguaje `English` y crea el objeto `nlp`.
- Procesa el texto y genera un <abbr title="en español ejemplar, a veces referido incorrectamente como instancia">instance</abbr> de un objeto `Doc` en la variable `doc`.
- Crea un slice de `Doc` para los tokens "tree kangaroos" y "tree
  kangaroos and narwhals".

<codeblock id="01_03_02">

Crear un slice de `Doc` funciona exactamente como creando un slice de una lista de Python usando la notación `:`. Recuerda que el último token del índice es _excluyente_ - por ejemplo, `0:4` describe los tokens 0 _hasta_ el token 4, pero no incluye el token 4.

</codeblock>

</exercise>

<exercise id="4" title="Atributos Léxicos">

En este ejemplo usarás los objetos `Doc` y `Token` de spaCy y los atributos léxicos para encontrar porcentajes en el texto. Estarás buscando por dos tokens subsecuentes: un número y un símbolo de porcentaje.

- Usa el atributo `like_num` del token para revisar si un token en el `doc` parece un número.
- Toma el token que sigue al token actual en el documento. El índice del siguiente token en el `doc` es `token.i + 1`.
- Revisa si el atributo `text` del siguiente token es un símbolo de porcentaje "%".

<codeblock id="01_04">

Para obtener el token en un índice específico, puedes indexar el `doc`. Por ejemplo, `doc[5]` es el token en el índice 5.

</codeblock>

</exercise>

<exercise id="5" title="Modelos Estadísticos" type="slides">

<slides source="chapter1_02_statistical-models">
</slides>

</exercise>

<exercise id="6" title="Paquetes de modelos" type="choice">

¿Qué **no** está incluido en un paquete con un modelo que puedes cargar a spaCy?

<choice>
<opt text="Un archivo de metadatos incluyendo el lenguaje, el pipeline y la licencia.">

Todos los modelos incluyen un `meta.json` que define el lenguaje que será inicializado, los nombres de los componentes del pipeline que serán cargados, así como metadatos como el nombre del modelo, versión, licencia, fuentes de los datos, autor y cifras sobre la precisión del modelo (si están disponibles).

</opt>
<opt text="Parámetros, en inglés conocidos como weights, binarios para hacer predicciones estadísticas.">

Los modelos incluyen parámetros binarios para poder predecir las anotaciones lingüísticas como part-of-speech tags, dependency labels o entidades nombradas.

</opt>
<opt correct="true" text="Los datos anotados con los que el modelo fue entrenado.">

Los modelos estadísticos te permiten generalizar basándote en un set de ejemplos de entrenamiento. Una vez están entrenados, usan los parámetros binarios para hacer predicciones. Es por esto que no es necesario incluirlos con los datos de entrenamiento.

</opt>
<opt text="Strings del vocabulario del modelo y sus hashes.">

Los paquetes de modelo incluye un `strings.json` que guarda las entradas en el vocabulario del modelo y el mapping a los hashes. Esto le permite a spaCy comunicarse únicamente en hashes y buscar el string correspondiente si es necesario.

</opt>
</choice>

</exercise>

<exercise id="7" title="Cargando modelos">

Los modelos que estamos usando en este curso ya están pre-instalados. Para obtener más detalles sobre los modelos estadísticos de spaCy y cómo instalarlos en tu máquina revisa [la documentación](https://spacy.io/usage/models).

- Usa `spacy.load` para cargar el modelo pequeño de inglés `'en_core_web_sm'`.
- Procesa el texto e imprime en pantalla el texto del documento.

<codeblock id="01_07">

Para cargar el modelo, llama a `spacy.load` usando su nombre en string. Los nombres de los modelos se diferencian dependiendo del lenguaje y los datos con los que fueron entrenados. Así que asegúrate que estés usando el nombre correcto.

</codeblock>

</exercise>

<exercise id="8" title="Prediciendo anotaciones lingüísticas">

Ahora puedes probar uno de los paquetes de modelos pre-entrenados de spaCy y ver sus predicciones en acción. ¡También puedes intentarlo con tu propio texto! Para averiguar lo que cada tag o label significa puedes llamar a `spacy.explain` en el loop. Por ejemplo, `spacy.explain('PROPN')` o `spacy.explain('GPE')`.

### Parte 1

- Procesa el texto del objeto `nlp` y crea un `doc`.
- Para cada token imprime en pantalla su texto, su `.pos_` (part-of-speech tag) y su `.dep_` (dependency label).

<codeblock id="01_08_01">

Para crear un `doc` llama el objeto `nlp` en un string de texto. Recuerda que necesitas usar los nombres de los atributos de los tokens con un guion bajo (`_`) para obtener el valor del string.

</codeblock>

### Parte 2

- Procesa el texto y crea un objeto `doc`.
- Itera sobre los `doc.ents` e imprime en pantalla el texto de la entidad y el atributo `label_`.

<codeblock id="01_08_02">

Para crear un `doc` llama el objeto `nlp` en un string de texto. Recuerda que necesitas usar los nombres de los atributos de los tokens con un guion bajo (`_`) para obtener el valor del string.

</codeblock>

</exercise>

<exercise id="9" title="Prediciendo entidades nombradas en contexto">

Los modelos son estadísticos y no son _siempre_ correctos. La corrección de sus predicciones depende de los datos de entrenamiento y del texto que estás procesando. Veamos un ejemplo.

- Procesa el texto con el objeto `doc`.
- Itera sobre las entidades e imprime en pantalla el texto de la entidad y el label.
- Parece ser que el modelo no predijo "iPhone X". Crea un span para esos tokens manualmente.

<codeblock id="01_09">

- Para crear un `doc` llama el objeto `nlp` en un string de texto. Las entidades nombradas están disponibles como la propiedad `doc.ents`.
- La forma más fácil de crear un objeto `Span` es usar la notación de slice - por ejemplo `doc[5:10]` para el token en la posición 5 _hasta_ la posición 10. Recuerda que el último índice del token es excluyente.

</codeblock>

</exercise>

<exercise id="10" title="Rule-based matching" type="slides">

<slides source="chapter1_03_rule-based-matching">
</slides>

</exercise>

<exercise id="11" title="Using the Matcher">

Let's try spaCy's rule-based `Matcher`. You'll be using the example from the
previous exercise and write a pattern that can match the phrase "iPhone X" in
the text.

- Import the `Matcher` from `spacy.matcher`.
- Initialize it with the `nlp` object's shared `vocab`.
- Create a pattern that matches the `'TEXT'` values of two tokens: `"iPhone"`
  and `"X"`.
- Use the `matcher.add` method to add the pattern to the matcher.
- Call the matcher on the `doc` and store the result in the variable `matches`.
- Iterate over the matches and get the matched span from the `start` to the
  `end` index.

<codeblock id="01_11">

- The shared vocabulary is available as the `nlp.vocab` attribute.
- A pattern is a list of dictionaries keyed by the attribute names. For example,
  `[{'TEXT': 'Hello'}]` will match one token whose exact text is "Hello".
- The `start` and `end` values of each match describe the start and end index of
  the matched span. To get the span, you can create a slice of the `doc` using
  the given start and end.

</codeblock>

</exercise>

<exercise id="12" title="Writing match patterns">

In this exercise, you'll practice writing more complex match patterns using
different token attributes and operators.

### Part 1

- Write **one** pattern that only matches mentions of the _full_ iOS versions:
  "iOS 7", "iOS 11" and "iOS 10".

<codeblock id="01_12_01">

- To match a token with an exact text, you can use the `TEXT` attribute. For
  example, `{'TEXT': 'Apple'}` will match tokens with the exact text "Apple".
- To match a number token, you can use the `IS_DIGIT` attribute, which will only
  return `True` for tokens consisting of only digits.

</codeblock>

### Part 2

- Write **one** pattern that only matches forms of "download" (tokens with the
  lemma "download"), followed by a token with the part-of-speech tag `'PROPN'`
  (proper noun).

<codeblock id="01_12_02">

- To specify a lemma, you can use the `'LEMMA'` attribute in the token pattern.
  For example, `{'LEMMA': 'be'}` will match tokens like "is", "was" or "being".
- To find proper nouns, you want to match all tokens whose `POS` value equals
  `'PROPN'`.

</codeblock>

### Part 3

- Write **one** pattern that matches adjectives (`'ADJ'`) followed by one or two
  `'NOUN'`s (one noun and one optional noun).

<codeblock id="01_12_03">

- To find adjectives, look for tokens whose `'POS'` value equals `'ADJ'`. For
  nouns, look for `'NOUN'`.
- Operators can be added via the `'OP'` key. For example, `'OP': '?'` to match
  zero or one time.

</codeblock>

</exercise>
