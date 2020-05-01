---
title: '第1章: 単語やフレーズ、名前、概念の検索'
description:
  "この章では、spaCyの基本的なテキスト処理の方法を紹介します。
  データ構造や機械学習モデルの扱い方や、これらを用いてテキストの言語的特徴を抽出する方法を学んでいきます。"
prev: null
next: /chapter2
type: chapter
id: 1
---

<exercise id="1" title="はじめに" type="slides">

<slides source="chapter1_01_introduction-to-spacy">
</slides>

</exercise>

<exercise id="2" title="spaCyを使ってみる">

ではさっそく、spaCyを試していきましょう！ この演習では、[spaCyが対応している55以上の言語](https://spacy.io/usage/models#languages)のうちのいくつかをことができます。

### Part 1: 英語

- `English`クラスを`spacy.lang.en`からインポートし、`nlp`オブジェクトを作ってください。
- `doc`オブジェクトを作り、文字列をプリントしてください。

<codeblock id="01_02_01">
</codeblock>

### Part 2: ドイツ語

- `German`クラスを`spacy.lang.de`からインポートし、`nlp`オブジェクトを作ってください。
- `doc`オブジェクトを作り、文字列をプリントしてください。

<codeblock id="01_02_02">
</codeblock>

### Part 3: スペイン語

- `Spanish`クラスを`spacy.lang.es`からインポートし、`nlp`オブジェクトを作ってください。
- `doc`オブジェクトを作り、文字列をプリントしてください。

<codeblock id="01_02_03">
</codeblock>

</exercise>

<exercise id="3" title="ドキュメントとスパンとトークン">

`nlp`を文字列に適用すると、spaCyはまず文字列を分割し、`Doc`オブジェクトを作ります。
この演習では、`Doc`やそのビューである`Token`と`Span`について詳しく学んでいきます。

### Step 1

- `English`クラスをインポートし、`nlp`オブジェクトを作ってください。
- テキストを処理し、`Doc`オブジェクトである`doc`を作ってください。
- `doc`の最初のトークンを選び、`text`をプリントしてください。

<codeblock id="01_03_01">

Pythonのリストの要素をインデックスを使って取得するのと同じ方法を`Doc`に対して用いることができます。
例えば、`doc[4]`は位置4のトークン、つまりテキストの前から5番目のトークンを表します。
他の多くの言語と同様、Pythonではインデックスは1ではなく0から始まることに注意してください。

</codeblock>

### Step 2

- `English`クラスをインポートし、`nlp`オブジェクトを作ってください。
- テキストを処理し、`Doc`オブジェクトである`doc`を作ってください。
- "tree kangaroos"と"tree kangaroos and narwhals"のトークンに対応するスライスを`Doc`から作成してください。

<codeblock id="01_03_02">

`Doc`からスライスを作るには、Pythonのリストと同様、`:`記法を使います。
スライスの右端のインデックスのトークンは、スライスに _含まれない_ ことに注意してください。
つまり、`0:4`は、位置0,1,2,3のトークンを表し、位置4のトークンは含まれません。

</codeblock>

</exercise>

<exercise id="4" title="語彙の属性">

spaCyの`Doc`と`Token`オブジェクトと、その語彙属性（lexical attributes）を使って、
文字列の中からパーセンテージを表す部分を抜き出す方法をみていきます。
つまり、数字とパーセント記号からなる連続した二つのトークンを探す方法をみていきます。

- `Token`オブジェクトの`like_num`を使って、`doc`に含まれるトークンが数字っぽいかどうかを判定してください。
- `Doc`のうち、数字のトークンの次のトークンを取得してみてください。あるトークン`token`の次のトークンのインデックスは
  `token.i + 1`です。
- 次のトークンの文字列がパーセント記号（%）かどうかをチェックしてください。

<codeblock id="01_04">

トークンは、`doc`からインデックスを使って取得できます。
例えば、`doc[5]`は位置5のトークンを表します。

</codeblock>

</exercise>

<exercise id="5" title="機械学習モデル" type="slides">

<slides source="chapter1_02_statistical-models">
</slides>

</exercise>

<exercise id="6" title="Model packages" type="choice">

次のうち、spaCyのモデルパッケージに含まれて**いない**ものはどれでしょう？

<choice>
<opt text="言語、パイプライン、ライセンスが記載されているメタファイル">

全てのモデルには`meta.json`というメタファイルが含まれています。
これには、使用言語、ロードすべきパイプライン要素の名前のほか、モデル名、バージョン、ライセンス、データソース、作者、制度の数値（もしあれば）
等が記載されています。

</opt>
<opt text="機械学習モデルの重み">

品詞タグや依存関係ラベル、固有表現等の言語特徴量の抽出をするため、機械学習モデルの重みが含まれています。

</opt>
<opt correct="true" text="機械学習モデル作成につかったラベル付きデータ">

機械学習モデルは、データをもとに学習を行い、モデルの重みを更新し、その重みを用いて
汎化した予測を行います。
つまり、予測には学習データが不必要なので、モデルパッケージには含まれていません。

</opt>
<opt text="モデルの語彙データの文字列と、そのハッシュ値">

モデルパッケージには、語彙データの要素とそのハッシュ値のマッピングが保存されている`strings.json`という
ファイルが含まれています。
ハッシュ値を用いることで、spaCyは内部で効率的にデータをやり取りしており、文字列は必要な場面でのみ参照されます。

</opt>
</choice>

</exercise>

<exercise id="7" title="モデルのロード">

このコースで使うモデルは、事前にインストールされているものです。
spaCyの機械学習モデルの詳細やインストール方法については、[公式ドキュメント](https://spacy.io/usage/models)をみてください。

- `spacy.load`を使って、小サイズの英語モデル`"en_core_web_sm"`をロードしてください。
- テキストを処理し、文字列を出力してください。

<codeblock id="01_07">

モデルをロードするには、`spacy.load`関数にモデル名を渡してください。
モデル名は、言語や使用されたトレーニングデータによって異なるので、適切なものを選んで使ってください。

</codeblock>

</exercise>

<exercise id="8" title="言語特徴量の解析">

さて、では実際にspaCyの学習済みモデルを用いて、解析結果をみてみましょう。
お気軽にご自分の文章で試してみてください！
タグやラベルの意味を知るには、`spacy.explain`を使ってください。
例えば、`spacy.explain("PROPN")` or `spacy.explain("GPE")`とすることで意味を出力することができます。

### パート1

- `nlp`オブジェクトでテキストを処理し、`doc`を作ってください
- それぞれのトークンについて、文字列、`.pos_`（品詞タグ）、`.dep_`（依存関係ラベル）をプリントしてください。

<codeblock id="01_08_01">

`doc`オブジェクトを作るには、`nlp`オブジェクトを文字列に対して呼び出します。
トークンの属性の文字列を出力するには、属性名にアンダースコアをつけることを忘れないで下さい。

</codeblock>

### パート2

- テキストを処理し、`doc`オブジェクトを作ってください。
- `doc.ents`をイテレートし、固有表現の文字列とラベルを出力してください。
- Iterate ove the `doc.ents` and print the entity text and `label_` attribute.

<codeblock id="01_08_02">

`doc`オブジェクトを作るには、`nlp`オブジェクトを文字列に対して呼び出します。
トークンの属性の文字列を出力するには、属性名にアンダースコアをつけることを忘れないで下さい。

</codeblock>

</exercise>

<exercise id="9" title="Predicting named entities in context">

機械学習モデルの出力は常に正しいとは限りません。
出力は、学習データや入力データに依存します。
一つ例をみてみましょう。

- `nlp`オブジェクトでテキストを処理してください。
- 固有表現をイテレートし、文字列とラベルを出力してください。
- モデルは「iPhone X」を正しく抽出できないようです。手動でスパンを作ってみてください。

<codeblock id="01_09">

- `doc`オブジェクトを作るには、文に対して`nlp`オブジェクトを呼び出してください。固有表現は
  `doc.ents`プロパティから取得することができます。
- `Span`オブジェクトを作る最も簡単な方法は、スライス記法を使うことです。例えば、`doc[5:10]`は位置5から位置9までのトークンを示します。
  右端は含まれないことに注意してください。

</codeblock>

</exercise>

<exercise id="10" title="ルールベースマッチ" type="slides">

<slides source="chapter1_03_rule-based-matching">
</slides>

</exercise>

<exercise id="11" title="Using the Matcher">

Let's try spaCy's rule-based `Matcher`. You'll be using the example from the
previous exercise and write a pattern that can match the phrase "iPhone X" in
the text.

- Import the `Matcher` from `spacy.matcher`.
- Initialize it with the `nlp` object's shared `vocab`.
- Create a pattern that matches the `"TEXT"` values of two tokens: `"iPhone"`
  and `"X"`.
- Use the `matcher.add` method to add the pattern to the matcher.
- Call the matcher on the `doc` and store the result in the variable `matches`.
- Iterate over the matches and get the matched span from the `start` to the
  `end` index.

<codeblock id="01_11">

- The shared vocabulary is available as the `nlp.vocab` attribute.
- A pattern is a list of dictionaries keyed by the attribute names. For example,
  `[{"TEXT": "Hello"}]` will match one token whose exact text is "Hello".
- The `start` and `end` values of each match describe the start and end index of
  the matched span. To get the span, you can create a slice of the `doc` using
  the given start and end.

</codeblock>

</exercise>

<exercise id="12" title="Writing match patterns">

In this exercise, you'll practice writing more complex match patterns using
different token attributes and operators.

### Part 1

- Write **one** pattern that only matches mentions of the _full_ iOS versions:
  "iOS 7", "iOS 11" and "iOS 10".

<codeblock id="01_12_01">

- To match a token with an exact text, you can use the `TEXT` attribute. For
  example, `{"TEXT": "Apple"}` will match tokens with the exact text "Apple".
- To match a number token, you can use the `"IS_DIGIT"` attribute, which will
  only return `True` for tokens consisting of only digits.

</codeblock>

### Part 2

- Write **one** pattern that only matches forms of "download" (tokens with the
  lemma "download"), followed by a token with the part-of-speech tag `"PROPN"`
  (proper noun).

<codeblock id="01_12_02">

- To specify a lemma, you can use the `"LEMMA"` attribute in the token pattern.
  For example, `{"LEMMA": "be"}` will match tokens like "is", "was" or "being".
- To find proper nouns, you want to match all tokens whose `"POS"` value equals
  `"PROPN"`.

</codeblock>

### Part 3

- Write **one** pattern that matches adjectives (`"ADJ"`) followed by one or two
  `"NOUN"`s (one noun and one optional noun).

<codeblock id="01_12_03">

- To find adjectives, look for tokens whose `"POS"` value equals `"ADJ"`. For
  nouns, look for `"NOUN"`.
- Operators can be added via the `"OP"` key. For example, `"OP": "?"` to match
  zero or one time.

</codeblock>

</exercise>
