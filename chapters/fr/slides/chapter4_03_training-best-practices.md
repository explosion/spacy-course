---
type: slides
---

# Meilleures pratiques pour l'entraînement des modèles spaCy

Notes: Quand tu commenceras à mener tes propres expérimentations, tu te rendras
peut-être compte que beaucoup de choses ne vont pas comme tu voudrais. Et c'est
ok.

Entraîner des modèles est un processus itératif, et tu devras essayer
différentes choses jusqu'à trouver ce qui fonctionne le mieux.

Dans cette leçon, je vais partager plusieurs meilleures pratiques et choses à
garder en tête quand tu entraînes tes propres modèles.

Jetons un oeil à certains des problèmes que tu pourrais rencontrer.

---

# Problème 1 : Les modèles peuvent "oublier" des choses

- Les modèles existants peuvent sur-optimiser sur les nouvelles données
  - ex. : si tu l'actualises uniquement avec `"SITE_WEB"`, il peut "oublier" ce
    qu'est une personne avec le label `"PER"`
- On appelle ça le problème de "l'oubli catastrophique"

Notes: Les modèles statistiques peuvent apprendre beaucoup de choses - mais ils
peuvent aussi les désapprendre.

Si tu actualises un modèle existant avec de nouvelles données, en particulier de
nouveaux labels, il peut sur-optimiser et s'ajuster _exagérément_ aux nouveaux
exemples.

Par exemple, si tu l'actualises uniquement avec des exemples de `"SITE_WEB"`,
il peut "oublier" d'autres labels qu'il prédisait correctement jusqu'alors -
comme `"PER"` pour "personne".

C'est également connu sous le nom de problème de l'oubli catastrophique.

---

# Solution 1 : Incorporer des prédictions précédemment correctes

- Par exemple, si tu l'entraînes sur `"SITE_WEB"`, inclus aussi des exemples de
  `"PER"`
- Fais tourner un modèle existant de spaCy sur les données et extrais les autres
  entités pertinentes

Notes: Pour éviter cela, assure-toi de toujours incorporer des exemples de ce
que le modèle prédisait correctement jusqu'à présent.

Si tu l'entraînes sur une nouvelle catégorie `"SITE_WEB"`, inclus aussi des
exemples de `"PER"` pour "personne".

spaCy peut t'aider pour cela. Tu peux créer ces exemples supplémentaires en
faisant tourner le modèle existant sur les données et en extrayant les spans
d'entités qui t'intéressent.

Tu peux ensuite mélanger ces exemples avec tes données existantes et actualiser
le modèle avec des annotations pour tous les labels.

---

# Problème 2 : Les modèles ne peuvent pas tout apprendre

- Les modèles de spaCy effectuent des prédictions basées sur le **contexte
  local**
- Les modèles peuvent avoir des difficultés à apprendre si la décision est
  difficile à prendre en se basant sur le contexte
- Les schémas de labellisation doivent être cohérents et pas trop spécifiques
  - Par exemple: `"VETEMENTS"` est préférable à `"VETEMENTS_ADULTES"` et
    `"VETEMENTS_ENFANTS"`

Notes: Un autre problème courant est que ton modèle n'apprenne pas ce que tu
veux qu'il apprenne.

Les modèles de spaCy effectuent des prédictions basées sur le contexte local -
par exemple, pour les entités nommées, ce sont les mots adjacents qui sont les
plus importants.

Si la décision est difficile à prendre en se basant sur le contexte, le modèle
pourra avoir des difficultés à l'apprendre.

Le schéma de labellisation doit également être cohérent et pas trop spécifique.

Par exemple, il pourrait être très difficile d'apprendre à un modèle à prédire
si quelque chose est un vêtement pour adulte ou un vêtement pour enfant en se
basant sur le contexte. En revanche, prédire simplement le label `"VETEMENTS"`
pourrait mieux fonctionner.

---

# Solution 2 : Planifie soigneusement ton schéma de labellisation

- Choisis des catégories qui sont représentées dans le contexte local
- Mieux vaut être trop générique que trop spécifique
- Utilise des règles pour passer de labels génériques à des catégories
  spécifiques

**MAUVAIS :**

```python
LABELS = ["CHAUSSURES_ADULTES", "CHAUSSURES_ENFANTS", "MES_GROUPES_PREFERES"]
```

**BON :**

```python
LABELS = ["VETEMENTS", "GROUPE_MUSICAL"]
```

Notes: Avant de commencer à entraîner et à actualiser des modèles, il est
judicieux de prendre du recul et de planifier ton schéma de labellisation.

Essaie de choisir des catégories qui sont représentées dans le contexte local et
rends-les plus génériques si possible.

Tu peux toujours ajouter un système à base de règles après coup pour aller du
générique vers du spécifique.

Des catégories génériques comme `"VETEMENTS"` ou `"GROUPE_MUSICAL"` sont à la
fois plus faciles à labelliser et plus faciles à apprendre.

---

# Pratiquons !

Notes: Jetons un oeil à ces problèmes en contexte et réglons-les !
