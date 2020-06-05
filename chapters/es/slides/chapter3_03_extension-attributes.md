---
type: slides
---

# Extensión de atributos

Notes: En esta lección aprenderás cómo añadir atributos personalizados para los objetos `Doc`,
`Token` y `Span` para guardar datos específicos a tus necesidades.

---

# Añadiendo atributos personalizados

- Añade metadatos personalizados a documentos, tokens y spans
- Accesible a través de la propiedad `._`

```python
doc._.title = "Mi documento"
token._.is_color = True
span._.has_color = False
```

- Se registran en los `Doc`, `Token` o `Span` globales usando el método `set_extension`

```python
# Importa las clases globales
from spacy.tokens import Doc, Token, Span

# Añade extensiones para el Doc, Token y Span
Doc.set_extension("title", default=None)
Token.set_extension("is_color", default=False)
Span.set_extension("has_color", default=False)
```

Notes: Los atributos personalizados te permiten añadir metadatos a los docs, tokens y spans. Los datos pueden ser añadidos una vez, o calculados dinámicamente.

Los atributos personalizados están disponibles a través de la propiedad `._` (punto y guión bajo). Esta notación hace que sea claro que fueron agregados por el usuario y no están integrados en spaCy como `token.text`.

Los atributos tienen que ser registrados en las clases `Doc`, `Token` y `Span` globales que puedes importar desde `spacy.tokens`. Ya trabajaste con ellas en los capítulos anteriores. Para registrar un atributo personalizado en los `Doc`, `Token` y `Span`, puedes usar el método `set_extension`.

El primer argumento es el nombre del atributo. Los argumentos keyword te permiten definir cómo debe ser calculado el valor. En este caso, tiene un valor por defecto y puede ser sobrescrito.

---

# Tipos de extensiones

1. Extensión de atributos
2. Extensión de propiedades
3. Extensión de métodos

Notes: Hay tres tipos de extensión: extensión de atributos, extensión de propiedades y extensión de métodos.

---

# Extensión de atributos

- Añadir un valor por defecto que puede ser sobrescrito

```python
from spacy.tokens import Token

# Añade una extensión en el Token con un valor por defecto
Token.set_extension("is_color", default=False)

doc = nlp("El cielo es azul.")

# Sobrescribe el valor de la extensión de atributo
doc[3]._.is_color = True
```

Notes: Las extensiones de atributo añaden un valor por defecto que puede ser sobrescrito.

Por ejemplo, un atributo personalizado del token, llamado `is_color`, que tiene por defecto el valor `False`.

En tokens individuales su valor puede ser cambiado cuando se sobrescribe - en este caso, `True` para el token "azul".

---

# Extensión de propiedades (1)

- Define una función getter y una función setter opcional
- La función getter solo es llamada cuando _se consulta_ el valor del atributo

```python
from spacy.tokens import Token

# Define la función getter
def get_is_color(token):
    colors = ["rojo", "amarillo", "azul"]
    return token.text in colors

# Añade una extensión en el Token con getter
Token.set_extension("is_color", getter=get_is_color)

doc = nlp("El cielo es azul.")
print(doc[3]._.is_color, "-", doc[3].text)
```

```out
True - azul
```

Notes: Las extensiones de propiedades funcionan como las propiedades de Python: pueden definir una función <abbr title="En español: obtenedor. Una función que obtiene y devuelve un valor y que Python ejecuta automáticamente cuando se accede a un atributo especial de un objeto.">getter</abbr> y una función <abbr title="En español: establecedor. Una función que de alguna forma establece un valor y que Python ejecuta automáticamente cuando se asigna un valor a un atributo especial de un objeto.">setter</abbr> opcional.

La función getter solo es llamada cuando consultas el atributo. Esto te permite calcular el valor dinámicamente, e inclusive puede tener en cuenta otros atributos personalizados.

Las funciones getter toman un argumento: el objeto, en este caso el token. En este ejemplo, la función devuelve si el texto de un token se encuentra en nuestra lista de colores.

Podemos proveer la función mediante el argumento keyword `getter` cuando registramos la extensión.

El token "azul" ahora devuelve `True` para `._.is_color`.

---

# Extensión de propiedades (2)

- Las extensiones de `Span` casi siempre deberían usar un getter

```python
from spacy.tokens import Span

# Define la función getter
def get_has_color(span):
    colors = ["rojo", "amarillo", "azul"]
    return any(token.text in colors for token in span)

# Añade una extensión en el Span con getter
Span.set_extension("has_color", getter=get_has_color)

doc = nlp("El cielo es azul.")
print(doc[1:4]._.has_color, "-", doc[1:4].text)
print(doc[0:2]._.has_color, "-", doc[0:2].text)
```

```out
True - cielo es azul
False - El cielo
```

Notes: Si quieres añadir extensiones de atributos en un span, casi siempre debes usar una extensión de propiedades con un getter. De otra manera, tendrías que actualizar a mano _cada uno de los spans posibles_ para añadir todos los valores.

En este ejemplo, la función `get_has_color` toma el span y devuelve si el texto de alguno de los tokens está en la lista de colores.

Después de haber procesado el doc, podemos revisar los diferentes slices del doc y la propiedad personalizada `._.has_color` nos devolverá un resultado sobre si el span contiene un token de color o no.

---

# Extensión de métodos

- Asigna una **función** que pasa a estar disponible como método de un objeto
- Te permite pasar **argumentos** a la función de extensión

```python
from spacy.tokens import Doc

# Define un método con argumentos
def has_token(doc, token_text):
    in_doc = token_text in [token.text for token in doc]
    return in_doc

# Añade una extensión en el Doc con el método
Doc.set_extension("has_token", method=has_token)

doc = nlp("El cielo es azul.")
print(doc._.has_token("azul"), "- azul")
print(doc._.has_token("nube"), "- nube")
```

```out
True - azul
False - nube
```

Notes: La extensión de métodos hace que la extensión del atributo sea un método que puede ser llamado.

Puedes pasarle uno o más argumentos y calcular los valores del atributo de manera dinámica - por ejemplo, basados en cierto argumento o configuración.

En este ejemplo, la función del método revisa si el doc contiene un token con un texto dado. El primer argumento del método es siempre el objeto en sí - en este caso, el doc. Se pasa automáticamente cuando se llama al método.
Todos los demás argumentos de la función serán argumentos en la extensión del método. En este caso, `token_text`.

Aquí el método personalizado, `._.has_token`, devuelve `True` para la palabra "azul" y `False` para la palabra "nube".

---

# ¡Practiquemos!

Notes: Ahora es tu turno. ¡Vamos a añadir extensiones personalizadas!
