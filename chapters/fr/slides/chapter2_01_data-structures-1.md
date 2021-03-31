---
type: slides
---

# Structures de données (1) : Vocabulaire, lexèmes et magasin de chaines

Notes: Bienvenue à nouveau ! Maintenant que tu as eu une expérience concrète
d'utilisation des objets de spaCy, le moment est venu pour toi d'en savoir plus
sur ce qui se passe sous le capot de spaCy.

Dans cette leçon, nous allons examiner de plus près le vocabulaire partagé et
comment spaCy gère les chaines de caractères.

---

# Vocabulaire partagé et magasin de chaines (1)

- `Vocab` : stocke les données partagées entre des documents multiples
- Pour économiser de l'espace mémoire, spaCy encode toutes les chaines en
  **valeurs de hachage**
- Les chaines ne sont stockées qu'une seule fois dans le `StringStore` via
  `nlp.vocab.strings`
- String store : **table de consultation** dans les deux sens

```python
nlp.vocab.strings.add("souvent")
souvent_hash = nlp.vocab.strings["souvent"]
souvent_string = nlp.vocab.strings[souvent_hash]
```

- Les hashs ne peuvent pas être inversés – c'est pourquoi nous avons besoin de
  fournir le vocabulaire partagé

```python
# Génère une erreur si nous n'avons pas déjà vu la chaine avant
string = nlp.vocab.strings[821433950267086228]
```

Notes: spaCy stocke toutes les données partagées dans un vocabulaire, le Vocab.

Il inclut les mots, mais aussi les schémas de nommage pour les étiquettes et les
labels.

Pour économiser de l'espace mémoire, toutes les chaines sont encodées en ID sous
forme de hashs. Si un mot est présent plus d'une fois, nous n'avons pas besoin
de l'enregistrer à chaque fois.

Au lieu de cela, spaCy utilise une fonction de hachage pour générer un ID et ne
stocke qu'une seule fois la chaine dans le magasin de chaines. Le magasin de
chaines est accessible avec `nlp.vocab.strings`.

C'est une table de consultation qui fonctionne dans les deux sens. Tu peux
chercher une chaine et obtenir son hash, et chercher un hash pour obtenir la
valeur de chaine correspondante. En interne, spaCy communique uniquement avec
des ID de hashs.

Les ID de hashs ne peuvent toutefois pas être inversés. Si un mot n'est pas dans
le vocabulaire, il n'y a aucun moyen d'obtenir sa chaine. C'est pourquoi nous
devons toujours fournir le vocabulaire partagé.

---

# Vocabulaire partagé et magasin de chaines (2)

- Recherche de la chaine et du hash dans `nlp.vocab.strings`

```python
doc = nlp("Ines nage souvent")
print("valeur de hash :", nlp.vocab.strings["souvent"])
print("valeur de chaine :", nlp.vocab.strings[821433950267086228])
```

```out
valeur de hash : 821433950267086228
valeur de chaine : souvent
```

- Le `doc` expose aussi le vocabulaire et les chaines

```python
doc = nlp("Ines nage souvent")
print("valeur de hash :", doc.vocab.strings["souvent"])
```

```out
valeur de hash : 821433950267086228
```

Notes: Pour obtenir le hash d'une chaine, nous pouvons le rechercher dans
`nlp.vocab.strings`.

Pour obtenir la représentation en chaine d'un hash, nous pouvons rechercher le
hash.

Un objet `Doc` expose aussi son vocabulaire et les chaines.

---

# Lexèmes : éléments du vocabulaire

- Un objet `Lexeme` est un élément du vocabulaire

```python
doc = nlp("Ines nage souvent")
lexeme = nlp.vocab["souvent"]

# Affiche les attributs lexicaux
print(lexeme.text, lexeme.orth, lexeme.is_alpha)
```

```out
souvent 821433950267086228 True
```

- Contient les informations **indépendantes du contexte** à propos d'un mot
  - Le texte du mot : `lexeme.text` et `lexeme.orth` (le hash)
  - Des attributs lexicaux comme `lexeme.is_alpha`
  - Etiquettes de partie de discours **non** dépendantes du contexte,
    dépendances ou labels d'entités

Notes: Les lexèmes sont des éléments du vocabulaire indépendants du contexte.

Tu peux obtenir un lexème en cherchant une chaine ou un ID de hash dans le
vocabulaire.

Les lexèmes exposent des attributs, tout comme les tokens.

Ils contiennent des informations indépendantes du contexte à propos d'un mot,
comme le texte, ou si le mot est composé de caractères alphabétiques.

Les lexèmes n'ont pas d'étiquettes de partie de discours, de labels d'entités ou
de dépendances. Ceux-ci dépendent du contexte.

---

# Vocabulaire, hashs et lexèmes

<img src="/vocab_stringstore_fr.png" width="70%" alt="Illustration des mots 'Ines', 'nage' et 'souvent' dans le Doc, Vocab et StringStore" />

Notes: Voici un exemple.

Le `Doc` contient les mots dans leur contexte – dans le cas présent, les tokens
"Ines", "nage" et "souvent" avec leurs étiquettes de partie de discours et leurs
dépendances.

Chaque token fait référence à un lexème, qui connait l'ID de hash du mot. Pour
obtenir la représentation en chaine du mot, spaCy recherche le hash dans le
magasin de chaines.

---

# Pratiquons !

Notes: Tout ceci semble un peu abstrait - voyons donc le vocabulaire et le
magasin de chaines en pratique.
