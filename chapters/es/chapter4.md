---
title: 'Capítulo 4: Entrenando un modelo de red neuronal'
description:
  "En este capítulo aprenderás a actualizar los modelos estadísticos de spaCy para personalizarlos para tu caso - por ejemplo, para predecir un nuevo tipo de entidad en comentarios en línea. Escribirás tu propio loop de entrenamiento desde cero y entenderás lo esencial de cómo funciona el entrenamiento, junto con consejos y trucos para hacer que tus proyectos de NLP sean más exitosos."
prev: /chapter3
next: null
type: chapter
id: 4
---

<exercise id="1" title="Entrenando y actualizando modelos" type="slides">

<slides source="chapter4_01_training-updating-models">
</slides>

</exercise>

<exercise id="2" title="El propósito de entrenar">

A pesar que spaCy viene con un rango de modelos pre-entrenados para predecir anotaciones lingüísticas casi _siempre_ quieres afinarlos con más ejemplos. Puedes hacer esto entrenándolos con más datos con labels.

¿Con qué **no** ayuda el entrenamiento?

<choice>

<opt text="Mejorar la precisión del modelo con tus datos.">

Si un modelo pre-entrenado no se desempeña bien con tus datos, entrenarlo con más ejemplos en normalmente una buena solución.

</opt>

<opt text="Aprneder nuevos esquemas de clasificación.">

Puedes usar el entrenamiento para enseñarle al modelo nuevos labels, tipos de entidades u otros esquemas de clasificación.

</opt>

<opt text="Descubrir nuevos patrones en datos sin labels." correct="true">

Los componentes de spaCy son modelos supervisados para anotaciones de texto, lo que quiere decir que solo pueden aprender a reproducir ejemplos, no a adivinar nuevos labels desde texto crudo.

</opt>

</choice>

</exercise>

<exercise id="3" title="Creando datos de entrenamiento (1)">

El `Matcher` basado en reglas de spaCy es una manera excelente de crear datos de entrenamiento rápidamente para modelos de entidades nombradas. Una lista de frases está disponible en la variable `TEXTS`. Puedes imprimirla en pantalla para inspeccionarla. Queremos encontrar todas las menciones de los diferentes modelos de iPhone, así que creamos datos de entrenamineto para enseñarle al modelo a reconocerlos como `"GADGET"`.

- Escribe un patrón para dos tokens que en minúsculas encuentran "iphone" y "x"
- Escribe un patrón para dos tokens: Un token que en minúsculas encuentra "iphone" y un dígito usando el operador `"?"`.

<codeblock id="04_03">

- Para encontrar la forma en minúsculas de un token puedes usar el atributo `"LOWER"`.
  Por ejemplo: `{"LOWER": "apple"}`.
- Para encontrar un token con un dígito puedes usar el flag `"IS_DIGIT"`. Por ejemplo: `{"IS_DIGIT": True}`.

</codeblock>

</exercise>

<exercise id="4" title="Creando datos de entrenamiento (2)">

Usemos los patrones que creamos en el ejercicio anterior para crear un set de ejemplos de entrenamiento. Una lista de frases está disponible en la variable `TEXTS`.

- Crea un objeto `doc` para cada texto usando `nlp.pipe`.
- Encuentra en el `doc` y crea una lista de spans resultantes.
- Obtén los tuples `(carácter de inicio, carácter del final, label)` de los spans resultantes.
- Da formato a cada ejemplo como un tuple de texto y un diccionario que hace mapping de `"entities"` a tuples de entidades.
- Añade el ejemplo a `TRAINING_DATA` e inspecciona los datos impresos en pantalla.

<codeblock id="04_04">

- Para encontrar resultados llama al `matcher` sobre un `doc`.
- Los resultados son tuples con `(match_id, start, end)`.
- Para añadir un ejemplo a la lista de ejemplos de entrenamiento puedes usar `TRAINING_DATA.append()`.

</codeblock>

</exercise>

<exercise id="5" title="El loop de entrenamiento" type="slides">

<slides source="chapter4_02_training-loop">
</slides>

</exercise>

<exercise id="6" title="Creando el pipeline">

En este ejercicio preparás un pipeline de spaCy para entrenar al entity recognizer para que reconozca las entidades `"GADGET"` en un texto - por ejemplo, "iPhone X".

- Crea un modelo `"en"` en blanco, por ejemplo, usando el método `spacy.blank`.
- Crea un nuevo entity recognizer usando `nlp.create_pipe` y añádelo al pipeline
- ñade el nuevo label "GADGET" al entity recognizer usando el método `add_label` en el componente del pipeline.

<codeblock id="04_06">

- Para crear un entity recognizer en blanco puedes llamar a `nlp.create_pipe` con `"ner"` en un string
- Para añadir un componente al pipeline usa el método `nlp.add_pipe`.
- El método `add_label` es un método del componente del pipeline, entity recognizer, que guardaste en la variable `ner`. Para añadirle un label puedes llamar a `ner.add_label` con el nombre del label en string, por ejemplo, `ner.add_label("SOME_LABEL")`.

