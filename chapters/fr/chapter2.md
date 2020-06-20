---
title: 'Chapitre 2: analyse de données à grande échelle avec spaCy'
description:
  "Dans ce chapitre, tu vas utiliser tes nouvelles compétences pour extraire des
  informations spécifiques à partir de grandes quantités de textes. Tu vas
  apprendre à tirer le meilleur parti des structures de données de spaCy, et
  comment combiner efficacement les approches statistiques et basées sur les
  règles pour l'analyse de textes."
prev: /chapter1
next: /chapter3
type: chapter
id: 2
---

<exercise id="1" title="Structures de données (1)" type="slides,video">

<slides source="chapter2_01_data-structures-1" start="11:06" end="13:37">
</slides>

</exercise>

<exercise id="2" title="Des chaines de caractères aux hashs">

### Partie 1

- Recherche la chaine de caractères "cat" dans `nlp.vocab.strings` pour obtenir
  le hash.
- Recherche le hash pour revenir à la chaine de caractères.

<codeblock id="02_02_01">

- Tu peux utiliser le magasin de chaines de caractères `nlp.vocab.strings` comme
  un dictionnaire Python normal. Par exemple `nlp.vocab.strings["unicorn"]` va
  retourner le hash, et la recherche du hash va retourner la chaine `"unicorn"`.

</codeblock>

### Partie 2

- Recherche l'étiquette de la chaine "PERSON" dans `nlp.vocab.strings` pour
  obtenir le hash.
- Recherche le hash pour revenir à la chaine de caractères.

<codeblock id="02_02_02">

- Tu peux utiliser le magasin de chaines de caractères `nlp.vocab.strings` comme
  un dictionnaire Python normal. Par exemple `nlp.vocab.strings["unicorn"]` va
  retourner le hash, et la recherche du hash va retourner la chaine `"unicorn"`.

</codeblock>

</exercise>

<exercise id="3" title="Vocabulaire, hashs et lexèmes">

Pourquoi ce code génère-t-il une erreur ?

```python
from spacy.lang.en import English
from spacy.lang.de import German

# Crée un objet nlp pour l'anglais et un pour l'allemand
nlp = English()
nlp_de = German()

# Obtient l'ID pour la chaine 'Bowie'
bowie_id = nlp.vocab.strings["Bowie"]
print(bowie_id)

# Recherche l'ID de "Bowie" dans le vocabulaire
print(nlp_de.vocab.strings[bowie_id])
```

<choice>

<opt correct="true" text='La chaine <code>"Bowie"</code> n'est pas présente dans le vocabulaire allemand, donc le hash ne peut pas être trouvé dans le magasin de chaines de caractères.'>

Les hashes ne peuvent pas être inversés. Pour éviter ce problème, ajoute le mot
au nouveau vocabulaire en traitant un texte ou en cherchant la chaine, ou
utilise le même vocabulaire pour résoudre le hash vers une chaine.

</opt>

<opt text='<code>"Bowie"</code> n'est pas un mot normal du dictionnaire en anglais ou en allemand, donc il ne peut pas être hashé.'>

N'importe quelle chaine de caractères peut être convertie en has.

</opt>

<opt text="<code>nlp_de</code> n'est pas un nom valide. Le vocabulaire peut
uniquement être partagé si les objets <code>nlp</code> ont le même nom.">

Le nom de variable `nlp` est seulement une convention. Si le code utilisait le
nom de variable `nlp` au lieu de `nlp_de`, il écraserait l'objet `nlp` existant,
vocabulaire y compris.

</opt>

</choice>

</exercise>

<exercise id="4" title="Structures de données (2)" type="slides,video">

<slides source="chapter2_02_data-structures-2" start="13:475" end="15:47">
</slides>

</exercise>

<exercise id="5" title="Créer un Doc">

Créons quelques objets `Doc` de toutes pièces !

### Partie 1

