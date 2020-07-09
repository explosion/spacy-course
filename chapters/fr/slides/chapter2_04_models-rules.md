---
type: slides
---

# Combinaison de modèles et de règles

Notes: La combinaison de modèles statistiques avec des systèmes basés sur des
règles est l'un des trucs les plus importants à avoir dans ta boite à outils de
NLP.

Dans cette leçon, tu vas apprendre comment le faire avec spaCy.

---

# Modèles statistiques vs. règles

|                              | **Modèles statistiques**                                                           | **Systèmes basés sur des règles** |
| ---------------------------- | ---------------------------------------------------------------------------------- | --------------------------------- |
| **Cas d'usage**              | l'application doit _généraliser_ à partir d'exemples                               |                                   |
| **Exemples du monde réel**   | noms de produits, noms de personnes, relations sujets/objets                       |                                   |
| **Fonctionnalités de spaCy** | reconnaissance d'entités, analyse de dépendances, étiquetage de partie de discours |                                   |

Notes: Les modèles statistiques sont utiles si ton application a besoin d'être
capable de généraliser à partir de quelques exemples.

Par exemple, un modèle statistique est avantageux pour détecter des noms de
personnes ou de produits. Au lieu de fournir une liste avec tous les noms de
personnes possibles, ton application sera capable de prédire si un span de
tokens est un nom de personne. De la même manière, tu peux prédire les
dépendances syntaxiques pour trouver les relations sujet/objet.

Pour ce faire, tu utiliserais les fonctionnalités de reconnaissance d'entités,
d'analyse de dépendances ou d'étiquetage de partie de discours de spaCy.

---

# Prédictions statistiques vs. règles

|                              | **Modèles statistiques**                                                           | **Systèmes basés sur des règles**                           |
| ---------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **Cas d'usage**              | l'application doit _généraliser_ à partir d'exemples                               | dictionnaire avec un nombre fini d'exemples                 |
| **Exemples du monde réel**   | noms de produits, noms de personnes, relations sujets/objets                       | pays du monde, villes, noms de médicaments, races de chiens |
| **Fonctionnalités de spaCy** | reconnaissance d'entités, analyse de dépendances, étiquetage de partie de discours | tokenizer, `Matcher`, `PhraseMatcher`                       |

Notes: les approches basées sur des règles sont en revanche pratiques quand il y
a un nombre plus ou moins limité d'éléments que tu veux trouver. Par exemple,
tous les pays ou toutes les villes du monde, des noms de médicaments ou encore
des races de chiens.

Dans spaCy, tu peux réaliser cela avec des règles de tokenisation
personnalisées, ainsi qu'avec le matcher et le matcher de phrases.

---

# Résumé : Recherche de motifs sur la base de règles

```python
# Initialise avec le vocabulaire partagé
from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)

# Les motifs sont des listes de dictionnaires décrivant les tokens
pattern = [{"LEMMA": "aime", "POS": "VERB"}, {"LOWER": "les"}, {"LOWER": "chats"}]
matcher.add("AIME_CHATS", None, pattern)

# Les opérateurs peuvent spécifier combien de fois un token doit être trouvé
pattern = [{"TEXT": "très", "OP": "+"}, {"TEXT": "heureux"}]
matcher.add("TRES_HEUREUX", None, pattern)

# L'appel du matcher sur le doc retourne une liste de tuples
# composés avec (match_id, début, fin)
doc = nlp("J'aime les chats et je suis très très heureux")
matches = matcher(doc)
```

Notes: Dans le chapitre précédent, tu as appris comment utiliser le matcher à
base de règles de spaCy pour trouver des motifs complexes dans tes textes. Voici
un rapide résumé.

Le matcher est initialisé avec le vocabulaire partagé - habituellement
`nlp.vocab`.

Les motifs sont des listes de dictionnaires, et chaque dictionnaire décrit un
token et ses attributs. Les motifs peuvent être ajoutés au matcher avec la
méthode `matcher.add`.

Les opérateurs te permettent de spécifier combien de fois il faut trouver un
token donné. Par exemple, "+" le recherchera une ou plusieurs fois.

