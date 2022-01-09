---
type: slides
---

# Composants de pipeline personnalisés

Notes: Maintenant que tu sais comment fonctionne le pipeline de spaCy, jetons un
oeil à une autre fonctionnalité très puissante : les composants de pipeline
personnalisés.

Les composants de pipeline personnalisés te permettent d'ajouter ta propre
fonction au pipeline de spaCy qui est exécuté lorsque tu appelles l'objet `nlp`
sur un texte – par exemple, pour modifier le doc et lui ajouter des données.

---

# Pourquoi des composants personnalisés ?

<img src="/pipeline.png" alt="Illustration du pipeline de spaCy" width="90%" />

- Crée une fonction qui s'exécute automatiquement quand tu appelles `nlp`
- Ajoute tes propres métadonnées aux documents et aux tokens
- Actualise les attributs natifs comme `doc.ents`

Notes: Une fois le texte tokenisé et l'objet `Doc` créé, les composants du
pipeline sont appliqués dans l'ordre. spaCy intègre un ensemble de composants
natifs, mais te permet aussi de créer ton propre composant.

Les composants personnalisés sont automatiquement exécutés quand tu appelles
l'objet `nlp` sur un texte.

Ils sont particulièrement utiles pour ajouter tes propres métadonnées aux
documents et aux tokens.

Tu peux aussi les utiliser pour actualiser les attributs natifs, comme les spans
d'entités nommées.

---

# Anatomie d'un composant (1)

- Fonction qui prend un `doc`, le modifie et le retourne
- Enregistré avec le décorateur `Language.component`
- Peut être ajouté avec la méthode `nlp.add_pipe`

```python
from spacy import Language

@Language.component("custom_component")
def custom_component_function(doc):
    # Effectue une action sur le doc ici
    return doc

nlp.add_pipe("custom_component")
```

Notes: Fondamentalement, un composant de pipeline est une fonction ou un
appelable qui prend un doc, le modifie et le retourne, pour qu'il puisse être
traité par le composant suivant dans le pipeline.

Pour indiquer à spaCy où trouver ton composant personnalisé et comment il doit
être appelé, tu peux le décorer avec le décorateur `Language.component`. Il te
suffit de l'ajouter sur la ligne juste au dessus de la définition de fonction.

Une fois qu'un composant est enregistré, il peut être ajouté au pipeline avec
la méthode `nlp.add_pipe`. La méthode prend au moins un argument : le nom du
composant sous forme de chaîne de caractères.

---

# Anatomie d'un composant (2)

```python
@Language.component("custom_component")
def custom_component_function(doc):
    # Effectue une action sur le doc ici
    return doc

nlp.add_pipe("custom_component")
```

| Argument | Description                  | Exemple                                   |
| -------- | ---------------------------- | ----------------------------------------- |
| `last`   | Si `True`, ajoute en dernier | `nlp.add_pipe("component", last=True)`      |
| `first`  | Si `True`, ajoute en premier | `nlp.add_pipe("component", first=True)`     |
| `before` | Ajoute avant le composant    | `nlp.add_pipe("component", before="ner")`   |
| `after`  | Ajoute après le composant    | `nlp.add_pipe("component", after="tagger")` |

Notes: Pour spécifier _où_ ajouter le composant dans le pipeline, tu peux
utiliser les arguments nommés suivants :

Définir `last` à `True` ajoutera le composant en dernier dans le pipeline. C'est
le comportement par défaut.

Définir `first` à `True` ajoutera le composant en premier dans le pipeline,
juste après le tokenizer.

Les arguments `before` et `after` te permettent de définir le nom d'un composant
existant avant ou après lequel insérer le nouveau composant. Par exemple,
`before="ner"` ajoutera le composant avant le named entity recognizer.

L'autre composant avant ou après lequel insérer le nouveau composant doit
exister, toutefois – sinon, spaCy génèrera une erreur.

---

# Exemple : un composant simple (1)

```python
# Crée l'objet nlp
nlp = spacy.load("fr_core_news_sm")

# Définit un composant personnalisé
@Language.component("custom_component")
def custom_component_function(doc):
    # Affiche la longueur du doc
    print("Longueur du doc :", len(doc))
    # Retourne l'objet doc
    return doc

# Ajoute le composant en premier dans le pipeline
nlp.add_pipe("custom_component", first=True)

# Affiche les noms des composants du pipeline
print("Pipeline :", nlp.pipe_names)
```

```out
Pipeline : ['custom_component', 'tok2vec', 'tagger', 'parser', 'ner', 'attribute_ruler', 'lemmatizer']
```

Notes: Voici un exemple de composant simple de pipeline.

On commence avec le petit pipeline français.

On définit ensuite le composant – une fonction qui prend un objet `Doc` et qui
le retourne.

Faisons quelque chose de simple et affichons la longueur du document qui
parcourt le pipeline.

N'oublie pas de retourner le doc pour qu'il puisse être traité par le composant
suivant dans le pipeline ! Le doc créé par le tokenizer est passé dans tous les
composants, donc il est important qu'ils retournent tous le doc modifié.

Pour indiquer à spaCy l'existence du nouveau composant, nous l'enregistrons
avec le décorateur `@Language.component` et l'appelons `"custom_component"`.

On peut maintenant ajouter le composant au pipeline. Ajoutons-le au tout début
juste après le tokenizer en définissant `first=True`.

Quand on imprime les noms des composants du pipeline, le composant personnalisé
apparait maintenant au début. Cela signifie qu'il sera appliqué en premier quand
nous traiterons un doc.

---

# Exemple : un composant simple (2)

```python
# Crée l'objet nlp
nlp = spacy.load("fr_core_news_sm")

# Définit un composant personnalisé
@Language.component("custom_component")
def custom_component_function(doc):

    # Affiche la longueur du doc
    print("Longueur du doc :", len(doc))

    # Retourne l'objet doc
    return doc

# Ajoute le composant en premier dans le pipeline
nlp.add_pipe("custom_component", first=True)

# Traite un texte
doc = nlp("Bonjour monde !")
```

```out
Longueur du doc : 3
```

Notes: Maintenant quand nous traitons un texte en utilisant l'objet `nlp`, le
composant personnalisé sera appliqué en premier au doc et la longueur du
document sera affichée.

---

# Pratiquons !

Notes: Il est temps de mettre cela en pratique et d'écrire ton premier composant
de pipeline !
