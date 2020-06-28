---
type: slides
---

# Vecteurs de mots et similarité sémantique

Notes : Dans cette leçon, tu vas apprendre à utiliser spaCy pour prédire à quel
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
  - ✅ `en_core_web_md` (modèle moyen)
  - ✅ `en_core_web_lg` (grand modèle)
  - 🚫 **PAS** `en_core_web_sm` (petit modèle)

Notes : spaCy peut comparer deux objets et prédire à quel point ils sont
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
nlp = spacy.load("en_core_web_md")

# Compare deux documents
doc1 = nlp("I like fast food")
doc2 = nlp("I like pizza")
print(doc1.similarity(doc2))
```

```out
0.8627204117787385
```

```python
# Compare deux tokens
doc = nlp("I like pizza and pasta")
token1 = doc[2]
token2 = doc[4]
print(token1.similarity(token2))
```

```out
0.7369546
```

Notes : Voici un exemple. Disons que nous voulons savoir si deux documents sont
similaires.

D'abord, nous chargeons le modèle anglais de taille moyenne, "en_core_web_md".

Nous pouvons ensuite créer deux objets doc et utiliser la méthode `similarity`
du premier doc pour le comparer au second.

Ici, la prédiction est un score plutôt élevé de similarité de 0,86 pour "I like
fast food" et "I like pizza".

Cela fonctionne aussi avec les tokens.

Selon les vecteurs de mots, les tokens "pizza" et "pasta" sont relativement
similaires, et obtiennent un score de 0,7.

---

# Exemples de similarité (2)

```python
# Compare un document avec un token
doc = nlp("I like pizza")
token = nlp("soap")[0]

print(doc.similarity(token))
```

```out
0.32531983166759537
```

```python
# Compare un span avec un document
span = nlp("I like pizza and pasta")[2:5]
doc = nlp("McDonalds sells burgers")

print(span.similarity(doc))
```

```out
0.619909235817623
```

Notes : Tu peux aussi utiliser les méthodes `similarity` pour comparer des
objets de types différents.

Par exemple, un document et un token.

Ici, le score de similarité est assez bas et les deux objets sont considérés
assez peu similaires.

Voici un autre exemple comparant un span – "pizza and pasta" – à un document
relatif à McDonalds.

Le score retourné ici est 0,61, donc il y a une forme de similarité.

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

Notes : Mais comment spaCy fait-il ça sous le capot ?

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
nlp = spacy.load("en_core_web_md")

doc = nlp("I have a banana")
# Accède au vecteur via l'attribut token.vector
print(doc[3].vector)
```

```out
 [2.02280000e-01,  -7.66180009e-02,   3.70319992e-01,
  3.28450017e-02,  -4.19569999e-01,   7.20689967e-02,
 -3.74760002e-01,   5.74599989e-02,  -1.24009997e-02,
  5.29489994e-01,  -5.23800015e-01,  -1.97710007e-01,
 -3.41470003e-01,   5.33169985e-01,  -2.53309999e-02,
  1.73800007e-01,   1.67720005e-01,   8.39839995e-01,
  5.51070012e-02,   1.05470002e-01,   3.78719985e-01,
  2.42750004e-01,   1.47449998e-02,   5.59509993e-01,
  1.25210002e-01,  -6.75960004e-01,   3.58420014e-01,
 -4.00279984e-02,   9.59490016e-02,  -5.06900012e-01,
 -8.53179991e-02,   1.79800004e-01,   3.38669986e-01,
  ...
```

Notes : Pour te donner une idée, voici un exemple montrant à quoi ressemblent
ces vecteurs.

D'abord, nous chargeons à nouveau le modèle moyen, qui comporte des vecteurs de
mots.

Ensuite, nous pouvons traiter un texte et chercher le vecteur d'un token en
utilisant l'attribut `.vector`.

Le résultat est un vecteur à 300 dimensions du mot "banana".

---

# La similarité depend du contexte d'application

- Utile pour de nombreuses applications : systèmes de recommandations, repérage
  de doublons etc.
- Il n'y a pas de définition objective de "similarité"
- Cela dépend du contexte et des besoins de l'application

```python
doc1 = nlp("I like cats")
doc2 = nlp("I hate cats")

print(doc1.similarity(doc2))
```

```out
0.9501447503553421
```

Notes : Prédire la similarité peut s'avérer utile pour toutes sortes
d'applications. Par exemple, pour recommander à un utilisateur des textes
similaires à ceux qu'il a lus. C'est aussi utile pour repérer du contenu en
doublon, comme des posts sur une plateforme en ligne.

Toutefois, il est important de retenir qu'il n'y a pas de définition objective
de ce qui est similaire et de ce qui ne l'est pas. Cela dépend toujours du
contexte et des besoins de ton application.

Voici un exemple : les vecteurs de mots de spaCy attribuent par défaut un score
élevé de similarité entre "I like cats" et "I hate cats". Cela parait logique,
car les deux textes expriment des sentiments à propos des chats. Mais dans un
contexte d'application différent, tu pourrais vouloir considérer les phrases
comme étant très _dissemblables_, parce qu'elles expriment des sentiments
opposés.

---

# Pratiquons !

Notes : Maintenant c'est à ton tour. Essayons quelques vecteurs de mots de spaCy
et utilisons-les pour prédire des similarités.
