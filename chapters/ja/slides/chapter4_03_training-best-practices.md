---
type: slides
---

# spaCyモデルのトレーニングのベストプラクティス

Notes: 実験を始めると、多くのことが自分の思い通りにいかないことに気づくかもしれません。しかし、それでいいのです。

モデルのトレーニングは反復的なプロセスであり、何が一番うまくいくのかを見つけるまで、さまざまなことを試していく必要があります。

このレッスンでは、モデルをトレーニングする際のベストプラクティスと留意点をいくつか紹介します。

あなたが遭遇するかもしれない問題のいくつかを見てみましょう。

---

# 問題点1: モデルは忘れ得る

- 既存のモデルは新しいデータにオーバーフィット可能です
  - 例：`"WEBSITE"`を学習し、`"PERSON"`が何であるかを「忘れてしまう」ことができます。
- 別名「壊滅的な物忘れ（catastrophic forgetting）」問題

Notes: 機械学習モデルは多くのことを学習することができますが、それは忘れないということではありません。

既存のモデルを新しいデータ、特に新しいラベルで更新している場合、モデルはオーバーフィットして、新しい例に対して適応しすぎることがあります。

例えば、「ウェブサイト」のデータだけで更新している場合、以前に正しく予測していた他のラベル（例えば「人」のラベル）を「忘れる」ことがあります。

これは壊滅的な忘却問題としても知られています。

---

# 解決策1: 以前の正解データを混ぜる

- 例えば、`"WEBSITE"`を学習する場合は、`"PERSON"`の例も含めます。
- 既存のspaCyモデルをデータ上で実行し、他のすべての関連する固有表現を抽出します。

**悪い例:**

```python
TRAINING_DATA = [
    ("Reddit is a website", {"entities": [(0, 6, "WEBSITE")]})
]
```

**良い例:**

```python
TRAINING_DATA = [
    ("Reddit is a website", {"entities": [(0, 6, "WEBSITE")]}),
    ("Obama is a person", {"entities": [(0, 5, "PERSON")]})
]
```

Note: 忘却を防ぐためには、モデルが以前に正しいと判断した例を常に混ぜるようにしてください。

新しいカテゴリ `"WEBSITE"` を学習する場合は，`"PERSON"` の例も含めてください．

spaCyはこれをサポートしてくれます。
既存のモデルをデータ上で実行し，注目すべき固有表現スパンを抽出することで，
これらの追加のデータを作成することができます．

そして、それらの例を既存のデータと混ぜて、すべてのラベルのアノテーションでモデルを更新することができます。

---

# 問題2: モデルはすべてを学習できるわけではありません

- spaCy's models make predictions based on **local context**
- Model can struggle to learn if decision is difficult to make based on context
- Label scheme needs to be consistent and not too specific
  - For example: `"CLOTHING"` is better than `"ADULT_CLOTHING"` and
    `"CHILDRENS_CLOTHING"`

Notes: Another common problem is that your model just won't learn what you want
it to.

spaCy's models make predictions based on the local context – for example, for
named entities, the surrounding words are most important.

If the decision is difficult to make based on the context, the model can
struggle to learn it.

The label scheme also needs to be consistent and not too specific.

For example, it may be very difficult to teach a model to predict whether
something is adult clothing or children's clothing based on the context.
However, just predicting the label "clothing" may work better.

---

# Solution 2: Plan your label scheme carefully

- Pick categories that are reflected in local context
- More generic is better than too specific
- Use rules to go from generic labels to specific categories

**BAD:**

```python
LABELS = ["ADULT_SHOES", "CHILDRENS_SHOES", "BANDS_I_LIKE"]
```

**GOOD:**

```python
LABELS = ["CLOTHING", "BAND"]
```

Notes: Before you start training and updating models, it's worth taking a step
back and planning your label scheme.

Try to pick categories that are reflected in the local context and make them
more generic if possible.

You can always add a rule-based system later to go from generic to specific.

Generic categories like "clothing" or "band" are both easier to label and easier
to learn.

---

# Let's practice!

Notes: Let's look at some of these problems in context and fix them!