</codeblock>

</exercise>

<exercise id="7" title="Contruyendo un loop de entrenamiento">

¡Escribamos un loop de entrenamiento sencillo desde cero!

El pipeline que creaste en el ejercicio anterior está disponible como el objeto `nlp`. Ya contiene el entity recognizer con el label añadido, `"GADGET"`.

El set pequeño de ejemplos con label que creaste anteriormente está disponible como `TRAINING_DATA`. Para ver los ejemplos puedes imprimirlos en pantalla con tu script.

- Llama a `nlp.begin_training`, crea un loop de entrenamiento por 10 iteraciones y mezcla los datos de entrenamiento.
- Crea lotes de datos de entrenamiento usando `spacy.util.minibatch` e itera sobre los lotes.
- Convierte los tuples de `(text, annotations)` en el lote a listas de `texts` y `annotations`.
- Para cada lote usa `nlp.update` para actualizar el modelo con los textos y anotaciones.

<codeblock id="04_07">

- Para empezar el entrenamiento y reiniciar los parámetros llama al método `nlp.begin_training()`.
- Para dividir los datos de entrenamiento en lotes llama a la función `spacy.util.minibatch` sobre la lista de ejemplos de entrenamiento.

</codeblock>

</exercise>

<exercise id="8" title="Explorando el modelo">

¡Miremos cómo se desempeña el modelo con datos que no ha visto antes! Para acelerar las cosas ya corrimos un modelo entrenado para el label `"GADGET"` sobre unos textos. Aquí tenemos algunos de los resultados:

| Texto                                                                                                             | Entidades              |
| ----------------------------------------------------------------------------------------------------------------- | ---------------------- |
| Apple is slowing down the iPhone 8 and iPhone X - how to stop it                                                  | `(iPhone 8, iPhone X)` |
| I finally understand what the iPhone X 'notch' is for                                                             | `(iPhone X,)`          |
| Everything you need to know about the Samsung Galaxy S9                                                           | `(Samsung Galaxy,)`    |
| Looking to compare iPad models? Here’s how the 2018 lineup stacks up                                              | `(iPad,)`              |
| The iPhone 8 and iPhone 8 Plus are smartphones designed, developed, and marketed by Apple                         | `(iPhone 8, iPhone 8)` |
| what is the cheapest ipad, especially ipad pro???                                                                 | `(ipad, ipad)`         |
| Samsung Galaxy is a series of mobile computing devices designed, manufactured and marketed by Samsung Electronics | `(Samsung Galaxy,)`    |

De todas las entidades en los textos, **cuántas tuvo correctas el modelo**? Ten en cuenta que los spans de entidades incompletos cuentan como errores también! Consejo: Cuenta el número de entidades que el modelo _debía_ haber predicho. Luego cuenta el número de entidades que _realmente_ predijo y divídelo por el número total de entidades correctas.

<choice>

<opt text="45%">

Intenta contar el número de entidades que el modelo predijo correctamente y divídelo por el número total de entidades correctas que el modelo _debía_ haber predicho.

</opt>

<opt text="60%">

Intenta contar el número de entidades que el modelo predijo correctamente y divídelo por el número total de entidades correctas que el modelo _debía_ haber predicho.

</opt>

<opt text="70%" correct="true">

El modelo tuvo una precición del 70% con nuestro datos de prueba.

</opt>

<opt text="90%">

Intenta contar el número de entidades que el modelo predijo correctamente y divídelo por el número total de entidades correctas que el modelo _debía_ haber predicho.

</opt>

</choice>

</exercise>

<exercise id="9" title="Buenas prácticas de entrenamiento" type="slides">

<slides source="chapter4_03_training-best-practices">
</slides>

</exercise>

<exercise id="10" title="Buenos datos vs. Malos datos">

Aquí tenemos un fragmento de los datos de entrenamiento del tipo de entidad `TOURIST_DESTINATION` en comentarios de viajeros.

```python
TRAINING_DATA = [
    (
        "i went to amsterdem last year and the canals were beautiful",
        {"entities": [(10, 19, "TOURIST_DESTINATION")]},
    ),
    (
        "You should visit Paris once in your life, but the Eiffel Tower is kinda boring",
        {"entities": [(17, 22, "TOURIST_DESTINATION")]},
    ),
    ("There's also a Paris in Arkansas, lol", {"entities": []}),
    (
        "Berlin is perfect for summer holiday: lots of parks, great nightlife, cheap beer!",
        {"entities": [(0, 6, "TOURIST_DESTINATION")]},
    ),
]
```

### Parte 1

¿Por qué son problemáticos estos datos y su esquema de labels?

<choice>

<opt text="Que un sitio sea un destino turístico es un jucio subjetico y no una categoría definitiva. Será muy difícil que el entity recognizer lo aprenda." correct="true">

