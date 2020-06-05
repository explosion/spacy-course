---
type: slides
---

# Aumentando la escala y el desempeño

Notes: En esta lección te mostraré algunos trucos y consejos para hacer que tu pipeline de spaCy corra lo más rápido posible y procese grandes volúmenes de texto de manera eficiente.

---

# Procesando grandes volúmenes de texto

- Usa el método `nlp.pipe`
- Procesa los textos como un stream, devuelve objetos`Doc` usando yield
- Mucho más rápido que llamar al objeto `nlp` en cada texto

**MAL:**

```python
docs = [nlp(text) for text in LOTS_OF_TEXTS]
```

**BIEN:**

```python
docs = list(nlp.pipe(LOTS_OF_TEXTS))
```

Notes: Si necesitas procesar una gran cantidad de textos y crear muchos objetos `Doc` seguidos, el método `nlp.pipe` puede acelerar este proceso de manera significativa.

Procesa los textos como un <abbr title="En español: un flujo, en este caso de datos. Se refiere a que no genera una lista desde el principio, sino cada elemento individualmente.">stream</abbr> y usa `yield` para devolver objetos `Doc`.

Es mucho más rápido que solo llamar al objeto `nlp` sobre cada texto, porque procesa en <abbr title="En español: grupos.">batches</abbr> los textos.

`nlp.pipe` es un generador que usa `yield` para devolver objetos `Doc`, así que para obtener una lista de `Doc`, recuerda llamar la función `list` sobre él.

---

# Pasando en contexto (1)

- Poniendo `as_tuples=True` en `nlp.pipe` te permite pasar tuples de `(text, context)`
- Usa `yield` para devolver tuples `(doc, context)`
- Útil para asociar metadatos con el `doc`

```python
data = [
    ("Esto es un texto", {"id": 1, "numero_pagina": 15}),
    ("y otro texto", {"id": 2, "numero_pagina": 16}),
]

for doc, context in nlp.pipe(data, as_tuples=True):
    print(doc.text, context["numero_pagina"])
```

```out
Esto es un texto 15
y otro texto 16
```

Notes: `nlp.pipe` también provee soporte para pasar tuples de text / contexto si defines `as_tuples` como `True`.

El método entonces usará `yield` para devolver tuples de doc / context.

Esto es útil para pasar metadatos adicionales, como un ID asociado con el texto o con el número de página.

---

# Pasando en contexto (2)

```python
from spacy.tokens import Doc

Doc.set_extension("id", default=None)
Doc.set_extension("numero_pagina", default=None)

data = [
    ("Esto es un texto", {"id": 1, "numero_pagina": 15}),
    ("y otro texto", {"id": 2, "numero_pagina": 16}),
]

for doc, context in nlp.pipe(data, as_tuples=True):
    doc._.id = context["id"]
    doc._.numero_pagina = context["numero_pagina]
```

Notes: Inclusive puedes pasarle metadatos a los atributos personalizados.

En este ejemplo, estamos registrando dos extensiones, `id` y `numero_pagina`, que tienen por defecto `None`.

Después de procesar el texto y pasarlo a través del contexto podemos sobrescribir las extensiones del doc con nuestros metadatos del contexto.

---

# Usando solo el tokenizer (1)

<img src="/pipeline.png" width="90%" alt="Illustration of the spaCy pipeline">

- ¡No corras el pipeline entero!

Notes: Otro escenario común: a veces ya tienes el modelo cargado para hacer otro procesamiento, pero solo necesitas el tokenizer para un texto en particular.

Correr todo el pipeline es innecesariamente lento, porque estarás obteniendo un montón de predicciones del modelo que no necesitas.

---

# Usando solo el tokenizer (2)

- Usa `nlp.make_doc` para convertir un texto en un objeto `Doc`

**MAL:**

```python
doc = nlp("¡Hola Mundo!")
```

**BIEN:**

```python
doc = nlp.make_doc("¡Hola Mundo!")
```

Notes: Si solo necesitas un objeto `Doc` que fue convertido en tokens puedes usar el método `nlp.make_doc` en vez de `nlp`. `nlp.make_doc` toma un texto y devuelve un doc.

Así es como lo hace spaCy detrás de cámaras: `nlp.make_doc` convierte el texto en un doc antes de llamar a los componentes del pipeline.

---

# Desactivando los componentes del pipeline

- Usa `nlp.disable_pipes` para deshabilitar temporalmente uno o más componentes del pipeline

```python
# Desactiva el tagger y el parser
with nlp.disable_pipes("tagger", "parser"):
    # Procesa el texto e imprime las entidades en pantalla
    doc = nlp(text)
    print(doc.ents)
```

- Los restaura después del bloque `with`
- Solo corre los componentes restantes

Notes: spaCy también te permite deshabilitar temporalmente componentes del pipeline usando el <abbr title='Que puede ser usado dentro de un bloque de código "with".'>context manager</abbr> `nlp.disable_pipes`.

Toma un número de argumentos variable, los nombres en string de los componentes a ser deshabilitados. Por ejemplo, si solo quieres usar el entity recognizer para procesar un documento, puedes deshabilitar temporalmente el tagger y el parser.

Después del bloque `with`, los componentes del pipeline deshabilitados se restauran automáticamente.

Dentro del bloque `with`, spaCy solo correrá los componentes restantes.

---

# ¡Practiquemos!

Notes: Ahora es tu turno. Vas a probar nuevos métodos y optimizar código para que sea más rápido y más eficiente.
