---
title: "Chapitre 4 : Entrainement d'un modèle de réseau de neurones"
description:
  "Dans ce chapitre, tu vas apprendre comment actualiser les modèles
  statistiques de spaCy afin de les personnaliser pour tes cas d'utilisation -
  par exemple, pour prédire un nouveau type d'entité pour des commentaires en
  ligne. Tu vas écrire ta propre boucle d'apprentissage en partant de zéro, et
  comprendre les bases de l'apprentissage, ainsi que des trucs et astuces pour
  mieux réussir tes projets de NLP sur mesure."
prev: /chapter3
next: null
type: chapter
id: 4
---

<exercise id="1" title="Apprentissage et actualisation des modèles" type="slides">

<slides source="chapter4_01_training-updating-models" start="35:02" end="38:495">
</slides>

</exercise>

<exercise id="2" title="Objectif de l'apprentissage">

Bien que spaCy comporte une série de modèles pré-entrainés pour prédire des
annotations linguistiques, tu voudras presque _toujours_ le perfectionner avec
plus d'exemples. Tu peux le faire en les entrainant avec davantage de données
étiquetées.

Qu'est-ce que l'apprentissage n'améliore **pas** ?

<choice>

<opt text="Le perfectionnement du modèle sur tes données.">

Si un modèle pré-entrainé ne donne pas de bons résultats sur tes données,
l'entrainer avec davantage d'exemples est souvent une bonne solution.

</opt>

<opt text="L’apprentissage de nouveaux schémas de classification.">

Tu peux utiliser l'apprentissage pour apprendre au modèle de nouveaux labels, de
nouveaux types d'entités ou d'autres schémas de classification.

</opt>

<opt text="La découverte de motifs sur des données non labellisées." correct="true">

Les composants de spaCy sont des modèles supervisés pour l'annotation de texte,
ce qui signifie qu'ils peuvent seulement apprendre à reproduire des exemples,
mais pas deviner de nouveaux labels à partir de texte brut.

</opt>

</choice>

</exercise>

<exercise id="3" title="Création de données d'apprentissage (1)">

Le `Matcher` basé sur les règles de spaCy est un excellent moyen pour créer
rapidement des données d'apprentissage pour les modèles d'entités nommées. Une
liste de phrases est accessible via la variable `TEXTS`. Tu peux l'imprimer pour
l'inspecter. Nous voulons trouver toutes les mentions de différents modèles
d'iPhone, donc nous allons créer des données d'entrainement pour apprendre à
notre modèle à les reconnaitre en tant que `"GADGET"`.

- Écris un motif pour deux tokens dont la forme en minuscules correspond à
  `"iphone"` et `"x"`.
- Écris un motif pour deux tokens : un token dont la forme en minuscules
  correspond à `"iphone"` et un chiffre.

<codeblock id="04_03">

- Pour trouver les formes minuscules d'un token, tu peux utiliser l'attribut
  `"LOWER"`. Par exemple : `{"LOWER": "apple"}`.
- Pour trouver un token numérique, tu peux utiliser le marqueur `"IS_DIGIT"`.
  Par exemple : `{"IS_DIGIT": True}`.

</codeblock>

</exercise>

<exercise id="4" title="Création de données d'apprentissage (2)">

Utilisons les motifs de correspondance que nous avons créé dans l'exercice
précédent pour améliorer un ensemble d'exemples d'apprentissage. Une liste de
phrases est accessible via la variable `TEXTS`.

- Crée un objet doc pour chaque texte en utilisant `nlp.pipe`.
- Trouve les correspondances sur le `doc` et crée une liste des spans qui
  correspondent.
- Obtiens les tuples `(start character, end character, label)` des spans qui
  correspondent.
- Formate chaque exemple en tuple avec le texte et un dictionnaire qui fait
  correspondre la clé `"entities"` aux tuples d'entités.
- Ajoute l'exemple au `TRAINING_DATA` et inspecte les données affichées.

<codeblock id="04_04">

