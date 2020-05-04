---
title: 'Chapter 4: ニューラルネットワークのトレーニング'
description:
  "この章では、ユースケースに合わせて機械学習モデルを更新数ｒ方法を学びます。例えば、オンラインのコメントを使って新しい固有表現タイプを予測する、などです。
  ゼロからトレーニングループを書いていき、トレーングの基礎を理解し、NLPプロジェクトをより成功させるためのヒントやコツを学んでいきます。"
prev: /chapter3
next: null
type: chapter
id: 4
---

<exercise id="1" title="モデルのトレーニングと更新" type="slides">

<slides source="chapter4_01_training-updating-models">
</slides>

</exercise>

<exercise id="2" title="トレーニングの目的">

spaCyは、言語特徴量を予測するための事前に訓練された様々なモデルが付属していますが、殆どの場合、より多くのデータでそれらを微調整したいと思うでしょう。より多くのラベル付けされたデータを用いてトレーニングをすれば可能です。

トレーニングはどの場面では役に立たないでしょうか？

<choice>

<opt text="用意したデータで精度を上げる">

事前に訓練されたモデルがあるデータ上でうまく機能しない場合は、新たなデータを使って訓練することが良い解決策になることがよくあります。

</opt>

<opt text="新たな分類スキームを学習する">

トレーニングをすると、新しいラベル、固有表現タイプ、その他の分類スキームなどをモデルに教えることができます。

</opt>

<opt text="ラベルなしデータからパターンを探す" correct="true">

spaCyのコンポーネントは、テキストアノテーションが必要な教師学習モデルです。
つまり、新たなラベルを生のデータから推測することはできず、データを再現するために学習させる必要がある、ということです。

</opt>

</choice>

</exercise>

<exercise id="3" title="学習データを作る(1)">

spaCyのルールベースの `Matcher` は，固有表現抽出の学習データを素早く作成するのに最適な方法です。
文章のリストが変数 `TEXTS` として用意されており、プリントすると、中身を見ることができます。
iPhoneのモデルが言及されている箇所を見つけるため、それらを `"GADGET"` として認識するようにモデルに教えるための学習データを作成することができます。

- 小文字が `"iphone"` と `"x"` に一致する2つのトークンのパターンを書きます。
- 小文字が `"iphone"` にマッチするトークンと、`"?"` 演算子を使った数字の2つのトークンのパターンを書きます。

<codeblock id="04_03">

- トークンの小文字を一致させるには、`"LOWER"`属性を使用します。例えば、`{"LOWER". "apple"}`のようにします。
- 数字のトークンを見つけるには、`"IS_DIGIT"` フラグを用います。例えば、 `{"IS_DIGIT". True}`のようになります。

</codeblock>

</exercise>

<exercise id="4" title="学習データを作る(2)">

前の演習で作成したマッチパターンを使って、学習例のセットをブートストラップしてみましょう。文章のリストは変数 `texts` として用意されています。

- `nlp.pipe`を使って各テキストに対応するdocオブジェクトを作成します。
- `doc`にmatcherを適用し、マッチしたスパンのリストを作成する。
- マッチしたスパンのタプル `(start character, end character, label)` を取得します。
- 各サンプルをテキストと辞書のタプルとして整形し、`"entities"` を固有表現タプルにマッピングします。
- データを `TRAINING_DATA` に追加し、プリントして検査します。

<codeblock id="04_04">

- 一致するものを見つけるには、`doc` に対して `matcher` を呼び出します。
- 結果は `(match_id, start, end)` のタプルです。
- 学習データのリストにデータを追加するには、`TRAINING_DATA.append()`を使ってください。

</codeblock>

</exercise>

<exercise id="5" title="トレーニングループ" type="slides">

<slides source="chapter4_02_training-loop">
</slides>

</exercise>

<exercise id="6" title="パイプラインの設定">

この演習では、テキスト中の `"GADGET"` 固有表現を認識するための固有表現抽出器を訓練するためのspaCyパイプラインを準備します。

- `spacy.blank` メソッドを用いて、何も入っていない`"en"`モデルを作成します。
- `nlp.create_pipe` を使って新しい固有表現抽出器を作成し、パイプラインに追加します。
- パイプラインコンポーネントの `add_label` メソッドを使って新しいラベル `"GADGET"` を固有表現抽出器に追加します。

<codeblock id="04_06">

