---
title: 'Capítulo 1: Encontrando palabras, frases, nombres y conceptos'
description:
  'Este capítulo te introducirá en lo básico del procesamiento de texto con
  spaCy. Aprenderás sobre las estructuras de datos, cómo trabajar con modelos
  estadísticos y cómo usarlos para predecir características lingüísticas en tu
  texto.'

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

¡Empecemos y probemos spaCy! En este ejercicio vas a poder probar algunos de los
55+ [lenguajes disponibles](https://spacy.io/usage/models#languages).

### Parte 1: Español

- Importa la clase `Spanish` de `spacy.lang.es` y crea el objeto `nlp`.
- Crea un `doc` e imprime en pantalla su texto.

<codeblock id="01_02_03"></codeblock>

### Parte 2: Inglés

- Importa la clase `English` de `spacy.lang.en` y crea el objeto `nlp`.
- Crea un `doc` e imprime en pantalla su texto.

<codeblock id="01_02_01"></codeblock>

### Parte 3: Alemán

- Importa la clase `German` de `spacy.lang.de` y crea el objeto `nlp`.
- Crea un `doc` e imprime en pantalla su texto.

<codeblock id="01_02_02"></codeblock>

</exercise>

<exercise id="3" title="Documentos, spans y tokens">

Cuando llamas `nlp` sobre un string, spaCy primero genera tokens del texto y
crea un objeto de documento. En este ejercicio aprenderás más sobre el `Doc`,
así como de sus <abbr title="En español: representaciones o vistas.">views</abbr> `Token` y
`Span`.

### Paso 1

- Importa la clase de lenguaje `Spanish` y crea el objeto `nlp`.
- Procesa el texto y genera un
  <abbr title="En español: ejemplar, a veces referido incorrectamente como instancia.">instance</abbr>
  de un objeto `Doc` en la variable `doc`.
- Selecciona el primer token de `Doc` e imprime en pantalla su `text`.

<codeblock id="01_03_01">

Puedes indexar un `Doc` de la misma manera en la que indexas en una lista de
Python. Por ejemplo, `doc[4]` dará como resultado el token en el índice 4, que
es el quinto token en el texto. Recuerda que en Python el primer índice es 0 y
no 1.

</codeblock>

### Paso 2

- Importa la clase de lenguaje `Spanish` y crea el objeto `nlp`.
- Procesa el texto y genera un
  <abbr title="En español: ejemplar, a veces referido incorrectamente como instancia.">instance</abbr>
  de un objeto `Doc` en la variable `doc`.
- Crea un slice de `Doc` para los tokens "panteras negras" y "panteras negras y los leones".

<codeblock id="01_03_02">

Crear un slice de `Doc` funciona exactamente como creando un slice de una lista
de Python usando la notación `:`. Recuerda que el último token del índice es
_excluyente_ - por ejemplo, `0:4` describe los tokens 0 _hasta_ el token 4, pero
no incluye el token 4.

</codeblock>

</exercise>

<exercise id="4" title="Atributos léxicos">

En este ejemplo usarás los objetos `Doc` y `Token` de spaCy y los atributos
léxicos para encontrar porcentajes en el texto. Estarás buscando dos tokens
subsecuentes: un número y un símbolo de porcentaje.

- Usa el atributo `like_num` del token para revisar si un token en el `doc`
  parece un número.
- Toma el token que sigue al token actual en el documento. El índice del
  siguiente token en el `doc` es `token.i + 1`.
- Revisa si el atributo `text` del siguiente token es un símbolo de porcentaje "%".

<codeblock id="01_04">

Para obtener el token en un índice específico, puedes indexar el `doc`. Por
ejemplo, `doc[5]` es el token en el índice 5.

</codeblock>

</exercise>

<exercise id="5" title="Modelos estadísticos" type="slides">

<slides source="chapter1_02_statistical-models">
</slides>

</exercise>

<exercise id="6" title="Paquetes de modelos" type="choice">

¿Qué **no** está incluido en un paquete con un modelo que puedes cargar a spaCy?

<choice>
<opt text="Un archivo de metadatos incluyendo el lenguaje, el pipeline y la licencia.">

Todos los modelos incluyen un `meta.json` que define el lenguaje que será
inicializado, los nombres de los componentes del pipeline que serán cargados,
así como metadatos como el nombre del modelo, versión, licencia, fuentes de los
datos, autor y cifras sobre la precisión del modelo (si están disponibles).

</opt>
<opt text="Parámetros binarios para hacer predicciones estadísticas.">

Los modelos incluyen parámetros binarios para poder predecir las anotaciones
lingüísticas como part-of-speech tags, dependency labels o entidades nombradas.

</opt>
<opt correct="true" text="Los datos anotados con los que el modelo fue entrenado.">

Los modelos estadísticos te permiten generalizar basándote en un set de ejemplos
de entrenamiento. Una vez están entrenados, usan los parámetros binarios para
hacer predicciones. Es por esto que no es necesario incluir los datos de
entrenamiento.

</opt>
<opt text="Strings del vocabulario del modelo y sus hashes.">

Los paquetes de modelo incluye un `strings.json` que guarda las entradas en el
vocabulario del modelo y el mapping a los hashes. Esto le permite a spaCy
comunicarse únicamente en hashes y buscar el string correspondiente si es
necesario.

</opt>
</choice>

</exercise>

<exercise id="7" title="Cargando modelos">

Los modelos que estamos usando en este curso ya están pre-instalados. Para
obtener más detalles sobre los modelos estadísticos de spaCy y cómo instalarlos
en tu máquina revisa [la documentación](https://spacy.io/usage/models).

- Usa `spacy.load` para cargar el modelo pequeño de español `"es_core_news_sm"`.
- Procesa el texto e imprime en pantalla el texto del documento.

<codeblock id="01_07">

Para cargar el modelo, llama a `spacy.load` usando su nombre en string. Los
nombres de los modelos se diferencian dependiendo del lenguaje y los datos con
los que fueron entrenados. Así que asegúrate de que estés usando el nombre
correcto.

</codeblock>

</exercise>

<exercise id="8" title="Prediciendo anotaciones lingüísticas">

Ahora puedes probar uno de los paquetes de modelos pre-entrenados de spaCy y ver
sus predicciones en acción. ¡También puedes intentarlo con tu propio texto! Para
averiguar lo que cada tag o label significa puedes llamar a `spacy.explain` en
el <abbr title="En español: bucle, un bloque de código que se repite.">loop</abbr>. Por ejemplo, `spacy.explain("PROPN")` o `spacy.explain("GPE")`.

### Parte 1

- Procesa el texto del objeto `nlp` y crea un `doc`.
- Para cada token imprime en pantalla su texto, su `.pos_` (part-of-speech tag)
  y su `.dep_` (dependency label).

<codeblock id="01_08_01">

Para crear un `doc` llama el objeto `nlp` en un string de texto. Recuerda que
necesitas usar los nombres de los atributos de los tokens con un guion bajo
(`_`) para obtener el valor del string.

</codeblock>

### Parte 2

- Procesa el texto y crea un objeto `doc`.
- Itera sobre los `doc.ents` e imprime en pantalla el texto de la entidad y el
  atributo `label_`.

<codeblock id="01_08_02">

Para crear un `doc` llama el objeto `nlp` en un string de texto. Recuerda que
necesitas usar los nombres de los atributos de los tokens con un guion bajo
(`_`) para obtener el valor del string.

</codeblock>

</exercise>

<exercise id="9" title="Prediciendo entidades nombradas en contexto">

Los modelos son estadísticos y no son _siempre_ correctos. La corrección de sus
predicciones depende de los datos de entrenamiento y del texto que estás
procesando. Veamos un ejemplo.

- Procesa el texto con el objeto `doc`.
- Itera sobre las entidades e imprime en pantalla el texto de la entidad y el
  label.
- Parece ser que el modelo no predijo "adidas ZX". Crea un span para esos tokens
  manualmente.

<codeblock id="01_09">

- Para crear un `doc` llama el objeto `nlp` en un string de texto. Las entidades
  nombradas están disponibles como la propiedad `doc.ents`.
- La forma más fácil de crear un objeto `Span` es usar la notación de slice -
  por ejemplo `doc[5:10]` para el token en la posición 5 _hasta_ la posición 10.
  Recuerda que el último índice del token es excluyente.

</codeblock>

</exercise>

<exercise id="10" title="Encontrando patrones basados en reglas" type="slides">

<slides source="chapter1_03_rule-based-matching">
</slides>

</exercise>

<exercise id="11" title="Usando el Matcher">

Probemos el `Matcher` basado en reglas de spaCy. Vas a usar un ejemplo del
ejercicio anterior y escribirás un patrón que encuentre la frase "adidas ZX" en
el texto.

- Importa el `Matcher` desde `spacy.matcher`.
- Inicialízalo con el `vocab` compartido del objeto `nlp`.
- Crea un patrón que encuentre los valores `"TEXT"` de dos tokens: `"adidas"` y
  `"ZX"`.
- Usa el método `matcher.add` para añadir el patrón al matcher.
- Llama al matcher en el `doc` y guarda el resultado en la variable `matches`.
- Itera sobre los resultados y obtén el span resultante desde el índice `start`
  hasta el índice `end`.

<codeblock id="01_11">

- El vocabulario compartido está disponible como el atributo `nlp.vocab`.
- El patrón es una lista de diccionarios que utiliza los nombres de los
  atributos como keys. Por ejemplo, `[{"TEXT": "Hola"}]` encontrará un token
  cuyo texto exacto sea "Hola".
- Los valores `start` y `end` de cada resultado describen el índice de inicio y
  el índice final de un span resultante. Para obtener el span puedes crear un
  slice del `doc` usando su inicio y final.

</codeblock>

</exercise>

<exercise id="12" title="Escribiendo patrones">

En este ejercicio practicarás escribir patrones más complejos usando
diferentes atributos de los tokens y operadores.

### Parte 1

- Escribe **un** patrón que únicamente encuentre menciones de las versiones
  _enteras_ de iOS: "iOS 7", "iOS 11" and "iOS 10".

<codeblock id="01_12_01">

- Para encontrar el token con el texto exacto puedes usar el atributo `TEXT`.
  Por ejemplo, `{"TEXT": "Apple"}` encontrará tokens que tengan el texto exacto
  "Apple".
- Para encontrar un token de número puedes usar el atributo `"IS_DIGIT"` que
  únicamente devolverá `True` para los tokens que solo tienen dígitos.

</codeblock>

### Parte 2

- Escribe **un** patrón que únicamente encuentre formas de "descargar" (tokens
  con el lemma "descargar") seguido por un token que tenga el part-of-speech tag
  `"PROPN"` (<abbr title="En español: nombre propio.">proper noun</abbr>).

<codeblock id="01_12_02">

- Para especificar un lemma puedes usar el atributo `"LEMMA"` en el patrón de
  tokens. Por ejemplo, `{"LEMMA": "ser"}` va a encontrar los tokens como "soy",
  "siendo" o "seré".
- Para encontrar nombres propios puedes encontrar todos los tokens que tengan
  `"PROPN"` como el valor del `"POS"`.

</codeblock>

### Parte 3

- Escribe **un** patrón que encuentre un sustantivo `"NOUN"` seguido de uno o dos adjetivos `"ADJ"`(un adjetivo y un adjetivo opcional).

<codeblock id="01_12_03">

- Para encontrar adjetivos busca los tokens que tengan como valor `"ADJ"` en su
  `"POS"`. Para sustantivos busca `"NOUN"`.
- Los operadores pueden ser añadidos a través del key `"OP"`. Por ejemplo,
  `"OP": "?"` para encontrar cero o una vez.

</codeblock>

</exercise>
