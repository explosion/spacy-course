---
title: 'Chapitre 1 : Recherche de mots, phrases, noms et concepts'
description:
  "Ce chapitre te présente les bases du traitement de texte avec spaCy.
  Tu vas découvrir les structures de données, comment utiliser les modèles
  statistiques, et comment les employer pour prédire des caractéristiques
  linguistiques dans ton texte."
prev: null
next: /chapter2
type: chapter
id: 1
---

<exercise id="1" title="Présentation de spaCy" type="slides,video">

<slides source="chapter1_01_introduction-to-spacy" start="0:165" end="3:01">
</slides>

</exercise>

<exercise id="2" title="Prise en main">

Commençons à utiliser spaCy ! Dans cet exercice, tu vas pouvoir essayer quelques
uns des 55+ [langages disponibles](https://spacy.io/usage/models#languages).

### Partie 1 : Anglais

- Importe la classe `English` depuis `spacy.lang.en` et crée l'objet `nlp`.
- Crée un `doc` et affiche son texte.

<codeblock id="01_02_01"></codeblock>

### Partie 2 : Allemand

- Importe la classe `German` depuis `spacy.lang.de` et crée l'objet `nlp`.
- Crée un `doc` et affiche son texte.

<codeblock id="01_02_02"></codeblock>

### Partie 3 : Espagnol

- Importe la classe `Spanish` depuis `spacy.lang.es` et crée l'objet `nlp`.
- Crée un `doc` et affiche son texte.

<codeblock id="01_02_03"></codeblock>

</exercise>

<exercise id="3" title="Documents, spans et tokens">

Quand tu passes une chaine de caractères à un objet `nlp`, spaCy commence par
découper le texte en tokens et crée un objet document. Dans cet exercice, tu
vas en apprendre davantage sur le `Doc`, ainsi que sur ses vues `Token` et
`Span`.

### Étape 1

- Importe la classe de langue `English` et crée l'objet `nlp`.
- Traite le texte et crée un objet `Doc` affecté à une variable `doc`.
- Sélectionne le premier token du `Doc` et affiche son attribut `text`.

<codeblock id="01_03_01">

Tu peux utiliser les indices dans un `Doc` comme dans une liste Python. Par
exemple, `doc[4]` désigne le token à l'indice 4, qui est le cinquième token
dans le texte. N'oublie pas qu'en Python le premier indice est 0, et pas 1.

</codeblock>

### Étape 2

- Importe la classe de langue `English` et crée l'objet `nlp`.
- Traite le texte et crée un objet `Doc` affecté à une variable `doc`.
- Crée les portions du `Doc` pour les tokens "tree kangaroos" et "tree
  kangaroos and narwhals".

<codeblock id="01_03_02">

La création d'une portion d'un `Doc` s'effectue exactement comme pour la
portion d'une liste en Python en utilisant la notation `:`. N'oublie pas que
l'indice du dernier token est _exclu_ – par exemple, `0:4` désigne les tokens à
partir de 0 _jusqu'au_ token 4, mais sans inclure le token 4.

</codeblock>

</exercise>

<exercise id="4" title="Attributs lexicaux">

Dans cet exemple, tu vas utiliser les objets `Doc` et `Token` de spaCy, et les
attributs lexicaux pour trouver des pourcentages dans un texte. Tu vas chercher
deux tokens consécutifs : un nombre et un symbole pourcentage.

- Utilise l'attribut `like_num` pour vérifier si un token du `doc` ressemble à
  un nombre.
- Obtiens le token _suivant_ le token courant dans le document. L'indice du
  token suivant dans le `doc` est `token.i + 1`.
- Vérifie si l'attribut `text` du token suivant est un symbole "%".

<codeblock id="01_04">

Pour obtenir le token situé à un indice, tu peux utiliser la notation indicielle
sur le `doc`. Par exemple, `doc[5]` est le token situé à l'indice 5.

</codeblock>

</exercise>

<exercise id="5" title="Modèles statistiques" type="slides,video">

<slides source="chapter1_02_statistical-models" start="3:12" end="7:01">
</slides>

</exercise>

<exercise id="6" title="Paquets de modèles" type="choice">

Qu'est-ce qui **n'est pas** inclus dans un paquet de modèle et que tu peux
charger dans spaCy ?

<choice>
<opt text="Un fichier de métadonnées contenant le langage, le pipeline et la licence.">

Tous les modèles comportent un `meta.json` qui définit la langue à initialiser,
les noms des composants de pipeline à charger ainsi que des méta-informations
générales comme le nom du modèle, sa version, la licence, les sources de
données, l'auteur et la justesse des données (si disponibles).

</opt>
<opt text="Des poids binaires pour effectuer des prédictions statistiques.">

Les modèles incluent des poids binaires pour prédire les annotations
linguistiques comme l'étiquetage de partie du discours, les relations de
dépendance ou les entités nommées.

</opt>
<opt correct="true" text="Les données annotées sur lesquelles le modèle a été entrainé.">

Les modèles statistiques permettent de généraliser à partir d'un jeu de données
d'apprentissage. Une fois entrainés, ils utilisent les poids binaires pour
effectuer des prédictions. Il n'est donc pas nécessaire de les fournir avec
leurs données d'apprentissage.

</opt>
<opt text="Les Strings du vocabulaire du modèle et leurs hashs.">

Les paquets de modèles contiennent un `strings.json` qui stocke les entrées de
vocabulaire du modèle et la correspondance avec leurs hashs. Cela permet à
spaCy de communiquer uniquement en hashes et de chercher la chaine
correspondante si nécessaire.

</opt>
</choice>

</exercise>

<exercise id="7" title="Chargement de modèles">

Les modèles que nous utilisons dans ce cours sont déjà pré-installés. Pour plus
d'informations sur les modèles statistiques de spaCy et la manière de les
installer sur ta machine, consulte [la documentation](https://spacy.io/usage/models).

- Utilise `spacy.load` pour charger le petit modèle anglais `"en_core_web_sm"`.
- Traite le texte et affiche le texte du document.

<codeblock id="01_07">

Pour charger un modèle, appelle `spacy.load` avec la chaine de caractères qui
le désigne. Les noms des modèles diffèrent selon les langues et les données sur
lesquelles ils ont été entrainés - donc fais attention à utiliser le bon nom.

</codeblock>

</exercise>

<exercise id="8" title="Prédiction d'attributs linguistiques">

Tu vas maintenant pouvoir essayer un des paquets de modèles pré-entrainés de
spaCy et le voir effectuer des prédictions. N'hésite pas à le tester avec ton
propre texte ! Pour savoir ce que signifie une étiquette ou un label, tu peux
appeler `spacy.explain` dans la boucle. Par exemple :
`spacy.explain("PROPN")` ou `spacy.explain("GPE")`.

### Partie 1

- Traite le texte avec l'objet `nlp` et crée un `doc`.
- Pour chaque token, affiche le texte du token, le `.pos_` du token
  (étiquette de partie du discours) et le `.dep_` du token (relation de
  dépendance).

<codeblock id="01_08_01">

Pour créer un `doc`, appelle l'objet `nlp` avec une chaine de caractères en
argument. Rappelle-toi que tu dois utiliser les noms d'attributs avec un
tiret bas pour obtenir les valeurs de la chaine.

</codeblock>

### Partie 2

- Traite le texte et crée un objet `doc`.
- Itère sur les `doc.ents` et affiche le texte de l'entité et son attribut
  `label_`.

<codeblock id="01_08_02">

Pour créer un `doc`, appelle l'objet `nlp` avec une chaine de caractères en
argument. Rappelle-toi que tu dois utiliser les noms d'attributs avec un
tiret bas pour obtenir les valeurs de la chaine.

</codeblock>

</exercise>

<exercise id="9" title="Prédiction d'entités nommées dans le contexte">

Les modèles statistiques ne sont pas _toujours_ exacts. La justesse de leurs
prédictions dépend du jeu de données d'apprentissage et du texte que tu traites.
Voyons cela avec un exemple.

- Traite le texte avec l'objet `nlp`.
- Itère sur les entités et affiche le texte et le label de chaque entité.
- Il semble que le modèle n'a pas prédit correctement "iPhone X". Crée un span
  manuellement pour ces tokens.

<codeblock id="01_09">

- Pour créer un `doc`, appelle l'objet `nlp` sur le texte. Les entités nommées
  sont accessibles avec l'attribut `doc.ents`.
- La manière la plus facile de créer un objet `Span` object est d'utiliser la
  notation par portion – par exemple `doc[5:10]` pour le token depuis la
  position 5 _jusqu'à_ la position 10. N'oublie pas que la dernière position
  d'indice du token n'est pas incluse.

</codeblock>

</exercise>

<exercise id="10" title="Correspondances avec des règles" type="slides,video">

<slides source="chapter1_03_rule-based-matching" start="7:118" end="10:55">
</slides>

</exercise>

<exercise id="11" title="Utilisation du Matcher">

Essayons le `Matcher` de spaCy basé sur des règles. Tu vas utiliser l'exemple
de l'exercice précédent et écrire un motif pour trouver la phrase "iPhone X"
dans le texte.

- Importe le `Matcher` depuis `spacy.matcher`.
- Initialise-le avec le `vocab` partagé de l'objet `nlp`.
- Crée un motif qui corresponde avec les valeurs de `"TEXT"` de deux tokens :
  `"iPhone"` et `"X"`.
- Utilise la méthode `matcher.add` pour ajouter le motif au matcher.
- Appelle le matcher sur le `doc` et affecte le résultat à la variable
  `matches`.
- Itère sur les correspondances et obtiens les spans correspondants depuis
  l'indice `start` jusqu'à l'indice `end`.

<codeblock id="01_11">

- Le vocabulaire partagé est accessible avec l'attribut `nlp.vocab`.
- Un motif est une liste de dictionnaires dont les clés sont des noms
  d'attributs. Par exemple, `[{"TEXT": "Hello"}]` recherchera un token dont le
  texte exact est "Hello".
- Les valeurs `start` et `end` de chaque correspondance indiquent les indices de
  début et de fin du span trouvé. Pour obtenir le span, tu peux créer une
  portion du `doc` en utilisant les valeurs fournies de début et de fin.

</codeblock>

</exercise>

<exercise id="12" title="Ecriture de motifs">

Dans cet exercice, tu vas t'entrainer à écrire des motifs de correspondance
plus complexes qui utilisent différents attributs des tokens et des opérateurs.

### Partie 1

- Écris **un** motif qui recherche uniquement les mentions de versions
  _complètes_ d'iOS :
  "iOS 7", "iOS 11" et "iOS 10".

<codeblock id="01_12_01">

- Pour obtenir la correspondance d'un token avec un texte exact, tu peux
  utiliser l'attribut `TEXT`. Par exemple, `{"TEXT": "Apple"}` recherchera
  des tokens dont le texte est exactement "Apple".
- Pour rechercher un token numérique, tu peux utiliser l'attribut `"IS_DIGIT"`,
  qui retournera `True` pour les tokens constitués uniquement de nombres.

</codeblock>

### Partie 2

- Écris **un** motif qui recherche uniquement des formes de "download" (tokens
  avec le lemme "download"), suivies par un token avec l'étiquette de partie
  de discours `"PROPN"` (nom propre).

<codeblock id="01_12_02">

- Pour spécifier un lemme, tu peux utiliser l'attribut `"LEMMA"` dans le motif
  du token.
  Par exemple, `{"LEMMA": "be"}` trouvera des tokens comme "is", "was"
  ou "being".
- Pour trouver des noms propres, tu pourras chercher tous les tokens dont la
  valeur de `"POS"` est `"PROPN"`.

</codeblock>

### Partie 3

- Écris **un** motif qui recherche des adjectifs (`"ADJ"`) suivis par un ou
  deux `"NOUN"` (un nom et un nom optionnel).

<codeblock id="01_12_03">

- Pour trouver des adjectifs, recherche les tokens dont la valeur de `"POS"`
  est `"ADJ"`. Pour des noms, recherche `"NOUN"`.
- Des opérateurs peuvent être ajoutés avec la clé `"OP"` key. Par exemple,
  `"OP": "?"` pour zéro ou une correspondance.

</codeblock>

</exercise>
