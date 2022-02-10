---
type: slides
---

# Entraînement et actualisation des modèles

Notes: Bienvenue au dernier chapitre, qui concerne un des aspects les plus
formidables du NLP moderne : l'entraînement de tes propres modèles !

Dans cette leçon, tu vas apprendre à entraîner et à mettre à jour les composants
de pipelines de spaCy et leurs modèles de réseaux de neurones, et les données
dont tu as besoin pour le faire - en te concentrant spécifiquement sur le
reconnaisseur d'entités nommées.

---

# Pourquoi mettre à jour le modèle ?

- Meilleurs résultats sur ton domaine spécifique
- Entraînement de schémas de classification spécifiques à ton problème
- Essentiel pour la classification de texte
- Très utile pour la reconnaissance d'entités nommées
- Moins critique pour l'étiquetage de partie de discours et l'analyse des
  relations de dépendances

Notes: Avant de commencer à expliquer le _comment_, il est utile de prendre une
seconde pour nous demander : Pourquoi voudrions-nous mettre à jour le modèle
avec nos propres exemples ? Pourquoi ne peut-on pas simplement s'appuyer sur des
pipelines pré-entraînés ?

Les modèles statistiques effectuent des prédictions basés sur les exemples sur
lesquels ils ont été entraînés.

Tu peux généralement rendre le modèle plus précis en lui montrant des exemples
de ton domaine.

Souvent tu veux prédire des catégories qui sont spécifiques à ton problème, donc
le modèle doit les apprendre.

C'est essentiel pour la classification de texte, très utile pour la
reconnaissance d'entités et un peu moins critique pour l'étiquetage de partie de
discours et l'analyse de dépendances.

---

# Comment fonctionne l'entraînement (1)

1. **Initialise** les poids du modèle aléatoirement
2. **Prédit** quelques exemples avec les poids courants
3. **Compare** les prédictions avec les vrais labels
4. **Calcule** comment changer les poids pour améliorer les prédictions
5. **Modifie** légèrement les poids
6. Retourne au point 2.

Notes: spaCy permet l'actualisation de modèles existants avec plus d'exemples,
et l'entraînement de nouveaux modèles. Si nous ne démarrons pas avec un
pipeline entraîné, nous commençons par initialiser les poids aléatoirement.

Ensuite, spaCy appele `nlp.update`, qui prédit une série d'exemples avec les
poids courants.

Le modèle compare ensuite les prédictions avec les bonnes réponses, et décide
comment changer les poids pour effectuer de meilleures prédictions les fois
suivantes.

Enfin nous effectuons une petite correction aux poids courants et passons au
lot d'exemples suivant.

spaCy continue ensuite d'appeler `nlp.update` sur chaque lot d'exemples des
données. Pendant l'entraînement, on effectue généralement plusieurs passes sur
les données pour entraîner jusqu'à ce que le modèle cesse de s'améliorer.

---

# Comment fonctionne l'entraînement (2)

<img src="/training_fr.png" alt="Diagramme du processus d'entraînement" />

- **Jeu d'apprentissage :** Exemples et leurs annotations.
- **Texte :** Le texte d'entrée pour lequel le modèle doit prédire un label.
- **Label :** Le label que le modèle doit prédire.
- **Gradient :** Comment changer les poids.

Notes: Voici une illustration montrant le processus.

Les données d'apprentissage sont les exemples avec lesquels nous voulons
actualiser le modèle.

Le texte doit être une phrase, un paragraphe ou un document plus long. Pour un
résultat optimal, il doit être similaire à ce que le modèle rencontrera en
production.

Le label est ce qu'on veut que le modèle prédise. Il peut s'agir d'une catégorie
de texte, ou d'un span d'entité et son type.

Le gradient est la manière dont nous devons modifier le modèle pour réduire
l'erreur actuelle. It est calculé quand nous comparons les labels prédits avec
les vrais labels.

A l'issue de l'apprentissage, nous pouvons enregistrer un modèle actualisé et
l'utiliser dans notre application.

---

# Exemple : Entraînement de l'entity recognizer

- L'entity recognizer reconnaît des mots et des phrases en contexte
- Chaque token peut seulement faire partie d'une entité
- Les exemples doivent être fournis avec le contexte

