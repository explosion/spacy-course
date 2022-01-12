---
type: slides
---

# Correspondances avec des règles

Notes: Dans cette leçon, nous allons faire connaissance avec le matcher de
spaCy, qui te permet d'écrire des règles pour trouver des mots et des phrases
dans un texte.

---

# Pourquoi pas simplement des expressions régulières ?

- Recherche de correspondances sur les objets `Doc`, pas seulement sur les
  chaînes de caractères
- Recherche de correspondances sur les tokens et les attributs des tokens
- Utilisation des prédictions d'un modèle
- Exemple : "capture" (verbe) vs. "capture" (nom)

Notes: par rapport aux expressions régulières, le matcher fonctionne avec des
objets `Doc` et `Token` et pas simplement avec des chaines de caractères.

Il est également plus flexible : tu peux rechercher des textes mais aussi
d'autres attributs lexicaux.

Tu peux même écrire des règles qui utilisent les prédictions d'un modèle.

Par exemple, trouve le mot "capture" seulement si c'est un verbe, pas un nom.

---

# Motifs de correspondance

- Listes de dictionnaires, un par token

- Recherche de correspondances exactes des textes

```python
[{"TEXT": "iPhone"}, {"TEXT": "X"}]
```

- Recherche d'attributs lexicaux

```python
[{"LOWER": "iphone"}, {"LOWER": "x"}]
```

- Recherche de n'importe quel attribut des tokens

```python
[{"LEMMA": "acheter"}, {"POS": "DET"}, {"POS": "NOUN"}]
```

Notes: Les motifs de correspondance sont des listes de dictionnaires. Chaque
dictionnaire décrit un token. Les clés sont les noms des attributs des tokens,
auxquelles sont associées les valeurs recherchées.

Dans cet exemple, nous recherchons deux tokens avec les textes "iPhone" et "X".

Nous pouvons aussi rechercher sur d'autres attributs des tokens. Ici, nous
recherchons deux tokens dont les formes minuscules sont "iphone" et "x".

Nous pouvons même écrire des motifs utilisant des attributs prédits par un
modèle. Ici, nous recherchons un token avec le lemme "acheter" suivi par un
déterminant et un nom. Le lemme est la forme de base, donc ce motif trouvera
des phrases comme "achetant le pain" ou "acheta le journal".

---

# Utilisation du Matcher (1)

```python
import spacy

# Importe le Matcher
from spacy.matcher import Matcher

# Charge un pipeline et crée l'objet nlp
nlp = spacy.load("fr_core_news_sm")

# Initialise le matcher avec le vocabulaire partagé
matcher = Matcher(nlp.vocab)

# Ajoute le motif au matcher
pattern = [{"TEXT": "iPhone"}, {"TEXT": "12"}]
matcher.add("IPHONE_PATTERN", [pattern])

# Traite un texte
doc = nlp("La date de sortie du futur iPhone 12 a fuité")

# Appelle le matcher sur le doc
matches = matcher(doc)
```

Notes: Pour utiliser un motif, nous devons d'abord importer le matcher à partir
de `spacy.matcher`.

Nous chargeons également un pipeline et créons l'objet `nlp`.

Le matcher est initialisé avec le vocabulaire partagé, `nlp.vocab`. Tu en sauras
plus là dessus par la suite – pour le moment, rappelle-toi seulement de toujours
le passer en argument.

La méthode `matcher.add` te permet d'ajouter un motif. Le premier argument est
un ID unique pour identifier quel motif a été trouvé. Le second argument est
une liste de motifs.

Pour trouver le motif sur un texte, nous pouvons appeler le matcher sur
n'importe quel doc.

Ceci nous retournera les correspondances.

---

# Utilisation du Matcher (2)

```python
# Appel du matcher sur le doc
doc = nlp("La date de sortie du futur iPhone 12 a fuité")
matches = matcher(doc)

# Itère sur les correspondances
for match_id, start, end in matches:
    # Obtiens le span en correspondance
    matched_span = doc[start:end]
    print(matched_span.text)
```

