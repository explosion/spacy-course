---
type: slides
---

# Scalabilité et performance

Notes: Dans cette leçon, tu vas apprendre quelques trucs et astuces pour faire
tourner tes pipelines spaCy aussi vite que possible, et pour traiter
efficacement d'importantes quantités de texte.

---

# Traitement d'importantes quantités de texte

- Utilise la méthode `nlp.pipe`
- Traite des textes en tant que flux, génère des objets `Doc`
- Beaucoup plus rapide que d'appeler `nlp` sur chaque texte

**MAUVAIS :**

```python
docs = [nlp(text) for text in LOTS_OF_TEXTS]
```

**BON :**

```python
docs = list(nlp.pipe(LOTS_OF_TEXTS))
```

Notes: Si tu as besoin de traiter d'importantes quantités de texte et de créer
de nombreux objets `Doc` à la suite, la méthode `nlp.pipe` peut accélérer
significativement le processus.

Elle traite les données en flux et génère des objets `Doc`.

C'est beaucoup plus rapide que d'appeler nlp sur chaque texte, car les textes
sont réunis en lots.

`nlp.pipe` est un générateur qui génère des objets `Doc`, donc pour obtenir une
liste des docs, rappelle-toi de lui appliquer la méthode `list`.

---

# Intégration de contexte (1)

- Définir `as_tuples=True` dans `nlp.pipe` te permet de lui passer des tuples
  `(text, context)`
- Génère des tuples `(doc, context)`
- Utile pour ajouter des métadonnées au `doc`

```python
data = [
    ("Ceci est un texte", {"id": 1, "numero_page": 15}),
    ("Et un autre texte", {"id": 2, "numero_page": 16}),
]

for doc, context in nlp.pipe(data, as_tuples=True):
    print(doc.text, context["numero_page"])
```

```out
Ceci est un texte 15
Et un autre texte 16
```

Notes: `nlp.pipe` supporte aussi le passage de tuples de texte / contexte si tu
définis `as_tuples` à `True`.

La méthode va alors générer des tuples doc / contexte.

C'est pratique pour intégrer des métadonnées supplémentaires, comme un ID
associé au texte, ou un numéro de page.

---

# Intégration de contexte (2)

```python
from spacy.tokens import Doc

Doc.set_extension("id", default=None)
Doc.set_extension("numero_page", default=None)

data = [
    ("Ceci est un texte", {"id": 1, "numero_page": 15}),
    ("Et un autre texte", {"id": 2, "numero_page": 16}),
]

for doc, context in nlp.pipe(data, as_tuples=True):
    doc._.id = context["id"]
    doc._.numero_page = context["numero_page"]
```

Notes: Tu peux même ajouter les métadonnées de contexte à des attributs
personnalisés.

Dans cet exemple, nous déclarons deux extensions, `id` et `numero_page`, avec
comme valeur par défaut `None`.

Après avoir traité le texte et en prenant en compte le contexte, nous pouvons
actualiser les extensions du doc avec nos métadonnées de contexte.

---

# Utilisation isolée du tokenizer (1)

<img src="/pipeline.png" width="90%" alt="Illustration du pipeline spaCy">

- ne lance pas le pipeline complet !

Notes: Un autre scénario courant : Parfois tu as déjà un modèle chargé pour
effectuer d'autres traitements, mais tu as seulement besoin du tokenizer pour un
texte particulier.

Lancer tout le pipeline est inutilement lent, parce que le modèle va te fournir
tout un tas de prédictions dont tu n'as pas besoin.

---

# Utilisation isolée du tokenizer (2)

- Utilise `nlp.make_doc` pour transformer un texte en un objet `Doc`

**MAUVAIS :**

```python
doc = nlp("Bonjour monde !")
```

**BON :**

```python
doc = nlp.make_doc("Bonjour monde !")
```

Notes: Si tu as seulement besoin d'un objet `Doc` tokenisé, tu peux utiliser la
méthode `nlp.make_doc` à la place, elle prend en argument un texte et retourne
un doc.

C'est aussi la manière dont spaCy le fait en coulisses : `nlp.make_doc`
transforme le texte en un doc avant que les composants du pipeline ne soient
appelés.

---

# Désactivation de composants du pipeline

- Utilise `nlp.select_pipes` pour désactiver temporairement un ou plusieurs
  composants

```python
# Désactive le tagger et le parser
with nlp.select_pipes(disable=["tagger", "parser"]):
    # Traite le texte et affiche les entités
    doc = nlp(text)
    print(doc.ents)
```

- Les réactive après le bloc `with`
- N'exécute que les composants restants

Notes: spaCy te permet aussi de désactiver temporairement des composants du
pipeline en utilisant le gestionnaire de contexte `nlp.select_pipes`.

Il accepte les arguments nommés `enable` et `disable` qui peuvent définir une
liste de chaînes de caractères indiquant les composants du pipeline à
désactiver. Par exemple, si tu veux seulement utiliser l'entity recognizer
pour traiter un document, tu peux désactiver temporairement le tagger et le
parser.

Après le bloc `with`, les composants de pipeline désactivés sont automatiquement
réactivés.

Dans le bloc `with`, spaCy exécutera uniquement les composants restants.

---

# Pratiquons !

Notes: Maintenant c'est à toi. Essayons ces nouvelles méthodes et optimisons du
code pour qu'il soit plus rapide et plus efficace.
