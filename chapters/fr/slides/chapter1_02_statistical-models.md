---
type: slides
---

# Modèles statistiques

Notes: Ajoutons du pouvoir à notre objet `nlp` !

Dans cette leçon, tu vas en apprendre plus les modèles statistiques de spaCy.

---

# Que sont les modèles statistiques ?

- Ils permettent à spaCy de prédire les attributs linguistiques _en contexte_
  - Étiquetage de partie du discours
  - Dépendances syntaxiques
  - Entités nommées
- Entrainés sur des exemples de textes labellisés
- Peuvent être améliorés avec des exemples supplémentaires

Notes: Certaines des choses les plus intéressantes à analyser dépendent du
contexte : par exemple, si un mot est un verbe or si une portion de texte est le
nom d'une personne.

Les modèles statistiques permettent à spaCy d'effectuer des prédictions en
contexte. Cela inclut généralement les étiquettes de partie de discours, les
dépendances syntaxiques et les entités nommées.

Les modèles sont entrainés sur de larges jeux de données de textes labellisés.

Ils peuvent être actualisés avec davantage d'exemples pour améliorer leurs
prédictions - par exemple, pour obtenir de meilleurs résultats sur tes propres
données.

---

# Paquets de modèles

<img src="/package.png" alt="Un paquet de modèles avec le label fr_core_news_sm" width="30%" align="right" />

```bash
$ python -m spacy download fr_core_news_sm
```

```python
import spacy

nlp = spacy.load("fr_core_news_sm")
```

- Poids binaires
- Vocabulaire
- Méta-information (langage, pipeline)

Notes: spaCy propose un certain nombre de modèles pré-entrainés que tu peux
télécharger avec la commande `spacy download`. Par exemple, le paquet
"en_core_web_sm" est un petit modèle pour la langue française qui propose toutes
les fonctionnalités de base et qui a été entrainé sur des textes d'actualité.

La méthode `spacy.load` charge un paquet de modèle et retourne un objet `nlp`.

Le paquet contient les poids binaires qui permettent à spaCy d'effectuer des
prédictions.

Il inclut aussi le vocabulaire, et des méta-informations pour indiquer à spaCy
quelle classe de langue utiliser et comment configurer le pipeline de
traitements.

---

# Prédiction des étiquettes de partie de discours

```python
import spacy

# Charge le petit modèle en langue française
nlp = spacy.load("fr_core_news_sm")

# Traite le texte
doc = nlp("Elle mangea la pizza")

# Itère sur les tokens
for token in doc:
    # Affiche le texte et l'étiquette de partie de discours prédite
    print(token.text, token.pos_)
```

```out
Elle PRON
mangea VERB
la DET
pizza NOUN
```

Notes: Jetons un oeil aux prédictions du modèle. Dans cet exemple, nous
utilisons spaCy pour prédire des étiquettes de partie de discours, les types des
mots dans leur contexte.

D'abord, nous chargeons le petit modèle en langue française et obtenons un objet
`nlp`.

Ensuite, nous traitons le texte "Elle mangea la pizza".

Pour chaque token dans le doc, nous pouvons afficher le texte et l'attribut
`.pos_`, l'étiquette de partie de discours prédite.

Dans spaCy, les attributs qui retournent des chaines de caractères se terminent
généralement par un tiret bas - les attributs sans tiret bas retournent un ID
sous forme de valeur entière.

Ici, le modèle a correctement prédit "mangea" comme étant un verbe et "pizza"
comme étant un nom.

---

# Prédiction de dépendances syntaxiques

```python
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)
```

```out
Elle PRON nsubj mangea
mangea VERB ROOT mangea
la DET det pizza
pizza NOUN obj mangea
```

Notes: En plus des étiquettes de partie de discours, nous pouvons aussi prédire
comment les mots sont reliés. Par exemple, si un mot est le sujet ou un objet
d'une phrase.

L'attribut `.dep_` retourne la dépendance syntaxique prédite.

L'attribut `.head` retourne le token de tête syntaxique ou noyau. Tu peux le
voir comme le token parent auquel le mot considéré se rattache.

---

# Schéma de relations de dépendances

<img src="/dep_example.png" alt="Visualisation du graphe de dépendances pour 'Elle mangea la pizza'" />

| Label     | Description               | Exemple |
| --------- | ------------------------- | ------- |
| **nsubj** | sujet nominal             | Elle    |
| **obj**   | complément d'objet direct | pizza   |
| **det**   | déterminant (article)     | la      |

Notes: Pour décrire les dépendances syntaxiques, spaCy utilise un système de
labellisation standardisé. Voici un exemple avec quelques labels courants :

Le pronom "Elle" est le sujet rattaché au verbe – ici, "mangea".

Le nom "pizza" est un complément d'objet direct rattaché au verbe "mangea".
Elle est mangée par le sujet, "Elle".

Le déterminant "la", également appelé article, est rattaché au nom "pizza".

---

# Prédiction d'Entités Nommées

<img src="/ner_example.png" alt="Visualisation des entités nommées dans 'Apple is looking at buying U.K. startup for $1 billion'" width="80%" />

```python
# Traite le texte
doc = nlp("Apple conçoit le nouvel iPhone à Cupertino.")

# Itère sur les entités prédites
for ent in doc.ents:
    # Affiche le texte de l'entité et son label
    print(ent.text, ent.label_)
```

```out
Apple ORG
iPhone MISC
Cupertino LOC
```

Notes: Les entités nommées sont des "objets du monde réel" auxquels on assigne
un nom - par exemple, une personne, une organisation ou un pays.

La propriété `doc.ents` te permet d'accéder aux entités nommées prédites par le
modèle.

Elle retourne un itérateur d'objets `Span`, donc nous pouvons imprimer le texte
de l'entité et son label en utilisant l'attribut `.label_`.

Dans notre exemple, le modèle a correctement prédit "Apple" en tant
qu'organisation, "U.K." comme entité géopolitique et "\$1 billion" comme somme
d'argent.

---

# Astuce : la méthode spacy.explain

Obtiens des définitions rapides des tags et des étiquettes les plus courants.

```python
spacy.explain("GPE")
```

```out
'Countries, cities, states'
```

```python
spacy.explain("NNP")
```

```out
'noun, proper singular'
```

```python
spacy.explain("dobj")
```

```out
'direct object'
```

Notes: Une petite astuce : Pour obtenir des définitions pour les tags et les
labels les plus courants, tu peux utiliser la fonction d'assistance
`spacy.explain`.

Par exemple, "GPE" pour entité géopolitique n'est pas vraiment intuitif – mais
`spacy.explain` peut t'indiquer que cela fait référence à des pays, des villes
et des états.

Cela s'applique aussi aux étiquettes de partie de discours et aux dépendances
syntaxiques.

---

# Passons à la pratique !

Notes: Maintenant c'est à toi de jouer. Jetons un oeil aux modèles statistiques
de spaCy et à leurs prédictions.
