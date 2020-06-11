---
title: 'Capítulo 3: Pipelines de procesamiento'
description:
  "En este capítulo aprenderás todo lo que necesitas saber sobre el pipeline de procesamiento de spaCy. Aprenderás lo que sucede cuando procesas un texto, cómo escribir tus propios componentes y añadirlos al pipeline y cómo usar atributos personalizados para añadir tus propios metadatos a los documentos, spans y tokens."
prev: /chapter2
next: /chapter4
type: chapter
id: 3
---

<exercise id="1" title="Pipelines de procesamiento" type="slides">

<slides source="chapter3_01_processing-pipelines">
</slides>

</exercise>

<exercise id="2" title="¿Qué sucede cuando llamas al objeto nlp?">

¿Qué hace spaCy cuando llamas a `nlp` sobre un string de texto?

```python
doc = nlp("Esto es una frase.")
```

<choice>

<opt text="Corre el tagger, el parser y el entity recognizer y después el tokenizer.">

El tokenizer siempre se corre _antes_ que todos los demás componentes del pipeline, porque transforma el string de texto en un objeto `Doc`. El pipeline tampoco tiene que estar compuesto por el tagger, el parser y el entity recognizer.

</opt>

<opt text="Convierte en tokens el texto y aplica cada componente del pipeline en orden." correct="true">

El tokenizer convierte un string de texto en un objeto `Doc`. Luego, spaCy aplica en orden cada componente del pipeline sobre el documento.

</opt>

<opt text="Se conecta con el servidor de spaCy para calcular el resultado y devolverlo.">

spaCy calcula todo en la máquina y no necesita conectarse con un servidor.

</opt>

<opt text="Inicializa el lenguaje, añade el pipeline y carga los parámetros binarios.">

Cuando llamas a `spacy.load()` para cargar un modelo, spaCy inicializará el lenguaje, añadirá el pipeline y cargará los parámetros binarios. Cuándo _llamas_ al objeto `nlp` sobre un texto, el modelo ya está cargado.

</opt>

</exercise>

<exercise id="3" title="Inspeccionando el pipeline">

¡Inspeccionemos el pipeline del modelo pequeño de español!

- Carga el modelo `es_core_news_sm` y crea el objeto `nlp`.
- Imprime en pantalla los nombres de los componentes del pipeline usando `nlp.pipe_names`.
- Imprime en pantalla el pipeline entero de tuples `(name, component)` usando `nlp.pipeline`.

<codeblock id="03_03">

La lista de los nombres de los componentes está disponible como el atributo `nlp.pipe_names`. El pipeline entero, compuesto de los tuples de `(name, component)`, está disponible como `nlp.pipeline`.

</codeblock>

</exercise>

<exercise id="4" title="Componentes personalizados del pipeline" type="slides">

<slides source="chapter3_02_custom-pipeline-components">
</slides>

</exercise>

<exercise id="5" title="Casos prácticos para los componentes personalizados">

¿Cuáles de estos problemas pueden ser resueltos por los componentes personalizados del pipeline? ¡Escoge todos los que apliquen!

1. Actualizar los modelos pre-entrenados y mejorar sus predicciones
2. Calcular tus propios valores basados en los tokens y sus atributos
3. Añadir entidades nombradas, por ejemplo, basadas en un diccionario
4. Implementar soporte para un lenguaje adicional

<choice>

<opt text="1 y 2.">

Los componentes personalizados solo pueden modificar al `Doc` y no pueden ser usados para actualizar los parámetros de los otros componentes directamente.

</opt>

<opt text="1 y 3.">

Los componentes personalizados solo pueden modificar al `Doc` y no pueden ser usados para actualizar los parámetros de los otros componentes directamente.

</opt>

<opt text="1 y 4.">

Los componentes personalizados solo pueden modificar al `Doc` y no pueden ser usados para actualizar los parámetros de los otros componentes directamente. También son añadidos al pipeline después de que se inicializa la clase de lenguaje y después de la conversión a tokens, así que no son adecuados para añadir nuevos lenguajes.

</opt>

<opt text="2 y 3." correct="true">

Los componentes personalizados son excelentes para añadir valores personalizados a los documentos, tokens y spans y para personalizar los `doc.ents`.

</opt>

<opt text="2 y 4.">

Los componentes personalizados son añadidos al pipeline después de que se inicializa la clase de lenguaje y después de la conversión a tokens, así que no son adecuados para añadir nuevos lenguajes.

</opt>

<opt text="3 y 4.">

Los componentes personalizados son añadidos al pipeline después de que se inicializa la clase de lenguaje y después de la conversión a tokens, así que no son adecuados para añadir nuevos lenguajes.

</opt>

</choice>

</exercise>

<exercise id="6" title="Componentes simples">

El ejemplo muestra un componente personalizado que imprime la longitud de un documento. ¿Puedes completarlo?

