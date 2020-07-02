---
type: slides
---

# Structures de données (2) : Doc, Span et Token

Notes: Maintenant que tu sais tout sur le vocabulaire et le magasin de chaines,
nous pouvons examiner de plus près les structures de données les plus
importantes : le `Doc`, ainsi que ses vues `Token` et `Span`.

---

# L'objet Doc

```python
# Crée un objet nlp
from spacy.lang.en import English
nlp = English()

# Importe la classe Doc
from spacy.tokens import Doc

# Les mots et les espaces à partir desquels créer le doc
words = ["Hello", "world", "!"]
spaces = [True, False, False]

# Crée un doc manuellement
doc = Doc(nlp.vocab, words=words, spaces=spaces)
```

Notes: Le `Doc` est une des structures de données centrales de spaCy. Il est
créé automatiquement quand tu traites un texte avec l'objet `nlp`. Mais tu peux
aussi instancier la classe manuellement.

Après avoir créé l'objet `nlp`, nous pouvons importer la classe `Doc` à partir
de `spacy.tokens`.

Ici nous créons un doc à partir de trois mots. Les espaces sont une liste de
valeurs booléennes indiquant si le mot est suivi ou non par un espace. Chaque
token inclut cette information - même le dernier !

La classe `Doc` requiert trois arguments : le vocabulaire partagé, les mots et
les espaces.

---

# L'objet Span (1)

<img src="/span_indices.png" width="65%" alt="Illustration d'un objet Span au sein d'un Doc avec les indices des tokens" />

Notes: Un `Span` est une portion d'un document composé d'un ou de plusieurs
tokens. Le `Span` requiert trois arguments : le doc auquel il fait référence, et
les indices de début et de fin du span. N'oublie pas que l'indice de fin est
exclu !

---

# L'objet Span (2)

```python
# Importe les classes Doc et Span
from spacy.tokens import Doc, Span

# Les mots et les espaces à partir desquels créer le doc
words = ["Hello", "world", "!"]
spaces = [True, False, False]

# Crée un doc manuellement
doc = Doc(nlp.vocab, words=words, spaces=spaces)

# Crée un span manuellement
span = Span(doc, 0, 2)

# Crée un span avec un label
span_with_label = Span(doc, 0, 2, label="GREETING")

# Ajoute le span à doc.ents
doc.ents = [span_with_label]
```

Notes: pour créer un `Span` manuellement, nous pouvons aussi importer la classe
à partir de `spacy.tokens`. Nous pouvons ensuite l'instancier avec le doc et les
indices de début et de fin du span, ainsi qu'avec un label optionnel.

Les `doc.ents` sont modifiables, donc nous pouvons ajouter manuellement des
entités en les remplaçant par une liste de spans.

---

# Meilleures pratiques

- `Doc` et `Span` sont très puissants et contiennent les références et les
  relations entre les mots et les phrases
  - **Convertis les résultats en chaines le plus tard possible**
  - **Utilise les attributs des tokens quand ils existent** – par exemple,
    `token.i` pour l'indice du token
- N'oublie pas de passer en argument le `vocab` partagé

Notes: Quelques trucs et astuces avant de commencer :

Les `Doc` et `Span` sont très puissants et sont optimisés pour la performance.
Ils te donnent accès à toutes les références et les relations entre les mots et
les phrases.

Si ton application a besoin de produire des chaines de caractères, fais en sorte
de convertir le doc le plus tard possible. Si tu le fais trop tôt, tu perdras
toutes les relations entre les tokens.

Pour être cohérent, fais en sorte d'utiliser les attributs natifs des tokens
chaque fois que c'est possible. Par exemple, `token.i` pour l'indice du token.

Aussi, n'oublie pas de toujours passer en argument le vocabulaire partagé !

---

# Pratiquons !

Notes: Maintenant essayons cela en créant quelques docs et spans en partant de
zéro.
