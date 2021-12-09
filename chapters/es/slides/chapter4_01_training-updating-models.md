---
type: slides
---

# Entrenando y actualizando modelos

Notes: Bienvenido/a al capítulo final, que trata uno de los aspectos más
emocionantes del NLP moderno: ¡entrenar tus propios modelos!

En esta lección aprenderás sobre entrenar y actualizar los modelos de redes
neuronales de spaCy y los datos que necesitarás para hacerlo - enfocándonos
específicamente en el named entity recognizer.

---

# ¿Por qué actualizar el modelo?

- Mejores resultados en tu área específica
- Aprende esquemas de clasificación específicamente para tu problema
- Esencial para la clasificación de texto
- Muy útil para el reconocimiento de entidades nombradas
- Menos importante para el etiquetado gramatical y el analizador de dependencias

Notes: Antes de comenzar a explicar _cómo_, vale la pena que tomemos un momento
para preguntarnos: ¿Por qué querríamos actualizar el modelo con nuestros
propios ejemplos? ¿Por qué no podemos simplemente depender de los modelos
pre-entrenados?

Los modelos estadísticos hacen predicciones basadas en los ejemplos con los que
fueron entrenados.

Normalmente, puedes hacer que el modelo sea más preciso mostrándole ejemplos de
tu área.

A menudo también quieres predecir categorías específicas a tu problema, así que
el modelo necesita aprender sobre ellas.

Esto es esencial para la clasificación de texto, muy útil para el
reconocimiento de entidades y un poco menos importante para el etiquetado
gramatical y el análisis de dependencias.

---

# Cómo funciona el entrenamiento (1)

1. **Inicializa** los parámetros del modelo de manera aleatoria
2. **Predice** unos cuantos ejemplos con los parámetros actuales
3. **Compara** la predicción con las etiquetas correctas
4. **Calcula** cómo cambiar los parámetros para mejorar las predicciones
5. **Actualiza** ligeramente los parámetros
6. Vuelve al paso 2

Notes: spaCy permite actualizar los modelos existentes con más ejemplos y
entrenar modelos nuevos. Si no estamos comenzando con un pipeline pre-entrenado,
primero inicializamos los parámetros de manera aleatoria.

Después spaCy invoca `nlp.update`, que predice un lote de ejemplos con los
parámetros actuales.

El modelo luego revisa las predicciones comparándolas con las respuestas
correctas y decide cómo cambiar los parámetros para obtener mejores
predicciones la próxima vez.

Finalmente, hacemos una pequeña corrección a los parámetros actuales y seguimos
adelante con el siguiente lote de ejemplos.

Después, spaCy continúa invocando `nlp.update` por cada lote de ejemplos en los
datos y continúa entrenando hasta que el modelo deja de mejorar.

---

# Cómo funciona el entrenamiento (2)

<img src="/training_es.png" alt="Diagrama del proceso de entrenamiento" />

- **Datos de entrenamiento:** Ejemplos y sus anotaciones.
- **Texto:** El texto para el cual el modelo debe predecir una etiqueta.
- **Label:** La etiqueta que el modelo debe predecir.
- **Gradiente:** Cómo cambiar los parámetros.

Notes: Aquí tenemos una ilustración mostrando el proceso.

Los datos de entrenamiento son los ejemplos con los que queremos actualizar el
modelo.

El texto debe ser una oración, un párrafo o un documento más largo. Para
mejores resultados, debería ser similar a lo que el modelo verá cuando se esté
ejecutando.

La etiqueta (label) es lo que queremos que el modelo prediga. Esto puede ser
una categoría de texto, o un span de entidad y su tipo.

El gradiente es cómo deberíamos cambiar el modelo para reducir el error actual.
Es calculado cuando comparamos la etiqueta predicha con la etiqueta verdadera.

Después de entrenar podemos guardar un modelo actualizado y usarlo en nuestra aplicación.

---

# Ejemplo: Entrenando el entity recognizer

- El entity recognizer etiqueta palabras y frases en contexto
- Cada token solo puede ser parte de una entidad
- Los ejemplos deben venir con contexto

