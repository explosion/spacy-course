---
type: slides
---

# Vecteurs de mots et similarité sémantique

Notes: Dans cette leçon, tu vas apprendre à utiliser spaCy pour prédire à quel
point des documents, des spans ou des tokens sont similaires les uns avec les
autres.

Tu vas aussi apprendre à utiliser les vecteurs de mots et à les exploiter dans
ton application de NLP.

---

# Comparaison de similarité sémantique

- `spaCy` peut comparer deux objets et prédire leur similarité
- `Doc.similarity()`, `Span.similarity()` et `Token.similarity()`
- Accepte un autre objet et retourne un score de similarité (de `0` à `1`)
- **Important :** nécessite un modèle qui inclut les vecteurs de mots, par
  exemple:
  - ✅ `fr_core_news_md` (modèle moyen)
  - ✅ `fr_core_news_lg` (grand modèle)
  - 🚫 **PAS** `fr_core_news_sm` (petit modèle)

Notes: spaCy peut comparer deux objets et prédire à quel point ils sont
similaires – par exemple, documents, spans ou simples tokens.

Les objets `Doc`, `Token` et `Span` possèdent une méthode `.similarity` qui
prend en argument un autre objet et retourne un nombre décimal entre 0 et 1,
indiquant dans quelle mesure ils sont similaires.

Un point très important : Pour pouvoir utiliser la similarité, tu dois utiliser
un modèle spaCy plus grand qui inclut les vecteurs de mots.

