---
title: 'Chapitre 3 : Traitements de textes en pipelines'
description:
  "Ce chapitre va te montrer tout ce qu'il y a à savoir à propos du pipeline de
  traitement de spaCy. Tu va apprendre ce qui se passe en coulisses quand tu
  traites un texte, comment écrire tes propres composants et les ajouter au
  pipeline, et comment utiliser des attributs personnalisés et ajouter tes
  propres métadonnées aux documents, aux spans et aux tokens."
prev: /chapter2
next: /chapter4
type: chapter
id: 3
---

<exercise id="1" title="Traitements de textes en pipelines" type="slides">

<slides source="chapter3_01_processing-pipelines" start="23:36" end="26:12">
</slides>

</exercise>

<exercise id="2" title="Que se passe-t-il quand tu appelles nlp?">

Que fait spaCy quand tu appelles `nlp` sur une chaine de caractères ?

```python
doc = nlp("Ceci est une phrase.")
```

<choice>

<opt text="Lance le tagger, le parser l’entity recognizer et enfin le tokenizer.">

Le tokenizer est toujours exécuté _avant_ tous les autres composants du
pipeline, parce qu'il transforme une chaine de caractères en objet `Doc`. De
plus, le pipeline ne doit pas nécessairement inclure le tagger, le parser et
l'entity recognizer.

</opt>

<opt text="Convertit le texte en tokens et applique chaque composant du pipeline dans l’ordre." correct="true">

Le tokenizer transforme une chaine de caractères en un objet `Doc`. spaCy
applique ensuite chaque composant du pipeline, dans l'ordre.

</opt>

<opt text="Se connecte au serveur de spaCy pour calculer et retourner le résultat.">

spaCy calcule tout sur ta machine et n'a pas besoin de se connecter à un
quelconque serveur.

</opt>

<opt text="Initialise la langue, ajoute le pipeline et charge le modèle binaire de poids.">

Quand tu appelles `spacy.load()` pour charger un modèle, spaCy va initialiser la
langue, ajouter le pipeline et charger le modèle binaire de poids. Quand tu
_appelles_ l'objet `nlp` sur un texte, le modèle est déjà chargé.

</opt>

</exercise>

<exercise id="3" title="Inspection du pipeline">

Inspectons le pipeline du petit modèle français !

- Charge le modèle `fr_core_news_sm` et crée l'objet `nlp`.
- Affiche les noms des composants du pipeline avec `nlp.pipe_names`.
- Affiche le pipeline complet de tuples `(name, component)` avec `nlp.pipeline`.

<codeblock id="03_03">

La liste des noms des composants est accessible via l'attribut `nlp.pipe_names`.
Le pipeline complet composé de tuples `(name, component)` est accessible avec
`nlp.pipeline`.

</codeblock>

</exercise>

<exercise id="4" title="Composants de pipeline personnalisés" type="slides">

<slides source="chapter3_02_custom-pipeline-components" start="26:235" end="29:05">
</slides>

</exercise>

<exercise id="5" title="Cas d'usages pour des composants personnalisés">

Lequel de ces problèmes peut être résolu avec des composants de pipeline
personnalisés. Choisis toutes les réponses pertinentes !

1. Actualisation des modèles pré-entrainés pour améliorer leurs prédictions
2. Calcul de nos propres valeurs basées sur les tokens et leurs attributs
3. Ajout d'entités nommées, par exemple basées sur un dictionnaire
4. Implémentation du support de langues supplémentaires

<choice>

<opt text="1 et 2.">

Les composants personnalisés peuvent seulement modifier le `Doc` et ne peuvent
pas être utilisés pour actualiser directement les poids binaires ou d'autres
composants.

</opt>

<opt text="1 et 3.">

Les composants personnalisés peuvent seulement modifier le `Doc` et ne peuvent
pas être utilisés pour actualiser directement les poids binaires ou d'autres
composants.

</opt>

<opt text="1 et 4.">

