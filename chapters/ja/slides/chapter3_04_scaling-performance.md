---
type: slides
---

# スケーリングとパフォーマンス

Notes: このレッスンでは、spaCyのパイプラインをなるべく速く実行し、大量のテキストを効率的に処理する裏技をご紹介します。

---

# 大量のテキストの処理

- `nlp.pipe`メソッドを使います
- テキストをストリームとして処理し、`Doc` オブジェクトを生成します
- テキストごとに `nlp` を呼び出すよりもはるかに速いです

**悪い例:**

```python
docs = [nlp(text) for text in LOTS_OF_TEXTS]
```

**良い例:**

```python
docs = list(nlp.pipe(LOTS_OF_TEXTS))
```

Notes: 大量のテキストを処理して大量の `Doc` オブジェクトを作成する必要がある場合、`nlp.pipe` メソッドを使うと大幅に高速化することができます。

このメソッドは、テキストをストリームとして処理し、`Doc` オブジェクトを生成します。

テキストをバッチ化するので、各テキストに対して単にnlpを呼び出すよりもはるかに高速です。

`nlp.pipe` は `Doc` オブジェクトを生成するジェネレータなので、ドキュメントのリストを取得するには、`list`を呼び出すことを忘れないようにしてください。

---

# コンテキストを使う(1)

- `nlp.pipe` で `as_tuples=True` を設定すると、`(text, context)` タプルを渡すことができます。
- 戻り値は`(doc, context)`タプルです。
- メタデータを `doc` に関連付けるのに便利です。

```python
data = [
    ("これは例文です", {"id": 1, "page_number": 15}),
    ("これは別の例文です", {"id": 2, "page_number": 16}),
]

for doc, context in nlp.pipe(data, as_tuples=True):
    print(doc.text, context["page_number"])
```

```out
これは例文です 15
これは別の例文です 16
```

Notes: `nlp.pipe` は、`as_tuples` を `True` に設定した場合、テキストとコンテキストのタプルを渡すことができます。

このメソッドは `Doc` とコンテキストのタプルを返します。

これは、テキストに関連付けられたIDやページ番号のような追加のメタデータを渡すのに便利です。

---

# コンテキストを使う(2)

```python
from spacy.tokens import Doc

Doc.set_extension("id", default=None)
Doc.set_extension("page_number", default=None)

data = [
    ("これは例文です", {"id": 1, "page_number": 15}),
    ("これは別の例文です", {"id": 2, "page_number": 16}),
]

for doc, context in nlp.pipe(data, as_tuples=True):
    doc._.id = context["id"]
    doc._.page_number = context["page_number"]
```

Notes: コンテキストのメタデータを拡張属性に追加することもできます。

この例では、`id` と `page_number` という2つの拡張子を登録しており、デフォルトは `None` です。

テキストを処理した後、コンテキストのメタデータで `doc` の拡張属性を上書きすることができます。

---

# トークナイザのみを使う(1)

<img src="/pipeline.png" width="90%" alt="spaCyパイプラインの図解">

- 全てのパイプラインを実行しないでください！

Notes: もう一つの一般的なシナリオをみていきます。他の処理を行うために既にモデルがロードされていますが、テキストのトークン化機能だけが必要な場合です。

不要な解析を大量に行ってしまうので、パイプライン全体を実行するのは不必要に時間がかかります。

---

# トークナイザのみを使う(2)

- `nlp.make_doc`を使ってテキストから`Doc`オブジェクトを作る

**悪い例:**

```python
doc = nlp("こんにちは！")
```

**良い例:**

```python
doc = nlp.make_doc("こんにちは！")
```

Notes: 
トークン化された `Doc` オブジェクトだけが必要な場合は、代わりに `nlp.make_doc` メソッドを使うことができます。

これは、spaCyが裏側でどのようにトークン化を行うかを示しています。
`nlp.make_doc`は、パイプラインコンポーネントを呼び出す前に、テキストを `Doc` に変換しています。

---

# パイプラインコンポーネントを無効化する

- パイプを一時的に無効にするには `nlp.disable_pipes` を使います。

```python
# タガーとパーサを無効化
with nlp.disable_pipes("tagger", "parser"):
    # テキストを処理し、固有表現をプリントする
    doc = nlp(text)
    print(doc.ents)
```

- `with`ブロックのあとに復元されます
- 残りのコンポーネントのみ実行します

Notes: spaCy では、`nlp.disable_pipes` コンテキストマネージャを使用してパイプラインコンポーネントを一時的に無効にすることもできます。

無効にするパイプラインコンポーネントの文字列名を1つ以上指定します。
例えば、固有表現抽出機能だけを使って `Doc` を処理したい場合は、一時的にタガーとパーサを無効にします。

`with` ブロックの後、無効化されたパイプラインコンポーネントは自動的に復元されます。

`with` ブロックでは、 spaCy は残りのコンポーネントのみを実行します。

（v2.3現在、日本語モデルには `tagger` コンポーネントが含まれていないため、左記コードは正常に動作しません。`nlp.disable_pipes("parser")` とすることでコードを実行することができます。）

---

# Let's practice!

Notes: それでは、演習の時間です。新しいメソッドを試して、より速く、より効率的になるようにコードを最適化してみましょう。
