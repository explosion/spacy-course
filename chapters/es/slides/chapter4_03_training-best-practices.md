---
type: slides
---

# Buenas prácticas para entrenar modelos de spaCy

Notes: Cuando comienzas a correr tus propios experimentos puede que veas que
muchas cosas no funcionan de la manera en la que quieres. Eso está bien.

Entrenar modelos es un proceso iterativo y tienes que probar cosas diferentes
hasta que encuentres lo que funciona mejor.

En esta lección mostraré algunas de las mejores prácticas y cosas para tener en
 cuenta a la hora de entrenar tus propios modelos.

Echemos un vistazo a algunos de los problemas con los que te puedes encontrar.

---

# Problema 1: Los modelos pueden "olvidar" cosas

- Un modelo existente puede <abbr title="En inglés: overfit.">sobreajustar</abbr>
  sobre nuevos datos
  - e.g.: si solo lo actualizas con `"WEBSITE"`, puede "desaprender" lo que es
    una persona (`"PER"`)
- También conocido como el problema del "catastrophic forgetting"

Notes: Los modelos estadísticos pueden aprender muchas cosas - pero eso no
quiere decir que no pueden olvidarlas.

Si estás actualizando un modelo existente con datos nuevos, especialmente
etiquetas nuevas, puede sobreajustar y ajustarse _demasiado_ a los nuevos
ejemplos.

Por ejemplo, si solo estás actualizándolo con ejemplos de `"WEBSITE"` para un
sitio web, puede "olvidar" otras etiquetas que antes había predicho de manera
correcta - como `"PER"` para una persona.

Esto también se conoce como el problema del "catastrophic forgetting".

---

# Solución 1: Incluye predicciones correctas anteriores

- Por ejemplo, si estás entrenando `"WEBSITE"`, incluye también ejemplos de
  `"PER"`
- Corre el modelo existente de spaCy sobre los datos y extrae todas las demás
  entidades relevantes

Note: Para prevenir esto, asegúrate de siempre incluir ejemplos de cosas que el
modelo clasificó antes correctamente.

Si estás entrenando una categoría nueva `"WEBSITE"`, también incluye ejemplos
de persona `"PER"`.

spaCy te puede ayudar con esto. Puedes crear esos ejemplos adicionales
corriendo el modelo existente sobre tus datos y extrayendo los spans de
entidades que te interesen.

Puedes después mezclar esos ejemplos con tus datos existentes y actualizar el
modelo con las anotaciones de todas las etiquetas.

---

# Problema 2: Los modelos no pueden aprender todo

- Los modelos de spaCy hacen predicciones basadas en el **contexto local**
- El modelo puede tener dificultades para aprender si es difícil tomar una
  decisión basada en el contexto
- El esquema de etiquetado debe ser consistente y no demasiado específico
  - Por ejemplo: `"ROPA"` es mejor que `"ROPA_ADULTOS"` y `"ROPA_MUJER"`

Notes: Otro problema común es que tu modelo simplemente no aprende lo que
quieres que aprenda.

Los modelos de spaCy hacen predicciones basadas en el contexto local - por
ejemplo, para entidades nombradas las palabras alrededor son las más
importantes.

Si la decisión es difícil de hacer basada en el contexto, el modelo puede tener
dificultades en aprenderla.

El esquema de etiquetas también tiene que ser consistente y no demasiado
específico.

Por ejemplo, puede ser difícil enseñarle al modelo a predecir si algo es ropa
de adultos o ropa de niños basado en el contexto. Sin embargo, solo predecir la
etiqueta `"ROPA"` puede funcionar mejor.

---

# Solución 2: Planea tu esquema de etiquetado cuidadosamente

- Escoge categorías que estén reflejadas en el contexto local
- Más genérico es mejor que demasiado específico
- Usa reglas que vayan de etiquetas genéricas a categorías específicas

**MAL:**

```python
LABELS = ["ZAPATOS_ADULTOS", "ZAPATOS_MUJER", "BANDAS_FAVORITAS"]
```

**BIEN:**

```python
LABELS = ["ROPA", "BANDA"]
```

Notes: Antes de comenzar a entrenar y actualizar modelos vale la pena tomar un
momento para planear tu esquema de etiquetado.

Intenta escoger categorías que estén reflejadas en el contexto local y haz que
sean lo más genéricas que sea posible.

Siempre puedes añadir un sistema basado en reglas después para ir de genérico a
específico.

Es más fácil etiquetar y aprender categorías genéricas como `"ROPA"` o
`"BANDA"`.

---

# ¡Practiquemos!

Notes: ¡Miremos algunos de los problemas en contexto y solucionémoslos!
