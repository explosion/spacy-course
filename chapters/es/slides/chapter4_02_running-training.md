---
type: slides
---

# Configurar y correr el entrenamiento

Notes: Ahora que ya has aprendido a crear un conjunto de datos (training data),
veamos cómo entrenar tu pipeline y configurar el entrenamiento. En esta
lección, aprenderás acerca del sistema de configuración de entrenamiento de
spaCy, cómo generar tu propia configuración de entrenamiento, cómo usar el CLI
para entrenar un modelo y cómo explorar luego el pipeline entrenado.

---

# Configuración del entrenamiento (1)

- **única fuente de verdad** para todos los ajustes
- usualmente llamado `config.cfg`
- define como iniciar el objeto `nlp`
- incluye todos los ajustes de los componentes del pipeline y sus modelos de
  implementaciones
- configura el proceso de entrenamiento e hiperparámetros
- hace que tu entrenamiento sea más reproducible

Notes: spaCy utiliza un archivo de configuración, habitualmente llamado
`config.cfg`, como "única fuente de verdad" para todos los ajustes. El archivo
de configuración define cómo iniciar el objeto `nlp`, qué componentes del
pipeline agregar y cómo deberían configurarse las implementaciones del modelo
interno. También incluye todos los ajustes para el proceso de entrenamiento y
cómo cargar los datos, incluidos los hiperparámetros. 

En vez de brindar varios argumentos en la línea de comando o recordar definir
cada setting en código, solo tienes que pasar tu archivo de configuración al
comando de entrenamiento de spaCy.

Los archivos de configuración habitualmente ayudan con la reproducibilidad:
tendrás todos los ajustes en un solo lugar y siempre sabrás cómo se entrenó
tu pipeline. También podrás chequear tu archivo de configuración en un
repositorio Git para versionarlo y compartirlo con otros para que puedan
entrenar el mismo pipeline con los mismos ajustes.

---

# Configuración del entrenamiento (2)

```ini
[nlp]
lang = "en"
pipeline = ["tok2vec", "ner"]
batch_size = 1000

[nlp.tokenizer]
@tokenizers = "spacy.Tokenizer.v1"

[components]

[components.ner]
factory = "ner"

[components.ner.model]
@architectures = "spacy.TransitionBasedParser.v2"
hidden_width = 64
# And so on...
```

Notes: Este es un extracto de un archivo de configuración utilizado para
entrenar un pipeline con un reconocedor de entidades nombradas. La
configuración se agrupa en secciones, y las secciones anidadas se definen con
un punto. Por ejemplo, `[components.ner.model]` define los ajustes del modelo
de implementación del reconocedor de entidades nombradas.

Los archivos de configuración pueden referenciar a funciones de Python
utilizando la anotación `@`. Por ejemplo, el analizador léxico define una
función de análisis léxico registrada. Puedes usarla para personalizar
diferentes partes del objeto `nlp` y del entrenamiento – desde ingresar tu
propio analizador léxico, hasta implementar tus propios modelos de arquitectura.
No nos preocupemos por eso ahora– lo que aprenderás en este capítulo
simplemente utilizará los innovadores defaults que spaCy provee.

---

# Generar una configuración

<!-- tarea pendiente: captura de pantalla del widget de inicio? -->