Les composants personnalisés peuvent seulement modifier le `Doc` et ne peuvent
pas être utilisés pour actualiser directement les poids binaires ou d'autres
composants. De plus quand ils sont ajoutés au pipeline, la classe de langue a
déjà été initialisée, donc ils ne peuvent pas servir à ajouter des langues
supplémentaires.

</opt>

<opt text="2 et 3." correct="true">

Les composants personnalisés sont fantastiques pour ajouter des valeurs
personnalisées aux documents, aux tokens et aux spans, ainsi que pour
personnaliser les `doc.ents`.

</opt>

<opt text="2 et 4.">

Les composants personnalisés sont ajoutés au pipeline après l'initialisation de
la classe de langue et la tokenisation, donc ils ne peuvent pas servir à ajouter
des langues supplémentaires.

</opt>

<opt text="3 et 4.">

Les composants personnalisés sont ajoutés au pipeline après l'initialisation de
la classe de langue et la tokenisation, donc ils ne peuvent pas servir à ajouter
des langues supplémentaires.

</opt>

</choice>

</exercise>

<exercise id="6" title="Composants simples">

L'exemple montre un composant personnalisé qui affiche la longueur des tokens
d'un document. Peux-tu le compléter ?

- Complète la fonction du composant avec la longueur du `doc`.
- Ajoute `length_component` au pipeline existant en tant que **premier**
  composant.
- Essaie le nouveau pipeline en traitant un texte quelconque avec l'objet `nlp`–
  par exemple "Ceci est une phrase.".

<codeblock id="03_06">

- Pour obtenir la longueur d'un objet `Doc`, tu peux appeler la fonction native
  `len()` de Python avec le `Doc` en argument.
- Utilise la méthode `nlp.add_pipe` pour ajouter le composant au pipeline.
  N'oublie pas de mettre l'argument nommé `first` à `True` pour t'assurer qu'il
  sera ajouté avant tous les autres composants.
- Pour traiter un texte, appelle l'objet `nlp` avec le texte en argument.

</codeblock>

</exercise>

<exercise id="7" title="Composants complexes">

Dans cet exercice, tu vas écrire un composant personnalisé qui utilise le
`PhraseMatcher` pour trouver des noms d'animaux dans le document et ajouter les
spans correspondants à `doc.ents`. Un `PhraseMatcher` avec les motifs des
animaux a déjà été créé sous le nom de variable `matcher`.

- Définis le composant personnalisé et applique le `matcher` au `doc`.
- Crée un `Span` pour chaque correspondance, assigne-lui l'ID de label pour
  `"ANIMAL"` et actualise le `doc.ents` avec les nouveaux spans.
- Ajoute le nouveau composant au pipeline _après_ le composant `"ner"`.
- Traite le texte puis affiche le texte et le label des entités figurant dans
  `doc.ents`.

<codeblock id="03_07">

- Rappelle-toi que les correspondances sont constituées d'une liste de tuples
  `(match_id, start, end)`.
- La classe `Span` prend 4 arguments : le `doc` parent, l'indice de début,
  l'indice de fin et le label.
- Pour ajouter un composant après un autre, utilise l'argument nommé `after`
  dans `nlp.add_pipe`.

</codeblock>

</exercise>

<exercise id="8" title="Extension d'attributs" type="slides">

<slides source="chapter3_03_extension-attributes" start="29:16" end="32:23">
</slides>

</exercise>

<exercise id="9" title="Configuration d'attributs étendus (1)">

Pratiquons l'extension d'attributs.

### Étape 1

- Utilise `Token.set_extension` pour déclarer `"is_country"` (valeur par défaut
  `False`).
- Mets-le à jour pour `"Suisse"` et affiche-le pour tous les tokens.

<codeblock id="03_09_01">

Rappelle-toi que les attributs étendus sont accessible via la propriété `._`.
Par exemple, `doc._.has_color`.

</codeblock>

### Étape 1

- Utilise `Token.set_extension` pour déclarer `"reversed"` (la fonction getter
  `get_reversed`).