```python
doc = nlp("Los nuevos adidas ZX vienen en camino")
doc.ents = [Span(doc, 2, 4, label="ROPA")]
```

- Textos sin entidades también son importantes

```python
doc = nlp("Necesito nuevas zapatillas! ¿Qué me recomiendan?")
doc.ents = []
```

- **Objetivo:** enseñarle al modelo a generalizar

Notes: Miremos el ejemplo de un componente específico: el entity recognizer.

El entity recognizer toma un documento y predice frases y sus etiquetas. Esto
significa que los datos de entrenamiento tienen que incluir textos, las
entidades que contienen y las etiquetas de entidades.

Las entidades no pueden superponerse, así que cada token solo puede ser parte
de una entidad.

Debido a que el entity recognizer predice entidades _en contexto_ también
necesita ser entrenado en las entidades _y_ su contexto.

La forma más fácil de hacer esto es mostrarle al modelo un texto y una lista de
posiciones de caracteres. Por ejemplo, "adidas ZX" es ropa, comienza en el
token 2 y termina en el token 4.

También es muy importante que el modelo aprenda palabras que _no son_ entidades.

En este caso, la lista de anotaciones del span estará vacía.

Nuestro objetivo es enseñarle al modelo a reconocer nuevas entidades en
contextos similares, aunque no estuviesen en nuestros datos de entrenamiento.

---

# Los datos de entrenamiento

- Ejemplos de lo que queremos que nuestro modelo prediga en contexto
- Para actualizar un **modelo existente**: entre unos cientos y miles de
  ejemplos
- Para entrenar una **nueva categoría**: entre unos miles a un millón de
  ejemplos
  - Los modelos de inglés de spaCy: 2 millones de palabras
- Creados normalmente a mano por anotadores humanos
- Puede ser semi-automatizado - ¡por ejemplo, usando el `Matcher` de spaCy!

Notes: Los datos de entrenamiento le dicen al modelo lo que queremos que
prediga. Esto podrían ser textos y entidades nombradas que queremos reconocer,
o tokens y sus etiquetas gramaticales correctas.

Para actualizar el modelo existente podemos comenzar con unos cientos a unos
miles de ejemplos.

Para entrenar una nueva categoría podemos necesitar hasta un millón.

Los pipelines de inglés pre-entrenados de spaCy fueron entrenados con
2 millones de palabras anotadas con etiquetado gramatical, dependencias y
entidades nombradas.

Los datos de entrenamiento son creados normalmente por humanos que le asignan
etiquetas a los textos.

Esto es mucho trabajo, pero puede ser semi-automatizado - por ejemplo, usando
el `Matcher` de spaCy.

---

# Entrenamiento vs. evaluación de datos

- **Entrenamiento de datos:** usado para actualizar el modelo
- **Evaluación de datos:**
  - los datos no han sido vistos durante el entrenamiento
  - se utiliza para calcular qué tan preciso es el modelo
  - los datos deben ser representativos de lo que el modelo verá cuando sea
    ejecutado

Notes: Cuando entrenes tu modelo, es importante saber cómo está progresando y
si es que está aprendiendo las cosas correctas. Esto se sabe al comparar las
predicciones de las respuestas que ya conocemos contra datos que _no_ han sido
vistos durante el entrenamiento. Así que, a demás de los datos para el
entrenamiento, también requieres datos para evaluación, también conocidos como
datos para desarrollo.

Los datos para evaluación se usan para calcular qué tan preciso es tu modelo. 
Por ejemplo, un puntaje de 90% significa que el modelo predijo 90% de los 
datos de evaluación correctamente.

Esto también significa que la evaluación debe ser representativa de los datos
que tu modelo verá durante su ejecución. De otro modo, el puntaje de precisión
será inútil porque no te indicará qué tan bueno _realmente_ es tu modelo.

---

# Generar un corpus de entrenamiento (1)