Una estrategia mejor sería tener únicamente el label `"GPE"` (entidad geopolítica) o `"LOCATION"` y luego usar un sistema basado en reglas para determinar si una entidad es un destino turístico en este contexto. Por ejemplo, puedes resolver los tipos de entidades en relación con un <abbr title="Un sistema de almacenamiento de conocimiento y sus relaciones. En español, base de conocimiento">knowledge base</abbr> o buscarlas en un wiki de viajes.

</opt>

<opt text="Paris también debería estar marcado como un destino turístico. De otra manera, el modelo se confundirá.">

Así sea posible que Paris, AK también sea una atracción turística, esto solo resalta lo subjetivo que es el esquema de labels y lo difícil que será decidir si el label aplica o no. Como resultado esta distinción tambíen será muy difícil de aprender para el entity recognizer.

</opt>

<opt text="Palabras extrañas fuera del vocabulario, como el 'amsterdem' mal escrito no deberían estar marcadas como entidades.">

Las palabras muy raras o mal deletreadas también pueden ser marcadas como entidades. De hecho, ser capaz de predecir categorías en texto mal deletreado en contexto es una de las grandes ventajas del reconocimiento estadístico de entidades nombradas.

</opt>

</choice>

### Parte 2

- Rescribe el `TRAINING_DATA` para que solo use el label `"GPE"` (ciudades, estados, países) en vez de `"TOURIST_DESTINATION"`.
- No te olvides de añadir tuples para las entidades `"GPE"` que no fueron marcadas con un label en los datos viejos.

<codeblock id="04_10">

- Para los spans que ya estaban marcados con labels, solo tienes que cambiar el label de `"TOURIST_DESTINATION"` a `"GPE"`.
- Un texto incluye una ciudad y un estado que no están marcados con un label todavía. Para añadir los spans de entidades, cuenta los carácteres para averiguar dónde empiezan y dónde terminan los spans de entidades. Luego añade los tuples `(start, end, label)` a las entidades.

</codeblock>

</exercise>

<exercise id="11" title="Training multiple labels">

Aquí tenemos una pequeña muestra de un dataset creado para entrenar un nuevo tipo de entidad `"WEBSITE"`. El dataset original contiene unas cuantas miles de frases. En este ejercicio estarás marcando con labels a mano. En la vida real, probablemente quieras automatizar esto y usar una herramienta para marcar con labels - por ejemplo, [Brat](http://brat.nlplab.org/), una popular solución de código libre, o [Prodigy](https://prodi.gy), nuestra propia herramienta de anotación que se integra con spaCy.

### Parte 1

- Completa las posiciones de los carácteres para las entidades `"WEBSITE"` en los datos. Tienes la libertad de usar `len()` si no quieres contar los carácteres.

<codeblock id="04_11_01">

- La posición de inicio y del final de un span de entidad son las posiciones de los carácteres en el texto. Por ejemplo, si una entidad comienza en la posición 5, entonces su posición de inicio es `5`. Recuerda que las posiciones del final son _excluyentes_ así que `10` significa _hasta_ el carácter 10.

</codeblock>

### Parte 2

Un modelo fue entrenado con los datos que acabas de marcar con labels, más unos miles de ejemplos similares. Después de entrenar está haciéndolo muy bien con `"WEBSITE"`, pero ahora no reconoce a `"PERSON"`. ¿Por qué podría estar pasando esto?

<choice>

<opt text='Es muy difícil para el modelo aprender sobre diferente catgorías como <code>"PERSON"</code> y <code>"WEBSITE"</code>.'>

Definitivamente es posible que un modelo aprenda sobre varias categorías diferentes. Por ejemplo, los modelo pre-entrenados de inglés de spaCy pueden reconocer personas, pero también organizaciones o porcentajes.

</opt>

<opt text='Los datos de entrenamiento no incluyeron ejemplos de <code>"PERSON"</code>, así que el modelo aprendió que este label es incorrecto.' correct="true">

Si entidades `"PERSON"` ocurren en los datos de entrenamiento, pero no están marcadas con labels, el modelo aprenderá que éstas no deben ser predecidas. Del mismo modo, si un tipo de entidad existente no está presente en los datos de entrenamiento el modelo puede "olvidar" y dejar de predecirlo.

</opt>

<opt text="Los hyperparámetros tienen que ser recalibrados para que ambos tipos de entidades sean reconocidos.">

A pesar que los hyperparámetros pueden influenciar la precisión de un modelo, es probable que este no sea el problema aquí.

</opt>

</choice>

### Parte 3

- Actualiza los datos de entrenamiento para incluir anotaciones para las entidades `"PERSON"`, "PewDiePie" y "Alexis Ohanian".

<codeblock id="04_11_02">

- Para incluir más entidades, añade otro tuple `(start, end, label)` a la lista.

</codeblock>

</exercise>

<exercise id="12" title="Cerrando el curso" type="slides">

<slides source="chapter4_04_wrapping-up">
</slides>

</exercise>
