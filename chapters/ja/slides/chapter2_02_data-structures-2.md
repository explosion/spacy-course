---
type: slides
---

# データ構造(2): DocとSpanとToken

Notes: さて、語彙データと文字列ストアについて紹介したので、次は最も重要な概念であるデータ構造についてみていきましょう。
`Doc`と、そのビューである`Token`と`Span`です。

---

# Docオブジェクト

```python
# nlpオブジェクトを作成
from spacy.lang.ja import Japanese
nlp = Japanese()

# Docクラスをインポート
from spacy.tokens import Doc

# Docクラスのもととなるwordsとspacesを作成
words = ["こんにちは", "世界", "！"]
spaces = [False, False, False]

# docを手動で作る
doc = Doc(nlp.vocab, words=words, spaces=spaces)
```

Notes: `Doc`はspaCyにおける中心的なデータ構造の一つです。
`nlp`オブジェクトでテキストを処理すると、自動で作成されます。
しかし、`Doc`クラスから手動でインスタンス化することもできます。

`nlp`オブジェクトを作った後は、`spacy.tokens`から`Doc`クラスをインポートしましょう。

ここでは、docを3つの単語から作成しています。spacesはブール値のリストで、各単語の後に
スペースが続くかどうかを示しています。最後尾のトークンを含めて、全てのトークンがスペースに関する情報を持っています。

`Doc`クラスは3つの引数をとります。共有語彙データ、単語リスト、スペースリストです。

---

# Spanオブジェクト (1)

<img src="/span_indices.png" width="65%" alt="トークンインデックスを持つDoc内のSpanオブジェクトのイラスト" />

Notes: `Span`は1個以上のトークンからなる、docのスライスです。
`Span`は少なくとも3つの引数をとります。1つめは参照先のdoc、2つめは開始インデックス、
3つめは終了インデックスです。`Span`は終了インデックスのトークンを含まない（exclusive）ことを覚えておいてください！

---

# Spanオブジェクト (2)

```python
# DocとSpanクラスをインポート
from spacy.tokens import Doc, Span

# Docクラスのもととなるwordsとspacesを作成
words = ["こんにちは", "世界", "！"]
spaces = [False, False, False]

# docを手動で作成
doc = Doc(nlp.vocab, words=words, spaces=spaces)

# spanを手動で作成
span = Span(doc, 0, 2)

# ラベルがついたスパンを作成
span_with_label = Span(doc, 0, 2, label="GREETING")

# spanをdoc.entsに加える
doc.ents = [span_with_label]
```

Notes: `Span`オブジェクトを手動で作るために、`spacy.tokens`から`Span`クラスをインポートします。
それから、docと開始インデックス、終了インデックス、ラベル（オプショナル）を用いてクラスをインスタンス化します。

`doc.ents`は書き込み可能なので、spanオブジェクトのリストを用いて上書きし、固有表現を追加しましょう。

---

# ベストプラクティス

- `Doc`と`Span`はとても強力で、単語間や文間の参照や関係性を持っています
  - **結果を文字列として出力するのは、なるべく後の方にしましょう**
  - **トークン属性を使える場合は、それを使いましょう。** 例えば、`token.i`をトークンのインデックスとして使いましょう
- 忘れずに共有の`vocab`を渡すようにしましょう

Notes: 演習を始める前に、いくつかのトリックを紹介します。

`Doc`と`Span`はとても強力で、パフォーマンス面でも優れています。
これらは、単語間や文間の関係性、参照を提供します。

もし作成したアプリケーションで文字列の出力が必要な場合、docを文字列に変換するのは出来るだけ後の方にしましょう。
文字列に変換してしまうと、トークン間の関係性の情報を失ってしまいます。

一貫性を保つために、出来るだけ`Token`オブジェクトにすでに実装されている属性を用いましょう。
例えば、`token.i`を使ってトークンのインデックスを参照してください。

そして、共有の語彙データを渡すことを常に忘れないでください。

---

# Let's practice!

Notes: ではここで学んだことを試してみて、ゼロからdocやspanを作ってみましょう。
