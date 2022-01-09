---
title: "Chapitre 4 : Entraînement d'un modèle de réseau de neurones"
description:
  "Dans ce chapitre, tu vas apprendre comment actualiser les modèles
  statistiques de spaCy afin de les personnaliser pour tes cas d'utilisation -
  par exemple, pour prédire un nouveau type d'entité pour des commentaires en
  ligne. Tu vas entraîner ton propre modèle en partant de zéro, et comprendre
  les bases de l'apprentissage, ainsi que des trucs et astuces pour mieux
  réussir tes projets de NLP sur mesure."
prev: /chapter3
next: null
type: chapter
id: 4
---

<exercise id="1" title="Entraînement et actualisation des modèles" type="slides">

<slides source="chapter4_01_training-updating-models">
</slides>

</exercise>

<exercise id="2" title="Données d'entraînement et d'évaluation">

Pour entraîner un modèle, tu as généralement besoin de données d'entraînement
_et_ de données pour l'évaluation. A quoi servent les données d'évaluation ?

<choice>

<opt text="À fournir davantage d'exemples d'entraînement de secours si les données d'entraînement ne sont pas suffisantes.">

Pendant l'entraînement, le modèle est actualisé uniquement à partir des données
d'entraînement. Les données de développement sont utilisées pour évaluer le
modèle en comparant ses prédictions sur des exemples qu'il n'a pas rencontrés
avec les bonnes annotations. C'est ce que reflète le score de précision.

</opt>

<opt text="À vérifier les prédictions sur des exemples inédits et à calculer le score de précision." correct="true">

Les données de développement sont utilisées pour évaluer le modèle en comparant
ses prédictions sur des exemples qu'il n'a pas rencontrés avec les bonnes
annotations. C'est ce que reflète le score de précision.

</opt>

<opt text="À définir des exemples d'entraînement sans annotations.">

Les données de développement sont utilisées pour évaluer le modèle en comparant
ses prédictions sur des exemples qu'il n'a pas rencontrés avec les bonnes
annotations. C'est ce que reflète le score de précision.

</opt>

</choice>

</exercise>

<exercise id="3" title="Création de données d'entraînement (1)">

Le `Matcher` basé sur les règles de spaCy est un excellent moyen pour créer
rapidement des données d'entraînement pour les modèles d'entités nommées. Une
liste de phrases est accessible via la variable `TEXTS`. Tu peux l'imprimer pour
l'inspecter. Nous voulons trouver toutes les mentions de différents modèles
d'iPhone, donc nous allons créer des données d'entraînement pour apprendre à
notre modèle à les reconnaître en tant que `"GADGET"`.

- Écris un motif pour deux tokens dont la forme en minuscules correspond à
  `"iphone"` et `"x"`.
- Écris un motif pour deux tokens : un token dont la forme en minuscules
  correspond à `"iphone"` et un nombre.

<codeblock id="04_03">

- Pour trouver les formes minuscules d'un token, tu peux utiliser l'attribut
  `"LOWER"`. Par exemple : `{"LOWER": "apple"}`.
- Pour trouver un token numérique, tu peux utiliser le marqueur `"IS_DIGIT"`.
  Par exemple : `{"IS_DIGIT": True}`.

</codeblock>

</exercise>

<exercise id="4" title="Création de données d'entraînement (2)">

Après avoir créé les données pour notre corpus, nous devons les sauvegarder
dans un fichier `.spacy`. Le code de l'exemple précédent est déjà fourni.

- Instancie le `DocBin` avec la liste des `docs`.
- Sauve le `DocBin` dans un fichier appelé `train.spacy`.

<codeblock id="04_04">

- Tu peux initialiser le `DocBin` avec une liste de documents en les passant
  via l'argument nommé `docs`.
- La méthode `to_disk` de `DocBin` prend un argument : le chemin du fichier
  dans lequel sauver les données binaires. N'oublie pas d'utiliser l'extension
  de fichier `.spacy`.

</codeblock>

</exercise>

<exercise id="5" title="Configuration et exécution de l'entraînement" type="slides">

<slides source="chapter4_02_running-training">
</slides>

</exercise>

<exercise id="6" title="La configuration d'entraînement">

Le fichier `config.cfg` est la "source unique de vérité" pour entraîner un
pipeline avec spaCy. Laquelle des affirmations suivantes n'est **pas vraie** à
propos du fichier de configuration ?

<choice>

<opt text="Il te permet de configurer le processus d'entraînement et les hyperparamètres.">

Le fichier de configuration comprend tous les paramètres pour le processus
d'entraînement, y compris les hyperparamètres.

</opt>

<opt text="Il aide à rendre ton entraînement plus reproductible.">

