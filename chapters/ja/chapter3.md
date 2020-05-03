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

<exercise id="8" title="Extension attributes" type="slides">

<slides source="chapter3_03_extension-attributes">
</slides>

</exercise>

<exercise id="9" title="Setting extension attributes (1)">

Let's practice setting some extension attributes.

### Step 1

- Use `Token.set_extension` to register `"is_country"` (default `False`).
- Update it for `"Spain"` and print it for all tokens.

<codeblock id="03_09_01">

Remember that extension attributes are available via the `._` property. For
example, `doc._.has_color`.

</codeblock>

### Step 2

- Use `Token.set_extension` to register `"reversed"` (getter function
  `get_reversed`).
- Print its value for each token.

<codeblock id="03_09_02">

Remember that extension attributes are available via the `._` property. For
example, `doc._.has_color`.

</codeblock>

</exercise>

<exercise id="10" title="Setting extension attributes (2)">

Let's try setting some more complex attributes using getters and method
extensions.

### パート1

- Complete the `get_has_number` function .
- Use `Doc.set_extension` to register `"has_number"` (getter `get_has_number`)
  and print its value.

<codeblock id="03_10_01">

- Remember that extension attributes are available via the `._` property. For
  example, `doc._.has_color`.
- The `get_has_number` function should return whether any of the tokens in the
  `doc` return `True` for `token.like_num` (whether the token resembles a
  number).

</codeblock>

### パート2

- Use `Span.set_extension` to register `"to_html"` (method `to_html`).
- Call it on `doc[0:2]` with the tag `"strong"`.

<codeblock id="03_10_02">

- Method extensions can take one or more arguments. For example:
  `doc._.some_method("argument")`.
- The first argument passed to the method is always the `Doc`, `Token` or `Span`
  object the method was called on.

</codeblock>

</exercise>

<exercise id="11" title="Entities and extensions">

In this exercise, you'll combine custom extension attributes with the model's
predictions and create an attribute getter that returns a Wikipedia search URL
if the span is a person, organization, or location.

- Complete the `get_wikipedia_url` getter so it only returns the URL if the
  span's label is in the list of labels.
- Set the `Span` extension `"wikipedia_url"` using the getter
  `get_wikipedia_url`.
- Iterate over the entities in the `doc` and output their Wikipedia URL.

<codeblock id="03_11">

- To get the string label of a span, use the `span.label_` attribute. This is
  the label predicted by the entity recognizer if the span is an entity span.
- Remember that extension attributes are available via the `._` property. For
  example, `doc._.has_color`.

</codeblock>

</exercise>

<exercise id="12" title="Components with extensions">

Extension attributes are especially powerful if they're combined with custom
pipeline components. In this exercise, you'll write a pipeline component that
finds country names and a custom extension attribute that returns a country's
capital, if available.

A phrase matcher with all countries is available as the variable `matcher`. A
dictionary of countries mapped to their capital cities is available as the
variable `CAPITALS`.

- Complete the `countries_component` and create a `Span` with the label `"GPE"`
  (geopolitical entity) for all matches.
- Add the component to the pipeline.
- Register the Span extension attribute `"capital"` with the getter
  `get_capital`.
- Process the text and print the entity text, entity label and entity capital
  for each entity span in `doc.ents`.

<codeblock id="03_12">

- The `Span` class takes four arguments: the `doc`, the `start` and `end` token
  index of the span and the `label`.
- Calling the `PhraseMatcher` on a `doc` returns a list of
  `(match_id, start, end)` tuples.
- To register a new extension attribute, use the `set_extension` method on the
  global class, e.g. `Doc`, `Token` or `Span`. To define a getter, use the
  `getter` keyword argument.
- Remember that extension attributes are available via the `._.` property. For
  example, `doc._.has_color`.

</codeblock>

</exercise>

<exercise id="13" title="Scaling and performance" type="slides">

<slides source="chapter3_04_scaling-performance">
</slides>

</exercise>

<exercise id="14" title="Processing streams">

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
