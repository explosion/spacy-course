---
title: 'Capítulo 4: Entrenando un modelo de red neuronal'
description:
  "En este capítulo aprenderás a actualizar los modelos estadísticos de spaCy para personalizarlos para tu caso - por ejemplo, para predecir un nuevo tipo de entidad en comentarios en internet. Escribirás tu propio loop de entrenamiento desde cero y entenderás lo esencial de cómo funciona el entrenamiento, junto con consejos y trucos para hacer que tus proyectos de NLP sean más exitosos."
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

A pesar de que spaCy viene con un rango de modelos pre-entrenados para predecir anotaciones lingüísticas casi _siempre_ querrás afinarlos con más ejemplos. Puedes hacer esto entrenándolos con más datos con labels.

¿Con qué **no** ayuda el entrenamiento?

<choice>

<opt text="Mejorar la precisión del modelo con tus datos.">

Si un modelo pre-entrenado no se desempeña bien con tus datos, entrenarlo con más ejemplos es normalmente una buena solución.

</opt>

<opt text="Aprender nuevos esquemas de clasificación.">

Puedes usar el entrenamiento para enseñarle al modelo nuevos labels, tipos de entidades u otros esquemas de clasificación.

</opt>

<opt text="Descubrir nuevos patrones en datos sin labels." correct="true">

Los componentes de spaCy son modelos supervisados para anotaciones de texto, lo que quiere decir que solo pueden aprender a reproducir ejemplos, no a adivinar nuevos labels desde texto crudo.

</opt>

</choice>

</exercise>

<exercise id="3" title="Creando datos de entrenamiento (1)">

El `Matcher` basado en reglas de spaCy es una manera excelente de crear datos de entrenamiento rápidamente para modelos de entidades nombradas. Una lista de frases está disponible en la variable `TEXTS`. Puedes imprimirla en pantalla para inspeccionarla. Queremos encontrar todas las menciones de los diferentes modelos de zapatillas adidas, así que creamos datos de entrenamiento para enseñarle al modelo a reconocerlas como `"ROPA"`.

- Escribe un patrón para dos tokens que en minúsculas encuentran "adidas" y "zx"
- Escribe un patrón para dos tokens: un token que en minúsculas encuentra "adidas" y un dígito.

<codeblock id="04_03">

- Para encontrar la forma en minúsculas de un token puedes usar el atributo `"LOWER"`.
  Por ejemplo: `{"LOWER": "apple"}`.
- Para encontrar un token con un dígito puedes usar el flag `"IS_DIGIT"`. Por ejemplo: `{"IS_DIGIT": True}`.

</codeblock>

</exercise>

<exercise id="4" title="Creando datos de entrenamiento (2)">

Usemos los patrones que creamos en el ejercicio anterior para crear un set de ejemplos de entrenamiento. Una lista de frases está disponible en la variable `TEXTS`.

- Crea un objeto `doc` para cada texto usando `nlp.pipe`.
- Busca en el `doc` y crea una lista de spans resultantes.
- Obtén los tuples `(carácter de inicio, carácter del final, label)` de los spans resultantes.
- Crea cada ejemplo como un tuple de texto y un diccionario que hace <abbr title="Convertir un dato de un conjunto de datos al equivalente en otro conjunto de datos. Como un diccionario convierte de un key a un value.">mapping</abbr> de `"entities"` a tuples de entidades.
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

En este ejercicio prepararás un pipeline de spaCy para entrenar al entity recognizer para que reconozca las entidades `"ROPA"` en un texto - por ejemplo, "adidas ZX".

- Crea un modelo `"es"` en blanco, por ejemplo, usando el método `spacy.blank`.
- Crea un nuevo entity recognizer usando `nlp.create_pipe` y añádelo al pipeline.
- Añade el nuevo label `"ROPA"` al entity recognizer usando el método `add_label` en el componente del pipeline.

<codeblock id="04_06">

- Para crear un entity recognizer en blanco puedes llamar a `nlp.create_pipe` con `"ner"` en un string.
- Para añadir un componente al pipeline usa el método `nlp.add_pipe`.
- El método `add_label` es un método del componente del pipeline, entity recognizer, que guardaste en la variable `ner`. Para añadirle un label puedes llamar a `ner.add_label` con el nombre del label en un string, por ejemplo, `ner.add_label("CUALQUIER_LABEL")`.

