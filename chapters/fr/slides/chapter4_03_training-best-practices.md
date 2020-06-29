---
type: slides
---

# Meilleures pratiques pour l'entrainement des modèles spaCy

Notes : Quand tu commenceras à mener tes propres expérimentations, tu te rendras
peut-être compte que beaucoup de choses ne vont pas comme tu voudrais. Et c'est
ok.

Entrainer des modèles est un processus itératif, et tu devras essayer
différentes choses jusqu'à trouver ce qui fonctionne le mieux.

Dans cette leçon, je vais partager plusieurs meilleures pratiques et choses à
garder en tête quand tu entraines tes propres modèles.

Jetons un oeil à certains des problèmes que tu pourrais rencontrer.

---

# Problème 1 : Les modèles peuvent "oublier" des choses

- Les modèles existants peuvent sur-optimiser sur les nouvelles données
  - e.g. : si tu l'actualises uniquement avec `"WEBSITE"`, il peut "oublier" ce
    qu'est une `"PERSON"`
- On appelle ça le problème de "l'oubli catastrophique"

Notes : Les modèles statistiques peuvent apprendre beaucoup de choses - mais
cela ne signifie pas qu'ils ne peuvent pas les désapprendre.

Si tu actualises un modèle existant avec de nouvelles données, en particulier de
nouveaux labels, il peut sur-optimiser et s'ajuster _exagérément_  aux nouveaux
exemples.

Par exemple, si tu l'actualises uniquement avec des exemples de "website", il
peut "oublier" d'autres labels qu'il prédisait correctement jusqu'à présent -
comme "person".

C'est également connu sous l'appellation de l'oubli catastrophique.

---

# Solution 1 : Incorporer des prédictions précédemment correctes

- Par exemple, si tu l'entraines sur `"WEBSITE"`, inclus aussi des exemples de
  `"PERSON"`
- Fais tourner un modèle existant de spaCy sur les données et extrais les autres
  entités pertinentes

**MAUVAIS :**

```python
TRAINING_DATA = [
    ("Reddit is a website", {"entities": [(0, 6, "WEBSITE")]})
]
```

**BON :**

```python
TRAINING_DATA = [
    ("Reddit is a website", {"entities": [(0, 6, "WEBSITE")]}),
    ("Obama is a person", {"entities": [(0, 5, "PERSON")]})
]
```

Note : Pour éviter cela, assure-toi de toujours incorporer des exemples de ce
que le modèle prédisait correctement jusqu'à présent.

Si tu l'entraines sur une nouvelle catégorie `"WEBSITE"`, inclus aussi des
exemples de `"PERSON"`.

spaCy peut t'aider pour cela. Tu peux créer ces exemples supplémentaires en
faisant tourner le modèle existant sur les données et en extrayant les spans
d'entités qui t'intéressent.

Tu peux ensuite mélanger ces exemples avec tes données existantes et actualiser
le modèle avec des annotations pour tous les labels.

---

# Problème 2 : Les modèles ne peuvent pas tout apprendre

- Les modèles de spaCy effectuent des prédictions basées sur le
  **contexte local**
- Les modèles peuvent avoir des difficultés à apprendre si la décision est
  difficile à prendre en se basant sur le contexte
- Les schémas de labellisation doivent être cohérents et pas trop spécifiques
  - Par exemple: `"CLOTHING"` est préférable à `"ADULT_CLOTHING"` et
    `"CHILDRENS_CLOTHING"`

Notes : Un autre problème courant est que ton modèle n'apprenne pas ce que tu
veux qu'il apprenne.

Les modèles de spaCy effectuent des prédictions basées sur le contexte local -
par exemple, pour les entités nommées, ce sont les mots adjacents qui sont les
plus importants.

Si la décision est difficile à prendre en se basant sur le contexte, le modèle
pourra avoir des difficultés à l'apprendre.

Le schéma de labellisation doit également être cohérent et pas trop spécifique.

Par exemple, il pourrait être très difficile d'apprendre à un modèle à prédire
si quelque chose est un vêtement pour adulte ou un vêtement pour enfant en se
basant sur le contexte. En revanche, prédire simplement le label "clothing"
(vêtement) pourrait mieux fonctionner.

---

# Solution 2 : Planifie soigneusement ton schéma de labellisation

- Choisis des catégories qui sont représentées dans le contexte local
- Mieux vaut être trop générique que trop spécifique
- Utilise des règles pour passer de labels génériques à des catégories
  spécifiques

**MAUVAIS :**

```python
LABELS = ["ADULT_SHOES", "CHILDRENS_SHOES", "BANDS_I_LIKE"]
```

**BON :**

```python
LABELS = ["CLOTHING", "BAND"]
```

Notes : Avant de commencer à entrainer et à actualiser des modèles, il est
judicieux de prendre du recul et de planifier ton schéma de labellisation.

Essaie de choisir des catégories qui sont représentées dans le contexte local et
rends-les plus génériques si possible.

Tu peux toujours ajouter un système à base de règles après coup pour aller du
générique vers du spécifique.

Les catégories génériques comme "clothing" ou "band" sont à la fois plus faciles
à labelliser et plus faciles à apprendre.

---

# Pratiquons !

Notes : Jetons un oeil à ces problèmes en contexte et réglons-les !
