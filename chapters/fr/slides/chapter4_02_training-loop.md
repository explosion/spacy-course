---
type: slides
---

# La boucle d'apprentissage

Notes: Si certaines autres bibliothèques te proposent une méthode qui gère
l'entrainement du modèle, spaCy te fournit un contrôle total sur la boucle
d'apprentissage.

---

# Les étapes d'une boucle d'apprentissage

1. **Boucle** un certain nombre de fois.
2. **Mélange** les données d'apprentissage.
3. **Divise** les données en lots.
4. **Actualise** le modèle pour chaque lot.
5. **Enregistre** le modèle actualisé.

Notes: La boucle d'apprentissage consiste en une série d'étapes qui sont
effectuées pour entrainer ou pour actualiser un modèle.

On a généralement besoin de le faire plusieurs fois, avec de multiples
itérations, pour que le modèle puisse apprendre efficacement. Si on veut
l'entrainer sur 10 itérations, on devra effectuer la boucle 10 fois.

Pour éviter que le modèle ne se retrouve bloqué dans une solution sous-optimale,
on mélange aléatoirement les données à chaque itération. C'est une stratégie
très courante lorsqu'on effectue une descente de gradient stochastique.

Ensuite, on divise les données d'apprentissage en lots comprenant plusieurs
exemples, selon la technique dite du minibatching. Cela améliore la fiabilité
des estimations de gradient.

Enfin, on actualise le modèle pour chaque lot, et on recommence la boucle
jusqu'à atteindre la dernière itération.

on peut alors enregistrer le modèle dans un répertoire et l'utiliser dans spaCy.

---

# Récap : Comment fonctionne l'apprentissage

<img src="/training_fr.png" alt="Diagramme du processus d'apprentissage" />

- **Données d'apprentissage :** Exemples et leurs annotations.
- **Texte :** Le texte à partir duquel le modèle doit prédire un label.
- **Label :** Le label que le modèle devrait prédire.
- **Gradient :** Comment changer les poids.

Notes: Pour récapituler :

Les données d'apprentissage sont les exemples avec lesquels on veut actualiser
le modèle.

Le texte doit être une phrase, un paragraphe ou un document plus long. Pour un
résultat optimal, il devrait être similaire à ce que le modèle rencontrera en
production.

Le label est ce qu'on veut que le modèle prédise. Il peut s'agir d'une catégorie
de texte, ou d'un span d'entité et son type.

Le gradient est la manière dont nous devons modifier le modèle pour réduire
l'erreur actuelle. It est calculé quand nous comparons les labels prédits avec
les vrais labels.

---

# Exemple de boucle

```python
TRAINING_DATA = [
    ("Comment précommander l'iPhone 12 ?", {"entities": [(23, 32, "GADGET")]})
    # Et bien d'autres exemples...
]
```

```python
# Boucle pour 10 itérations
for i in range(10):
    # Mélange les données d'apprentissage
    random.shuffle(TRAINING_DATA)
    # Crée des lots et itère dessus
    for batch in spacy.util.minibatch(TRAINING_DATA):
        # Sépare le lot en textes et annotations
        texts = [text for text, annotation in batch]
        annotations = [annotation for text, annotation in batch]
        # Actualise le modèle
        nlp.update(texts, annotations)

# Enregistre le modèle
nlp.to_disk(path_to_model)
```

Notes: Voici un exemple.

Imaginons que nous avons une liste d'exemples d'apprentissage composée de textes
et d'annotations d'entités.

Nous voulons effectuer 10 boucles, donc nous itérons sur une `range` de 10.

Ensuite, nous utilisons le module `random` pour mélanger aléatoirement les
données d'apprentissage.

Ensuite nous utilisons l'utilitaire `minibatch` de spaCy pour diviser les
exemples en lots.

Pour chaque lot, nous obtenons le texte et les annotations et nous appelons la
méthode `nlp.update` pour actualiser le modèle.

Enfin, nous appelons la méthode `nlp.to_disk` pour enregistrer le modèle
entrainé dans un répertoire.

---

# Actualisation d'un modèle existant

- Améliore les prédictions sur de nouvelles données
- Particulièrement utile pour améliorer les catégories existantes, comme
  `"PERSON"`
- Aussi possible pour ajouter de nouvelles catégories
- Fais attention et assure-toi que le modèle "n'oublie" pas les anciennes

Notes: spaCy te permet d'actualiser un modèle pré-entrainé avec davantage de
données - par exemple, pour améliorer ses prédictions sur différents textes.

C'est particulièrement utile si tu veux améliorer les catégories que le modèle
connait déjà, comme "person" ou "organization".

Tu peux aussi actualiser le modèle pour ajouter de nouvelles catégories.

Assure-toi seulement de toujours l'actualiser avec des exemples de la nouvelle
catégorie _et_ des exemples des autres catégories qu'il prédisait déjà
correctement. Sinon l'amélioration sur la nouvelle catégorie pourrait nuire aux
autres catégories.

---

# Etablissement d'un nouveau pipeline à partir de zéro

```python
# Commence avec un modèle français vide
nlp = spacy.blank("fr")
# Crée un entity recognizer vide et l'ajoute au pipeline
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)
# Ajoute un nouveau label
ner.add_label("GADGET")

# Commence l'apprentissage
nlp.begin_training()
# S'entraine sur 10 itérations
for itn in range(10):
    random.shuffle(examples)
    # Divise les exemples en lots
    for batch in spacy.util.minibatch(examples, size=2):
        texts = [text for text, annotation in batch]
        annotations = [annotation for text, annotation in batch]
        # Actualise le modèle
        nlp.update(texts, annotations)
```

Notes: Dans cet exemple, nous commençons avec un modèle français vide en
utilisant la méthode `spacy.blank`. Le modèle vide n'a aucun composant de
pipeline, uniquement les données de la langue et les règles de tokenisation.

On crée ensuite un entity recognizer vide et on l'ajoute au pipeline.

Avec la méthode `add_label`, on peut ajouter les nouvelles chaines de labels au
modèle.

On peut alors appeler `nlp.begin_training` pour initialiser le modèle avec des
poids aléatoires.

Pour obtenir une meilleure justesse, on bouclera à plusieurs reprises sur les
exemples en mélangeant les données à chaque itération.

A chaque itération, on divise les exemples en lots avec la fonction utilitaire
`minibatch` de spaCy. Chaque exemple est composé d'un texte et de ses
annotations.

Enfin, on actualise le modèle avec les textes et les annotations et on continue
la boucle.

---

# Pratiquons !

Notes: Il est temps de pratiquer ! Maintenant que tu as vu la boucle
d'apprentissage, utilisons les données créées dans l'exercice précédent pour
actualiser le modèle.
