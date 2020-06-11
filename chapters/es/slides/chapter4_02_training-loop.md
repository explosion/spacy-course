---
type: slides
---

# El loop de entrenamiento

Notes: Mientras que algunas libraries te dan un solo método para ocuparse del entrenamiento del modelo, spaCy te da control total sobre el loop de entrenamiento.

---

# Los pasos de un loop de entrenamiento

1. **Loop** por un número de veces.
2. **Mezcla** los datos de entrenamiento.
3. **Divide** los datos en lotes.
4. **Actualiza** el modelo para cada lote.
5. **Guarda** el modelo actualizado.

Notes: El loop de entrenamiento es una serie de pasos tomados para entrenar o actualizar un modelo.

Generalmente tenemos que llevarlo a cabo múltiples veces, por iteraciones múltiples, para que el modelo aprenda de manera efectiva. Si queremos entrenar por 10 iteraciones, tenemos que hacer el loop 10 veces.

Para prevenir que el modelo se atasque en una solución subóptima, mezclamos los datos de manera aleatoria para cada iteración. Esto es una estrategia común cuando estamos haciendo <abbr title="En inglés: Stochastic Gradient Descent (SGD).">descenso del gradiente estocástico</abbr>.

Luego, dividimos los datos de entrenamiento en lotes de varios ejemplos, también conocido como <abbr title="En español: minilote.">"minibatching"</abbr>. Esto incrementa la fiabilidad de los estimados del gradiente.

Finalmente, actualizamos el modelo para cada lote y comenzamos el loop de nuevo hasta que hayamos alcanzado la última iteración.

Entonces podemos guardar el modelo en un directorio y usarlo en spaCy.

---

# Resumen: Cómo funciona el entrenamiento

<img src="/training_es.png" alt="Diagram of the training process" />

- **Datos de entrenamiento:** Ejemplos y sus anotaciones.
- **Texto:** El texto al que el modelo debe predecirle un label.
- **Label:** El label que el modelo debe predecir.
- **Gradiente:** Cómo cambiar los parámetros.

Notes: Para resumir:

Los datos de entrenamiento son los ejemplos con los que queremos actualizar el modelo.

El texto debería ser una frase, un párrafo o un documento más largo. Para mejores resultados debería ser similar a lo que el modelo verá cuando se esté ejecutando.

El label es lo que queremos que el modelo prediga. Esto puede ser una categoría de texto, o un span de entidad y su tipo.

El gradiente es cómo deberíamos cambiar el modelo para reducir el error actual. Es calculado cuando comparamos el label predicho con el label verdadero.

---

# Ejemplo de un loop

```python
TRAINING_DATA = [
    ("Cómo pre-ordenar los adidas ZX", {"entities": [(21, 30, "ROPA")]})
    # y muchos más ejemplos...
]
```

```python
# Haz un loop por 10 iteraciones
for i in range(10):
    # Mezcla los datos de entrenamiento
    random.shuffle(TRAINING_DATA)
    # Crea lotes e itera sobre ellos
    for batch in spacy.util.minibatch(TRAINING_DATA):
        # Divide el lote en textos y anotaciones
        texts = [text for text, annotation in batch]
        annotations = [annotation for text, annotation in batch]
        # Actualiza el modelo
        nlp.update(texts, annotations)

# Guarda el modelo
nlp.to_disk(path_to_model)
```

Notes: Aquí tenemos un ejemplo.

Imaginemos que tenemos una lista de ejemplos de entrenamiento compuesta por textos y anotaciones de entidades.

Queremos hacer un loop por 10 iteraciones, así que iteramos sobre un `range` de 10.

Después, usamos el módulo `random` para mezclar de manera aleatoria los datos de entrenamiento.

Luego usamos la función de utilidad `minibatch` para dividir los ejemplos en lotes.

Para cada lote, obtenemos los textos y las anotaciones y llamamos al método `nlp.update` para actualizar el modelo.

Finalmente, llamamos al método `nlp.to_disk` para guardar el modelo entrenado a un directorio.

---

# Actualizando un modelo existente

- Mejorar las predicciones con nuevos datos
- Especialmente útil para mejorar categorías existentes, como `"PER"`
- También es posible añadir nuevas categorías
- Ten cuidado y asegúrate de que el modelo no "olvide" las viejas

Notes: spaCy te permite actualizar los modelos pre-entrenados con más datos - por ejemplo, para mejorar sus predicciones con textos diferentes.

Esto es especialmente útil si quieres mejorar las categorías que el modelo ya conoce, como `"PER"` para persona u `"ORG"` para organización.

También puedes actualizar el modelo para añadir nuevas categorías.

Simplemente asegúrate de que siempre actualices el modelo con ejemplos de la nueva categoría _y_ ejemplos de las categorías que antes estaba prediciendo de manera correcta. De otra manera mejorar una nueva categoría puede lastimar a las demás categorías.

---

# Creando un nuevo pipeline desde cero

```python
# Comienza con un modelo de español en blanco
nlp = spacy.blank("es")
# Crea un entity recognizer en blanco y añádelo al pipeline
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)
# Añade un nuevo label
ner.add_label("ROPA")

# Comienza el entrenamiento
nlp.begin_training()
# Entrena por 10 iteraciones
for itn in range(10):
    random.shuffle(examples)
    # Divide los ejemplos en lotes
    for batch in spacy.util.minibatch(examples, size=2):
        texts = [text for text, annotation in batch]
        annotations = [annotation for text, annotation in batch]
        # Actualiza el modelo
        nlp.update(texts, annotations)
```

Notes: En este ejemplo comenzamos con un modelo de español en blanco usando el método `spacy.blank`. El modelo en blanco no tiene ningún componente del pipeline, solo los datos del lenguaje y las reglas para convertir el texto en tokens.

Luego creamos un entity recognizer en blanco y lo añadimos al pipeline.

Usando el método `add_label` luego podemos añadir nuevos labels en strings al modelo.

Ahora podemos llamar a `nlp.begin_training` para inicializar el modelo con parámetros aleatorios.

Para obtener mejor precisión, queremos hacer un loop sobre los ejemplos más de una vez y mezclar los datos de manera aleatoria en cada iteración.

En cada iteración dividimos los ejemplos en lotes usando la función de utilidad de spaCy `minibatch`. Cada ejemplo está compuesto por un texto y sus anotaciones.

Finalmente, actualizamos el modelo con los textos y anotaciones y continuamos haciendo el loop.

---

# ¡Practiquemos!

Notes: ¡Hora de practicar! Ahora que has visto el loop de entrenamiento usemos los datos creados en el ejercicio anterior para actualizar el modelo.
