---
type: slides
---

# Cerrando el curso

Notes: ¡Felicitaciones - terminaste el curso!

---

# Tus nuevas habilidades con spaCy

- Extraer **características lingüísticas**: part-of-speech tags, dependencias, entidades nombradas
- Trabajar con **modelos estadísticos** pre-entrenados
- Encontrar palabras y frases usando **reglas** con el `Matcher` y el `PhraseMatcher`
- Buenas prácticas para trabajar con las **estructuras de datos** `Doc`, `Token` `Span`, `Vocab`, `Lexeme`
- Encontrar **similitudes semánticas** usando **word vectors**
- Escribir **componentes personalizados del pipeline** con la **extensión de atributos**
- **Aumentar la escala** de tus pipelines de spaCy y hacer que sean rápidos
- Crear **datos de entrenamiento** para los modelos estadísticos de spaCy
- **Entrenar y actualizar** los modelos de redes neuronales de spaCy con nuevos datos

Notes: Aquí tenemos un resumen de todas las nuevas habilidades que aprendiste hasta ahora:

En el primer capítulo aprendiste cómo extraer características lingüísticas como part-of-speech tags, dependencias sintácticas y entidades nombradas. También a cómo trabajar con modelos estadísticos pre-entrenados.

También aprendiste a escribir reglas poderosas para extraer palabras y frases usando el `Matcher` y el `PhraseMatcher` de spaCy.

El capítulo 2 fue sobre extraer información y también aprendiste cómo trabajar con las estructuras de datos, el `Doc`, `Token` y `Span`, así como el `Vocab` y las entradas léxicas.

También usaste spaCy para predecir similitudes semánticas usando word vectors.

En el capítulo 3 tuviste mayores detalles sobre el pipeline de spaCy y aprendiste a escribir tus propios componentes personalizados del pipeline para modificar el doc.

También creaste tus propias extensiones de atributos para docs, tokens y spans. También aprendiste sobre los streams de procesamiento y a hacer que tu pipeline sea más rápido.

Finalmente, en el capítulo 4 aprendiste sobre entrenar y actualizar los modelos estadísticos de spaCy, específicamente el entity recognizer.

Aprendiste unos trucos útiles sobre cómo crear datos de entrenamiento y cómo diseñar tu esquema de labels para obtener los mejores resultados.

---

# Más cosas para hacer con spaCy (1)

- [Entrenar y actualizar](https://spacy.io/usage/training) otros componentes del pipeline
  - Part-of-speech tagger
  - Dependency parser
  - Text classifier

Notes: Por supuesto que todavía hay muchas más cosas que puedes hacer con spaCy que no alcanzamos a cubrir en este curso.

Así nos hayamos enfocado principalmente en entrenar el entity recognizer, también puedes entrenar y actualizar los demás componentes estadísticos del pipeline, como el part-of-speech tagger y el dependency parser.

Otro componente del pipeline útil es el text classifier, que puede aprender a predecir labels que aplican a todo el texto. Esto no es parte de los modelos pre-entrenados, pero lo puedes añadir al modelo existente y entrenarlo con tus propios datos.

---

# Más cosas para hacer con spaCy (2)

- [Personalizar el tokenizer](https://spacy.io/usage/linguistic-features#tokenization)
  - Añadir reglas y excepciones para dividir el texto de otra manera
- [Añadir y mejorar el soporte para otros lenguajes](https://spacy.io/usage/adding-languages)
  - 55+ lenguajes actualmente
  - Mucho espacio para mejoras y más lenguajes
  - Permite entrenar modelos para otros lenguajes

Notes: En este curso básicamente aceptamos la conversión a tokens por defecto tal y cómo está. ¡Pero no tienes que hacerlo!

spaCy te permite personalizar las reglas para determinar dónde y cómo dividir el texto.

También puedes añadir y mejorar el soporte para otros lenguajes.

Así spaCy ya permita convertir a tokens para muchos lenguajes diferente, todavía hay mucho espacio para mejorar.

Permitir la conversión a tokens en un nuevo lenguaje es el primer paso hacia poder entrenar un modelo estadístico.

---

# ¡Mira el sitio web para más información y documentación!

<img src="/website.png" alt="Laptop showing the spacy.io website" width="50%" />

👉 [spacy.io](https://spacy.io)

Notes: Para más ejemplos, tutoriales y documentación de la API a profundidad, revisa el sitio web de spaCy.

---

# ¡Gracias y nos vemos pronto! 👋

Notes: ¡Muchas gracias por tomar este curso! Espero que te hayas divertido y espero escuchar todas las cosas sensacionales que construirás con spaCy.