- 新しい固有表現抽出器を作成するには、文字列 `"ner"` を指定して `nlp.create_pipe` を呼び出します。
- コンポーネントをパイプラインに追加するには、`nlp.add_pipe`メソッドを用います。
- `add_label` メソッドは固有表現抽出器のメソッドで、変数 `ner` からアクセスできます。ラベルを追加するには、`ner.add_label` にラベル名を指定して `ner.add_label("SOME_LABEL")` というふうに呼び出します。

</codeblock>

</exercise>

<exercise id="7" title="トレーニングループを作る">

シンプルなトレーニングループをゼロから作ってみましょう！

前の演習で作成したパイプラインは `nlp` オブジェクトとして利用可能です。これには既に `"GADGET"` というラベルが追加された固有表現抽出器が含まれています。

先ほど作成したラベル付きのデータが `TRAINING_DATA` 変数に入っています。データを見るには、スクリプトの中でコピーしてください。

- `nlp.begin_training`を呼び出し、10回の訓練ループを作成し、訓練データをシャッフルします。
- `spacy.util.minibatch` を用いて学習データのバッチを作成し、反復処理します。
- バッチ内の `(text, annotations)` タプルを `texts` と `annotations` のリストに変換します。
- バッチごとに、`nlp.update` を使ってモデルを更新します。

<codeblock id="04_07">

- 学習を開始して重みをリセットするには `nlp.begin_training()` メソッドを呼び出します。
- 学習データをバッチに分割するには、`spacy.util.minibatch` 関数を呼び出します。

</codeblock>

</exercise>

<exercise id="8" title="Exploring the model">

見たことのないデータに対してモデルがどのように動作するか見てみましょう! 
少しスピードを上げるために、訓練モデルをすでにいくつかのテキストに対して実行しています。以下に結果の一部を示します。

| Text                                                                                                              | Entities               |
| ----------------------------------------------------------------------------------------------------------------- | ---------------------- |
| Apple is slowing down the iPhone 8 and iPhone X - how to stop it                                                  | `(iPhone 8, iPhone X)` |
| I finally understand what the iPhone X 'notch' is for                                                             | `(iPhone X,)`          |
| Everything you need to know about the Samsung Galaxy S9                                                           | `(Samsung Galaxy,)`    |
| Looking to compare iPad models? Here’s how the 2018 lineup stacks up                                              | `(iPad,)`              |
| The iPhone 8 and iPhone 8 Plus are smartphones designed, developed, and marketed by Apple                         | `(iPhone 8, iPhone 8)` |
| what is the cheapest ipad, especially ipad pro???                                                                 | `(ipad, ipad)`         |
| Samsung Galaxy is a series of mobile computing devices designed, manufactured and marketed by Samsung Electronics | `(Samsung Galaxy,)`    |

文章中のすべての固有表現の中で、**モデルの予測の正解数はいくつでしょう**？
スパンの間違いも、誤りとしてカウントとします！
ヒント：モデルが予測すべき固有表現の数をカウントします。そして、実際にモデルが正しく予測できた数を求め、それを先程のカウントで割ります。

<choice>

<opt text="45%">

モデルが正しく予測した固有表現の数を数え、それをモデルが正しく予測すべきだった固有表現の数で割ってください。

</opt>

<opt text="60%">

モデルが正しく予測した固有表現の数を数え、それをモデルが正しく予測すべきだった固有表現の数で割ってください。

</opt>

<opt text="70%" correct="true">

テストデータに対し、モデルの精度は70%でした。

</opt>

<opt text="90%">

モデルが正しく予測した固有表現の数を数え、それをモデルが正しく予測すべきだった固有表現の数で割ってください。

</opt>

</choice>

</exercise>

<exercise id="9" title="トレーニングのベストプラクティス" type="slides">

<slides source="chapter4_03_training-best-practices">
</slides>

</exercise>

<exercise id="10" title="Good data vs. bad data">

Here's an excerpt from a training set that labels the entity type
`TOURIST_DESTINATION` in traveler reviews.

```python
TRAINING_DATA = [
    (
        "i went to amsterdem last year and the canals were beautiful",
        {"entities": [(10, 19, "TOURIST_DESTINATION")]},
    ),
    (
        "You should visit Paris once in your life, but the Eiffel Tower is kinda boring",
        {"entities": [(17, 22, "TOURIST_DESTINATION")]},
    ),
    ("There's also a Paris in Arkansas, lol", {"entities": []}),
    (
        "Berlin is perfect for summer holiday: lots of parks, great nightlife, cheap beer!",
        {"entities": [(0, 6, "TOURIST_DESTINATION")]},
    ),
]
```