- Importe le `Doc` depuis `spacy.tokens`.
- Crée un `Doc` à partir des `words` et des `spaces`. N'oublie pas de passer le
  vocabulaire en argument !

<codeblock id="02_05_01">

La classe `Doc` prend 3 arguments : le vocabulaire partagé, généralement
`nlp.vocab`, une liste de `words` et une liste de `spaces`, valeurs booléennes
indiquant si le mot est suivi par un espace ou pas.

</codeblock>

### Partie 2

- Importe le `Doc` depuis `spacy.tokens`.
- Crée un `Doc` à partir des `words` et des `spaces`. N'oublie pas de passer le
  vocabulaire en argument !

<codeblock id="02_05_02">

Inspecte chaque mot du résultat textuel souhaité et vérifie s'il est suivi par
un espace. Si c'est le cas, les valeurs d'espace doivent être `True`. Sinon,
elles doivent être `False`.

</codeblock>

### Partie 3

- Importe le `Doc` depuis `spacy.tokens`.
- Complète les `words` et `spaces` pour correspondre au texte désiré et créer
  un `doc`.

<codeblock id="02_05_03">

Fais attention aux tokens individuels. Pour voir comment spaCy effectue
normalement cette chaine, tu peux essayer d'afficher les tokens pour
`nlp("Oh, really?!")`.

</codeblock>

</exercise>

<exercise id="6" title="Docs, spans et entités en partant de zéro">

Dans cet exercice, tu vas créer les objets `Doc` et `Span` manuellement, et
actualiser les entités nommées – exactement comme spaCy le fait en coulisses. Un
objet `nlp` partagé a déjà été créé.

- Importe les classes `Doc` et `Span` depuis `spacy.tokens`.
- Utilise la classe `Doc` directement pour créer un `doc` à partir des mots et
  des espaces.
- Crée un `Span` pour "David Bowie" à partir du `doc` et assigne-lui le libellé
  `"PERSON"`.
- Remplace `doc.ents` par une liste d'une seule entité, le `span` "David Bowie".

<codeblock id="02_06">

- Le `Doc` est initialisé avec trois arguments : le vocabulaire partagé, par
  exemple `nlp.vocab`, une liste de mots et une liste de valeurs booléenes
  indiquant si le mot doit ou non être suivi par un espace.
- La classe `Span` prend quatre arguments: le `doc` de référence, l'index du
  token de début, l'index du token de fin et un libellé optionnel.
- La propriété `doc.ents` est accessible en écriture, tu peux donc lui assigner
  n'importe quel itérable composé d'objets `Span`.

</codeblock>

</exercise>

<exercise id="7" title="Meilleures pratiques pour les structures de données">

Le code de cet exemple essaie d'analyser un texte et de recueillir tous les noms
propres qui sont suivis par un verbe.

```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Berlin is a nice city")

# Obtient tous les tokens et les étiquettes de partie de discours
token_texts = [token.text for token in doc]
pos_tags = [token.pos_ for token in doc]

for index, pos in enumerate(pos_tags):
    # Vérifie si le token courant est un nom propre
    if pos == "PROPN":
        # Vérifie si le token suivant est un verbe
        if pos_tags[index + 1] == "VERB":
            result = token_texts[index]
            print("Found proper noun before a verb:", result)
```

### Partie 1

Pourquoi le code est-il mauvais ?

<choice>

<opt text="Le token <code>result</code> devrait être reconverti en un objet <code>Token</code>. Cela te permettrait de les réutiliser dans spaCy.">

Il ne sera pas nécessaire de reconvertir les chaines en objets `Token`. Evite
plutôt de convertir les tokens en chaines de caractères si tu as encore besoin
d'accéder à leurs attributs et leurs relations.

</opt>

<opt correct="true" text="Il utilise uniquement des listes de chaines de caractères au lieu des attributs natifs des tokens. C'est souvent moins efficace, et cela ne permet pas d'exprimer des relations complexes.">

