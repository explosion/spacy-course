---
title: 'Capítulo 4: Entrenando un modelo de red neuronal'
description:
  'En este capítulo aprenderás a actualizar los modelos estadísticos de spaCy
  para personalizarlos para tu caso - por ejemplo, para predecir un nuevo tipo
  de entidad en comentarios en internet. Entrenarás propio modelo desde cero y
  entenderás lo esencial de cómo funciona el entrenamiento, junto con consejos
  y trucos para hacer que tus proyectos de NLP sean más exitosos.'
prev: /chapter3
next: null
type: chapter
id: 4
---

<exercise id="1" title="Entrenando y actualizando modelos" type="slides">

<slides source="chapter4_01_training-updating-models">
</slides>

</exercise>

<exercise id="2" title="Entrenar y evaluar">

Para entrenar un modelo, generalmente necesitas datos de entrenamiento y datos
de evaluación. ¿Para qué se utlizan los datos de evaluación?

<choice>

<opt text="Para proveer más ejemplos de entrenamiento en caso de que los datos de entrenamiento no sean suficientes.">

Durante el entrenamiento, el modelo solo se actualizará con los datos de
entrenamiento. Los datos de evaluación se usan para evaluar el modelo al
comparar sus predicciones sobre ejemplos que no han sido vistos contra las
anotaciones correctas. Esto se refleja en un puntaje de presición.

</opt>

<opt text="Para contrastar las predicciones contra ejemplos no vistos y así calcular el puntaje de presición." correct="true">

Los datos de desarrollo se usan para evaluar el modelo y comparar sus
predicciones sobre ejemplos antes no vistos contra las anotaciones correctas.
Esto se refleja en el puntaje de presición.

</opt>

<opt text="Define training examples without annotations.">

The development data is used to evaluate the model by comparing its predictions
on unseen examples to the correct annotations. This is then reflected in the
accuracy score.

</opt>

</choice>

</exercise>

<exercise id="3" title="Creando datos de entrenamiento (1)">

El `Matcher` basado en reglas de spaCy es una manera excelente de crear datos de
entrenamiento rápidamente para modelos de entidades nombradas. Una lista de
frases está disponible en la variable `TEXTS`. Puedes imprimirla en pantalla
para inspeccionarla. Queremos encontrar todas las menciones de los diferentes
modelos de zapatillas adidas, así que creamos datos de entrenamiento para
enseñarle al modelo a reconocerlas como `"ROPA"`.

- Escribe un patrón para dos tokens que en minúsculas encuentran "adidas" y "zx"
- Escribe un patrón para dos tokens: un token que en minúsculas encuentra
  "adidas" y un dígito.

<codeblock id="04_03">

- Para encontrar la forma en minúsculas de un token puedes usar el atributo
  `"LOWER"`. Por ejemplo: `{"LOWER": "apple"}`.
- Para encontrar un token con un dígito puedes usar el flag `"IS_DIGIT"`. Por
  ejemplo: `{"IS_DIGIT": True}`.

</codeblock>

</exercise>

<exercise id="4" title="Creando datos de entrenamiento (2)">

Después de crear los datos para nuestro corpus, necesitamos guardar el 
resultado a un archivo `.spacy`. El código del ejemplo anterior está disponible.

- Crea un objeto `DocBin` con la lista de `docs`.
- Guarda el `DocBin` a un archivo llamado `train.spacy`.

<codeblock id="04_04">

- Puedes inicializar el `DocBin` con una lista de docs al pasarlos como
  keyword arguments `docs`.
- El método `to_disk` de `DocBin` toma un solo argumento: la ruta del archivo
  en el que se van a guardar los datos binarios. Asegúrate de usar la extensión
  de archivo `.spacy`.

</codeblock>

</exercise>

<exercise id="5" title="Configurar y correr el entrenamiento" type="slides">

<slides source="chapter4_02_running-training">
</slides>

</exercise>

<exercise id="6" title="El config de entrenamiento">

The `config.cfg` file is the "single source of truth" for training a pipeline
with spaCy. Which of the following is **not true** about the config?

<choice>

<opt text="Te permite configurar los procesos de entrenamiento y los hiperparámetros.">