L'appel du matcher sur un objet doc retournera une liste de correspondances.
Chaque correspondance est un tuple composé d'un ID, et des indices des tokens de
début et de fin dans le document.

---

# Ajout de prédictions statistiques

```python
matcher = Matcher(nlp.vocab)
matcher.add("CHIEN", None, [{"LOWER": "bouvier"}, {"LOWER": "bernois"}])
doc = nlp("J'ai un Bouvier bernois")

for match_id, start, end in matcher(doc):
    span = doc[start:end]
    print("Span en correspondance :", span.text)
    # Obtiens le token racine du span et le token de tête de la racine
    print("Token racine :", span.root.text)
    print("Token de tête de la racine :", span.root.head.text)
    # Obtiens le token précédent et son étiquette de partie de discours
    print("Token précédent :", doc[start - 1].text, doc[start - 1].pos_)
```

```out
Span en correspondance : Bouvier bernois
Token racine : Bouvier
Token de tête de la racine : ai
Token précédent : un DET
```

Notes: Voici un exemple de règle de matcher pour "golden retriever".

Si nous itérons sur les correspondances retournées par le matcher, nous pouvons
obtenir l'identifiant de la correspondance, ainsi que les indices de début et de
fin du span en correspondance. Nous pouvons ensuite obtenir plus d'informations
sur lui. Les objets `Span` nous donnent accès au document original et à tous les
autres attributs des tokens et fonctionnalités linguistiques prédites par le
modèle.

Par exemple, nous pouvons obtenir le token racine du span. Si le span est
composé de plus d'un token, ce sera le token qui décide la catégorie de la
phrase. Par exemple, la racine de "Bouvier bernois" est "Bouvier". Nous
pouvons aussi trouver la tête de la racine. C'est le "parent" syntaxique qui
commande la phrase - dans le cas présent, le verbe "avoir".

Enfin, nous pouvons inspecter le token précédent et ses attributs. Ici c'est un
déterminant, l'article "un".

---

# Recherche efficace de motifs (1)

- le `PhraseMatcher` est comme les expressions régulières ou la recherche par
  mot-clé – mais avec l'accès aux tokens !
- Accepte des objets `Doc` en motifs
- Plus efficace et rapide que le `Matcher`
- Parfait pour rechercher de grandes listes de mots

Notes: Le matcheur de phrase est un autre outil très utile pour trouver des
séquences de mots dans tes données.

Il effectue une recherche de mot-clé sur le document, mais au lieu de seulement
trouver des chaines de caractères, il te fournit un accès direct aux tokens dans
leur contexte.

Il prend des objets `Doc` comme motifs.

Il est aussi très rapide.

Cela le rend très utile pour trouver de grands dictionnaires et listes de mots
sur de grands volumes de texte.

---

# Recherche efficace de motifs (2)

```python
from spacy.matcher import PhraseMatcher

matcher = PhraseMatcher(nlp.vocab)

pattern = nlp("Bouvier bernois")
matcher.add("CHIEN", None, pattern)
doc = nlp("J'ai un Bouvier bernois")

# Itère sur les correspondances
for match_id, start, end in matcher(doc):
    # Obtiens le span en correspondance
    span = doc[start:end]
    print("Span en correspondance :", span.text)
```

```out
Span en correspondance : Bouvier bernois
```

Notes: Ceci est un exemple.

Le matcheur de phrase peut être importé à partir de `spacy.matcher` et suit la
même API que le matcheur normal.

Au lieu d'une liste de dictionnaires, on lui passe un objet `Doc` comme motif.

On peut ensuite itérer sur les correspondances dans le texte, et obtenir l'ID de
la correspondance, et le début et la fin de la portion en correspondance. Ceci
nous permet de créer un objet `Span` pour les tokens correspondant à "Bouvier
bernois" afin de les analyser dans leur contexte.

---

# Pratiquons !

Notes: Essayons quelques-unes des nouvelles techniques pour combiner les règles
avec les modèles statistiques.
