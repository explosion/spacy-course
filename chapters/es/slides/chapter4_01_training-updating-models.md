---
type: slides
---

# Entrenando y actualizando modelos

Notes: Bienvenido/a al capítulo final, que trata uno de los aspectos más emocionantes del NLP moderno: ¡entrenar tus propios modelos!

En esta lección aprenderás sobre entrenar y actualizar los modelos de redes neuronales de spaCy y los datos que necesitarás para hacerlo - enfocándonos específicamente en el named entity recognizer.

---

# ¿Por qué actualizar el modelo?

- Mejores resultados en tu área específica
- Aprende esquemas de clasificación específicamente para tu problema
- Esencial para la clasificación de texto
- Muy útil para el reconocimiento de entidades nombradas
- Menos importante para el part-of-speech tagger y el dependency parser

Notes: Antes de comenzar a explicar _cómo_, vale la pena que tomemos un momento para preguntarnos: ¿Por qué querríamos actualizar el modelo con nuestros propios ejemplos? ¿Por qué no podemos simplemente depender de los modelos pre-entrenados?

Los modelos estadísticos hacen predicciones basados en los ejemplos con los que fueron entrenados.

Normalmente, puedes hacer que el modelo sea más preciso mostrándole ejemplos de tu área.

A menudo también quieres predecir categorías específicas a tu problema, así que el modelo necesita aprender sobre ellas.

Esto es esencial para la clasificación de texto, muy útil para el reconocimiento de entidades y un poco menos importante para el tagging y el parsing.

---

# Cómo funciona el entrenamiento (1)

1. **Inicializa** los parámetros del modelo de manera aleatoria con `nlp.begin_training`
2. **Predice** unos cuantos ejemplos con los parámetros actuales llamando a `nlp.update`
3. **Compara** la predicción con los labels verdaderos
4. **Calcula** cómo cambiar los parámetros para mejorar las predicciones
5. **Actualiza** los parámetros un poco
6. Vuelve al paso 2

Notes: spaCy permite actualizar los modelos existentes con más ejemplos y entrenar modelos nuevos.

Si no estamos comenzando con un modelo pre-entrenado, primero inicializamos los parámetros de manera aleatoria.

Después llamamos a `nlp.update`, que predice un lote de ejemplos con los parámetros actuales.

El modelo luego revisa las predicciones comparándolas con las respuestas correctas y decide cómo cambiar los parámetros para obtener mejores predicciones la próxima vez.

Finalmente, hacemos una pequeña corrección a los parámetros actuales y seguimos adelante con el siguiente lote de ejemplos.

Continuamos llamando a `nlp.update` para cada lote de ejemplos en los datos.

---

# Cómo funciona el entrenamiento (2)

<img src="/training_es.png" alt="Diagram of the training process" />

- **Datos de entrenamiento:** Ejemplos y sus anotaciones.
- **Texto:** El texto al que el modelo debe predecirle un label.
- **Label:** El label que el modelo debe predecir.
- **Gradiente:** Cómo cambiar los parámetros.

Notes: Aquí tenemos una ilustración mostrando el proceso.

Los datos de entrenamiento son los ejemplos con los que queremos actualizar el modelo.

El texto debe ser una frase, párrafo o un documento más largo. Para mejores resultados, debería ser similar a lo que el modelo verá cuando se esté ejecutando.

El label es lo que queremos que el modelo prediga. Esto puede ser una categoría de texto, o un span de entidad y su tipo.

El gradiente es cómo deberíamos cambiar el modelo para reducir el error actual. Es calculado cuando comparamos el label predicho con el label verdadero.

Después de entrenar podemos guardar un modelo actualizado y usarlo en nuestra aplicación.

---

# Ejemplo: Entrenando el entity recognizer

- El entity recognizer le pone tags a palabras y frases en contexto
- Cada token solo puede ser parte de una entidad
- Los ejemplos deben venir con contexto

```python
("Los nuevos adidas ZX vienen en camino", {"entities": [(11, 20, "ROPA")]})
```

- Textos sin entidades también son importantes

```python
("Necesito nuevas zapatillas! ¿Qué me recomiendan?", {"entities": []})
```

- **Objetivo:** enseñarle al modelo a generalizar

Notes: Miremos el ejemplo de un componente específico: el entity recognizer.

El entity recognizer toma un documento y predice frases y sus labels. Esto significa que los datos de entrenamiento tienen que incluir textos, las entidades que contienen y los labels de entidades.

Las entidades no pueden superponerse, así que cada token solo puede ser parte de una entidad.

Debido a que el entity recognizer predice entidades _en contexto_ también necesita ser entrenado en las entidades _y_ su contexto.

La forma más fácil de hacer esto es mostrarle al modelo un texto y una lista de posiciones de caracteres. Por ejemplo, "adidas ZX" es ropa, comienza en el carácter 11 y termina en el carácter 20.

También es muy importante que el modelo aprenda palabras que _no son_ entidades.

En este caso, la lista de anotaciones del span estará vacía.

Nuestro objetivo es enseñarle al modelo a reconocer nuevas entidades en contextos similares, aunque no estuviesen en nuestros datos de entrenamiento.

---

# Los datos de entrenammiento

- Ejemplos de lo que queremos que nuestro modelo prediga en contexto
- Para actualizar un **modelo existente**: entre unos cientos y miles de ejemplos
- Para entrenar una **nueva categoría**: entre unos miles a un millón de ejemplos
  - Los modelos de inglés de spaCy: 2 millones de palabras
- Creados normalmente a mano por anotadores humanos
- Puede ser semi-automatizado - ¡por ejemplo, usando el `Matcher` de spaCy!

Notes: Los datos de entrenamiento le dicen al modelo lo que queremos que prediga. Esto podrían ser textos y entidades nombradas que queremos reconocer, o tokens y sus part-of-speech tags correctos.

Para actualizar el modelo existente podemos comenzar con unos cientos a unos miles de ejemplos.

Para entrenar una nueva categoría podemos necesitar hasta un millón.

Los modelos de inglés pre-entrenados de spaCy fueron entrenados con 2 millones de palabras anotadas con part-of-speech tags, dependencias y entidades nombradas.

Los datos de entrenamiento son creados normalmente por humanos que le asignan labels a los textos.

Esto es mucho trabajo, pero puede ser semi-automatizado - por ejemplo, usando el `Matcher` de spaCy.

---

# ¡Practiquemos!

Notes: Ahora es el momento de comenzar y preparar datos de entrenamiento. Miremos algunos ejemplos y creemos un conjunto de datos pequeño para un nuevo tipo de entidad.