</codeblock>

</exercise>

<exercise id="7" title="Contruyendo un loop de entrenamiento">

¡Escribamos un loop de entrenamiento sencillo desde cero!

El pipeline que creaste en el ejercicio anterior está disponible como el objeto `nlp`. Ya contiene el entity recognizer con el label añadido, `"ROPA"`.

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
| Apple está ralentizando el iPhone 8 y el iPhone X - cómo pararlo                                                  | `(iPhone 8, iPhone X)` |
| Finalmente entiendo para qué es el 'notch' del iPhone X 'notch'                                                             | `(iPhone X,)`          |
| Todo lo que necesitas saber sobre el Samsung Galaxy S9                                                           | `(Samsung Galaxy,)`    |
| ¿Quieres comparar modelos de iPad? Aquí comparamos los modelos del 2018                                             | `(iPad,)`              |
| El iPhone 8 y el iPhone 8 Plus son smartphones diseñados, desarrollados y vendidos por Apple                         | `(iPhone 8, iPhone 8)` |
| cuál es el ipad más barato, especialmente el ipad pro???                                                                 | `(ipad, ipad)`         |
| Samsung Galaxy son una serie de aparatos electrónicos móviles diseñados, desarrollados y vendidos por Samsung Electronics | `(Samsung Galaxy,)`    |

De todas las entidades en los textos, **¿cuántas tuvo correctas el modelo?** ¡Ten en cuenta que los spans de entidades incompletos cuentan como errores también! Consejo: cuenta el número de entidades que el modelo _debía_ haber predicho. Luego cuenta el número de entidades que _realmente_ predijo y divídelo por el número total de entidades correctas.

<choice>

<opt text="45%">

Intenta contar el número de entidades que el modelo predijo correctamente y divídelo por el número total de entidades correctas que el modelo _debía_ haber predicho.

</opt>

<opt text="60%">

Intenta contar el número de entidades que el modelo predijo correctamente y divídelo por el número total de entidades correctas que el modelo _debía_ haber predicho.

</opt>

<opt text="70%" correct="true">

El modelo tuvo una precisión del 70% con nuestros datos de prueba.

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

Aquí tenemos un fragmento de los datos de entrenamiento del tipo de entidad `DESTINO_TURISTICO` en comentarios de viajeros.

```python
TRAINING_DATA = [
    (
        "El año pasado fuí a Venecie y los canales son hermosos",
        {"entities": [(20, 27, "DESTINO_TURISTICO")]},
    ),
    (
        "Tu deberías visitar Madrid una vez en tu vida, pero el "
        "museo prado es aburrido",
        {"entities": [(20, 26, "DESTINO_TURISTICO")]},
    ),
    ("Yo sé que también hay un Madrid en Colombia, jaja", {"entities": []}),
    (
        "Una ciudad como Berlín es perfecta para las vacaciones de verano: "
        "muchos, parques, gran vida nocturna, cerveza barata!",
        {"entities": [(16, 22,  "DESTINO_TURISTICO")]},
    ),
]
```

### Parte 1

¿Por qué son problemáticos estos datos y su esquema de labels?

<choice>

<opt text="Que un sitio sea un destino turístico es una opinión subjetiva y no una categoría definitiva. Será muy difícil que el entity recognizer lo aprenda." correct="true">

Una estrategia mejor sería tener únicamente el label `"LOC"` o `"LOCATION"` y luego usar un sistema basado en reglas para determinar si una entidad es un destino turístico en este contexto. Por ejemplo, puedes resolver los tipos de entidades en relación con un <abbr title="Un sistema de almacenamiento de conocimiento y sus relaciones. En español: base de conocimiento.">knowledge base</abbr> o buscarlas en un wiki de viajes.

</opt>

<opt text="Paris también debería estar marcado como un destino turístico. De otra manera, el modelo se confundirá.">

Así sea posible que Madrid, Colombia también sea una atracción turística, esto solo resalta lo subjetivo que es el esquema de labels y lo difícil que será decidir si el label aplica o no. Como resultado esta distinción también será muy difícil de aprender para el entity recognizer.

