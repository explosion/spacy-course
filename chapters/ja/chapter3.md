---
title: '第3章: パイプライン処理'
description:
  "この章では spaCy の処理パイプラインについて知っておくべきことをすべて紹介します。テキストを処理するときに裏側で起こっていること、自分でコンポーネントを書いてパイプラインに追加する方法, カスタム属性を使用してdocやスパン、トークンに独自のメタデータを追加する方法, などを学びます。"
prev: /chapter2
next: /chapter4
type: chapter
id: 3
---

<exercise id="1" title="処理パイプライン" type="slides">

<slides source="chapter3_01_processing-pipelines">
</slides>

</exercise>

<exercise id="2" title="nlpを呼び出すとき、何が起こっているか？">

`nlp`をテキストに対して呼び出すとき、spaCyは何をしているでしょうか？

```python
doc = nlp("This is a sentence.")
```

<choice>

<opt text="タグづけ、依存関係解析、固有表現抽出を行い、トークナイズしている">

トークナイザはテキストを`Doc`オブジェクトに変換するため、常に全てのパイプラインの前に適用されます。
そして、パイプラインには、タガー、パーサー、固有表現抽出器は必ずしも必要ありません。

</opt>

<opt text="テキストをトークナイズし、パイプラインのそれぞれのコンポーネントを順番に適用している">

トークナイザはテキストを`Doc`オブジェクトに変換します。
spaCyはパイプライン内のすべてのコンポーネントを順に`Doc`に適用します。

</opt>

<opt text="spaCyのサーバに接続し、結果を計算して返している">

spaCyはマシン上で全てを計算するので、サーバに接続する必要はありません。

</opt>

<opt text="言語を初期化し、パイプラインを追加し、モデルの重みをロードしています">

`spacy.load()` を呼び出してモデルをロードすると、言語の初期化、パイプラインの追加モデルの重みのロードを行います。
テキストに対して`nlp` オブジェクトを呼び出すとき、モデルは既にロードされています。

</opt>

</exercise>

<exercise id="3" title="Inspecting the pipeline">

英語の小サイズのモデルのパイプラインの中身を見てみましょう！

- `en_core_web_sm`モデルを読み込み、`nlp` オブジェクトを作成します。
- `nlp.pipe_names`を用いてパイプラインのコンポーネント名を表示します。
- `nlp.pipeline`を用いて`(name, component)`タプルからなる全てのパイプラインを表示します。

<codeblock id="03_03">

コンポーネント名のリストは`nlp.pipe_names`属性で入手できます。
`(name, component)`タプルからなるパイプラインのリストは`nlp.pipeline`から取得できます。

</codeblock>

</exercise>

<exercise id="4" title="カスタムのパイプラインコンポーネント" type="slides">

<slides source="chapter3_02_custom-pipelie-components">
</slides>

</exercise>

<exercise id="5" title="カスタムコンポーネントのユースケース">

これらの問題のうち、カスタムコンポーネントによって解決できるものはどれですか？該当するものをすべて選択してください。

1. 事前に訓練されたモデルを更新し、その予測を改善する
2. トークンとその属性に基づいてオリジナルの値を計算する
3. 辞書に基づいた名前付きエンティティの追加などを行う
4. 追加言語のサポートの実装

<choice>

<opt text="1と2">

カスタムコンポーネントは`Doc`を変更するだけで、他のコンポーネントの重みを直接更新することはできません。

</opt>

<opt text="1と3">

カスタムコンポーネントは`Doc`を変更するだけで、他のコンポーネントの重みを直接更新することはできません。

</opt>

<opt text="1と4">

カスタムコンポーネントは`Doc`を変更するだけで、他のコンポーネントの重みを直接更新することはできません。また、言語クラスがすでに初期化され、テキストがトークン化された後にパイプラインに追加されるので、新しい言語を追加するのには適していません。

</opt>

<opt text="2と3" correct="true">

カスタムコンポーネントは、Doc、トークン、スパンにカスタム値を追加したり、`doc.ents`をカスタマイズしたりするのに最適です。

</opt>

<opt text="2と4">

カスタムコンポーネントは、言語クラスがすでに初期化され、テキストがトークン化された後にパイプラインに追加されるので、新しい言語を追加するのには適していません。

</opt>

<opt text="3と4">

カスタムコンポーネントは`Doc`を変更するだけで、他のコンポーネントの重みを直接更新することはできません。また、言語クラスがすでに初期化され、テキストがトークン化された後にパイプラインに追加されるので、新しい言語を追加するのには適していません。

</opt>

</choice>

</exercise>

<exercise id="6" title="シンプルなコンポーネント">