Par exemple, le modèle anglais moyen ou grand – mais _pas_ le petit. Donc si tu
veux utiliser les vecteurs, choisis toujours un modèle qui se termine par "md"
ou par "lg". Tu trouveras de plus amples informations dans la
[documentation des modèles](https://spacy.io/models).

---

# Exemples de similarité (1)

```python
# Charge un plus grand modèle avec les vecteurs
nlp = spacy.load("fr_core_news_md")

# Compare deux documents
doc1 = nlp("J'aime la pizza")
doc2 = nlp("J'aime la quiche lorraine")
print(doc1.similarity(doc2))
```

```out
0.9686798359892211
```

```python
# Compare deux tokens
doc = nlp("J'aime la pizza et la quiche")
token1 = doc[3]
token2 = doc[6]
print(token1.similarity(token2))
```

```out
0.62105
```

Notes: Voici un exemple. Disons que nous voulons savoir si deux documents sont
similaires.

D'abord, nous chargeons le modèle français de taille moyenne, "fr_core_news_md".

Nous pouvons ensuite créer deux objets doc et utiliser la méthode `similarity`
du premier doc pour le comparer au second.

Ici, la prédiction est un score plutôt élevé de similarité de 0,96 pour "J'aime
la pizza" et "J'aime la quiche lorraine".

Cela fonctionne aussi avec les tokens.

Selon les vecteurs de mots, les tokens "pizza" et "quiche" sont relativement
similaires, et obtiennent un score de 0,62.

---

# Exemples de similarité (2)

```python
# Compare un document avec un token
doc = nlp("J'aime la pizza")
token = nlp("savon")[0]

print(doc.similarity(token))
```

```out
0.12344265753392583
```

```python
# Compare un span avec un document
span = nlp("J'aime la pizza et les pâtes")[3:7]
doc = nlp("McDonalds vend des hamburgers")

print(span.similarity(doc))
```

```out
0.6186440160069984
```

Notes: Tu peux aussi utiliser les méthodes `similarity` pour comparer des objets
de types différents.

Par exemple, un document et un token.

Ici, le score de similarité est assez bas et les deux objets sont considérés
assez peu similaires.

Voici un autre exemple comparant un span – "pizza et les pâtes" – à un document
relatif à McDonalds.

Le score retourné ici est 0,62, donc il y a une forme de similarité.

---

# Comment spaCy prédit la similarité ?

- La similarité est déterminée en utilisant des **vecteurs de mots**
- Des représentations multi-dimensionnelles de la signification des mots
- Générées avec un algorithme comme
  [Word2Vec](https://en.wikipedia.org/wiki/Word2vec) et beaucoup de textes
- Peuvent être ajoutés aux modèles statistiques de spaCy
- Par défaut : similarité cosinus, mais peut être modifiée
- Les vecteurs des `Doc` et `Span` sont par défaut la moyenne des vecteurs des
  tokens
- Les phrases courtes sont meilleures que les longs documents comportant de
  nombreux mots non pertinents

Notes: Mais comment spaCy fait-il ça sous le capot ?

La similarité est déterminée en utilisant des vecteurs de mots, des
représentations multi-dimensionnelles de la signification des mots.

Tu as peut-être entendu parler de Word2Vec, c'est un algorithme qui est souvent
utilisé pour entrainer des vecteurs de mots à partir de textes bruts.

Les vecteurs peuvent être ajoutés aux modèles statistiques de spaCy.

Par défaut, la similarité retournée par spaCy est la similarité cosinus entre
deux vecteurs - mais cela peut être modifié si nécessaire.

Les vecteurs des objets composés de plusieurs tokens, comme le `Doc` et le
`Span`, sont par défaut la moyenne des vecteurs de leurs tokens.

C'est aussi pour cela que tu obtiens généralement de meilleurs résultats avec
des phrases courtes qui comportent moins de mots non pertinents.

---

# Les vecteurs de mots dans spaCy

```python
# Charge un plus grand modèle avec des vecteurs
nlp = spacy.load("fr_core_news_md")

doc = nlp("J'ai une banane")
# Accède au vecteur via l'attribut token.vector
print(doc[3].vector)
```

```out
[ 0.14514    0.02404   -2.4107    -0.065107   1.4499     3.8751
  0.99248   -0.025606  -1.5564    -0.96526    1.816      1.5542
  1.9257    -0.21898   -0.62248   -0.12514   -1.4924     0.15898
  0.55028    0.26447   -1.3465     1.0917    -0.0059614 -0.41609
 -0.33383   -0.12654   -0.44623    0.90977    0.032714   0.84107
  2.0505    -1.4368     0.63731   -1.0465     0.40865    0.95406
 -0.43177    0.54945    0.55856   -1.3008    -0.60014   -1.7091
 -0.79766    2.2568     2.2223     2.1332    -0.72503    1.3304
 -1.0363     1.3716     1.4821    -1.2326    -1.4727    -0.43259
  0.95354    0.15735    2.0788    -0.69058   -0.37      -1.9991
 -1.9433     0.29023   -0.11225   -1.5691     1.1563     0.88076
  ...
```

Notes: Pour te donner une idée, voici un exemple montrant à quoi ressemblent ces
vecteurs.

D'abord, nous chargeons à nouveau le modèle moyen, qui comporte des vecteurs de
mots.

Ensuite, nous pouvons traiter un texte et chercher le vecteur d'un token en
utilisant l'attribut `.vector`.

Le résultat est un vecteur à 300 dimensions du mot "banane".

---

# La similarité depend du contexte d'application

- Utile pour de nombreuses applications : systèmes de recommandations, repérage
  de doublons etc.
- Il n'y a pas de définition objective de "similarité"
- Cela dépend du contexte et des besoins de l'application

```python
doc1 = nlp("J'aime les chats")
doc2 = nlp("Je déteste les chats")

print(doc1.similarity(doc2))
```

```out
0.6684962278316768
```

Notes: Prédire la similarité peut s'avérer utile pour toutes sortes
d'applications. Par exemple, pour recommander à un utilisateur des textes
similaires à ceux qu'il a lus. C'est aussi utile pour repérer du contenu en
doublon, comme des posts sur une plateforme en ligne.

Toutefois, il est important de retenir qu'il n'y a pas de définition objective
de ce qui est similaire et de ce qui ne l'est pas. Cela dépend toujours du
contexte et des besoins de ton application.

Voici un exemple : les vecteurs de mots de spaCy attribuent par défaut un score
élevé de similarité entre "J'aime les chats" et "Je déteste les chats". Cela
parait logique, car les deux textes expriment des sentiments à propos des chats.
Mais dans un contexte d'application différent, tu pourrais vouloir considérer
les phrases comme étant très _dissemblables_, parce qu'elles expriment des
sentiments opposés.

---

# Pratiquons !

Notes: Maintenant c'est à ton tour. Essayons quelques vecteurs de mots de spaCy
et utilisons-les pour prédire des similarités.
