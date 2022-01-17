---
type: slides
---

# Configuration et exécution de l'entraînement

Notes: Maintenant que tu as appris à créer des données d'entraînement, jetons
un oeil à l'entraînement de ton pipeline et à la configuration de
l'entraînement. Dans cette leçon, tu vas apprendre tout ce qui concerne le
système de configuration d'entraînement de spaCy, comment générer ta propre
configuration d'entraînement, comment utiliser la ligne de commande pour
entraîner un modèle et comment explorer tes pipelines entraînés ensuite.

---

# Configuration de l'entraînement (1)

- **source unique de vérité** pour tous les paramètres
- généralement nommée `config.cfg`
- définit comment initialiser l'objet `nlp`
- comprend tous les paramètres des composants du pipeline et leurs
  implémentations de modèles
- configure le processus d'entraînement et les hyperparamètres
- rend ton entraînement reproductible

Notes: spaCy utilise un fichier de configuration, généralement nommé
`config.cfg`, comme "source unique de vérité" pour tous les paramètres. Le
fichier de configuration définit comment initialiser l'objet `nlp`, quels
composants de pipeline ajouter et comment configurer leurs implémentations de
modèles internes. Il comprend aussi tous les paramètres du processus
d'entraînement et la manière de charger les données, y compris les
hyperparamètres.

Au lieu de devoir fournir de nombreux arguments en ligne de commande ou te
rappeler de définir chacun des paramètres dans le code, il te suffit de passer
ton fichier de configuration à la commande d'entraînement de spaCy.

Les fichiers de configuration contribuent également à la reproductibilité : tu
auras tous tes paramètres à un seul endroit et tu sauras toujours comment ton
pipeline a été entraîné. Tu pourras même charger ton fichier de configuration
dans un dépôt Git pour le versionner et le partager avec d'autres afin
qu'ils puissent entraîner le même pipeline avec les mêmes paramètres.

---

# Configuration de l'entraînement (2)

```ini
[nlp]
lang = "fr"
pipeline = ["tok2vec", "ner"]
batch_size = 1000

[nlp.tokenizer]
@tokenizers = "spacy.Tokenizer.v1"

[components]

[components.ner]
factory = "ner"

[components.ner.model]
@architectures = "spacy.TransitionBasedParser.v2"
hidden_width = 64
# Et ainsi de suite...
```

Notes: Voici un extrait d'un fichier de configuration utilisé pour entraîner un
pipeline avec un reconnaisseur d'entités nommées. La configuration est groupée
en sections, et les sections imbriquées sont définies avec un point. Par 
exemple, `[components.ner.model]` definit les paramètres d'implémentation de
modèle pour le reconnaisseur d'entités nommées.

Les fichiers de configuration peuvent aussi référencer des fonctions Python
avec la notation `@`. Par exemple, le tokenizer définit une fonction déclarée de
tokenizer. Tu peux utiliser cela pour personnaliser différentes parties de
l'objet `nlp` et de l'entraînement – depuis l'intégration de ton propre
tokenizer, jusqu'à l'implémentation de tes propres architectures de modèles.
Mais ne nous préoccupons pas de cela pour l'instant – tout ce que tu vas
apprendre dans ce chapitre utilisera simplement les valeurs par défaut prêtes à
l'emploi fournies par spaCy !

---

# Génération d'une configuration