Parce que le fichier de configuration comprend _tous_ les paramètres et aucune
valeur par défaut cachée, il peut contribuer à rendre tes expérimentations
d'entraînement plus reproductibles, et d'autres pourront re-jouer tes
expérimentations avec exactement les mêmes paramètres.

</opt>

<opt text="Il crée un package Python installable avec ton pipeline." correct="true">

Le fichier de configuration comprend tous les paramètres liés à l'entraînement
et à l'établissement du pipeline, mais il n'empaquette pas ton pipeline. Pour
créer un package Python installable, tu dois utiliser la commande
`spacy package`.

</opt>

<opt text="Il définit les composants du pipeline et leurs paramètres.">

Le bloc `[components]` du fichier de configuration comprend tous les composants
de pipeline et leurs paramètres, y compris les implémentations de modèles
utilisées.

</opt>

</choice> 

</exercise>

<exercise id="7" title="Génération d'un fichier de configuration">

La [commande `init config`](https://spacy.io/api/cli#init-config) auto-génère
un fichier de configuration avec les paramètres par défaut. Nous voulons
entraîner un reconnaisseur d'entités nommées, donc nous allons générer un
fichier de configuration pour un composant de pipeline, `ner`. Comme nous
exécutons la commande dans un environnement Jupyter pour ce cours, nous
utilisons le préfixe `!`. Si tu exécutes la commande dans ton terminal local,
tu n'as pas besoin d'inclure ce préfixe.

## Partie 1

- Utilise la commande `init config` de spaCy pour auto-générer une
  configuration pour un pipeline français.
- Sauve la configuration dans un fichier `config.cfg`.
- Utilise l'argument `--pipeline` pour spécifier un composant de pipeline,
  `ner`

<codeblock id="04_07_01">

- L'argument `--lang` définit la classe de langue, par ex. `fr` pour le
  français

</codeblock>

## Partie 2

Jetons un oeil à la configuration spaCy générée à l'instant ! Tu peux lancer la
commande ci-dessous pour faire afficher la configuration dans le terminal et
l'inspecter.

<codeblock id="04_07_02"></codeblock>

</exercise>

<exercise id="8" title="Utilisation de la ligne de commande d'entraînement">

Utilisons le fichier de configuration généré dans l'exercice précédent et le
corpus d'entraînement que nous avons créé pour entraîner un reconnaisseur
d'entités nommées !

La commande [`train`](https://spacy.io/api/cli#train) te permet d'entraîner un
modèle à partir d'un fichier de configuration. Un fichier `config_gadget.cfg`
est déjà présent dans le répertoire `exercises/fr`, ainsi qu'un fichier
`train_gadget.spacy` contenant les exemples d'entraînement et un fichier
`dev_gadget.spacy` contenant les exemples d'évaluation. Parce que nous
exécutons la commande dans un environnement Jupyter pour ce cours, nous
utilisons le préfixe `!`. Si tu exécutes la commande dans ton terminal local,
tu n'as pas besoin d'inclure ce préfixe.

- Exécute la commande `train` avec le fichier `exercises/fr/config_gadget.cfg`
- Sauve le pipeline dans un répertoire `output`
- Spécifie les chemins `exercises/fr/train_gadget.spacy` et
  `exercises/fr/dev_gadget.spacy`

<codeblock id="04_08">

- Le premier argument de la commande `spacy train` est le chemin vers le
  fichier de configuration.

</codeblock>

</exercise>

<exercise id="9" title="Exploration du modèle">

Voyons comment le modèle se comporte sur des données inconnues ! Pour accélérer
un peu les choses, nous avons déjà fait tourner un modèle entraîné pour le label
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

Sur nos données de test, le modèle a atteint une précision de 70 %.

</opt>

<opt text="90%">

Essaie de compter le nombre d'entités correctement prédites et divise-le par le
nombre total d'entités correctes que le modèle _aurait dû_ prédire.

</opt>

</choice>

</exercise>

<exercise id="10" title="Meilleures pratiques d'entraînement" type="slides">

<slides source="chapter4_03_training-best-practices" start="42:36" end="44:55">
</slides>

</exercise>

<exercise id="11" title="Bonnes données, mauvaises données">

Voici un extrait d'un jeu d'entraînement qui labellise le type d'entité
`DESTINATION_TOURISTIQUE` dans des évaluations de voyageurs.

```python
doc1 = nlp("je suis allé à amsterdem l'an dernier et les canaux étaient magnifiques")
doc1.ents = [Span(doc1, 4, 5, label="DESTINATION_TOURISTIQUE")]

doc2 = nlp("Tu devrais visiter Paris au moins une fois dans ta vie, "
    "mais la Tour Eiffel ce n'est pas terrible")
doc2.ents = [Span(doc2, 3, 4, label="DESTINATION_TOURISTIQUE")]

doc3 = nlp("Il y a aussi un Paris dans l'Arkansas, lol")
doc3.ents = []

doc4 = nlp("Berlin est la destination parfaite pour les vacances d'été : "
    "beaucoup de parcs, une vie nocturne trépidante et de la bière pas chère !")
doc4.ents = [Span(doc4, 0, 1, label="DESTINATION_TOURISTIQUE")]
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

- Réécris le `doc.ents` pour utiliser uniquement des spans avec le label
  `"GPE"` (villes, états, pays) au lieu de `"DESTINATION_TOURISTIQUE"`.
- N'oublie pas d'ajouter les spans pour les entités `"GPE"` qui n'avaient pas
  été labellisées dans les anciennes données.

<codeblock id="04_11">

- Pour les spans qui sont déjà labellisés, tu as juste à changer le nom du label
  de `"DESTINATION_TOURISTIQUE"` en `"GPE"`.
- Un texte comporte une ville et un état qui ne sont pas encore labellisés. Pour
  ajouter les spans des entités, compte les tokens pour trouver où commence
  et où finit le span. N'oublie pas que le dernier token est _exclu_. Ensuite
  ajoute un nouveau `Span` à `doc.ents`.
- Garde un oeil sur la tokenisation ! Affiche les tokens du `Doc` si tu n'es pas
  sûr.
  

</codeblock>

</exercise>

<exercise id="12" title="Entraînement avec plusieurs labels">

Voici un petit échantillon d'un jeu de données créé pour entraîner un nouveau
type d'entité `"SITE_WEB"`. Le jeu de données original contient quelques milliers
de phrases. Dans cet exercice, tu vas effectuer la labellisation à la main. En
situation réelle, tu l'automatiserais probablement en utilisant un outil
d'annotations - par exemple, [Brat](http://brat.nlplab.org/), une solution
open-source populaire, ou [Prodigy](https://prodi.gy), notre propre outil
d'annotations qui s'intègre avec spaCy.

### Partie 1

- Complète les positions des tokens pour les entités `"SITE_WEB"` dans les
  données.

<codeblock id="04_12_01">

- Rappelle-toi que la position du token de fin d'un span est exclue. Donc une
  entité qui commence au token 2 et qui s'arrête au token 3 aura un début à `2`
  et une fin à `4`.

</codeblock>

### Partie 2

Un modèle a été entraîné avec les données que tu viens d'étiqueter, plus
quelques milliers d'autres exemples. Après l'entraînement, il fait de
l'excellent travail sur `"SITE_WEB"`, mais ne reconnaît plus `"PER"`. À quoi
cela pourrait-il être dû ?

<choice>

<opt text='Il est très difficile pour le modèle d’apprendre plusieurs catégories comme <code>"PER"</code> et <code>"SITE_WEB"</code>.'>

Il est parfaitement possible pour un modèle d'apprendre des catégories très
différentes. Par exemple, le modèle anglais pré-entraîné de spaCy est capable de
reconnaître des personnes, mais aussi des organisations ou des pourcentages.

</opt>

<opt text='Les données entraînement ne comportaient aucun exemple de <code>"PER"</code>, donc le modèle a appris que ce label est incorrect.' correct="true">

Si des entités `"PER"` sont présentes dans les données d'entraînement mais
ne sont pas labellisées, le modèle va apprendre qu'elles ne doivent pas être
prédites. De même, si un type d'entité existante n'est pas présent dans les
données d'entraînement, le modèle peut les \"oublier\" et arrêter de les
prédire.

</opt>

<opt text="Les hyperparamètres doivent être réglés à nouveau pour que les deux types d’entités puissent être reconnus.">

Si les hyperparamètres peuvent influer sur la précision d'un modèle, ils ne
sont probablement pas le problème ici.

</opt>

</choice>

### Partie 3

- Actualise les données d'entraînement pour inclure des annotations pour les
  entités `"PER"` "PewDiePie" et "Alexis Ohanian".

<codeblock id="04_12_02">

- Pour ajouter d'autres entités, ajoute un autre `Span` à `doc.ents`.
- Garde à l'esprit que le token de fin d'un span est exclu. Donc une entité qui
  commence au token 2 et qui s'arrête au token 3 aura un début à `2` et une fin
  à `4`.

</codeblock>

</exercise>

<exercise id="13" title="Résumé" type="slides">

<slides source="chapter4_04_wrapping-up" start="45:01" end="47:195">
</slides>

</exercise>