```python
doc = nlp("L'iPhone 12 arrive bientôt")
doc.ents = [Span(doc, 1, 3, label="GADGET")]
```

- Les textes dépourvus d'entités sont importants aussi

```python
doc = nlp("Il me faut un nouveau téléphone ! Des suggestions à me faire ?")
doc.ents = []
```

- **But :** apprendre au modèle à généraliser

Notes: Jetons un oeil à un exemple pour un composant spécifique : l'entity
recognizer.

L'entity recognizer prend un document et prédit des phrases et leurs labels
_en contexte_. Cela signifie que les données d'entraînement doivent comprendre
des textes, les entités qu'ils contiennent et les labels des entités.

Les entités ne peuvent pas se chevaucher, donc chaque token ne peut faire partie
que d'une seule entité.

La manière la plus facile pour le faire est de montrer au modèle un texte et des
spans d'entités. spaCy peut être actualisé à partir d'objets `Doc` ordinaires
en annotant les entités avec `doc.ents`. Par exemple , "iPhone X" est un gadget,
commence au token 1 et finit au token 2.

Il est également très important que le modèle apprenne des mots qui _ne sont
pas_ des entités.

Dans ce cas, la liste des annotations de spans sera vide.

Notre objectif est d'apprendre au modèle à reconnaître de nouvelles entités dans
des contextes similaires, même si celles-ci n'étaient pas présentes dans les
données d'entraînement.

---

# Les données d'entraînement

- Exemples de ce qu'on veut que le modèle prédise en contexte
- Actualise un **modèle existant** : quelques centaines à quelques milliers
  d'exemples
- Entraîne une **nouvelle catégorie** : quelques milliers à un million
  d'exemples
  - les modèles anglais de spaCy : 2 millions de mots
- Généralement créés manuellement par des annotateurs humains
- Peut être semi-automatisé – par exemple, en utilisant le `Matcher` de spaCy !

Notes: Les données d'entraînement indiquent au modèle ce qu'on veut qu'il
prédise. Il peut s'agir de textes ou d'entités nommées qu'on veut qu'il
reconnaisse, de tokens et de leur étiquetage correct de partie de discours, ou
quoi que ce soit d'autre que le modèle devrait prédire.

Pour mettre à jour un modèle existant, on peut commencer avec quelques centaines
à quelques milliers d'exemples.

Pour entraîner une nouvelle catégorie, cela peut en nécessiter jusqu'à un
million.

Les pipelines anglais pré-entraînés de spaCy ont par exemple été entraînés sur
2 millions de mots labellisés avec des étiquettes de partie de discours, des
relations de dépendance et des entités nommées.

Les données d'entraînement sont généralement créées par des humains qui
affectent des labels à des textes.

C'est beaucoup de travail, mais il peut être semi-automatisé – par exemple, en
utilisant le `Matcher` de spaCy.

---

# Données d'entraînement vs. d'évaluation

- **Données d'entraînement** : utilisés pour actualiser le modèle
- **Données d'évaluation** :
  - données non vues par le modèle pendant l'entraînement
  - utilisées pour calculer la précision du modèle
  - doivent être représentatives des données que le modèle rencontrera en
    production

Notes: Lorsque tu entraînes ton modèle, il est important de savoir comment il
progresse et s'il apprend correctement. On le fait en comparant les prédictions
du modèle sur des exemples qu'il _n'a pas_ vus pendant son entraînement avec
les bonnes réponses que nous connaissons. En plus des données d'entraînement,
nous avons donc besoin de données d'évaluation, également appelées données de
développement.

Les données d'évaluation sont utilisées pour calculer le niveau de précision de
ton modèle. Par exemple, un score de précision de 90% signifie que le modèle
a prédit correctement 90% des exemples d'évaluation.

Cela signifie aussi que les données d'évaluation doivent être représentatives
des données que ton modèle rencontrera en production. Sinon, le score de
précision sera inutile, parce qu'il ne te dira pas _réellement_ à quel point
ton modèle est bon.

---

# Génération d'un corpus d'entraînement (1)