- spaCy peut auto-générer un fichier de configuration par défaut pour toi
- [widget de démarrage rapide](https://spacy.io/usage/training#quickstart)
  interactif dans la doc
- commande [`init config`](https://spacy.io/api/cli#init-config) en ligne de
  commande

```bash
$ python -m spacy init config ./config.cfg --lang fr --pipeline ner
```

- `init config` : la commande à exécuter
- `config.cfg` : le chemin vers lequel sauver la configuration générée
- `--lang` : la classe de langue du pipeline, par ex. `fr` pour le français
- `--pipeline` : les noms des composants à inclure, séparés par des virgules

Notes: Bien sûr, tu n'as pas à écrire les fichiers de configuration à la main,
et dans bien des cas, tu n'as même pas besoin de les personnaliser du tout.
spaCy peut auto-générer un fichier de configuration pour toi.

Le widget de démarrage rapide de la documentation te permet de générer une
configuration interactivement en sélectionnant la langue et les composants de
pipeline dont tu as besoin, ainsi que des paramètres matériels et
d'optimisation optionnels.

Sinon, tu peux aussi utiliser la commande native de spaCy `init config`. Elle
prend comme premier argument le nom du fichier de sortie. En général on nomme
ce fichier `config.cfg`. L'argument `--lang` définit la classe de langue qui
devra être utilisée pour le pipeline, par exemple `fr` pour le français.
L'argument `--pipeline` te permet de spécifier un ou plusieurs noms de
composants à inclure, séparés par des virgules. Dans notre exemple, nous créons
une configuration avec un composant de pipeline, le reconnaisseur d'entités
nommées.

---

# Entraînement d'un pipeline (1)

- tout ce dont tu as besoin est le `config.cfg` et les données d'entraînement
  et de développement
- les paramètres de configuration peuvent être modifiés en ligne de commande

```bash
$ python -m spacy train ./config.cfg --output ./output --paths.train train.spacy --paths.dev dev.spacy
```

- `train` : la commande à exécuter
- `config.cfg` : le chemin vers le fichier de configuration
- `--output` : le chemin vers le répertoire de sortie où sauver le pipeline
  entraîné
- `--paths.train` : modifie le chemin vers les données d'entraînement
- `--paths.dev` : modifie le chemin vers les données d'évaluation

Notes: Pour entraîner un pipeline, tout ce dont tu as besoin est le fichier de
configuration ainsi que les données d'entraînement et de développement. Ce sont
les fichiers `.spacy` que tu as déjà manipulés dans les exercices précédents.

Le premier argument de `spacy train` est le chemin vers le fichier de
configuration. L'argument `--output` te permet de spécifier le répertoire où
sauver le pipeline entraîné final.

Tu peux aussi modifier différents paramètres de configuration depuis la ligne
de commande. Dans notre exemple, nous modifions `paths.train` avec le chemin 
vers le fichier `train.spacy` et `paths.dev` avec le fichier `dev.spacy`.

---

# Entraînement d'un pipeline (2)

```
============================ Training pipeline ============================
ℹ Pipeline: ['tok2vec', 'ner']
ℹ Initial learn rate: 0.001

E    #       LOSS TOK2VEC  LOSS NER  ENTS_F  ENTS_P  ENTS_R  SCORE
---  ------  ------------  --------  ------  ------  ------  ------
  0       0          0.00     26.50    0.73    0.39    5.43    0.01
  0     200         33.58    847.68   10.88   44.44    6.20    0.11
  1     400         70.88    267.65   33.50   45.95   26.36    0.33
  2     600         67.56    156.63   45.32   62.16   35.66    0.45
  3     800        138.28    134.12   48.17   74.19   35.66    0.48
  4    1000        177.95    109.77   51.43   66.67   41.86    0.51
  6    1200         94.95     52.13   54.63   67.82   45.74    0.55
  8    1400        126.85     66.19   56.00   65.62   48.84    0.56
 10    1600         38.34     24.16   51.96   70.67   41.09    0.52
 13    1800        105.14     23.23   56.88   69.66   48.06    0.57

✔ Saved pipeline to output directory
/path/to/output/model-last
```

Notes: Voici un exemple d'affichage de ce que tu verras pendant et après un
entraînement. Tu te souviens peut-être du début de ce chapitre où on voulait
généralement effectuer plusieurs passes sur les données au cours de
l'entraînement. Chaque passe sur les données est appelée une "epoch". C'est ce
qui apparaît dans la première colonne du tableau.

Pour chaque epoch, spaCy affiche les scores de précision tous les 200
exemples. Ce sont les étapes montrées dans la deuxième colonne. Tu peux changer
la fréquence dans la configuration. Chaque ligne montre la perte et le score de
précision calculé à cette étape de l'entraînement.

Le score le plus intéressant à surveiller est le score combiné dans la dernière
colonne. Il reflète à quel point ton modèle prédit précisément les bonnes
réponses pour les données d'évaluation.

L'entraînement se poursuit jusqu'à ce que le modèle cesse de s'améliorer et
s'arrête automatiquement.

---

# Chargement d'un pipeline entraîné

- le résultat après entraînement est un pipeline spaCy chargeable normal
  - `model-last` : le dernier pipeline entraîné
  - `model-best` : le meilleur pipeline entraîné
- chargement avec `spacy.load`

```python
import spacy

nlp = spacy.load("/path/to/output/model-best")
doc = nlp("iPhone 11 vs iPhone 8 : quelle sont les différences ?")
print(doc.ents)
```

Notes: le pipeline sauvé après entraînement est un pipeline spaCy chargeable
normal – exactement comme les pipelines entraînés fournis par spaCy, par
exemple `fr_core_news_sm`. À la fin, le dernier pipeline entraîné et le
pipeline avec le meilleur score sont sauvés dans le répertoire de sortie.

Tu peux charger ton pipeline entraîné en passant le chemin à `spacy.load`. Tu
peux ensuite l'utiliser pour traiter et analyser ton texte.

---

# Astuce : Ton pipeline sous forme de package

<!-- TODO: illustration of pipeline packages, similar to earlier chapters? -->

- [`spacy package`](https://spacy.io/api/cli#package): crée un package Python
  installable contenant ton pipeline
- facile à versionner et à déployer

```bash
$ python -m spacy package /path/to/output/model-best ./packages --name mon_pipeline --version 1.0.0
```

```bash
$ cd ./packages/fr_mon_pipeline-1.0.0
$ pip install dist/fr_mon_pipeline-1.0.0.tar.gz
```

Charge et utilise le pipeline après installation:

```python
nlp = spacy.load("fr_mon_pipeline")
```

Notes: Pour faciliter le déploiement de tes pipelines, spaCy fournit une
commande pratique pour les empaqueter en packages Python. La commande
`spacy package` prend le chemin de ton pipeline exporté et un répertoire de
sortie. Elle génère ensuite un package Python qui contient ton pipeline. Le
package Python est un fichier `.tar.gz` qui peut être installé dans ton
environnement.

Tu peux également fournir un nom et un numéro de version optionnels à la
commande. Ceci te permet de gérer plusieurs versions différentes d'un pipeline,
par exemple si tu décides de personnaliser ton pipeline ensuite ou de
l'entraîner avec davantage de données.

Le package se comporte comme n'importe quel autre package Python. Après
installation, tu peux charger ton pipeline en utilisant son nom. Note que spaCy
ajoutera automatiquement le code de langue au nom. Donc ton pipeline
`mon_pipeline` deviendra `fr_mon_pipeline`.

---

# Pratiquons !

Notes: Mettons-nous au travail et entraînons ton premier pipeline ! Tu vas
t'exercer à générer une configuration pour un reconnaisseur d'entités nommées
et à entraîner un pipeline avec les données sur lesquelles tu as travaillé
dans les exercices précédents.