Convertis toujours les résultats en chaines le plus tard possible, et essaie
d'utiliser les attributs natifs des tokens pour garder un code cohérent.

</opt>

<opt text='<code>pos_</code> n'est pas le bon attribut pour extraire des noms propres. Tu devrais utiliser <code>tag_</code> et les libellés <code>"NNP"</code> et <code>"NNS"</code> à la place.'>

L'attribut `.pos_` retourne l'étiquetage approximatif de partie de discours et
`"PROPN"` est la bonne étiquette pour chercher des noms propres.

</opt>

</choice>

### Partie 2

- Réécris le code pour utiliser les attributs de tokens natifs au lieu des
  listes `token_texts` et `pos_tags`.
- Boucle sur chaque `token` du `doc` et contrôle son attribut `token.pos_`.
- Utilise `doc[token.i + 1]` pour vérifier le token suivant et son attribut
  `.pos_`.
- Si un nom propre est trouvé devant un verbe, affiche son `token.text`.

<codeblock id="02_07">

- Supprime les `token_texts` et `pos_tags` – on n'a pas besoin de compiler
  d'avance des listes de chaines de caractères !
- Au lieu d'itérer sur les `pos_tags`, boucle sur chaque `token` dans le `doc`
  et vérifie l'attribut `token.pos_`.
- Pour savoir si le token suivant est un verbe, jette un oeil à
  `doc[token.i + 1].pos_`.

</codeblock>

</exercise>

<exercise id="8" title="Vecteurs de mots et similarité sémantique" type="slides,video">

<slides source="chapter2_03_word-vectors-similarity" start="15:58" end="19:47">
</slides>

</exercise>

<exercise id="9" title="Inspecter des vecteurs de mots">