```python
import spacy

nlp = spacy.blank("fr")

# Crée un Doc avec des spans d'entités
doc1 = nlp("L'iPhone 12 arrive bientôt")
doc1.ents = [Span(doc1, 1, 3, label="GADGET")]
# Crée un autre Doc sans spans d'entités
doc2 = nlp("Il me faut un nouveau téléphone ! Des suggestions à me faire ?")

docs = [doc1, doc2]  # et ainsi de suite...
```

Notes: spaCy peut être actualisé avec des données dans le même format que
celui qu'il crée : des objets `Doc`. Tu as déjà appris à créer des objets
`Doc` et `Span` dans le chapitre 2.

Dans cet exemple, nous créons deux objets `Doc` pour notre corpus : un qui
contient une entité et un autre qui ne contient aucune entité. Pour ajouter les
entités au `Doc`, nous pouvons ajouter un `Span` aux `doc.ents`.

Bien sûr, il te faudra beaucoup d'autres exemples pour entraîner efficacement
ton modèle à généraliser et à prédire des entités similaire en contexte. Selon
la tâche, tu auras normalement besoin d'au moins quelques centaines à quelques
milliers d'exemples représentatifs.

---

# Génération d'un corpus d'entraînement (2)

- Séparer les données en deux parties :
  - **données d'entraînement** : utilisées pour actualiser le modèle
  - **données de développement** : utilisées pour évaluer le modèle

```python
random.shuffle(docs)
train_docs = docs[:len(docs) // 2]
dev_docs = docs[len(docs) // 2:]
```

Notes: Comme mentionné précédemment, nous n'avons pas seulement besoin de
données pour entraîner le modèle. Nous voulons aussi pouvoir évaluer sa
précision sur des exemples qu'il n'a pas rencontrés pendant son entraînement.
Cela se fait généralement en mélangeant et en séparant les données en deux :
une partie pour l'entraînement et une pour l'évaluation. Ici nous utilisons une
répartition simple à 50/50.

---

# Génération d'un corpus d'entraînement (3)

- `DocBin`: conteneur pour stocker et sauvegarder efficacement les objets `Doc`
- peut être sauvé sous forme de fichier binaire
- les fichiers binaires sont utilisés pour l'entraînement

```python
# Crée et sauve un ensemble de documents pour l'entraînement
train_docbin = DocBin(docs=train_docs)
train_docbin.to_disk("./train.spacy")
# Crée et sauve un ensemble de documents pour l'évaluation
dev_docbin = DocBin(docs=dev_docs)
dev_docbin.to_disk("./dev.spacy")
```

Notes: En général tu voudras stocker tes données d'entraînement et de
développement sous forme de fichiers sur disque, pour pouvoir les charger au
cours du processus d'entraînement de spaCy.

Le `DocBin` est un conteneur pour stocker et sérialiser efficacement les objets
`Doc`. Tu peux l'instancier avec une liste d'objets `Doc` et appeler sa méthode
`to_disk` pour le sauver sous forme de fichier binaire. On utilise typiquement
l'extension `.spacy` pour ces fichiers.

Comparé à d'autres protocoles de sérialisation binaire comme `pickle`, le
`DocBin` est plus rapide et génère des tailles de fichiers plus réduites parce
qu'il stocke seulement une fois le vocabulaire partagé. Tu peux en apprendre
plus sur son fonctionnement dans la
[documentation](https://spacy.io/api/docbin).

---

# Astuce : Conversion de tes données

- `spacy convert` te permet de convertir des corpus depuis des formats courants
- supporte `.conll`, `.conllu`, `.iob` et l'ancien format JSON de spaCy

```bash
$ python -m spacy convert ./train.gold.conll ./corpus
```

Notes: Dans certains cas, il se peut que tu disposes de données d'entraînement
et de développement dans un format courant – par exemple, CoNLL ou IOB. La
commande `convert` de spaCy convertit automatiquement ces fichiers dans le
format binaire de spaCy. Elle peut aussi convertir les fichiers qui sont au
format JSON utilisé par spaCy v2.

---

# Pratiquons !

Notes: Maintenant il est temps de commencer à préparer le corpus
d'entraînement. Jetons un oeil à quelques exemples et créons un petit jeu de
données pour un nouveau type d'entité.