El archivo de configuración incluye todos los ajustes para el proceso de
entrenamiento, incluyendo los hiperparámetros.

</opt>

<opt text="Ayuda a hacer tu entrenamiento más replicable.">

Debido a que config incluye _todos_ los ajustes y no hay ajustes por defecto
escondidos, puede ayudar a hacer tus experimentos más replicables y otras
personas podrán volver a correr tus experimentos con exactamente los mismos
ajustes.

</opt>

<opt text="Creates un paquete de Python instalable con tu pipeline." correct="true">

El archivo config incluye todos los ajustes relacionados con el entrenamiento
y con la configuración del pipeline, pero no lo guarda en un paquete. Para
crear un paquete instalable de Python, puedes usar el comando `spacy package`.

</opt>

<opt text="Define los componentes del pipeline y sus ajustes.">

El bloque de `[components]` del archivo config incluye todos los componentes
del pipeline y sus ajustes, incluyendo el las implementaciones del modelo
utilizado.

</opt>

</choice>

<exercise id="7" title="Generando un archivo config">

El comando [`init config`](https://spacy.io/api/cli#init-config) auto-genera
un archivo config para entrenamiento con los ajustes por defecto. Nosotros
queremos entrenar un named entity recognizer, así que vamos a genera un archivo
config para un componente de pipeline de tipo `ner`. Debidlo a que estamos
ejecutando el comando desde un entorno de Jupyter en este curso, vamos a 
utilizar el prefijo `!`. Si ejecutas el comando en tu terminal local, puedes
omitir el prefijo.

### Parte 1

- Usa el comando `init config` de spaCy para auto-generar la configuración.
- Guarda la configuración a un archivo `config.cfg`.
- Usa el argumento `--pipeline` para especificar un componente de pipeline tipo
  `ner`.

<codeblock id="04_07_01"></codeblock>

### Parte 2

¡Echemos un vistazo a la configuración que spaCy acaba de generar! Puedes
correr el comando siguiente para imprimir el archivo config a la terminal e
inspeccionarlo.

<codeblock id="04_07_02"></codeblock>

</exercise>

<exercise id="8" title="Cómo utilizar el CLI de entrenamiento">

¡Utilicemos el nuevo archivo config que generamos en el ejercicio anterior así
como el corpus que creamos para entrenar un named entity recognizer!

El comando [`train`](https://spacy.io/api/cli#train) te permite entrenar un
modelo utilizando un archivo config file. Un archivo `config_gadget.cfg` ya
está listo en el directorio `exercises/en`, así como el archivo
`train_gadget.spacy` que contiene ejemplos de entrenamiento y un archivo
llamado `dev_gadget.spacy` que contiene los datos de evaluación. Debido a que
estamos ejecutando el comando en un entorno de Jupyterm en este curso, usaremos
el prefijo `!`. Si planeas correr el comando en tu terminal local, puedes
omitir este prefijo.

- Invoca el comando `train` con el archivo `exercises/en/config_gadget.cfg`.
- Guarda el pipeline entrenado en el directorio de nombre `output`.
- Pasa también las rutas de archivo `exercises/en/train_gadget.spacy` y
  `exercises/en/dev_gadget.spacy`.

<codeblock id="04_08">

- El primer argumento del comando `spacy train` command es la ruta del archivo
config.

</codeblock>

</exercise>

<exercise id="9" title="Explorando el modelo">

¡Miremos cómo se desempeña el modelo con datos que no ha visto antes! Para
acelerar las cosas ya corrimos un modelo entrenado para el label `"GADGET"`
sobre unos textos. Aquí tenemos algunos de los resultados:

| Texto                                                                                                                     | Entidades              |
| ------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| Apple está ralentizando el iPhone 8 y el iPhone X - cómo pararlo                                                          | `(iPhone 8, iPhone X)` |
| Finalmente entiendo para qué es el 'notch' del iPhone X 'notch'                                                           | `(iPhone X,)`          |
| Todo lo que necesitas saber sobre el Samsung Galaxy S9                                                                    | `(Samsung Galaxy,)`    |
| ¿Quieres comparar modelos de iPad? Aquí comparamos los modelos del 2018                                                   | `(iPad,)`              |
| El iPhone 8 y el iPhone 8 Plus son smartphones diseñados, desarrollados y vendidos por Apple                              | `(iPhone 8, iPhone 8)` |
| cuál es el ipad más barato, especialmente el ipad pro???                                                                  | `(ipad, ipad)`         |
| Samsung Galaxy son una serie de aparatos electrónicos móviles diseñados, desarrollados y vendidos por Samsung Electronics | `(Samsung Galaxy,)`    |

De todas las entidades en los textos, **¿cuántas tuvo correctas el modelo?**
¡Ten en cuenta que los spans de entidades incompletos cuentan como errores
también! Consejo: cuenta el número de entidades que el modelo _debía_ haber
predicho. Luego cuenta el número de entidades que _realmente_ predijo y divídelo
por el número total de entidades correctas.

<choice>

<opt text="45%">

Intenta contar el número de entidades que el modelo predijo correctamente y
divídelo por el número total de entidades correctas que el modelo _debía_ haber
predicho.

</opt>

<opt text="60%">

Intenta contar el número de entidades que el modelo predijo correctamente y
divídelo por el número total de entidades correctas que el modelo _debía_ haber
predicho.

</opt>

<opt text="70%" correct="true">

El modelo tuvo una precisión del 70% con nuestros datos de prueba.

</opt>

<opt text="90%">

Intenta contar el número de entidades que el modelo predijo correctamente y
divídelo por el número total de entidades correctas que el modelo _debía_ haber
predicho.

</opt>

</choice>

</exercise>

<exercise id="10" title="Buenas prácticas de entrenamiento" type="slides">

<slides source="chapter4_03_training-best-practices">
</slides>

</exercise>

<exercise id="11" title="Buenos datos vs. Malos datos">

Aquí tenemos un fragmento de los datos de entrenamiento del tipo de entidad
`DESTINO_TURISTICO` en comentarios de viajeros.

```python
doc1 = nlp("El año pasado fuí a Venecie y los canales estaban hermosos")
doc1.ents = [Span(doc1, 5, 6, label="DESTINO_TURISTICO")]

doc2 = nlp("Deberías visitar Madrid una vez en tu vida, "
           "pero el museo prado es aburrido")
doc2.ents = [Span(doc2, 2, 3, label="DESTINO_TURISTICO"),
             Span(doc2, 11, 13, label="DESTINO_TURISTICO")]

doc3 = nlp("Yo sé que también hay un Madrid en Colombia, jaja")
doc3.ents = []

doc4 = nlp("Una ciudad como Berlín es perfecta para las vacaciones de verano: "
           "muchos, parques, gran vida nocturna, cerveza barata!")
doc4.ents = [Span(doc4, 3, 4, label="DESTINO_TURISTICO")]
```

### Parte 1

¿Por qué son problemáticos estos datos y su esquema de labels?

<choice>

<opt text="Que un sitio sea un destino turístico es una opinión subjetiva y no una categoría definitiva. Será muy difícil que el entity recognizer lo aprenda." correct="true">

Una estrategia mejor sería tener únicamente el label `"LOC"` o `"LOCATION"` y
luego usar un sistema basado en reglas para determinar si una entidad es un
destino turístico en este contexto. Por ejemplo, puedes resolver los tipos de
entidades en relación con un
<abbr title="Un sistema de almacenamiento de conocimiento y sus relaciones. En español: base de conocimiento.">knowledge
base</abbr> o buscarlas en un wiki de viajes.

</opt>

<opt text="Madrid y Colombia también deberían estar marcados como un destinos turísticos. De otra manera, el modelo se confundirá.">

La ciudad de Madrid en Colombia podrí también ser una atracción turística. Esto
solo resalta lo subjetivo que es el esquema de etiquetado y lo difícil que será
decidir si el label aplica o no. Como resultado esta distinción también será
muy difícil de aprender para el entity recognizer.

</opt>

<opt text="Palabras extrañas fuera del vocabulario, como el 'Venecie' mal escrito no deberían estar marcadas como entidades.">

Las palabras muy raras o mal deletreadas también pueden ser marcadas como
entidades. De hecho, ser capaz de predecir categorías en texto mal deletreado en
contexto es una de las grandes ventajas del reconocimiento estadístico de
entidades nombradas.

</opt>

</choice>

### Parte 2

- Reescribe el `TRAINING_DATA` para que solo use el label `"LOC"` en vez de
  `"DESTINO_TURISTICO"`.
- No te olvides de añadir tuples para las entidades `"LOC"` que no fueron
  marcadas con un label en los datos viejos.

<codeblock id="04_11">

- Para los spans que ya estaban marcados con labels, solo tienes que cambiar el
  label de `"DESTINO_TURISTICO"` a `"LOC"`.
- On texto incluye una ciudad y un país que aún no han sido etiquetados. Para
  añadir los spans correspondientes, cuenta los tokens para encontrar en dónde
  comenzan y terminan. ¡Recuerda que el último token es excluyente! Después,
  agrega los nuevos `Span` a `doc.ents`.
- ¡Cuidado con la tokenización! Imprime los tokens en el `Doc` si tienes dudas.

</codeblock>

</exercise>

<exercise id="12" title="Entrenando múltiples etiquetas">

Aquí tenemos una pequeña muestra de un dataset creado para entrenar un nuevo
tipo de entidad `"WEBSITE"`. El dataset original contiene unas cuantas miles de
frases. En este ejercicio estarás marcando con labels a mano. En la vida real,
probablemente quieras automatizar esto y usar una herramienta para marcar con
labels - por ejemplo, [Brat](http://brat.nlplab.org/), una popular solución de
código libre, o [Prodigy](https://prodi.gy), nuestra propia herramienta de
anotación que se integra con spaCy.

### Parte 1

- Completa las posiciones de los caracteres para las entidades `"WEBSITE"` en
  los datos. Tienes la libertad de usar `len(doc1)` si no quieres contar los
  caracteres.

<codeblock id="04_12_01">

- La posición de inicio y del final de un span de entidad son las posiciones de
  los caracteres en el texto. Por ejemplo, si una entidad comienza en la
  posición 5, entonces su posición de inicio es `5`. Recuerda que las posiciones
  del final son _excluyentes_ así que `10` significa _hasta_ el carácter 10.

</codeblock>

### Parte 2

Un modelo fue entrenado con los datos que acabas de marcar con labels, más unos
miles de ejemplos similares. Después de entrenar está haciéndolo muy bien con
`"WEBSITE"`, pero ahora no reconoce a `"PER"`. ¿Por qué podría estar pasando
esto?

<choice>

<opt text='Es muy difícil para el modelo aprender sobre diferentes catgorías como <code>"PER"</code> y <code>"WEBSITE"</code>.'>

Definitivamente es posible que un modelo aprenda sobre varias categorías
diferentes. Por ejemplo, los modelo pre-entrenados de español de spaCy pueden
reconocer personas, pero también organizaciones o lugares.

</opt>

<opt text='Los datos de entrenamiento no incluyeron ejemplos de <code>"PER"</code>, así que el modelo aprendió que este label es incorrecto.' correct="true">

Si las entidades `"PER"` ocurren en los datos de entrenamiento, pero no están
marcadas con etiquetas, el modelo aprenderá que éstas no deben ser predichas.
Del mismo modo, si un tipo de entidad existente no está presente en los datos
de entrenamiento el modelo puede "olvidar" y dejar de predecirlo.

</opt>

<opt text="Los hiperparámetros tienen que ser recalibrados para que ambos tipos de entidades sean reconocidos.">

A pesar de que los hiperparámetros pueden influenciar la precisión de un modelo,
es probable que este no sea el problema aquí.

</opt>

</choice>

### Parte 3

- Actualiza los datos de entrenamiento para incluir anotaciones para las
  entidades `"PER"`, "PewDiePie" y "Alexis Ohanian".

<codeblock id="04_12_02">

- To add more entities, add another `Span` to the `doc.ents`.
- Keep in mind that the end token of a span is exclusive. So an entity that
  starts at token 2 and ends at token 3 will have a start of `2` and an end of
    `3`.

</codeblock>

</exercise>

<exercise id="13" title="Cerrando el curso" type="slides">

<slides source="chapter4_04_wrapping-up" start="47:5175" end="50:21">
</slides>

</exercise>