### パート1

Why is this data and label scheme problematic?

<choice>

<opt text="Whether a place is a tourist destination is a subjective judgement and not a definitive category. It will be very difficult for the entity recognizer to learn." correct="true">

A much better approach would be to only label `"GPE"` (geopolitical entity) or
`"LOCATION"` and then use a rule-based system to determine whether the entity is a
tourist destination in this context. For example, you could resolve the entities
types back to a knowledge base or look them up in a travel wiki.

</opt>

<opt text="Paris should also be labelled as tourist destinations for consistency. Otherwise, the model will be confused.">

While it's possible that Paris, AK is also a tourist attraction, this only
highlights how subjective the label scheme is and how difficult it will be to
decide whether the label applies or not. As a result, this distinction will also
be very difficult to learn for the entity recognizer.

</opt>

<opt text="Rare out-of-vocabulary words like the misspelled 'amsterdem' shouldn't be labelled as entities.">

Even very uncommon words or misspellings can be labelled as entities. In fact,
being able to predict categories in misspelled text based on the context is one
of the big advantages of statistical named entity recognition.

</opt>

</choice>

### パート2

- Rewrite the `TRAINING_DATA` to only use the label `"GPE"` (cities, states,
  countries) instead of `"TOURIST_DESTINATION"`.
- Don't forget to add tuples for the `"GPE"` entities that weren't labeled in the
  old data.

<codeblock id="04_10">

- For the spans that are already labelled, you'll only need to change the label
  name from `"TOURIST_DESTINATION"` to `"GPE"`.
- One text includes a city and a state that aren't labeled yet. To add the
  entity spans, count the characters to find out where the entity span starts
  and where it ends. Then add `(start, end, label)` tuples to the entities.

</codeblock>

</exercise>

<exercise id="11" title="Training multiple labels">

Here's a small sample of a dataset created to train a new entity type `"WEBSITE"`.
The original dataset contains a few thousand sentences. In this exercise, you'll
be doing the labeling by hand. In real life, you probably want to automate this
and use an annotation tool – for example, [Brat](http://brat.nlplab.org/), a
popular open-source solution, or [Prodigy](https://prodi.gy), our own annotation
tool that integrates with spaCy.

### パート1

- Complete the entity offsets for the `"WEBSITE"` entities in the data. Feel free
  to use `len()` if you don't want to count the characters.

<codeblock id="04_11_01">

- The start and end offset of an entity span are the character offsets into the
  text. For example, if an entity starts at position 5, the start offset is `5`.
  Remember that the end offsets are _exclusive_ – so `10` means _up to_
  character 10.

</codeblock>

### パート2

A model was trained with the data you just labelled, plus a few thousand similar
examples. After training, it's doing great on `"WEBSITE"`, but doesn't recognize
`"PERSON"` anymore. Why could this be happening?

<choice>

<opt text='It’s very difficult for the model to learn about different categories like <code>"PERSON"</code> and <code>"WEBSITE"</code>.'>

It's definitely possible for a model to learn about very different categories.
For example, spaCy's pre-trained English models can recognize persons, but also
organizations or percentages.

</opt>

<opt text='The training data included no examples of <code>"PERSON"</code>, so the model learned that this label is incorrect.' correct="true">

If `"PERSON"` entities occur in the training data but aren't labelled, the model
will learn that they shouldn't be predicted. Similarly, if an existing entity
type isn't present in the training data, the model may \"forget\" and stop
predicting it.

</opt>

<opt text="The hyperparameters need to be retuned so that both entity types can be recognized.">

While the hyperparameters can influence a model's accuracy, they're likely not
the problem here.

</opt>

</choice>

### パート3

- Update the training data to include annotations for the `"PERSON"` entities
  "PewDiePie" and "Alexis Ohanian".

<codeblock id="04_11_02">

- To add more entities, append another `(start, end, label)` tuple to the list.

</codeblock>

</exercise>

<exercise id="12" title="Wrapping up" type="slides">

<slides source="chapter4_04_wrapping-up">
</slides>

</exercise>