```python
import spacy

nlp = spacy.blank("es")

# Crea un Doc con spans de entidades
doc1 = nlp("el iPhone X está por salir")
doc1.ents = [Span(doc1, 1, 2, label="GADGET")]
# Crea otro Doc sin spans de entidades
doc2 = nlp("¡Necesito un nuevo teléfono! ¿Alguien tiene recomendaciones?")

docs = [doc1, doc2]  # y así sucesivamente...
```

Notes: spaCy puede ser actualizado con datos del mismo formato de los que crea:
objetos `Doc`. Ya aprendiste todo lo que hay que saber acerca de la creación de
objetos `Doc` y `Span` en el capítulo 2.

En este ejemplo, estamos creando dos objetos `Doc` para nuestro corpus: uno que
contiene una entidad y otro sin ninguna entidad. Para agregar entidades a un
`Doc`, podemos agregar un`Span` a `doc.ents`.

Por supuesto que necesitarás muchos más ejemplos para entrenar efectivamente
tu modelo para que pueda generalizar y predecir entidades similares en contexto.
Dependiendo de la tarea, generalmente quieres al menos unos cuantos cientos o
miles de ejemplos representativos.

---

# Generar un corpus de entrenamiento (2)

- dividir datos en dos porciones:
  - **datos para entrenamiento:** utilizados para actualizar el modelo
  - **datos para desarrollo:** utilizados para evaluar el modelo

```python
random.shuffle(docs)
train_docs = docs[:len(docs) // 2)]
dev_docs = docs[len(docs) // 2):]
```

Notes: Como mencioné anteriormente, no solo necesitamos datos para entrenar el
modelo. También necesitamos evaluar la precisión del modelo utilizando datos
que no hayan sido vistos durante el entrenamiento. Esto se hace generalmente
aleatorizando y dividiendo tus datos en dos partes: una parte para
entrenamiento y otra para evaluación. Aquí utilizamos una división simple de
50/50.

---

# Generar un corpus de entrenamiento (3)

- `DocBin`: contenedor para retener y guardar objetos `Doc` eficientemente
- puede ser guardado a un archivo binario
- los archivos binarios se utilizan para entrenamiento

```python
# Crea y guarda una colección de docs para entrenamiento
train_docbin = DocBin(docs=train_docs)
train_docbin.to_disk("./train.spacy")
# Crea y guarda una colección de docs para evaluación
dev_docbin = DocBin(docs=dev_docs)
dev_docbin.to_disk("./dev.spacy")
```

Notes: Normalmente querrás guardar tus datos de entrenamiento y desarrollo como
archivos en disco para que puedas cargarlos durante el proceso de entrenamiento
de spaCy.

El `DocBin` es un contenedor para guardar y serializar objetos `Doc` 
eficientemente. También puedes instanciarlo con yna lista de objetos `Doc` e
invocar su método `to_disk` para guardarlo en un archivo binario. Normalmente
usamos la extension `.spacy` para este tipo de archivos.

Comparado con otros protocolos de serialización como `pickle`, el `DocBin` es
más rápido y produce archivos de menor tamaño debido a que guarda el 
vocabulario compartido una sola vez. Puedes leer más acerca de su
funcionamiento en la [documentación](https://spacy.io/api/docbin).

---

# Tip: Conversión de tus datos

- `spacy convert` te permite convertir corpora en formatos comunes
- ofrece soporte para `.conll`, `.conllu`, `.iob` y para el formato anterior
  de archivos JSON de spaCy

```bash
$ python -m spacy convert ./train.gold.conll ./corpus
```

Notes: En algunos casos, es posible que ya tengas listos datos de entrenamiento
y desarrollo en un formato común – por ejemplo, CoNLL o IOB. El comando de
spaCy `convert` automáticamente convierte estos archivos en formato binario
de spaCy. También convierte archivos JSON con el formato anterior spaCy (v2).
---

# ¡Practiquemos!

Notes: Ahora es el momento de comenzar y preparar datos de entrenamiento. Miremos algunos ejemplos y creemos un conjunto de datos pequeño para un nuevo tipo de entidad.