- Completa la función del componente con la longitud del `doc`.
- Añade el `length_component` al pipeline existente como el **primer** componente.
- Prueba el nuevo pipeline y procesa cualquier texto con el objeto `nlp` - por ejemplo, "Esto es una frase."

<codeblock id="03_06">

- Para obtener la longitud del objeto `Doc`, puedes llamar la función integrada de Python, `len()`, sobre él.
- Usa el método `nlp.add_pipe` para añadir el componente al pipeline. Recuerda poner `True` en el argumento keyword `first`, para asegurarte de que se añada antes que los demás componentes.
- Para procesar un texto, llama al objeto `nlp` sobre él.

</codeblock>

</exercise>

<exercise id="7" title="Componentes complejos">

En este ejercicio escribirás un componente personalizado que use el `PhraseMatcher` para encontrar nombres de animales en el documento y añada los spans resultantes a los `doc.ents`. En la variable `matcher` ya se creó un `PhraseMatcher` con los patrones de animales.

- Define el componente personalizado y aplica el `matcher` al `doc`.
- Crea un `Span` para cada resultado, asígnale el label ID para `"ANIMAL"` y sobrescribe los `doc.ents` con los nuevos spans.
- Añade el nuevo componente al pipeline _después_ del componente `"ner"`.
- Procesa el texto e imprime en pantalla el texto de la entidad y los entity labels de las entidades en `doc.ents`.

<codeblock id="03_07">

- Recuerda que los resultados son una lista de tuples `(match_id, start, end)`.
- La clase `Span` toma 4 argumentos: el `doc` padre, el índice de inicio, el índice del final y el label.
- Para añadir el componente después de otro usa el argumento keyword `after` de `nlp.add_pipe`.

</codeblock>

</exercise>

<exercise id="8" title="Extensión de atributos" type="slides">

<slides source="chapter3_03_extension-attributes">
</slides>

</exercise>

<exercise id="9" title="Añadiendo extensiones de atributos (1)">

Vamos a practicar añadiendo algunas extensiones de atributos.

### Paso 1

- Usa `Token.set_extension` para registrar `"is_country"` (por defecto `False`).
- Actualízalo para `"España"` e imprímelo en pantalla para todos los tokens.

<codeblock id="03_09_01">

Recuerda que los atributos que fueron extendidos están disponibles a través de la propiedad `._`. Por ejemplo, `doc._.has_color`.

</codeblock>

### Paso 2

- Usa `Token.set_extension` para registrar `"reversed"` (función getter `get_reversed`).
- Imprime en pantalla su valor por cada token.

<codeblock id="03_09_02">

Recuerda que los atributos que fueron extendidos están disponibles a través de la propiedad `._`. Por ejemplo, `doc._.has_color`.

</codeblock>

</exercise>

<exercise id="10" title="Añadiendo extensiones de atributos (2)">

Intentemos añadir algunos atributos más complejos usando getters y extensiones de métodos.

### Parte 1

- Completa la función `get_has_number`.
- Usa `Doc.set_extension` para registrar `"has_number"` (getter `get_has_number`) e imprimir su valor en pantalla.

<codeblock id="03_10_01">

- Recuerda que los atributos que fueron extendidos están disponibles a través de la propiedad `._`. Por ejemplo, `doc._.has_color`.
- La función `get_has_number` debería devolver si cualquiera de los tokens en el `doc` devuelve `True` para `token.like_num` (si un token parece un número).

</codeblock>

### Parte 2

- Usa `Span.set_extension` para registrar `"to_html"` (método `to_html`).
- Llámalo sobre `doc[0:2]` con el tag `"strong"`.

<codeblock id="03_10_02">

- Las extensiones de método pueden tomar uno o más argumentos. Por ejemplo, `doc._.some_method("argument")`.
- El primer argumento que se le pasa al método siempre es el objeto `Doc`, `Token` o `Span` sobre el cual se llama al método.

</codeblock>

</exercise>

<exercise id="11" title="Entidades y extensiones">

En este ejercicio combinarás la extensión de atributos personalizados con las predicciones del modelo y crearás un getter de atributo que devuelve una URL de búsqueda de Wikipedia si el span es una persona, organización o lugar.

- Completa el getter `get_wikipedia_url` para que solo devuelva la URL si el label del span está en la lista de labels.
- Añade la extensión del `Span`, `"wikipedia_url"`, usando el getter `get_wikipedia_url`.
- Itera sobre las entidades en el `doc` y devuelve sus URLs de Wikipedia.

<codeblock id="03_11">

- Para obtener el string label de un span usa el atributo `span.label_`. Este es el label predicho por el entity recognizer si el span es un span que contiene una entidad.
- Recuerda que los atributos que fueron extendidos están disponibles a través de la propiedad `._`. Por ejemplo, `doc._.has_color`.

</codeblock>

</exercise>

<exercise id="12" title="Componentes con extensiones">

