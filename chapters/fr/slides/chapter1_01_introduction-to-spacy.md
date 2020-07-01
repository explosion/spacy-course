---
type: slides
---

# Présentation de spaCy

Notes: Salut, je m'appelle Inès ! Je suis l'un des principaux développeurs de
spaCy, une bibliothèque populaire pour le traitement automatique du langage
naturel en Python.

Dans cette leçon, nous allons aborder les principaux concepts de spaCy et faire
nos premiers pas.

---

# L'objet nlp

```python
# Importe la classe de langue "English"
from spacy.lang.en import English

# Crée l'objet nlp
nlp = English()
```

- contient le pipeline de traitement
- inclut des règles spécifiques à la langue pour la tokenisation.

Notes: Au coeur de spaCy se trouve l'objet contenant le pipeline de traitement.
Nous nommons généralement cette variable "nlp".

Par exemple, pour créer un objet `nlp` en langue anglaise, tu peux importer la
classe de langue `English` depuis `spacy.lang.en` et l'instancier. Tu peux
utiliser l'objet nlp comme une fonction pour analyser le texte.

Il contient l'ensemble des différents composants du pipeline.

Il inclut aussi des règles spécifiques à la langue utilisées pour la
tokenisation du texte en mots et ponctuations. spaCy supporte un grand nombre de
langues qui sont accessibles à partir de `spacy.lang`.

---

# L'objet Doc

```python
# Créé en traitant une chaine de caractères avec l'objet nlp
doc = nlp("Hello world!")

# Itère sur les tokens dans un Doc
for token in doc:
    print(token.text)
```

```out
Hello
world
!
```

Notes: Quand tu traites un texte avec l'objet `nlp`, spaCy crée un objet `Doc` –
abréviation de "document". Le Doc te permet d'accéder aux informations sur le
texte de manière structurée, sans perte d'information.

Le Doc se comporte d'ailleurs comme une séquence Python normale qui te permet
d'itérer sur ses tokens, ou d'obtenir un token à partir de son indice. Nous
reviendrons là dessus plus tard !

---

# L'objet Token

<img src="/doc.png" alt="Illustration d'un objet Doc contenant quatre tokens" width="50%" />

```python
doc = nlp("Hello world!")

# Utilisation d'un indice au sein du Doc pour obtenir un Token unique
token = doc[1]

# Obtiens le texte du token avec l'attribut .text
print(token.text)
```

```out
world
```

Notes: Les objets `Token` représentent les tokens dans un document – par
exemple, un mot ou un signe de ponctuation.

Pour obtenir un token à une position donnée, tu peux utiliser l'indice dans le
doc.

Les objets `Token` proposent aussi différents attributs qui te fournissent plus
d'informations sur les tokens. Par exemple, l'attribut `.text` retourne le texte
exact du token.

---

# L'objet Span

<img src="/doc_span.png" width="50%" alt="Illustration d'un objet Doc contenant quatre tokens dont trois sont regroupés dans un Span" />

```python
doc = nlp("Hello world!")

# Une portion du Doc est un objet Span
span = doc[1:3]

# Obtiens le texte du span avec l'attribut .text
print(span.text)
```

```out
world!
```

Notes: Un objet `Span` est une portion du document composée d'un ou plusieurs
tokens. Il s'agit seulement d'une vue du `Doc` qui ne contient pas elle-même de
données.

Pour créer un span, tu peux utiliser la notion entre crochets de Python. Par
exemple, `1:3` créera une portion commençant avec le token situé à la position
1, jusqu'à – mais sans inclure ! – le token à la position 3.

---

# Attributs lexicaux

```python
doc = nlp("It costs $5.")
```

```python
print("Index:   ", [token.i for token in doc])
print("Text:    ", [token.text for token in doc])

print("is_alpha:", [token.is_alpha for token in doc])
print("is_punct:", [token.is_punct for token in doc])
print("like_num:", [token.like_num for token in doc])
```

```out
Index:    [0, 1, 2, 3, 4]
Text:     ['It', 'costs', '$', '5', '.']

is_alpha: [True, True, False, False, False]
is_punct: [False, False, False, False, True]
like_num: [False, False, False, True, False]
```

Notes: Tu peux voir ici certains des attributs disponibles sur les tokens :

`i` est l'indice du token au sein du document parent.

`text` retourne le texte du token.

`is_alpha`, `is_punct` et `like_num` retournent des valeurs booléennes indiquant
si les tokens sont composés de caractères alphabétiques, s'ils sont des signes
de ponctuation et s'ils _ressemblent_ à un nombre. Par exemple, un token "10" –
un, zéro – ou le mot "dix" – D, I, X.

Ces attributs sont également appelés attributs lexicaux : ils se comprennent
comme des éléments de vocabulaire et ne dépendent pas du contexte du token.

---

# Passons à la pratique !

Notes: Voyons cela en pratique en traitant ton premier texte avec spaCy.
