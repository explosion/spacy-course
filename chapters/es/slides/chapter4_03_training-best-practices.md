---
type: slides
---

# Buenas prácticas para entrenar modelos de spaCy

Notes: Cuando comienzas a correr tus propios experimentos puede que veas que muchas cosas no funcionan de la manera en la que quieres. Eso está bien.

Entrenar modelos es un proceso iterativo y tienes que probar cosas diferentes hasta que encuentres lo que funciona mejor.

En esta lección mostraré algunas de las mejores prácticas y cosas que tener en cuenta a la hora de entrenar tus propios modelos.

Echemos un vistazo a algunos de los problemas con los que te puedes encontrar.

---

# Problema 1: Los modelos pueden "olvidar" cosas

- Un modelo existente puede sobreajustar sobre nuevos datos
  - e.g.: si solo lo actualizas con `"WEBSITE"`, puede "desaprender" lo que es una `"PERSON"`
- También conocido como el problema del "olvido catastrófico"

Notes: Los modelos estadísticos pueden aprender muchas cosas - pero eso no quiere decir que no pueden olvidarlas.

Si estás actualizando un modelo existente con datos nuevos, especialmente labels nuevos, puede sobreajustar y ajustarse _demasiado_ a los nuevos ejemplos.

Por ejemplo, si solo estás actualizándolo con ejemplos de "website", puede "olvidar" otros labels que antes había predicho de manera correcta - como "person".

Esto también se conoce como el problema del olvido catastrófico.

---

# Solución 1: Incluye predicciones correctas anteriores

- Por ejemplo, si estás entrenando `"WEBSITE"`, también incluyes ejemplos de `"PERSON"`
- Corre el modelo existente de spaCy sobre los datos y extrae todas las demás entidades relevantes

**MAL:**

```python
TRAINING_DATA = [
    ("Reddit is a website", {"entities": [(0, 6, "WEBSITE")]})
]
```

**BIEN:**

```python
TRAINING_DATA = [
    ("Reddit is a website", {"entities": [(0, 6, "WEBSITE")]}),
    ("Obama is a person", {"entities": [(0, 5, "PERSON")]})
]
```

Note: Para prevenir esto asegurate que siempre incluyas ejemplos de lo que el modelo antes predijo correctamente.

Si estás entrenando una nueva categoría `"WEBSITE"`, también incluyes ejemplos de `"PERSON"`

spaCy puede ayudarte con esto. Puedes crear ejemplos adicionales corriendo el modelo existente sobre los datos y extrayendo los spans de entidades que te interesan.

También puedes mezclar esos ejemplos junto con tus datos existentes y actualizar el modelo con anotaciones de todos los labels.

---

# Problema 2: Los modelos no pueden aprender todo

- Los modelos de spaCy hacen predicciones basados en el **contexto local**
- El modelo puede tener dificultades para aprender si es difícil tomar una decisión basada en el contexto
- El esquema de labels debe ser consistente y no demasiado específico
  - Por ejemplo: `"CLOTHING"` (ropa) es mejor que `"ADULT_CLOTHING"` (ropa de adultos) y `"CHILDRENS_CLOTHING"` (ropa de niños)

Notes: Otro problema común es que tu modelo simplemente no aprende lo que quieres que aprenda.

Los modelos de spaCy hacen predicciones basadas en el contexto local - por ejemplo, para entidades nombradas las palabras al rededor son las más importantes.

Si la decisión es difícil de hacer basada en el contexto, el modelo puede tener dificultades en aprenderla.

El esquema de labels también tiene que ser consistente y no demasiado específico.

Por ejemplo, puede ser difícil enseñarle al modelo a predecir si algo es ropa de adulto o ropa de niños basado en el contexto. Sin embargo, solo predecir el label "ropa" puede funcionar mejor.

---

# Solución 2: Planea tu esquema de label cuidadosamente

- Escoge categorías que estén reflejadas en el contexto local
- Más genérico es mejor que demasiado específico
- Usa reglas que vayan de label genéricos a categorías específicas

**MAL:**

```python
LABELS = ["ADULT_SHOES", "CHILDRENS_SHOES", "BANDS_I_LIKE"]
```

**BIEN:**

```python
LABELS = ["CLOTHING", "BAND"]
```

Notes: Antes de comenzar a entrenas y actualizar modelos vale la pena tomar un momento para planear tu esquema de labels.

Intenta escoger categorías que estén reflejadas en el contexto local y haz que sean lo más genéricas si es posible.

Siempre puedes añadir un sistema basado en reglas que después para ir de genérico a específico.

Es más fácil ponerle labels y aprender categorías genéricas como "ropa" o "banda".

---

# ¡Practiquemos!

Notes: ¡Miremos algunos de los problemas en contexto y solucionémoslos!