この例では、Docのトークンの長さを表示するカスタムコンポーネントを紹介しています。
足りないぶぶんを埋め、完成させてください。

- コンポーネントの関数を`doc`の長さを用いて完成させます。
- 既存のパイプラインの先頭に`length_component`を追加します。
- 新しいパイプラインを試してみて、`nlp` オブジェクトを使ってテキストを処理してみてください。
  例文：「これは文章です。」

<codeblock id="03_06">

- `Doc`オブジェクトの長さを取得するには、Pythonの組み込みの`len()`メソッドが使えます。
- コンポーネントをパイプラインに追加するには`nlp.add_pipe`メソッドを使います。
  キーワード引数`first`に`True`を指定すると、他のすべてのコンポーネントよりも前に追加されることを忘れないでください。
- テキストを処理するには、`nlp`オブジェクトを呼び出します。

</codeblock>

</exercise>

<exercise id="7" title="複雑なコンポーネント">

この演習では、`PhraseMatcher`を使ってドキュメント内の動物の名前を見つけ、一致したスパンを`doc.ents`に追加するカスタムコンポーネントを書いてみましょう。
動物のパターンを持つ `PhraseMatcher` はすでに変数 `matcher` として作成されています。

- カスタムコンポーネントを定義し、`doc`に `matcher` を適用します。
- 各マッチに対して `Span` を作成し、`"ANIMAL"` にラベルIDを割り当て、`doc.ents` を新しいスパンで上書きします。
- 新しいコンポーネントを `"ner"` コンポーネントの後にパイプラインに追加します。
- テキストを処理し、`doc.ents`内のエンティティのエンティティテキストとエンティティラベルをプリントします。

<codeblock id="03_07">

- マッチは `(match_id, start, end)` タプルのリストであることを思い出してください。
- `Span`クラスは4つの引数を取ります：親の`doc`、開始インデックス、終了インデックス、ラベルです。
- コンポーネントを別のコンポーネントの後ろから追加するには、`nlp.add_pipe`の`after` キーワード引数を用います。

</codeblock>

</exercise>

<exercise id="8" title="拡張属性" type="slides">

<slides source="chapter3_03_extension-attributes">
</slides>

</exercise>

<exercise id="9" title="拡張属性の設定(1)">

拡張属性の設定を試してみましょう。

### ステップ1

- `Token.set_extension` を用いて `"is_country"` (デフォルトは `False`) を登録します。
- `"スペイン"`について更新し、すべてのトークンをプリントします。

<codeblock id="03_09_01">

拡張属性は`._`からアクセスできることを思い出してください。例えば、`doc._.has_color`のようにします。

</codeblock>

### ステップ3

- `Token.set_extension`を使って`"reversed"`を登録してください（getter `get_reversed`）
- それぞれのトークンについて、プリントしてください。

<codeblock id="03_09_02">

拡張属性は`._`からアクセスできることを思い出してください。例えば、`doc._.has_color`のようにします。

</codeblock>

</exercise>

<exercise id="10" title="拡張属性の設定(2)">

ゲッターとメソッド属性を用いたより複雑な属性の設定をしていきましょう。

### パート1

- 関数`get_has_number`を完成させます。
- `Doc.set_extension`を用いて`"has_number"`(getter `get_has_number`)を登録し、その値を表示します。

<codeblock id="03_10_01">

- 拡張属性は`._`からアクセスできることを思い出してください。例えば、`doc._.has_color`のようにします。
- 関数 `get_has_number` は、`doc` に含まれるトークンが `token.like_num` に対して `True` を返すかどうか（トークンが数字に似ているかどうか）を返す必要があります。

</codeblock>

### パート2

- `Span.set_extension`を使って`"to_html"`を登録します。（method `to_html`）
- `doc[0:2]`に対して、`"strong"`を使って呼び出します。

<codeblock id="03_10_02">

- メソッドの拡張子は1つ以上の引数を取ることができます。例えば、`doc._.some_method("argument")`のようになります。
- メソッドに渡される最初の引数は、呼び出されたメソッドの親である `Doc`, `Token`, `Span` オブジェクトです。

</codeblock>

</exercise>

<exercise id="11" title="固有表現と拡張属性">

この演習では、カスタム拡張属性とモデルの予測を組み合わせて、スパンが人、組織、または場所の場合にウィキペディアの検索URLを返すゲッター属性を作成します。

- ゲッター `get_wikipedia_url` を完成させ、ラベルのリストにスパンのラベルが含まれている場合にのみURLを返すようにします。
- ゲッター `get_wikipedia_url` を用いて`Span`の拡張子 `"wikipedia_url"` を設定します。
- `doc`内のエンティティをイテレートし、WikipediaのURLを出力します。

