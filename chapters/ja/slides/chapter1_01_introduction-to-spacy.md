---
type: slides
---

# はじめに

Notes: こんにちは、私はInesです！spaCyはPythonの先進的な自然言語処理ライブラリで、私はそのコアデベロッパーの一人です。

このレッスンでは、spaCyのもっとも重要なコンセプトや、spaCyの使い方を紹介していきます。

---

# nlpオブジェクト

```python
# 英語の言語クラスをインポート
from spacy.lang.en import English

# nlpオブジェクトを作成
nlp = English()
```

- 言語処理パイプラインを管理
- 単語分割等、言語依存のルールを管理

Notes: `nlp`はspaCyの中心的なオブジェクトで、言語処理のパイプラインを管理します。

例えば、英語の`nlp`オブジェクトを作成するには、`spacy.lang.en`から`English`クラスをインポートし、
インスタンス化します。インスタンス化した「nlp」は普通の関数のように使ってテキストを解析できます。

`nlp`は全ての言語処理コンポーネントをパイプライン上に保持しています。

また、`nlp`は単語分割のルールや句読点等、言語依存のデータも持っています。英語以外にも、日本語やドイツ語等、
様々な言語クラスが`spacy.lang`に実装されています。

---

# Docオブジェクト

```python
# nlpを用いて、テキストを処理することで作成
doc = nlp("Hello world!")

# Docからtokenを取り出す
for token in doc:
    print(token.text)
```

```out
Hello
world
!
```

Notes: `nlp`を用いてテキストを処理すると、`Doc`オブジェクトが作成されます。
（Docは「document」の略です。）
この`Doc`は非破壊的に作成され、入力テキストに関する構造化された情報を持っています。

`Doc`はリストのようなPythonのシーケンスのように扱うことができるので、トークンをイテレートしたり、
インデックスでトークンを取得できます。これについては、後でもう少し詳しくみていきます！

---

# Tokenオブジェクト

<img src="/doc.png" alt="Illustration of a Doc object containing four tokens" width="50%" />

```python
doc = nlp("Hello world!")

# インデックスでトークンを取得
token = doc[1]

# トークンの文字列を .text属性を使って取得
print(token.text)
```

```out
world
```

Notes: `Token`オブジェクトは、単語や句読点等、テキストのトークンの情報を持っています。

インデックスを用いて、特定の場所のトークンを`Doc`から取得できます。

`Token`の属性を使うことで、`Token`に関する様々な情報を得られます
例えば、`.text`属性を使うことで、トークンの生文字列を取得できます。

---

# Spanオブジェクト

<img src="/doc_span.png" width="50%" alt="Illustration of a Doc object containing four tokens and three of them wrapped in a Span" />

```python
doc = nlp("Hello world!")

# `Doc`オブジェクトからスライスで`Span`オブジェクトを取得
span = doc[1:3]

# スパンの文字列を .text属性で得る
print(span.text)
```

```out
world!
```

Notes: `Span`オブジェクトは`Doc`オブジェクトのスライスで、複数の`Token`からなります。
`Span`は単なるビューであり、それ自体は何のデータも持っていません。

`Span`オブジェクトを作成するには、Pythonのスライス記法を使います。
例えば、`1:4`は位置1から位置3のトークンからなる`Span`オブジェクトを作ります。
（位置4のトークンは含まれないことに注意してください）

---

# 語彙の属性

```python
doc = nlp("It costs $5.")
```

```python
print("Index:   ", [token.i for token in doc])
print("Text:    ", [token.text for token in doc])

print("is_alpha:", [token.is_alpha for token in doc])
print("is_punct:", [token.is_punct for token in doc])
print("like_num:", [token.like_num for token in doc])
```

```out
Index:    [0, 1, 2, 3, 4]
Text:     ['It', 'costs', '$', '5', '.']

is_alpha: [True, True, False, False, False]
is_punct: [False, False, False, False, True]
like_num: [False, False, False, True, False]
```

Notes: ここでは、いくつかのトークンの属性を紹介します。

`i` は`Token`が含まれる`Doc`オブジェクトにおけるインデックスを表します。

`text`はトークンの文字列です。

`is_alpha`はトークンの文字列がアルファベットからなるかどうか、`is_punct`は句読点かどうか、`like_num`は数字に似ているか（例えば"10"や"ten"）、を表すブール値です。

これらの属性は、語彙のエントリを参照しており、文脈に依存しないため、語彙属性（lexical attributes）と呼ばれます。

---

# Let's practice!

Notes: では実際に、spaCyを使ってテキストを処理してみましょう！
