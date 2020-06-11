---
type: slides
---

# Buenas prácticas para entrenar modelos de spaCy

Notes: Cuando comienzas a correr tus propios experimentos puede que veas que muchas cosas no funcionan de la manera en la que quieres. Eso está bien.

Entrenar modelos es un proceso iterativo y tienes que probar cosas diferentes hasta que encuentres lo que funciona mejor.

En esta lección mostraré algunas de las mejores prácticas y cosas para tener en cuenta a la hora de entrenar tus propios modelos.

Echemos un vistazo a algunos de los problemas con los que te puedes encontrar.

---

# Problema 1: Los modelos pueden "olvidar" cosas

- Un modelo existente puede <abbr title="En inglés: overfit.">sobreajustar</abbr> sobre nuevos datos
  - e.g.: si solo lo actualizas con `"WEBSITE"`, puede "desaprender" lo que es una persona `"PER"`
- También conocido como el problema del "Catastrophic Forgetting"

Notes: Los modelos estadísticos pueden aprender muchas cosas - pero eso no quiere decir que no pueden olvidarlas.

Si estás actualizando un modelo existente con datos nuevos, especialmente labels nuevos, puede sobreajustar y ajustarse _demasiado_ a los nuevos ejemplos.

Por ejemplo, si solo estás actualizándolo con ejemplos de `"WEBSITE"` para un sitio web, puede "olvidar" otros labels que antes había predicho de manera correcta - como `"PER"` para una persona.

Esto también se conoce como el problema del "Catastrophic Forgetting".

---

# Solución 1: Incluye predicciones correctas anteriores

- Por ejemplo, si estás entrenando `"WEBSITE"`, incluye también ejemplos de `"PER"`
- Corre el modelo existente de spaCy sobre los datos y extrae todas las demás entidades relevantes

**MAL:**

```python
TRAINING_DATA = [
    ("Reddit es un website", {"entities": [(0, 6, "WEBSITE")]})
]
```

**BIEN:**

```python
TRAINING_DATA = [
    ("Reddit es un website", {"entities": [(0, 6, "WEBSITE")]}),
    ("Obama es una persona", {"entities": [(0, 5, "PER")]})
]
```

Notes: Para prevenir esto asegúrate de que siempre incluyas ejemplos de lo que el modelo antes predijo correctamente.

Si estás entrenando una nueva categoría `"WEBSITE"`, incluye también ejemplos de `"PER"`

spaCy puede ayudarte con esto. Puedes crear ejemplos adicionales corriendo el modelo existente sobre los datos y extrayendo los spans de entidades que te interesan.

También puedes mezclar esos ejemplos junto con tus datos existentes y actualizar el modelo con anotaciones de todos los labels.

---

# Problema 2: Los modelos no pueden aprender todo

- Los modelos de spaCy hacen predicciones basados en el **contexto local**
- El modelo puede tener dificultades para aprender si es difícil tomar una decisión basada en el contexto
- El esquema de labels debe ser consistente y no demasiado específico
  - Por ejemplo: `"ROPA"` es mejor que `"ROPA_ADULTOS"` y `"ROPA_MUJER"`

Notes: Otro problema común es que tu modelo simplemente no aprende lo que quieres que aprenda.

Los modelos de spaCy hacen predicciones basadas en el contexto local - por ejemplo, para entidades nombradas las palabras alrededor son las más importantes.

Si la decisión es difícil de hacer basada en el contexto, el modelo puede tener dificultades en aprenderla.

El esquema de labels también tiene que ser consistente y no demasiado específico.

Por ejemplo, puede ser difícil enseñarle al modelo a predecir si algo es ropa de adulto o ropa de niños basado en el contexto. Sin embargo, solo predecir el label `"ROPA"` puede funcionar mejor.

---

# Solución 2: Planea tu esquema de labels cuidadosamente

- Escoge categorías que estén reflejadas en el contexto local
- Más genérico es mejor que demasiado específico
- Usa reglas que vayan de label genéricos a categorías específicas

**MAL:**

```python
LABELS = ["ZAPATOS_ADULTOS", "ZAPATOS_MUJER", "BANDAS_FAVORITAS"]
```

**BIEN:**

```python
LABELS = ["ROPA", "BANDA"]
```

Notes: Antes de comenzar a entrenar y actualizar modelos vale la pena tomar un momento para planear tu esquema de labels.

Intenta escoger categorías que estén reflejadas en el contexto local y haz que sean lo más genéricas que sea posible.

Siempre puedes añadir un sistema basado en reglas después para ir de genérico a específico.

Es más fácil ponerle labels y aprender categorías genéricas como `"ROPA"` o `"BANDA"`.

---

# ¡Practiquemos!

Notes: ¡Miremos algunos de los problemas en contexto y solucionémoslos!