- Pour trouver les correspondances, appelle le `matcher` sur un `doc`.
- Les correspondances retournées sont des tuples `(match_id, start, end)`.
- Pour ajouter un exemple à la liste des exemples d'apprentissage, tu peux
  utiliser `TRAINING_DATA.append()`.

</codeblock>

</exercise>

<exercise id="5" title="La boucle d'apprentissage" type="slides">

<slides source="chapter4_02_training-loop" start="39:00" end="42:25">
</slides>

</exercise>

<exercise id="6" title="Définition du pipeline">

Dans cet exercice, tu vas préparer un pipeline spaCy pour entrainer l'entity
recognizer à reconnaitre des entités `"GADGET"` dans un texte – par exemple,
"iPhone X".

- Crée un modèle vide `"fr"`, par exemple avec la méthode `spacy.blank`.
- Crée un nouvel entity recognizer en utilisant `nlp.create_pipe` et ajoute-le
  au pipeline.
- Ajoute le nouveau label `"GADGET"` à l'entity recognizer en utilisant la
  méthode `add_label` sur le composant de pipeline.

<codeblock id="04_06">

- Pour créer un entity recognizer vide, tu peux appeler `nlp.create_pipe` avec
  la chaine `"ner"`.
- Pour ajouter le composant au pipeline, utilise la méthode `nlp.add_pipe`.
- La méthode `add_label` est une méthode du composant de pipeline entity
  recognizer, stocké dans la variable `ner`. Pour lui ajouter un label, tu peux
  appeler `ner.add_label` avec la chaine de caractères du label, par exemple
  `ner.add_label("SOME_LABEL")`.

</codeblock>

</exercise>

<exercise id="7" title="Construction d'une boucle d'apprentissage">

Ecrivons une boucle simple d'apprentissage à partir de zéro !

Le pipeline que tu as créé dans l'exercice précédent est disponible en tant
qu'objet `nlp`. Il contient déjà l'entity recognizer avec le label ajouté
`"GADGET"`.

Le petit jeu d'exemples labellisés que tu as créé précédemment est disponible en
tant que `TRAINING_DATA`. Pour voir les exemples, tu peux les imprimer dans ton
script.

- Appelle `nlp.begin_training`, crée une boucle d'apprentissage pour 10
  itérations et mélange les données d'apprentissage.
- Crée des lots de données d'apprentissage avec `spacy.util.minibatch` et itère
  sur les lots.
- Convertis les tuples `(text, annotations)` en listes de `texts` et
  `annotations`.
- Pour chaque lot, utilise `nlp.update` pour actualiser le modèle avec les
  textes et les annotations.

<codeblock id="04_07">

- Pour commencer l'apprentissage et réinitialiser les poids, appelle la méthode
  `nlp.begin_training()`.
- Pour diviser les données d'apprentissage divide en lots, appelle la fonction
  `spacy.util.minibatch` sur la liste des exemples d'apprentissage.

</codeblock>

</exercise>

<exercise id="8" title="Exploration du modèle">

Voyons comment le modèle se comporte sur des données inconnues ! Pour accélérer
un peu les choses, nous avons déjà fait tourner un modèle entrainé pour le label
`"GADGET"` sur du texte. Voici certains des résultats :

| Text                                                                                                              | Entities               |
| ----------------------------------------------------------------------------------------------------------------- | ---------------------- |
| Apple ralentit l'iPhone 8 et l'iPhone X - comment arrêter ça                                                      | `(iPhone 8, iPhone X)` |
| J'ai enfin compris à quoi servait l'encoche sur l'iPhone X                                                                                                                   | `(iPhone X,)`          |
| Tout ce que vous devez savoir à propos du Samsung Galaxy S9                                                                                                                  | `(Samsung Galaxy,)`    |
| Vous voulez comparer les modèles d'iPad ? Voici comment se présente la gamme 2020                                                                                                                | `(iPad,)`              |
| L'iPhone 8 et l'iPhone 8 Plus sont des smartphones conçus, développés et vendus by Apple                          | `(iPhone 8, iPhone 8)` |
| quel est l'ipad le moins cher, parmi les ipad pro ???                                                                                                                 | `(ipad, ipad)`         |
| Les Samsung Galaxy sont une série d'appareils informatiques mobiles  conçus, fabriqués et vendus par Samsung Electronics                                                                                                         | `(Samsung Galaxy,)`    |

