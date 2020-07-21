---
type: slides
---

# Traitements de textes en pipelines

Notes: Bienvenue à nouveau ! Ce chapitre est consacré aux pipelines : une série
de fonctions appliquée à un doc pour ajouter des attributs comme les étiquettes
de partie de discours, les relations de dépendances ou les entités nommées.

Dans cette leçon, tu vas découvrir les composants de pipeline fournis par spaCy,
et ce qui se passe en coulisses quand tu appelles nlp sur un texte sous forme de
chaine de caractères.

---

# Que se passe-t-il quand tu appelles nlp ?

<img src="/pipeline.png" alt="Illustration du pipeline de spaCy pipeline transformant un texte en Doc traité" width="90%" />

```python
doc = nlp("Ceci est une phrase.")
```

Notes: Tu l'as déjà fait de nombreuses fois maintenant : passer une chaine de
caractères à l'objet `nlp`, et recevoir un objet `Doc`.

Mais que fait _vraiment_ l'objet `nlp` ?

D'abord, le tokenizer est appliqué pour transformer la chaine en un objet `Doc`.
Ensuite, un ensemble de composants du pipeline est appliqué dans l'ordre au doc.
Dans le cas présent, le tagger, ensuite le parser, puis l'entity recognizer.
Finalement, le document traité est retourné pour que tu puisses travailler avec.

---

# Composants intégrés au pipeline

| Nom         | Description             | Crée                                                      |
| ----------- | :---------------------- | :-------------------------------------------------------- |
| **tagger**  | Part-of-speech tagger   | `Token.tag`, `Token.pos`                                  |
| **parser**  | Dependency parser       | `Token.dep`, `Token.head`, `Doc.sents`, `Doc.noun_chunks` |
| **ner**     | Named entity recognizer | `Doc.ents`, `Token.ent_iob`, `Token.ent_type`             |
| **textcat** | Text classifier         | `Doc.cats`                                                |

Notes: spaCy est fourni avec les composants intégrés suivants.

Le part-of-speech tagger définit les attributs `token.tag` et `token.pos`.

Le dependency parser ajoute les attributs `token.dep` et `token.head` et est
également chargé de détecter les phrases et les groupes nominaux, également
appelés "noun chunks".

Le named entity recognizer ajoute les entités détectées à la propriété
`doc.ents`. Il définit aussi les attributs de type d'entité sur les tokens qui
indiquent si un token fait partie ou non d'une entité.

Enfin, le text classifier définit les labels de catégories qui s'appliquent à
l'ensemble du texte, et les ajoute à la propriété `doc.cats`.

Comme les catégories de textes sont toujours très spécifiques, le text
classifier n'est pas inclus par défaut dans les modèles pré-entrainés. Mais tu
peux l'utiliser pour entrainer ton propre système.

---

# Sous le capot

<img src="/package_meta_fr.png" alt="Illustration d'un package nommé fr_core_news_sm, de dossiers, fichiers et du meta.json" />

- L'ordre du pipeline est défini dans le `meta.json` du modèle
- Les composants intégrés ont besoin de données binaires pour effectuer des
  prédictions

Notes: Tous les modèles que tu peux charger dans spaCy comportent plusieurs
fichiers et un `meta.json`.

Le meta définit des éléments tels que la langue et le pipeline. Cela indique à
spaCy quels composants instancier.

Les composants intégrés qui effectuent des prédictions ont également besoin de
données binaires. Les données sont incluses dans le package de modèle et
chargées dans le composant quand tu charges le modèle.

---

# Attributs de pipeline

- `nlp.pipe_names`: liste de noms des composants du pipeline

```python
print(nlp.pipe_names)
```

```out
['tagger', 'parser', 'ner']
```

- `nlp.pipeline`: liste de tuples `(name, component)`

```python
print(nlp.pipeline)
```

```out
[('tagger', <spacy.pipeline.Tagger>),
 ('parser', <spacy.pipeline.DependencyParser>),
 ('ner', <spacy.pipeline.EntityRecognizer>)]
```

Notes: Pour voir les noms des composants de pipeline présents dans l'objet nlp
courant, tu peux utiliser l'attribut `nlp.pipe_names`.

Pour la liste des tuples de noms et fonctions des composants, tu peux utiliser
l'attribut `nlp.pipeline`.

Les fonctions des composants sont les fonctions appliquées au doc pour le
traiter et définir les attributs - par exemple étiquetage de partie de discours
ou entités nommées.

---

# Pratiquons !

Notes: Voyons maintenant quelques pipelines spaCy et jetons un oeil sous le
capot !
