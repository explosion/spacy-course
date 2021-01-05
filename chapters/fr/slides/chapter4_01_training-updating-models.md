---
type: slides
---

# Entrainement et actualisation des modèles

Notes: Bienvenue au dernier chapitre, qui concerne un des aspects les plus
formidables du NLP moderne : l'entrainement de tes propres modèles !

Dans cette leçon, tu vas apprendre à entrainer et à mettre à jour les modèles de
réseaux de neurones de spaCy et les données dont tu as besoin pour le faire - en
te concentrant spécifiquement sur le named entity recognizer.

---

# Pourquoi mettre à jour le modèle ?

- Meilleurs résultats sur ton domaine spécifique
- Apprentissage de schémas de classification spécifiques à ton problème
- Essentiel pour la classification de texte
- Très utile pour la reconnaissance d'entités nommées
- Moins critique pour l'étiquetage de partie de discours et l'analyse des
  relations de dépendances

Notes: Avant de commencer à expliquer le _comment_, il est utile de prendre une
seconde pour nous demander : Pourquoi voudrions-nous mettre à jour le modèle
avec nos propres exemples ? Pourquoi ne peut-on pas simplement s'appuyer sur les
modèles pré-entrainés ?

Les modèles statistiques effectuent des prédictions basés sur les exemples sur
lesquels ils ont été entrainés.

Tu peux généralement rendre le modèle plus précis en lui montrant des exemples
de ton domaine.

Souvent tu veux prédire des catégories qui sont spécifiques à ton problème, donc
le modèle doit les apprendre.

C'est essentiel pour la classification de texte, très utile pour la
reconnaissance d'entités et un peu moins critique pour l'étiquetage de partie de
discours et l'analyse de dépendances.

---

# Comment fonctionne l'apprentissage (1)

1. **Initialise** les poids du modèle aléatoirement avec `nlp.begin_training`
2. **Prédit** quelques exemples avec les poids courants en appelant `nlp.update`
3. **Compare** les prédictions avec les vrais labels
4. **Calcule** comment changer les poids pour améliorer les prédictions
5. **Modifie** légèrement les poids
6. Retourne au point 2.

Notes: spaCy permet l'actualisation de modèles existants avec plus d'exemples,
et l'entrainement de nouveaux modèles.

Si nous ne démarrons pas avec un modèle pré-entrainé, nous initialisons d'abord
les poids aléatoirement.

Ensuite, nous appelons `nlp.update`, qui prédit une série d'exemples avec les
poids courants.

Le modèle compare ensuite les prédictions avec les bonnes réponses, et décide
comment changer les poids pour effectuer de meilleures prédictions les fois
suivantes.

Finalement, nous effectuons une petite correction aux poids courants et passons
au lot suivant d'exemples.

On continue d'appeler `nlp.update` sur chaque lot d'exemples dans les données.

---

# Comment fonctionne l'apprentissage (2)

<img src="/training_fr.png" alt="Diagramme du processus d'apprentissage" />

- **Jeu d'apprentissage :** Exemples et leurs annotations.
- **Texte :** Le texte d'entrée pour lequel le modèle devrait prédire un label.
- **Label :** Le label que le modèle devrait prédire.
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

# Exemple : Entrainement de l'entity recognizer

- L'entity recognizer reconnait des mots et des phrases en contexte
- Chaque token peut seulement faire partie d'une entité
- Les exemples doivent être fournis avec le contexte

```python
("L'iPhone 12 arrive bientôt", {"entities": [(2, 8, "GADGET")]})
```

- Les textes dépourvus d'entités sont importants aussi

```python
("Il me faut un nouveau téléphone ! Des suggestions à me faire ?", {"entities": []})
```

- **But :** apprendre au modèle à généraliser

Notes: Jetons un oeil à un exemple pour un composant spécifique : l'entity
recognizer.

L'entity recognizer prend un document et prédit des phrases et leurs labels.
Cela signifie que les données d'apprentissage doivent comprendre des textes, les
entités qu'ils contiennent et les labels des entités.

Les entités ne peuvent pas se chevaucher, donc chaque token ne peut faire partie
que d'une seule entité.

Comme l'entity recognizer prédit les entités _en contexte_, il a aussi besoin
d'être entrainé sur des entités _et_ sur le contexte qui les environne.

La manière la plus facile pour le faire est de montrer au modèle un texte et une
liste de positions de caractères. Par exemple , "iPhone X" est un gadget,
commence au caractère 0 et finit au caractère 8.

Il est également très important que le modèle apprenne des mots qui _ne sont
pas_ des entités.

Dans ce cas, la liste des annotations de spans sera vide.

Notre objectif est d'apprendre au modèle à reconnaitre de nouvelles entités dans
des contextes similaires, même s'ils n'étaient pas présents dans les données
d'apprentissage.

---

# Les données d'apprentissage

- Exemples de ce qu'on veut que le modèle prédise en contexte
- Actualise un **modèle existant** : quelques centaines à quelques milliers
  d'exemples
- Entraine une **nouvelle catégorie** : quelques milliers à un million
  d'exemples
  - les modèles anglais de spaCy : 2 millions de mots
- Généralement créés manuellement par des annotateurs humains
- Peut être semi-automatisé – par exemple, en utilisant le `Matcher` de spaCy !

Notes: Les données d'apprentissage indiquent au modèle ce qu'on veut qu'il
prédise. Il peut s'agir de textes ou d'entités nommées qu'on veut qu'il
reconnaisse, ou de tokens et de leur étiquetage correct de partie de discours.

Pour mettre à jour un modèle existant, on peut commencer avec quelques centaines
à quelques milliers d'exemples.

Pour entrainer une nouvelle catégorie, cela peut en nécessiter jusqu'à un
million.

Les modèles anglais de spaCy ont par exemple été entrainés sur 2 millions de
mots labellisés avec les étiquettes de partie de discours, les relations de
dépendance et les entités nommées.

Les données d'apprentissage sont généralement créées par des humains qui
affectent des labels à des textes.

C'est beaucoup de travail, mais il peut être semi-automatisé – par exemple, en
utilisant le `Matcher` de spaCy.

---

# Pratiquons !

Notes: Maintenant il est temps de commencer à préparer les données
d'apprentissage. Jetons un oeil à quelques exemples et créons un petit jeu de
données pour un nouveau type d'entité.
