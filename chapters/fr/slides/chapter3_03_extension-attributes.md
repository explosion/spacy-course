---
type: slides
---

# Attributs étendus

Notes: Dans cette leçon, tu vas apprendre comment ajouter des attributs
personnalisés aux objets `Doc`, `Token` et `Span` pour stocker des données
personnalisées.

---

# Définition d'attributs personnalisés

- Ajoute des métadonnées personnalisées aux documents, tokens et spans
- Accessible via la propriété `._`

```python
doc._.title = "Mon document"
token._.is_color = True
span._.has_color = False
```

- Déclaré sur les classes globales `Doc`, `Token` ou `Span` en utilisant la
méthode `set_extension`

```python
# Importe les classes globales
from spacy.tokens import Doc, Token, Span

# Définit des extensions sur Doc, Token et Span
Doc.set_extension("title", default=None)
Token.set_extension("is_color", default=False)
Span.set_extension("has_color", default=False)
```

Notes: Les attributs personnalisés te permettent d'ajouter n'importe quelle
métadonnée aux docs, tokens et spans. Les données peuvent être ajoutées
ponctuellement, ou peuvent être calculées dynamiquement.

Les attributs personnalisés sont accessibles via la propriété `._` (point tiret
bas). Cela indique clairement qu'ils ont été ajoutés par l'utilisateur, et
qu'ils ne sont pas natifs à spaCy, comme `token.text`.

Les attributs doivent être déclarés sur les classes globales `Doc`, `Token` et
`Span` que tu peux importer à partir de `spacy.tokens`. Tu as déjà travaillé
avec dans les chapitres précédents. Pour déclarer un attribut personnalisé sur
`Doc`, `Token` et `Span`, tu peux utiliser la méthode `set_extension`.

Le premier argument est le nom de l'attribut. Les arguments nommés te permettent
de définir comment la valeur doit être calculée. Dans le cas présent, elle a une
valeur par défaut et peut être modifiée.

---

# Types d'attributs étendus

1. Extensions d'attributs
2. Extensions de propriétés
3. Extensions de méthodes

Notes: Ce sont trois types d'extensions : extensions d'attributs, extensions de
propriétés et extensions de méthodes.

---

# Extensions d'attributs

- Définit une valeur par défaut qui peut être modifiée

```python
from spacy.tokens import Token

# Définit l'extension sur le Token avec une valeur par défaut
Token.set_extension("is_color", default=False)

doc = nlp("Le ciel est bleu.")

# Modifie la valeur de l'attribut étendu
doc[3]._.is_color = True
```

Notes: Les attributs étendus définissent une valeur par défaut qui peut être
modifiée.

Par exemple, un attribut personnalisé `is_color` sur le token possédant une
valeur par défaut définie à `False`.

Sur des tokens individuels, sa valeur peut être modifiée en la remplaçant – dans
le cas présent, True pour le token "bleu".

---

# Extensions de propriétés (1)

- Définit une fonction getter et une fonction optionnelle setter
- Le getter n'est appelé que quand tu _récupères_ la valeur de l'attribut

```python
from spacy.tokens import Token

# Définit la fonction getter
def get_is_color(token):
    colors = ["rouge", "jaune", "bleu"]
    return token.text in colors

# Définit l'extension de Token avec le getter
Token.set_extension("is_color", getter=get_is_color)

doc = nlp("Le ciel est bleu.")
print(doc[3]._.is_color, "-", doc[3].text)
```

```out
Vrai - bleu
```

Notes: Les extensions de propriétés fonctionnent comme les propriétés en Python
: elles peuvent définir une fonction getter et une fonction optionnelle setter.

La fonction getter est appelée uniquement quand tu récupères l'attribut. Cela
permet de calculer la valeur dynamiquement, et même de prendre en compte
d'autres attributs personnalisés.

Les fonctions getter prennent un argument : l'objet, dans le cas présent, le
token. Dans cet exemple, la fonction indique en retour si le texte du token
figure dans notre liste de couleurs.

Nous pouvons ensuite fournir la fonction via l'argument nommé `getter` quand
nous déclarons l'extension.

Le token "blue" retourne maintenant `True` pour `._.is_color`.

---

# Extensions de propriétés (2)

- Les extensions de `Span` devraient presque toujours utiliser un getter

```python
from spacy.tokens import Span

# Définit la fonction getter
def get_has_color(span):
    colors = ["rouge", "jaune", "bleu"]
    return any(token.text in colors for token in span)

# Définit l'extension de Span avec le getter
Span.set_extension("has_color", getter=get_has_color)

doc = nlp("Le ciel est bleu.")
print(doc[1:4]._.has_color, "-", doc[1:4].text)
print(doc[0:2]._.has_color, "-", doc[0:2].text)
```

```out
True - ciel est bleu
False - Le ciel
```

Notes: Si tu veux définir des attributs étendus sur un span, tu voudras presque
toujours utiliser une extension de propriété avec un getter. Sinon, tu serais
obligé d'actualiser _tous les spans possibles_ à la main pour définir toutes les
valeurs.

Dans cet exemple, la fonction `get_has_color` prend en argument le span et
indique en retour si le texte d'un de ses tokens figure dans la liste des
couleurs.

Après avoir traité le doc, nous pouvons vérifier différentes portions du doc et
la propriété personnalisée `._.has_color` indique en retour si le span contient
ou pas une couleur.

---

# Extensions de méthodes

- Assigne une **fonction** qui devient accessible en tant que méthode de l'objet
- Te permet de passer des **arguments** à la fonction d'extension

```python
from spacy.tokens import Doc

# Définit la méthode avec des arguments
def has_token(doc, token_text):
    in_doc = token_text in [token.text for token in doc]
    return in_doc

# Définit l'extension du Doc avec la méthode
Doc.set_extension("has_token", method=has_token)

doc = nlp("Le ciel est bleu.")
print(doc._.has_token("bleu"), "- bleu")
print(doc._.has_token("nuage"), "- nuage")
```

```out
True - bleu
False - nuage
```

Notes: Les extensions de méthodes te permettent d'obtenir une extension
d'attribut sous forme de méthode appelable.

Tu peux ensuite lui passer un ou plusieurs arguments, et calculer dynamiquement
des valeurs d'attributs - par exemple, basées sur une configuration ou un
argument particuliers.

Dans cet exemple, la méthode vérifie si le doc contient un token avec un texte
donné. Le premier argument de la méthode est toujours l'objet lui-même – dans le
cas présent, le doc. Il est passé automatiquement quand la méthode est appelée.
Tous les autres arguments de la fonction seront des arguments de la méthode
étendue. Dans le cas présent, `token_text`.

Ici, la méthode personnalisée `._.has_token` retourne `True` pour le mot "bleu"
et `False` pour le mot "nuage".

---

# Pratiquons !

Notes: Maintenant c'est à toi. Ajoutons quelques extensions personnalisées !