</opt>

<opt text="Palabras extrañas fuera del vocabulario, como el 'Venecie' mal escrito no deberían estar marcadas como entidades.">

Las palabras muy raras o mal deletreadas también pueden ser marcadas como entidades. De hecho, ser capaz de predecir categorías en texto mal deletreado en contexto es una de las grandes ventajas del reconocimiento estadístico de entidades nombradas.

</opt>

</choice>

### Parte 2

- Reescribe el `TRAINING_DATA` para que solo use el label `"LOC"` en vez de `"DESTINO_TURISTICO"`.
- No te olvides de añadir tuples para las entidades `"LOC"` que no fueron marcadas con un label en los datos viejos.

<codeblock id="04_10">

- Para los spans que ya estaban marcados con labels, solo tienes que cambiar el label de `"DESTINO_TURISTICO"` a `"LOC"`.
- Un texto incluye una ciudad y un estado que no están marcados con un label todavía. Para añadir los spans de entidades, cuenta los caracteres para averiguar dónde empiezan y dónde terminan los spans de entidades. Luego añade los tuples `(start, end, label)` a las entidades.

</codeblock>

</exercise>

<exercise id="11" title="Entrenando varios labels">

Aquí tenemos una pequeña muestra de un dataset creado para entrenar un nuevo tipo de entidad `"WEBSITE"`. El dataset original contiene unas cuantas miles de frases. En este ejercicio estarás marcando con labels a mano. En la vida real, probablemente quieras automatizar esto y usar una herramienta para marcar con labels - por ejemplo, [Brat](http://brat.nlplab.org/), una popular solución de código libre, o [Prodigy](https://prodi.gy), nuestra propia herramienta de anotación que se integra con spaCy.

### Parte 1

- Completa las posiciones de los caracteres para las entidades `"WEBSITE"` en los datos. Tienes la libertad de usar `len()` si no quieres contar los caracteres.

<codeblock id="04_11_01">

- La posición de inicio y del final de un span de entidad son las posiciones de los caracteres en el texto. Por ejemplo, si una entidad comienza en la posición 5, entonces su posición de inicio es `5`. Recuerda que las posiciones del final son _excluyentes_ así que `10` significa _hasta_ el carácter 10.

</codeblock>

### Parte 2

Un modelo fue entrenado con los datos que acabas de marcar con labels, más unos miles de ejemplos similares. Después de entrenar está haciéndolo muy bien con `"WEBSITE"`, pero ahora no reconoce a `"PER"`. ¿Por qué podría estar pasando esto?

<choice>

<opt text='Es muy difícil para el modelo aprender sobre diferentes catgorías como <code>"PER"</code> y <code>"WEBSITE"</code>.'>

Definitivamente es posible que un modelo aprenda sobre varias categorías diferentes. Por ejemplo, los modelo pre-entrenados de español de spaCy pueden reconocer personas, pero también organizaciones o lugares.

</opt>

<opt text='Los datos de entrenamiento no incluyeron ejemplos de <code>"PER"</code>, así que el modelo aprendió que este label es incorrecto.' correct="true">

Si entidades `"PER"` ocurren en los datos de entrenamiento, pero no están marcadas con labels, el modelo aprenderá que éstas no deben ser predichas. Del mismo modo, si un tipo de entidad existente no está presente en los datos de entrenamiento el modelo puede "olvidar" y dejar de predecirlo.

</opt>

<opt text="Los hiperparámetros tienen que ser recalibrados para que ambos tipos de entidades sean reconocidos.">

A pesar de que los hiperparámetros pueden influenciar la precisión de un modelo, es probable que este no sea el problema aquí.

</opt>

</choice>

### Parte 3

- Actualiza los datos de entrenamiento para incluir anotaciones para las entidades `"PER"`, "PewDiePie" y "Alexis Ohanian".

<codeblock id="04_11_02">

- Para incluir más entidades, añade otro tuple `(start, end, label)` a la lista.

</codeblock>

</exercise>

<exercise id="12" title="Cerrando el curso" type="slides">

<slides source="chapter4_04_wrapping-up">
</slides>

</exercise>
