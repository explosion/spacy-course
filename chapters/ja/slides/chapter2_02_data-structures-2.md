---
type: slides
---

# データ構造(2): DocとSpanとToken

Notes: さて、語彙データと文字列ストアについて紹介し終えたので、次は最も重要なデータ構造をみていきましょう。
`Doc`と、そのビューである`Token`と`Span`です。
Now that you know all about the vocabulary and string store, we can take
a look at the most important data structure: the `Doc`, and its views `Token`
and `Span`.

---

# The Doc object

```python
# nlpオブジェクトを作成
from spacy.lang.en import English
nlp = English()

# Docクラスをインポート
from spacy.tokens import Doc

# Docクラスのもととなるwordsとspacesを作成
words = ["Hello", "world", "!"]
spaces = [True, False, False]

# docを手動で作る
doc = Doc(nlp.vocab, words=words, spaces=spaces)
```

Notes: `Doc`はspaCyにおける中心的なデータ構造の一つです。
これは`nlp`オブジェクトでテキストを処理すれば、自動で作られます。
しかし、`Doc`クラスから手動でインスタンス化することもできます。

`nlp`オブジェクトを作った後は、`spacy.tokens`から`Doc`クラスをインポートしましょう。

ここでは、docを3つの単語から作成しています。spacesはブール値のリストで、各単語の後に
スペースが続くかどうかを示しています。最後尾のトークンを含めて、全てのトークンがスペースに関する
情報を持っています。

`Doc`クラスは3つの引数をとります。共有語彙データ、単語リスト、スペースリストです。

---

# Spanオブジェクト (1)

<img src="/span_indices.png" width="65%" alt="トークンインデックスを持つDoc内のSpanオブジェクトのイラスト" />

Notes: `Span`は0個以上のトークンからなる、docのスライスです。
`Span`は少なくとも3つの引数をとります。1つめは参照先のdoc、2つめは開始インデックス、
3つめは終了インデックスです。`Span`は終了インデックスのトークンを含まない（exclusive）ことを覚えておいてください！

---

# Spanオブジェクト (2)

```python
# DocとSpanクラスをインポート
from spacy.tokens import Doc, Span

# Docクラスのもととなるwordsとspacesを作成
words = ["Hello", "world", "!"]
spaces = [True, False, False]

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

# Best practices

- `Doc` and `Span` are very powerful and hold references and relationships of
  words and sentences
  - **Convert result to strings as late as possible**
  - **Use token attributes if available** – for example, `token.i` for the token
    index
- Don't forget to pass in the shared `vocab`

Notes: A few tips and tricks before we get started:

The `Doc` and `Span` are very powerful and optimized for performance. They give
you access to all references and relationships of the words and sentences.

If your application needs to output strings, make sure to convert the doc as
late as possible. If you do it too early, you'll lose all relationships between
the tokens.

To keep things consistent, try to use built-in token attributes wherever
possible. For example, `token.i` for the token index.

Also, don't forget to always pass in the shared vocab!

---

# Let's practice!

Notes: Now let's try this out and create some docs and spans from scratch.
