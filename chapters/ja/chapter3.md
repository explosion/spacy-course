---
title: '第3章: パイプライン処理'
description:
  "この章では spaCy の処理パイプラインについて知っておくべきことをすべて紹介します。テキストを処理するときに裏側で起こっていること、自分でコンポーネントを書いてパイプラインに追加する方法、拡張属性を使用してdocやスパン、トークンに独自のメタデータを追加する方法、などを学びます。"
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
doc = nlp("これは文章です。")
```

<choice>

<opt text="タグづけ、依存関係解析、固有表現抽出を行い、トークナイズしている">

トークナイザはテキストを`Doc`オブジェクトに変換するため、常に全てのパイプラインの前に適用されます。
そしてパイプラインには、タガー、パーサー、固有表現抽出器は必ずしも必要ありません。

</opt>

<opt text="テキストをトークナイズし、パイプラインのそれぞれのコンポーネントを順番に適用している" correct="true">

トークナイザはテキストを`Doc`オブジェクトに変換します。
spaCyはパイプライン内のすべてのコンポーネントを順に`Doc`に適用します。

</opt>

<opt text="spaCyのサーバに接続し、結果を計算して返している">

spaCyはローカルマシン上で全てを計算するので、サーバに接続する必要はありません。

</opt>

<opt text="言語を初期化し、パイプラインを追加し、モデルの重みをロードしている">

`spacy.load()` を呼び出してモデルをロードすると、言語の初期化、パイプラインの追加モデルの重みのロードを行います。
テキストに対して`nlp` オブジェクトを呼び出すとき、モデルは既にロードされています。

</opt>

</exercise>

<exercise id="3" title="パイプラインの中身">

日本語の小サイズのモデルのパイプラインの中身を見てみましょう！

- `ja_core_news_sm`モデルを読み込み、`nlp` オブジェクトを作成します。
- `nlp.pipe_names`を用いてパイプラインのコンポーネント名を表示します。
- `nlp.pipeline`を用いて`(name, component)`タプルからなる全てのパイプラインを表示します。

<codeblock id="03_03">

コンポーネント名のリストは`nlp.pipe_names`属性で入手できます。
`(name, component)`タプルからなるパイプラインのリストは`nlp.pipeline`から取得できます。

</codeblock>

</exercise>

<exercise id="4" title="カスタムのパイプラインコンポーネント" type="slides">

<slides source="chapter3_02_custom-pipeline-components">
</slides>

</exercise>

<exercise id="5" title="カスタムコンポーネントのユースケース">

これらの問題のうち、カスタムコンポーネントによって解決できるものはどれですか？該当するものをすべて選択してください。

1. 事前に訓練されたモデルを更新し、その予測を改善する
2. トークンとその属性に基づいてオリジナルの値を計算する
3. 辞書に基づいた固有表現の追加などを行う
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
足りない部分を埋め、完成させてください。

- コンポーネントの関数を`doc`の長さを用いて完成させます。
- 既存のパイプラインの先頭に`length_component`を追加します。
- 新しいパイプラインを試してみて、`nlp` オブジェクトを使ってテキストを処理してみてください。
  例文：「これは文章です。」

<codeblock id="03_06">

- `Doc`オブジェクトの長さを取得するには、Pythonの組み込みの`len()`メソッドが使えます。
- コンポーネントをパイプラインに追加するには`nlp.add_pipe`メソッドを使います。
  キーワード引数`first`に`True`を指定すると、他のすべてのコンポーネントよりも前に追加されます。
- テキストを処理するには、`nlp`オブジェクトを呼び出します。

</codeblock>

</exercise>

<exercise id="7" title="複雑なコンポーネント">

この演習では、`PhraseMatcher`を使って文中の動物の名前を見つけ、一致したスパンを`doc.ents`に追加するカスタムコンポーネントを書いてみましょう。
動物のパターンを持つ `PhraseMatcher` はすでに変数 `matcher` として作成されています。

- カスタムコンポーネントを定義し、`doc`に `matcher` を適用します。
- 各マッチに対して `Span` を作成し、`"ANIMAL"` にラベルIDを割り当て、`doc.ents` を新しいスパンで上書きします。
- 新しいコンポーネントを `"ner"` コンポーネントの後にパイプラインに追加します。
- テキストを処理し、`doc.ents`内の固有表現の文字列とラベルを表示します。

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
- `"スペイン"`について更新し、すべてのトークンを表示します。

<codeblock id="03_09_01">

拡張属性は`._`からアクセスできることを思い出してください。例えば、`doc._.has_color`のようにします。

</codeblock>

### ステップ3

- `Token.set_extension`を使って`"reversed"`を登録してください（getter `get_reversed`）。
- それぞれのトークンについて、表示してください。

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
- `doc[0:3]`に対して、`"strong"`を使って呼び出します。

<codeblock id="03_10_02">

- メソッドの拡張子は1つ以上の引数を取ることができます。例えば、`doc._.some_method("argument")`のようになります。
- メソッドに渡される最初の引数は、呼び出されたメソッドの親である `Doc`, `Token`, `Span` オブジェクトです。

</codeblock>

</exercise>

<exercise id="11" title="固有表現と拡張属性">

この演習では、拡張属性とモデルの予測を組み合わせて、スパンが人、組織、または場所の場合にWikipediaの検索URLを返すゲッター属性を作成します。

- ゲッター `get_wikipedia_url` を完成させ、ラベルのリストにスパンのラベルが含まれている場合にのみURLを返すようにします。
- ゲッター `get_wikipedia_url` を用いて`Span`の拡張子 `"wikipedia_url"` を設定します。
- `doc`内の固有表現をイテレートし、WikipediaのURLを表示します。

<codeblock id="03_11">

- スパンの文字列ラベルを取得するには、`span.label_` 属性を使用します。これは、スパンが固有表現である場合に固有表現抽出器が予測するラベルです。
- 拡張属性は`._`プロパティで利用できることを覚えておいてください。例えば、`doc._.has_color`とします。

</codeblock>

</exercise>

<exercise id="12" title="拡張属性とコンポーネント">

拡張属性は、カスタムパイプラインコンポーネントと組み合わせて使用すると強力です。この演習では、国の名前を検索するパイプラインコンポーネントと、国の首都を返すカスタム拡張属性を書いてみましょう。

変数 `matcher` に、すべての国を含むPhraseMatcherがはいっています。
国と首都の関係の辞書が変数 `CAPITALS` として利用できます。

- `countries_component`を完成させ、すべてのマッチに対して `"GPE"` (地政学的実体) のラベルを持つ `Span` を作成します。
- コンポーネントをパイプラインに追加します。
- ゲッター `get_capital` にスパンの拡張属性 `"capital"` を登録します。
- テキストを処理し、`doc.ents`に入っている各固有表現スパンのテキスト、ラベル、キャピタルを表示します。

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

この演習では、より効率的なテキスト処理のために `nlp.pipe` を使います。
`nlp` オブジェクトはすでに作成されています。アメリカの人気ファストフードチェーンに関するツイートのリストが変数 `TEXTS` に入っています。

### パート1

- 例題を書き換えて `nlp.pipe` を使うようにしてください。テキストを繰り返し処理するのではなく、`nlp.pipe`によって生成された `doc` オブジェクトを繰り返し処理するようにしてください。

<codeblock id="03_14_01">

- `nlp.pipe` を使うと、最初の2行のコードを1つにまとめることができます。
- `nlp.pipe` は `TEXTS` を受け取り、`doc`をイテレートできるオブジェクトを生成します。

</codeblock>

### パート2

- 例を書き換えて `nlp.pipe` を使ってください。
  結果をリストにするために、`list()` を呼び出すことを忘れないでください。

<codeblock id="03_14_02"></codeblock>

### パート3

- 例を書き換えて `nlp.pipe` を使ってください。
  結果をリストにするために、`list()` を呼び出すことを忘れないでください。

<codeblock id="03_14_03"></codeblock>

</exercise>

<exercise id="15" title="データをコンテキストで処理する">

この演習では、拡張属性を使用して、著者と書籍のメタ情報を追加します。

変数 `DATA` には `[text, context]` の例のリストが入っています。
テキストは有名な書籍からの引用であり、コンテキストはキー `"author"`と `"book"` を持つ辞書です。

- `set_extension`メソッドを用いて `Doc` に拡張属性 `"author"`と `"book"`を登録します。
- `nlp.pipe` を用いて `as_tuples=True` として `DATA` の `[text, context]` ペアを処理します。
- `doc._.book` と `doc._.author` を、コンテキストとして渡された情報を用いて上書きします。

<codeblock id="03_15">

- `Doc.set_extension`メソッドは2つの引数を取ります。属性の文字列名と、デフォルト、ゲッター、セッター、メソッドを示すキーワード引数です。例えば、`default=True` のようにします。
- `as_tuples` が `True` に設定されている場合、`nlp.pipe` メソッドは `(text, context)` タプルのリストを受け取り、`(doc, context)` タプルを生成します。

</codeblock>

</exercise>

<exercise id="16" title="処理対象の選択">

この演習では、`nlp.make_doc` と `nlp.disable_pipes` メソッドを使用して、テキストを処理する際に実行するコンポーネントを選択します。

### パート1

- `nlp.make_doc`を使ってテキストのトークン化のみを実行するようにコードを書き換えます。

<codeblock id="03_16_01">

`nlp.make_doc`メソッドはテキストに対して呼び出すことができ、 `nlp` オブジェクトと同様に `Doc` を返します。

</codeblock>

### パート2

- `nlp.disable_pipes` メソッドを使ってパーサを無効にします。
- テキストを処理して `doc` 内のすべての固有表現を表示します。

<codeblock id="03_16_02">

`nlp.disable_pipes` メソッドは可変数の引数をとります。例えば、`nlp.disable_pipes("ner")` は固有表現抽出器を無効にします。

</codeblock>

</exercise>