- Affiche sa valeur pour chaque token.

<codeblock id="03_09_02">

Rappelle-toi que les attributs étendus sont accessible via la propriété `._`.
Par exemple, `doc._.has_color`.

</codeblock>

</exercise>

<exercise id="10" title="Configuration d'attributs étendus (2)">

Essayons de définir des attributs plus complexes en utilisant des getters et
des extensions de méthodes.

### Partie 1

- Complète la fonction `get_has_number`.
- Utilise `Doc.set_extension` pour déclarer `"has_number"` (getter
  `get_has_number`) et affiche sa valeur.

<codeblock id="03_10_01">

- Rappelle-toi que les attributs étendus sont accessibles via la propriété `._`.
  Par exemple, `doc._.has_color`.
- La fonction `get_has_number` devrait indiquer si au moins l'un des tokens du
  `doc` retourne `True` pour `token.like_num` (qui indique si le token ressemble
  à un nombre).

</codeblock>

### Partie 2

- Utilise `Span.set_extension` pour déclarer `"to_html"` (méthode `to_html`).
- Appelle-là sur `doc[0:2]` avec la balise `"strong"`.

<codeblock id="03_10_02">

- Les méthodes étendues peuvent accepter un ou plusieurs arguments. Par exemple
  : `doc._.some_method("argument")`.
- Le premier argument passé à la méthode est toujours le `Doc`, le `Token` ou le
  `Span` sur lequel la méthode a été appelée.

</codeblock>

</exercise>

<exercise id="11" title="Entités et extensions">

Dans cet exercice, tu vas combiner l'extension d'attributs personnalisés avec
les prédictions du modèle et créer un accesseur d'attribut qui retourne une URL
de recherche Wikipédia si le span est une personne, une organisation ou un lieu.

- Complète le getter `get_wikipedia_url` pour qu'il retourne une URL uniquement
  si le label du span est dans la liste des labels.
- Définis l'extension de `Span` nommée `"wikipedia_url"` avec le getter
  `get_wikipedia_url`.
- Itère sur les entités du `doc` et affiche leur URL Wikipédia.

<codeblock id="03_11">

- Pour obtenir le label textuel d'un span, utilise l'attribut `span.label_`.
  C'est le label prédit par l'entity recognizer si le span constitue une entité.
- Rappelle-toi que les attributs étendus sont accessibles via la propriété `._`.
  Par exemple, `doc._.has_color`.

</codeblock>

</exercise>

<exercise id="12" title="Composants avec extensions">

Les extensions d'attributs sont particulièrement puissantes quand elles sont
combinées avec des composants de pipeline personnalisés. Dans cet exercice, tu
vas écrire un composant de pipeline qui trouve des noms de pays et une extension
personnalisée qui retourne le nom de la capitale du pays s'il est disponible.

Un matcher de phrases avec tous les pays est proposé via la variable `matcher`.
Un dictionnaire des pays avec leurs capitales en correspondance est proposé via
la variable `CAPITALS`.

- Complète le composant `countries_component` et crée un `Span` avec le label
  `"GPE"` (entité géopolitique) pour toutes les correspondances.
- Ajoute le composant au pipeline.
- Déclare l'extension d'attribut Span nommée `"capital"` avec le getter
  `get_capital`.
- Traite le texte et affiche le texte de l'entité, le label de l'entité, et la
  capitale de l'entité pour chaque span d'entité de `doc.ents`.

<codeblock id="03_12">

- La classe `Span` requiert quatre arguments: le `doc`, les indices de token
  `start` et `end` du span et le `label`.
- L'appel du `PhraseMatcher` sur un `doc` retourne une liste de tuples
  `(match_id, start, end)`.
- Pour déclarer un nouvel attribut étendu, utilise la méthode `set_extension`
  sur la classe globale, c'est-à-dire `Doc`, `Token` ou `Span`. Pour définir un
  getter, utilise l'argument nommé `getter`.
