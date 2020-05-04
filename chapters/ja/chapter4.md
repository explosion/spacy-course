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

<exercise id="10" title="良いデータ vs. 悪いデータ">

Here's an excerpt from a training set that labels the entity type `TOURIST_DESTINATION` in traveler reviews.
旅行者のレビューについて、固有表現タイプ`TOURIST_DESTINATION` のラベルをつけるトレーニングセットからの抜粋です。

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

なぜこのデータとラベル定義には問題があるでしょうか？

<choice>

<opt text="場所が観光地かどうかは主観的な判断であり、確定的なカテゴリーではないので、固有表現抽出器が学習するのは非常に難しいから" correct="true">

より良いアプローチは、`"GPE"`(地政学的実体)または`"LOCATION"`というラベルだけを付け、ルールベースのシステムを使って、その実体が観光地であるかどうかを判断することです。
例えば、知識ベースを用いたり、トラベルウィキで調べたりすることができます。

</opt>

<opt text="パリは一貫性を保つためにも観光地と表記すべきであるから。そうしないとモデルが混乱してしまいます。">

パリ、AKは観光地である可能性もありますが、これはラベルスキームがいかに主観的であり、ラベルが適用されるかどうかを判断することがいかに難しいかを浮き彫りにするだけです。
結果として、この区別を固有表現抽出器が学習するのは非常に困難になります。

</opt>

<opt text="誤字脱字の「amsterdem」のような珍しい単語を固有表現としてラベル付けすべきでないから">

非常に珍しい単語やスペルミスであっても、固有表現としてラベル付けすることができます。
実際、文脈に基づいてスペルミスのあるテキストのカテゴリを予測できることは、機械学習ベースの固有表現抽出器の強みの一つです。

</opt>

</choice>

### パート2

- `TRAINING_DATA`を書き換えて、`"TOURIST_DESTINATION"`ではなく、`"GPE"`(都市、州、国)というラベルだけを使うようにしてください。
- もとのデータではラベルが付いていなかった `"GPE"` 固有表現のタプルを追加することを忘れないようにしてください。

<codeblock id="04_10">

- 既にラベル付けされているスパンについては、ラベル名を `"TOURIST_DESTINATION"` から `"GPE"` に変更するだけです。
- 1つのテキストには、まだラベル付けされていない都市と州が含まれています。固有表現スパンを追加するには、文字数を数えて、スパンがどこから始まり、どこで終わるかを調べます。そして、`(start, end, label)`タプルをエンティティに追加します。

</codeblock>

</exercise>

<exercise id="11" title="複数ラベルでのトレーニング">

ここに、新しい固有表現タイプを学習するために作成されたデータセットの一部があります。元のデータセットには数千文が含まれています。
この演習では、ラベル付けを手作業で行います。
実際には、おそらくこれを自動化してアノテーションツールを使用したいと思うでしょう。
例えば、[Brat](http://brat.nlplab.org/)という人気のあるオープンソースのソリューションや、[Prodigy](https://prodi.gy)というspaCyと統合された我々自身のアノテーションツールなどです。

### パート1

- データにある`"WEBSITE"`の固有表現のオフセットを計算してください。
  手動で文字数をカウントしたくないときは、`len()`を使ってください。

<codeblock id="04_11_01">

- 固有表現スパンの開始オフセットと終了オフセットは、テキストへの文字オフセットです。
  例えば、あるエンティティが5の位置から始まる場合、開始オフセットは `5` となります。末尾オフセットは、その位置の文字を含まないことに注意してください。

</codeblock>

### パート2

先ほどラベルを付けたデータに加えて、数千の類似した例を加えてモデルを学習しました。
学習後、`"WEBSITE"`ではうまくいっていますが、`"PERSON"`を抽出しなくなってしまいました。なぜこのようなことが起こるのでしょうか?

<choice>

<opt text='モデルにとって、<code>"PERSON"</code>と<code>"WEBSITE"</code>のように異なるカテゴリを学習するのは難しいから'>

モデルがかなり異なる複数のカテゴリを学習することは可能です。
たとえば、spaCyの事前学習の英語モデルは、人と組織とパーセンテージを認識することができます。

</opt>

<opt text='学習データには<code>"PERSON"</code>の例が含まれていなかったため、モデルはこのラベルが正しくないと学習したから' correct="true">

もし`"PERSON"`固有表現がトレーニングに含まれているにも関わらずラベル付けされていなかったら、モデルはこのスパンを出力すべきでないというように学習してしまいます。
同様に、今まであったラベルがトレーニングデータに含まれていない場合、モデルはそのラベルのことを忘れてしまい、予測しなくなってしまうことがあります。
</opt>

<opt text="両方のエンティティタイプを認識できるように、ハイパーパラメータを再調整する必要があるから">

ハイパーパラメータはモデルの精度に影響を与える可能性がありますが、ここでは問題ではないでしょう。

</opt>

</choice>

### パート3

- `"PERSON"`の固有表現「PewDiePie」と「Alexis Ohanian」のアノテーションを含むように学習データを更新します。

<codeblock id="04_11_02">

- もっと固有表現を追加するには、さらに`(start, end, label)`のタプルをリストに追加します。

</codeblock>

</exercise>

<exercise id="12" title="ラッピング" type="slides">

<slides source="chapter4_04_wrapping-up">
</slides>

</exercise>