Parmi toutes les entités présentes dans les textes, **combien le modèle en
a-t-il identifiées correctement** ? Rappelle-toi que que les spans d'entités
incomplets comptent aussi comme des erreurs ! Astuce : Compte le nombre
d'entités que le modèle _aurait dû_ prédire. Ensuite compte le nombre d'entités
qu'il a _effectivement_ prédites correctement et divise-le par le nombre total
d'entités correctes.

<choice>

<opt text="45%">

Essaie de compter le nombre d'entités correctement prédites et divise-le par le
nombre total d'entités correctes que le modèle _aurait dû_ prédire.

</opt>

<opt text="60%">

Essaie de compter le nombre d'entités correctement prédites et divise-le par le
nombre total d'entités correctes que le modèle _aurait dû_ prédire.

</opt>

<opt text="70%" correct="true">

Sur nos données de test, le modèle a atteint une justesse de 70 %.

</opt>

<opt text="90%">

Essaie de compter le nombre d'entités correctement prédites et divise-le par le
nombre total d'entités correctes que le modèle _aurait dû_ prédire.

</opt>

</choice>

</exercise>

<exercise id="9" title="Meilleures pratiques d'apprentissage" type="slides">

<slides source="chapter4_03_training-best-practices" start="42:36" end="44:55">
</slides>

</exercise>

<exercise id="10" title="Bonnes données vs. mauvaises données">

Voici un extrait d'un jeu d'apprentissage qui labellise le type d'entité
`TOURIST_DESTINATION` dans des évaluations de voyageurs.

```python
TRAINING_DATA = [
    (
        "je suis allé à amsterdem l'an dernier et les canaux étaient magnifiques",
        {"entities": [(15, 24, "TOURIST_DESTINATION")]},
    ),
    (
        "Tu devrais visiter Paris au moins une fois dans ta vie, mais la Tour Eiffel ce n'est pas terrible",
        {"entities": [(19, 24, "TOURIST_DESTINATION")]},
    ),
    ("There's also a Paris in Arkansas, lol", {"entities": []}),
    (
        "Berlin est la destination parfaite pour les vacances d'été : beaucoup de parcs, une vie nocturne trépidante et de la bière pas chère !",
        {"entities": [(0, 6, "TOURIST_DESTINATION")]},
    ),
]
```

### Partie 1

Pourquoi ces données et ce schéma d'étiquetage sont-ils problématiques ?

<choice>

<opt text="Déterminer si un lieu est une destination touristique est un jugement subjectif et pas une catégorie certaine. Ce sera très difficile à apprendre pour l’entity recognizer." correct="true">

Il serait bien plus judicieux de labelliser uniquement avec le label `"GPE"`
(entité géopolitique) ou `"LOCATION"` (lieu) et ensuite d'utiliser un système à
base de règles pour déterminer si l'entité est ou non une destination
touristique dans ce contexte. Par exemple, tu pourrais recouper les types
d'entités avec une base de connaissances ou les chercher dans un wiki de voyage.

</opt>

<opt text="Paris devrait être aussi labellisé comme destination touristique par cohérence. Sinon le modèle sera induit en erreur.">

Même s'il est possible que Paris, AK soit aussi une attraction touristique, cela
ne fait que souligner à quel point le schéma de labellisation est subjectif et à
quel point il sera difficile de décider si le label s'applique ou non. De ce
fait, cette distinction sera très difficile à apprendre pour l'entity
recognizer.

</opt>

<opt text="Les mots rares hors-vocabulaire comme le 'amsterdem' mal orthographié ne devraient pas être labellisés comme entités.">

Même des mots très peu communs ou des mots mal orthographiés peuvent être
labellisés comme entités. En fait, la capacité à prédire des catégories sur des
textes mal orthographiés en se basant sur le contexte est l'un des principaux
avantages des reconnaissances statistiques d'entités nommées.