Dans cet exercice, nous utiliserons un
[modèle anglais](https://spacy.io/models/en) plus étendu, qui comporte environ
20.000 vecteurs de mots. Le modèle est déjà pré-installé.

- Charge le modèle moyen avec vecteurs de mots `"en_core_web_md"`.
- Affiche le vecteur pour `"bananas"` en utilisant l'attribut `token.vector`.

<codeblock id="02_09">

- Pour charger un modèle statistique, appelle `spacy.load` avec son nom sous
  forme de chaine de caractères.
- Pour accéder à un token dans un doc, tu peux utiliser son index. Par exemple,
  `doc[4]`.

</codeblock>

</exercise>

<exercise id="10" title="Comparer des similarités">

Dans cet exercice, tu vas utiliser les méthodes `similarity` de spaCy pour
comparer des objets `Doc`, `Token` et `Span` et obtenir leurs scores de
similarité.

### Partie 1

- Utilise la méthode `doc.similarity` pour comparer `doc1` à `doc2` et afficher
  le résultat.

<codeblock id="02_10_01">

La méthode `doc.similarity` prend un argument: l'autre objet auquel l'objet
courant doit être comparé.

</codeblock>

### Partie 2

- Utilise la méthode  `token.similarity` pour comparer `token1` à `token2` et
  afficher le résultat.

<codeblock id="02_10_02">

- La méthode `token.similarity` prend un argument: l'autre objet auquel l'objet
courant doit être comparé.

</codeblock>

### Partie 3

- Crée des spans pour "great restaurant" et "really nice bar".
- Utilise `span.similarity` pour les comparer et afficher le résultat.

<codeblock id="02_10_03"></codeblock>

</exercise>

<exercise id="11" title="Combiner modèles et règles" type="slides,video">

<slides source="chapter2_04_models-rules" start="19:58" end="23:25">
</slides>

</exercise>

<exercise id="12" title="Débuggons les motifs (1)">

Pourquoi ce motif ne trouve-t-il pas les tokens "Silicon Valley" dans le `doc` ?

```python
pattern = [{"LOWER": "silicon"}, {"TEXT": " "}, {"LOWER": "valley"}]
```

```python
doc = nlp("Can Silicon Valley workers rein in big tech from within?")
```

<choice>

<opt text='Les tokens "Silicon" et "Valley" ne sont pas en minuscules, donc l'attribut <code>"LOWER"</code> ne correspondra pas.'>

L'attribut `"LOWER"` dans le motif décrit des tokens dont la _forme minuscule_
correspond à une valeur donnée. Ainsi `{"LOWER": "valley"}` trouvera les tokens
"Valley", "VALLEY", "valley" etc.

</opt>

<opt correct="true" text='Le tokenizer ne crée pas de tokens pour les espaces simples, donc il n'y pas de token dont la valeur est <code>" "</code> au milieu.'>

Le tokenizer effectue déjà la séparation sur la base des espaces et chaque
dictionnaire du motif contient un token.

</opt>

<opt text='Il manque un opérateur <code>"OP"</code> aux tokens pour indiquer qu'ils devraient être trouvés exactement une fois.'>

Par défaut, tous les tokens décrits dans un motif doivent être trouvés
exactement une fois. Les opérateurs sont nécessaires uniquement pour modifier ce
comportement – par exemple, pour trouver zéro ou plusieurs fois un token.

</opt>

</choice>

</exercise>

<exercise id="13" title="Débuggons les motifs (2)">

Les deux motifs de cet exercice comportent des erreurs et ne vont pas
fonctionner comme souhaité. Peux-tu les corriger ? Si tu es bloqué, essaie
d'afficher les tokens du `doc` pour voir comment le texte sera séparé et ajuster
les motifs pour que chaque dictionnaire représente un token.

- Édite `pattern1` pour qu'il trouve correctement toutes les mentions quelle que
  soit la casse pour `"Amazon"` suivi d'un nom propre commençant par une
  majuscule.
- Édite `pattern2` pour qu'il trouve correctement toutes les mentions quelle que
  soit la casse de `"ad-free"`, et d'un nom à la suite.

<codeblock id="02_13">

- Essaie de traiter les chaines qui devraient être trouvées par l'objet `nlp` –
  par exemple `[token.text for token in nlp("ad-free viewing")]`.
- Inspecte les tokens et vérifie que chaque dictionnaire du motif décrit
  correctement un seul token.

</codeblock>

</exercise>

<exercise id="14" title="Efficient phrase matching">

Parfois il est plus efficace de rechercher des chaines de caractères exactes au
lieu d'écrire des motifs décrivant individuellement les tokens. C'est
particulièrement vrai pour les catégories finies - comme l'ensemble des pays du
monde. Nous disposons déjà d'une liste de pays, alors utilisons-là comme base
pour notre script d'extraction d'informations. Une liste de chaines est
caractères est accessible par la variable `COUNTRIES`.

- Importe le `PhraseMatcher` et initialise-le avec le `vocab` partagé dans la
  variable `matcher`.
- Ajoute les motifs de phrase et appelle le matcher sur le `doc`.

<codeblock id="02_14">

Le `vocab` partagé est accessible avec `nlp.vocab`.

</codeblock>

</exercise>

<exercise id="15" title="Extraire des pays et des relations">

Dans l'exercice précédent, tu as écrit un script utilisant le `PhraseMatcher` de
spaCy pour trouver des noms de pays dans un texte. Nous allons maintenant
l'utiliser sur un texte plus long, analyser la syntaxe et mettre à jour les
entités du document avec les pays trouvés.

- Itère sur les correspondances et crée un `Span` avec l'étiquette `"GPE"`
  (entité géopolitique).
- Mets à jour les entités dans `doc.ents` en y ajoutant les spans trouvés.
- Obtiens la tête du token racine du span trouvé.
- Affiche le texte de la tête et le span.

<codeblock id="02_15">

- Rappelle-toi que le texte est disponible avec la variable `text`.
- Le otken racine du span est accessible avec `span.root`. La tête d'un token
  est accessible avec l'attribut `token.head`.

</codeblock>

</exercise>