- Rappelle-toi que les attributs étendus sont accessibles via la propriété
  `._.`. Par exemple, `doc._.has_color`.

</codeblock>

</exercise>

<exercise id="13" title="Scalabilité et performance" type="slides">

<slides source="chapter3_04_scaling-performance" start="32:335" end="34:515">
</slides>

</exercise>

<exercise id="14" title="Traitement de flux">

Dans cet exercice, tu vas utiliser `nlp.pipe` pour un traitement plus efficace
du texte. L'objet `nlp` a déjà été créé pour toi. Une liste de tweets à propos
d'une chaine américaine connue de fast-food est disponible via la variable
nommée `TEXTS`.

### Partie 1

- Réécris l'exemple pour utiliser `nlp.pipe`. Au lieu d'itérer sur les textes et
  de les traiter, itère sur les objets `doc` générés par `nlp.pipe`.

<codeblock id="03_14_01">

- L'utilisation de `nlp.pipe` te permet de fusionner les deux premières lignes
  de code en une seule.
- `nlp.pipe` prend `TEXTS` en argument et génère des objets `doc` sur lesquels
  tu peux boucler.

</codeblock>

### Partie 2

- Réécris l'exemple pour utiliser `nlp.pipe`. N'oublie pas d'appeler `list()`
  sur le résultat pour le transformer en liste.

<codeblock id="03_14_02"></codeblock>

### Partie 3

- Réécris l'exemple pour utiliser `nlp.pipe`. N'oublie pas d'appeler `list()`
  sur le résultat pour le transformer en liste.

<codeblock id="03_14_03"></codeblock>

</exercise>

<exercise id="15" title="Traitement de données avec contexte">

Dans cet exercice, tu vas utiliser les attributs personnalisés pour ajouter aux
citations des métadonnées sur l'auteur et le livre correspondants.

Une liste d'exemples sous la forme `[text, context]` est disponible via la
variable `DATA`. Les textes sont des citations de livres célèbres, et les
contextes sont des dictionnaires avec pour clés `"author"` et `"book"`.

- Utilise la méthode `set_extension` pour déclarer les attributs personnalisés
  `"author"` et `"book"` sur le `Doc`, avec `None` comme valeur par défaut.
- Traite les paires `[text, context]` contenues dans `DATA` en utilisant
  `nlp.pipe` avec `as_tuples=True`.
- Réécris `doc._.book` et `doc._.author` avec les valeurs respectives
  d'informations obtenues avec le contexte.

<codeblock id="03_15">

- La méthode `Doc.set_extension` prend deux arguments : le nom de l'attribut
  sous forme de chaine, et un argument nommé indiquant la valeur par défaut, le
  getter, le setter, ou la méthode. Par exemple, `default=True`.
- Quand `as_tuples` est mis à `True`, la méthode `nlp.pipe` prend en argument
  une liste de tuples `(text, context)` et génère des tuples `(doc, context)`.

</codeblock>

</exercise>

<exercise id="16" title="Traitement sélectif">

Dans cet exercice, tu vas utiliser les méthodes `nlp.make_doc` et
`nlp.disable_pipes` pour appliquer uniquement les composants sélectionnés lors
du traitement d'un texte.

### Partie 1

- Réécris le code en utilisant `nlp.make_doc` pour uniquement tokeniser le
  texte.

<codeblock id="03_16_01">

La méthode `nlp.make_doc` peut être appelée sur un texte et retourne un `Doc`,
exactement comme l'objet `nlp`.

</codeblock>

### Partie 2

- Désactive le tagger et le parser en utilisant la méthode `nlp.disable_pipes`.
- Traite le texte et affiche toutes les entités contenues dans le `doc`.

<codeblock id="03_16_02">

La méthode `nlp.disable_pipes` prend un nombre variable d'arguments : le nom
sous forme de chaine de caractères des composants du pipeline à désactiver. Par
exemple, `nlp.disable_pipes("ner")` désactivera le named entity recognizer.

</codeblock>

</exercise>