</opt>

</choice>

### Partie 2

- Réécris le `TRAINING_DATA` pour utiliser uniquement le label `"GPE"` (villes,
  états, pays) au lieu de `"TOURIST_DESTINATION"`.
- N'oublie pas d'ajouter les tuples pour les entités `"GPE"` qui n'avaient pas
  été labellisées dans les anciennes données.

<codeblock id="04_10">

- Pour les spans qui sont déjà labellisés, tu as juste à changer le nom du label
  de `"TOURIST_DESTINATION"` en `"GPE"`.
- Un texte comporte une ville et un état qui ne sont pas encore labellisés. Pour
  ajouter les spans des entités, compte les caractères pour trouver où commence
  et où finit le span. Ensuite ajoute les tuples `(start, end, label)` aux
  entités.

</codeblock>

</exercise>

<exercise id="11" title="Apprentissage avec plusieurs labels">

Voici un petit échantillon d'un jeu de données créé pour entrainer un nouveau
type d'entité `"WEBSITE"`. Le jeu de données original contient quelques milliers
de phrases. Dans cet exercice, tu vas effectuer la labellisation à la main. En
situation réelle, tu l'automatiserais probablement en utilisant un outil
d'annotations - par exemple, [Brat](http://brat.nlplab.org/), une solution
open-source populaire, ou [Prodigy](https://prodi.gy), notre propre outil
d'annotations qui s'intègre avec spaCy.

### Partie 1

- Complète les positions des entités `"WEBSITE"` dans les données. Tu peux
  utiliser `len()` si tu ne veux pas compter les caractères.

<codeblock id="04_11_01">

- Les positions de début et de fin d'un span d'entité sont les positions des
  caractères dans le texte. Par exemple, si une entité commence à la position 5,
  sa position de départ est `5`. N'oublie pas que les positions de fin sont
  _exclues_ - donc `10` signifie _jusqu'au_ caractère 10.

</codeblock>

### Partie 2

Un modèle a été entrainé avec les données que tu viens d'étiqueter, plus
quelques milliers d'autres exemples. Après l'apprentissage, il fait de
l'excellent travail sur `"WEBSITE"`, mais ne reconnait plus `"PERSON"`. A quoi
cela pourrait-il être dû ?

<choice>

<opt text='Il est très difficile pour le modèle d’apprendre plusieurs catégories comme <code>"PERSON"</code> et <code>"WEBSITE"</code>.'>

Il est parfaitement possible pour un modèle d'apprendre des catégories très
différentes. Par exemple, le modèle anglais pré-entrainé de spaCy est capable de
reconnaitre des personnes, mais aussi des organisations ou des pourcentages.

</opt>

<opt text='Les données d’apprentissage ne comportaient aucun exemple de <code>"PERSON"</code>, donc le modèle a appris que ce label est incorrect.' correct="true">

Si des entités `"PERSON"` sont présentes dans les données d'apprentissage mais
ne sont pas labellisées, le modèle va apprendre qu'elles ne doivent pas être
prédites. De même, si un type d'entité existante n'est pas présent dans les
données d'apprentissage, le modèle peut les \"oublier\" et arrêter de les
prédire.

</opt>

<opt text="Les hyperparamètres doivent être réglés à nouveau pour que les deux types d’entités puissent être reconnus.">

Si les hyperparamètres peuvent influer sur la justesse d'un modèle, ils ne sont
probablement pas le problème ici.

</opt>

</choice>

### Partie 3

- Actualise les données d'apprentissage pour inclure des annotations pour les
  entités `"PERSON"` "PewDiePie" et "Alexis Ohanian".

<codeblock id="04_11_02">

- Pour ajouter d'autres entités, ajoute un autre tuple `(start, end, label)` à
  la liste.

</codeblock>

</exercise>

<exercise id="12" title="Résumé" type="slides">

<slides source="chapter4_04_wrapping-up" start="45:01" end="47:195">
</slides>

</exercise>
