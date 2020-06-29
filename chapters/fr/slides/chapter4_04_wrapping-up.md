---
type: slides
---

# Résumé

Notes : Félicitations – tu as atteint la fin du cours !

---

# Tes nouvelles compétences spaCy

- Extraction de **caractéristiques linguistiques** : partie de discours,
  dépendances, entités nommées
- Travail avec **modèles statistiques** pré-entrainés
- Recherche de mots et de phrases selon des **règles de correspondance** avec
  `Matcher` et `PhraseMatcher`
- Meilleures pratiques pour l'emploi des **structures de données** `Doc`,
  `Token` `Span`, `Vocab`, `Lexeme`
- Recherche de **similarités sémantiques** avec les **vecteurs de mots**
- Écriture de **composants de pipeline** avec des **extensions d'attributs**
- **Accroissement d'échelle** des pipelines spaCy pour les rendre rapides
- Création de **données d'apprentissage** pour les modèles statistiques de spaCy
- **Entrainement et actualisation** des modèles de réseaux de neurones de spaCy
  avec de nouvelles données

Notes : Voici une vue d'ensemble de toutes les nouvelles compétences que tu as
apprises jusqu'à présent :

Dans le premier chapitre, tu as appris comment extraire des caractéristiques
linguistiques comme les étiquettes de partie de discours, les dépendances
syntaxiques et les entités nommées, et comment travailler avec des modèles
pré-entrainés.

Tu as aussi appris à écrire des règles de correspondances puissantes pour
extraire des mots et des phrases en utilisant le matcher et le phrase matcher de
spaCy.

Le chapitre 2 était consacré à l'extraction d'informations, et tu as appris
comment travailler avec les structures de données, les `Doc`, `Token` et `Span`,
ainsi qu'avec le `Vocab` et les éléments lexicaux.

Tu as aussi utilisé spaCy pour prédire des similarités sémantiques en utilisant
des vecteurs de mots.

Dans le chapitre 3, tu as acquis des connaissances plus complètes sur le
pipeline de spaCy, et tu as appris à écrire tes propres composants de pipeline
personnalisés qui modifient le doc.

Tu as également créé tes propres extensions d'attributs personnalisées pour des
docs, des tokens et des spans, et tu as appris à traiter des flux et à rendre
tes pipelines plus rapides.

Enfin, dans le chapitre 4, tu as appris à entrainer et à actualiser les modèles
statistiques de spaCy, spécifiquement l'entity recognizer.

Tu as appris quelques trucs utiles sur la manière de créer des données
d'apprentissage, et comment concevoir ton schéma de labellisation pour obtenir
les meilleurs résultats.

---

# D'autres choses à faire avec spaCy (1)

- [Entrainement et actualisation](https://spacy.io/usage/training) d'autres
  composants de pipeline
  - Etiqueteur de partie de discours
  - Analyseur de dépendances
  - Classificateur de texte

Notes : Bien sur, il y a beaucoup plus de choses que spaCy peut faire et que
nous n'avons pas couvertes dans ce cours.

Si nous nous sommes surtout concentrés sur l'entrainement de la reconnaissance
d'entités, tu peux aussi entrainer et actualiser les autres composants
statistiques du pipeline comme l'étiqueteur de partie de discours et l'analyseur
de dépendances.

Le classificateur de texte est un autre composant de pipeline utile, qui peut
apprendre à prédire des labels s'appliquant à tout un texte. Cela ne fait pas
partie des modèles pré-entrainés, mais tu peux l'ajouter à un modèle existant
et l'entrainer sur tes propres données.

---

# D'autres choses à faire avec spaCy (2)

- [Personnalisation du tokeniseur](https://spacy.io/usage/linguistic-features#tokenization)
  - Ajout de règles et d'exceptions pour scinder différemment le texte
- [Ajout ou amélioration du support pour d'autres langues](https://spacy.io/usage/adding-languages)
  - Plus de 55 langues actuellement
  - Marge de progression importante pour des améliorations et plus de langues
  - Possibilité d'entrainer des modèles pour d'autres langues

Notes : Dans ce cours, nous avons simplement accepté la tokenisation par défaut
telle qu'elle était. Mais tu n'es pas obligé !

spaCy te permet de personnaliser les règles utilisés pour déterminer où et
comment scinder le texte.

Tu peux aussi ajouter et améliorer le support pour d'autres langues.

Si spaCy permet déjà la tokenisation pour beaucoup de langues différentes, il y
a toujours des possibilités d'améliorations.

La gestion de la tokenisation pour une nouvelle langue est la première étape
afin de pouvoir entrainer un modèle statistique.

---

# Consulte le site web pour plus d'info et la documentation !

<img src="/website.png" alt="Ordinateur portable montrant le site web spacy.io" width="50%" />

👉 [spacy.io](https://spacy.io)

Notes : Pour plus d'exemples, de tutoriels et une documentation complète sur
l'API, consulte le site web de spaCy.

---

# Merci et à bientôt ! 👋

Notes : Merci beaucoup d'avoir suivi ce cours ! J'espère que tu t'es amusé, et
j'ai hâte d'apprendre les trucs cools que tu auras réussi à construire avec
spaCy.