La extensión de atributos es especialmente poderosa si es combinada con los componentes personalizados del pipeline. En este ejercicio escribirás un componente del pipeline que encuentra nombres de países y una extensión de atributo personalizada que devuelve la ciudad capital del país si está disponible.

Un patrón de frases con todos los países está disponible como la variable `matcher`. Un diccionario de países relacionados con sus ciudades capitales está disponible como la variable `CAPITALS`.

- Completa el `countries_component` y crea un `Span` con el label `"LOC"` para todos los resultados.
- Añade el componente al pipeline.
- Registra la extensión del atributo del Span, `"capital"`, con el getter `get_capital`.
- Procesa el texto e imprime en pantalla el texto de la entidad, el label y la capital de la entidad para cada span que contiene una entidad en `doc.ents`.

<codeblock id="03_12">

- La clase `Span` toma cuatro argumentos: el `doc`, los índices del span de `start` y `end` y el `label`.
- Llamar al `PhraseMatcher` sobre un `doc` devuelve una lista de tuples con `(match_id, start, end)`.
- Para registrar una nueva extensión de atributo usa el método `set_extension` en la clase global, por ejemplo, `Doc`, `Token` o `Span`. Para definir un getter usa el argumento keyword `getter`.
- Recuerda que los atributos que fueron extendidos están disponibles a través de la propiedad `._`. Por ejemplo, `doc._.has_color`.

</codeblock>

</exercise>

<exercise id="13" title="Aumentando la escala y el desempeño" type="slides">

<slides source="chapter3_04_scaling-performance">
</slides>

</exercise>

<exercise id="14" title="Procesando streams">

En este ejercicio, usarás el `nlp.pipe` para procesar de manera más eficiente el texto. El objeto `nlp` ya fue creado para ti. Una lista de tweets sobre una cadena americana de cómida rápida popular están disponibles en la variable `TEXTS`.

### Parte 1

- Reescribe el ejemplo usando `nlp.pipe`. En vez de iterar sobre los textos y procesarlos, itera sobre los objetos `doc` que han sido devueltos por `nlp.pipe` usando yield.

<codeblock id="03_14_01">

- Usar `nlp.pipe` te permite combinar las dos primeras líneas de código en una sola.
- `nlp.pipe` toma los `TEXTS` y usa `yield` para devolver objetos `doc` sobre los que puedes hacer un loop.

</codeblock>

### Parte 2

- Reescribe el ejemplo usando `nlp.pipe`. No olvides llamar a `list()` alrededor del resultado para convertirlo en una lista.

<codeblock id="03_14_02"></codeblock>

### Parte 3

- Reescribe el ejemplo usando `nlp.pipe`. No olvides llamar a `list()` alrededor del resultado para convertirlo en una lista.

<codeblock id="03_14_03"></codeblock>

</exercise>

<exercise id="15" title="Procesando datos con contexto">

En este ejercicio usarás los atributos personalizados para añadir metainformación sobre el autor y el libro a citas.

Una lista de ejemplos `[text, context]` está disponible como la variable `DATA`. Los textos son citas de libros famosos y los contextos son diccionarios con los keys `"author"` y `"book"`.

- Usa el método `set_extension` para registrar los atributos personalizados `"author"` y `"book"` en el `Doc`, con el valor por defecto `None`.
- Procesa los pares `[text, context]` en `DATA` usando `nlp.pipe` con `as_tuples=True`.
- Sobrescribe el `doc._.book` y `doc._.author` con la información respectiva pasada como el contexto.

<codeblock id="03_15">

- El método `Doc.set_extension` toma dos argumentos: el nombre en string del atributo y el argumento keyword indicando el valor por defecto, el getter, el setter o el método. Por ejemplo, `default=True`.
- Si `as_tuples` es puesto como `True`, el método `nlp.pipe` toma una lista de tuples `(text, context)` y usa `yield` para devolver tuples de `(doc, context)`.

</codeblock>

</exercise>

<exercise id="16" title="Procesamiento selectivo">

En este ejercicio usarás los métodos `nlp.make_doc` y `nlp.disable_pipes` para correr unicamente los componentes seleccionados cuando se procesa un texto.

### Parte 1

- Reescribe el código para que solo convierta el texto en tokens usando `nlp.make_doc`.

<codeblock id="03_16_01">

El método `nlp.make_doc` puede ser llamado sobre un texto y devuelve un `Doc`, igual que el objeto `nlp`.

</codeblock>

### Parte 2

- Deshabilita el tagger y el parser usando el método `nlp.disable_pipes`.
- Procesa el texto e imprime en pantalla todas las entidades en el `doc`.

<codeblock id="03_16_02">

El método `nlp.disable_pipes` recibe un número variable de argumentos: los nombres en string de los componentes del pipeline que serán deshabilitados. Por ejemplo, `nlp.disable_pipes("ner")` deshabilitará el named entity recognizer.

</codeblock>

</exercise>