<codeblock id="03_11">

- スパンの文字列ラベルを取得するには、`span.label_` 属性を使用します。これは、スパンが固有表現である場合に固有表現抽出器が予測するラベルです。
- 拡張属性は`._`プロパティで利用できることを覚えておいてください。例えば、`doc._.has_color`とします。

</codeblock>

</exercise>

<exercise id="12" title="拡張属性とコンポーネント">

拡張属性は、カスタムパイプラインコンポーネントと組み合わせて使用すると特に強力です。この演習では、国の名前を検索するパイプラインコンポーネントと、国の首都を返すカスタム拡張属性を書いてみましょう。

変数 `matcher` に、すべての国を含むフレーズマッチャがはいっています。
国と首都の関係の辞書が変数 `CAPITALS` として利用できる。

- `countries_component`を完成させ、すべてのマッチに対して `"GPE"` (地政学的実体) のラベルを持つ `Span` を作成します。
- コンポーネントをパイプラインに追加します。
- ゲッター `get_capital` にスパンの拡張属性 `"capital"` を登録します。
- テキストを処理し、`doc.ents`に入っている各固有表現スパンのテキスト、ラベル、キャピタルをプリントします。

<codeblock id="03_12">

- `Span` クラスは、`doc`、トークンインデックス `start` と `end`、そして `label` の 4 つの引数をとります。
- `doc` に対して `PhraseMatcher` を呼び出すと、`(match_id, start, end)` タプルのリストを返します。
- 新しい拡張属性を登録するには、グローバルクラスの `set_extension` メソッドを利用します。ゲッターを登録するには、`getter` キーワード引数を使用します。
- 拡張属性は、`._.`プロパティで利用できます。例えば、`doc._.has_color` のようにします。

</codeblock>

</exercise>

<exercise id="13" title="スケーリングとパフォーマンス" type="slides">

<slides source="chapter3_04_scaling-performance">
</slides>

</exercise>

<exercise id="14" title="ストリームの処理">

In this exercise, you'll be using `nlp.pipe` for more efficient text processing.
The `nlp` object has already been created for you. A list of tweets about a
popular American fast food chain are available as the variable `TEXTS`.

### パート1

- Rewrite the example to use `nlp.pipe`. Instead of iterating over the texts and
  processing them, iterate over the `doc` objects yielded by `nlp.pipe`.

<codeblock id="03_14_01">

- Using `nlp.pipe` lets you merge the first two lines of code into one.
- `nlp.pipe` takes the `TEXTS` and yields `doc` objects that you can loop over.

</codeblock>

### パート2

- Rewrite the example to use `nlp.pipe`. Don't forget to call `list()` around
  the result to turn it into a list.

<codeblock id="03_14_02"></codeblock>

### パート3

- Rewrite the example to use `nlp.pipe`. Don't forget to call `list()` around
  the result to turn it into a list.

<codeblock id="03_14_03"></codeblock>

</exercise>

<exercise id="15" title="Processing data with context">

In this exercise, you'll be using custom attributes to add author and book meta
information to quotes.

A list of `[text, context]` examples is available as the variable `DATA`. The
texts are quotes from famous books, and the contexts dictionaries with the keys
`"author"` and `"book"`.

- Use the `set_extension` method to register the custom attributes `"author"`
  and `"book"` on the `Doc`, which default to `None`.
- Process the `[text, context]` pairs in `DATA` using `nlp.pipe` with
  `as_tuples=True`.
- Overwrite the `doc._.book` and `doc._.author` with the respective info passed
  in as the context.

<codeblock id="03_15">

- The `Doc.set_extension` method takes two arguments: the string name of the
  attribute, and a keyword argument indicating the default, getter, setter or
  method. For example, `default=True`.
- If `as_tuples` is set to `True`, the `nlp.pipe` method takes a list of
  `(text, context)` tuples and yields `(doc, context)` tuples.

</codeblock>

</exercise>

<exercise id="16" title="Selective processing">

In this exercise, you'll use the `nlp.make_doc` and `nlp.disable_pipes` methods
to only run selected components when processing a text.

### パート1

- Rewrite the code to only tokenize the text using `nlp.make_doc`.

<codeblock id="03_16_01">

The `nlp.make_doc` method can be called on a text and returns a `Doc`, just like
the `nlp` object.

</codeblock>

### パート2

- Disable the tagger and parser using the `nlp.disable_pipes` method.
- Process the text and print all entities in the `doc`.

<codeblock id="03_16_02">

The `nlp.disable_pipes` method takes a variable number of arguments: the string
names of the pipeline components to disable. For example,
`nlp.disable_pipes("ner")` will disable the named entity recognizer.

</codeblock>

</exercise>