```out
iPhone 12
```

- `match_id`: valeur de hash du nom du motif
- `start`: indice de début du span en correspondance
- `end`: indice de fin du span en correspondance

Notes: Quand tu appelles le matcher sur un doc, il retourne une liste de tuples.

Chaque tuple contient trois valeurs : l'ID du motif, l'indice de début et
l'indice de fin du span en correspondance.

Cela signifie que nous pouvons itérer sur les correspondances et créer un objet
`Span` : une portion du doc depuis l'indice de début jusqu'à l'indice de fin.

---

# Recherche d'attributs lexicaux

```python
pattern = [
    {"LOWER": "coupe"},
    {"LOWER": "du"},
    {"LOWER": "monde"},
    {"LOWER": "fifa"},
    {"IS_DIGIT": True},
    {"IS_PUNCT": True}
]
```

```python
doc = nlp("Coupe du Monde FIFA 2018 : la France a gagné !")
```

```out
Coupe du Monde FIFA 2018 :
```

Notes: Voici un exemple de motif un peu plus complexe utilisant des attributs
lexicaux.

Nous recherchons six tokens :

Quatre tokens insensibles à la casse pour "coupe", "du", "monde" et "fifa".

Un token composé uniquement de valeurs numériques.

Et un token de type ponctuation.

Le motif trouve les "Coupe du Monde FIFA 2018 :".

---

# Recherche sur d'autres attributs des tokens

```python
pattern = [
    {"LEMMA": "photographier", "POS": "VERB"},
    {"POS": "DET"},
    {"POS": "NOUN"}
]
```

```python
doc = nlp("Avant elle photographiait les fleurs. Désormais elle photographiera les oiseaux.")
```

```out
photographiait les fleurs
photographiera les oiseaux
```

Notes: Dans cet exemple, nous recherchons trois tokens :

Un verbe avec le lemme "photographier", suivi par un déterminant et par un nom.

Ce motif trouvera "photographiait les fleurs" et "photographiera les oiseaux".

---

# Utilisation d'opérateurs et de quantificateurs (1)

```python
pattern = [
    {"LEMMA": "acheter", "POS": "VERB"},
    {"POS": "DET"},
    {"POS": "ADJ", "OP": "?"}, # optionnel : trouve 0 or 1 fois
    {"POS": "NOUN"}
]
```

```python
doc = nlp("J'ai acheté un nouveau smartphone. Maintenant j'achète des applis.")
```

```out
acheté un nouveau smartphone
achète des applis
```

Notes: Les opérateurs et les quantificateurs te permettent de définir combien de
fois un token doit être trouvé. Ils peuvent être ajoutés avec la clé "OP".

Ici, l'opérateur "?" rend le token du déterminant optionnel, donc il trouvera un
token avec le lemme "acheter", un déterminant, un adjectif optionnel et un nom.

---

# Utilisation d'opérateurs et de quantificateurs (2)

| Exemple       | Description                    |
| ------------- | ------------------------------ |
| `{"OP": "!"}` | Négation : trouve 0 fois       |
| `{"OP": "?"}` | Optionnel : trouve 0 ou 1 fois |
| `{"OP": "+"}` | Trouve 1 ou plusieurs fois     |
| `{"OP": "*"}` | Trouve 0 ou plusieurs fois     |

Notes: "OP" peut prendre quatre valeurs distinctes :

Un "!" exclut le token, donc il doit être trouvé 0 fois.

Un "?" rend le token optionnel, il peut être trouvé 0 ou 1 fois.

Un "+" cherche le token 1 ou plusieurs fois.

Et enfin, un "\*" cherche le token 0 ou plusieurs fois.

Les opérateurs peuvent rendre tes motifs beaucoup plus puissants, mais ils
ajoutent aussi de la complexité - donc utilise-les à bon escient.

---

# Passons à la pratique !

Notes: La recherche de correspondances basée sur les motifs ouvre de nombreuses
nouvelles possibilités d'extraction d'informations. Alors essayons et écrivons
quelques motifs !