- spaCy puede auto-generar un archivo de configuración default por ti
- interactivo [wodget de inicio](https://spacy.io/usage/training#quickstart)
  en los archivos
- [`init config`](https://spacy.io/api/cli#init-config) comando en CLI

```bash
$ python -m spacy init config ./config.cfg --pipeline ner
```

- `init config`: el comando a correr
- `config.cfg`: ruta de salida de la configuración generada
- `--pipeline`: nombres, separados con comas, de los componentes a incluir

Notes: Claramente no tienes que escribir todos los archivos de configuración a
mano, y en muchos de los casos, ni siquiera necesitarás personalizarlos. spaCy
puede auto-generar un archivo de configuración default por ti.

El widget de inicio en la documentación te permite generar una configuración de
forma interactiva al seleccionar el lenguaje y los componentes del pipeline que
necesites, y además hardware opcional y ajustes de optimización.

Como alternativa, puedes usar el comando `init config` ya instalado en spaCy.
Toma el archivo de salida como el primer argumento. Generalmente llamamos a
este archivo `config.cfg`. El argumento `--pipeline` te permite especificar uno
o más componentes pipeline separados por una coma para incluir. En este
ejemplo, estamos creando una configuración con un componente pipeline, el
reconocedor de entidades nombradas.

---

# Entrenar un pipeline (1)

- todo lo que necesitas es el `config.cfg` y los datos de entrenamiento y
  desarrollo
- los ajustes de configuración pueden modificarse en la línea de comando

```bash
$ python -m spacy train ./config.cfg --output ./output --paths.train train.spacy --paths.dev dev.spacy
```

- `train`: el comando a correr
- `config.cfg`: ruta de archivo de configuración
- `--output`: ruta del directorio de salida para guardar el pipeline entrenado
- `--paths.train`: anular con ruta a los datos de entrenamiento
- `--paths.dev`: anular con ruta a los datos de evaluación

Notes: Para entrenar un pipeline, todo lo que necesita es un archivo de
configuración y el entrenamiento y los datos de desarrollo. Estos son los
archivos `.spacy` con los que trabajaste en los ejercicios anteriores.

El primer argumento de `spacy train` es la ruta al archivo de configuración.
El argumento `--output` te permite especificar un directorio para guardar el
pipeline final entrenado.

Puedes modificar diferentes ajustes de configuración en la línea de comando.
En este caso, podemos modificar `paths.train` utilizando la ruta al archivo
`train.spacy` y `paths.dev` utilizando el archivo `dev.spacy`.

---

# Entrenando un pipeline (2)

```
============================ Training pipeline ============================
ℹ Pipeline: ['tok2vec', 'ner']
ℹ Initial learn rate: 0.001

E    #       LOSS TOK2VEC  LOSS NER  ENTS_F  ENTS_P  ENTS_R  SCORE
---  ------  ------------  --------  ------  ------  ------  ------
  0       0          0.00     26.50    0.73    0.39    5.43    0.01
  0     200         33.58    847.68   10.88   44.44    6.20    0.11
  1     400         70.88    267.65   33.50   45.95   26.36    0.33
  2     600         67.56    156.63   45.32   62.16   35.66    0.45
  3     800        138.28    134.12   48.17   74.19   35.66    0.48
  4    1000        177.95    109.77   51.43   66.67   41.86    0.51
  6    1200         94.95     52.13   54.63   67.82   45.74    0.55
  8    1400        126.85     66.19   56.00   65.62   48.84    0.56
 10    1600         38.34     24.16   51.96   70.67   41.09    0.52
 13    1800        105.14     23.23   56.88   69.66   48.06    0.57

✔ Saved pipeline to output directory
/path/to/output/model-last
```

Notes: Aquí está un ejemplo del output que verás durante y después del
entrenamiento. Podrás recordar por las secciones anteriores de este capítulo 
que generalmente quieres hacer varias pasadas a los datos durante el
entrenamiento. Cada pasada sobre los datos lleva el nombre de "epoch".
Estas se muestran en la primera columna de la tabla.

Dentro de cada epoch, spaCy muestra las puntuaciones después de cada 200
ejemplos. Estos se muestran en pasos dentro de la segunda columna. Puedes
cambiar la frecuencia en la configuración. Cada línea muestra la pérdida y
la precisión calculada en este punto durante el entrenamiento.

El puntaje mpas interesante que hay que observar es el combinado en la última
columna. Este puntaje refleja qué tan preciso es tu modelo con respecto a las
respuestas correctas en los datos de evaluación.

El entrenamiento continúa hasta que el modelo deja de mejorar y en ese momento
el entrenamiento se detiene de manera automática.

---

# Cargando un pipeline entrenado

- la salida de datos después de un pipeline normal de spaCy
  - `model-last`: el pipeline entrenado más recientemente
  - `model-best`: el pipeline mejor entrenado
- cárgalo con `spacy.load`

```python
import spacy

nlp = spacy.load("/ruta/de/arhcivo/model-best")
doc = nlp("iPhone 11 vs iPhone 8: Cuál es la diferencia?")
print(doc.ents)
```

Notes: El pipeline guardado después del entrenamiento es un pipeline cargable
normal de spaCy – funciona exactamente como los pipelines entrenados normales
de spaCy, for example `en_core_web_sm`. Al final, el pipeline más recientemente
entrenado y el pipeline con mejores resultados son guardados en el directorio de
salida de datos.

Puedes cargar tu pipeline entrenado al pasar la ruta de archivo a `spacy.load`.
Después de esto puedes usarlo para analizar textos.

---

# Tip: Empaquetando tu pipeline

<!-- TODO: illustration of pipeline packages, similar to earlier chapters? -->

- [`spacy package`](https://spacy.io/api/cli#package): crea un paquete de
  Python instalable que contiene tu pipeline
- es fácil de versionar y de implementar

```bash
$ python -m spacy package /path/to/output/model-best ./packages --name mi_pipeline --version 1.0.0
```

```bash
$ cd ./packages/es_mi_pipeline-1.0.0
$ pip install dist/es_mi_pipeline-1.0.0.tar.gz
```

Carga y utiliza el pipeline después de instalarlo:

```python
nlp = spacy.load("es_mi_pipeline")
```

Notes: Para facilitar la implementación de tus pipelines, spaCy provee un
comando a práctico para empaquetarlos como paquetes de Python. El comando
`spacy package` toma una ruta de archivo de tu pipeline exportada y un
directorio de salida. Entonces genera un paquete de Python que contiene tu
pipeline. El paquete de Python package es un archivo `.tar.gz` file y puede ser
instalado en tu entorno.

También puedes proporcionar un nombre y una versión opcionales en el comando.
Esto te permite administrar varias versiones diferentes de un pipeline, por
ejemplo, si decides personalizar tus pipelines después o entrenarlo con más
datos.

El paquete se comporta como cualquier otro paquete de Python. Después de 
instalarlo, puedes cargar tu pipeline usando su nombre. Nota que spaCy agregará
el código del lenguaje al nombre de manera automática. Así que tu pipeline
`mi_pipeline` se convertirá en `es_mi_pipeline`.

---

# ¡Vamos a practicar!

Notes: ¡Comencemos a trabajar para entrenar tu primer pipeline! Vas a practicar
cómo generar una configuración para un named entity reocogizer y entrenar un
pipeline utilizando los datos en los que trabajaste en los ejercicios
anteriores.
