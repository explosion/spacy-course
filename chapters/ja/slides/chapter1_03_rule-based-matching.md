---
type: slides
---

# ルールベースマッチ

Notes: この演習では、spaCyのmatcherをみていきましょう。
matcherを使えば、ルールベースで単語やフレーズを見つける処理を書くことができます。

---

# 正規表現じゃだめなの？

- 単なる文字列ではなく、`Doc`オブジェクトにマッチします
- トークンや、その属性にマッチします
- モデルの予測結果も使えます
- 例："duck"（動詞） vs. "duck"（名詞）

Notes: 正規表現と異なり、単なる文字列ではなく`Doc`や`Token`にマッチします。

そして正規表現よりも柔軟です。文字列のみならず、語彙属性をベースに検索することができます。

さらに、モデルの予測結果をもとにしたルールを書くこともできます。

例えば、「duck」という単語が名詞ではなく動詞の時のみマッチする、というルールがかけます。

---

# マッチのパターン

- トークンごとの辞書のリスト

- トークン文字列に完全一致するもののみマッチ　

```python
[{"TEXT": "iPhone"}, {"TEXT": "X"}]
```

- 語彙属性にマッチ

```python
[{"LOWER": "iphone"}, {"LOWER": "x"}]
```

- 色々な属性をもとにマッチ

```python
[{"LEMMA": "buy"}, {"POS": "NOUN"}]
```

Notes: マッチのパターンは辞書のリストで表します。
それぞれの辞書は、各トークンを表します。
辞書のキーはトークンの属性を、辞書の値はマッチする値を表します。

この例では、「iPhone」と「X」の二つのトークンからなるトークン列を探しています。

文字列以外の属性にマッチさせることもできます。
ここでは、小文字化した場合に「iphone」と「x」からなるトークン列を探しています。

さらに、モデルの予測結果をもとにマッチさせることもできます。
ここでは、見出し語が「buy」、名詞のトークンの組を探しています。
つまり、「buying milk」や「bought flowers」等にマッチします。

---

# Using the Matcher (1)

```python
import spacy

# Matcherをインポート
from spacy.matcher import Matcher

# モデルをロードし、nlpオブジェクトを作成
nlp = spacy.load("en_core_web_sm")

# matcherを共有語彙データを用いて初期化
matcher = Matcher(nlp.vocab)

# パターンをmatcherに追加
pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]
matcher.add("IPHONE_PATTERN", None, pattern)

# テキストを処理
doc = nlp("Upcoming iPhone X release date leaked")

# matcherをdocに対して呼び出し
matches = matcher(doc)
```

Notes: パターンを使うには、まず最初に`spacy.matcher`からmatcherをインポートします。

そして、モデルをロードし`nlp`オブジェクトを作成します。

matcherは共有語彙データ`nlp.vocab`を用いて初期化します。
これについては後ほど詳しくみていきます。とりあえず、このようにして初期化する必要があると覚えておいてください。

パターンは、`matcher.add`メソッドを用いて登録します。
第一引数は、それぞれのパターンを識別するためのユニークIDです。
第二引数は、オプショナルなコールバック関数です。
今は必要ないので、`None`を与えておきます。
第三引数はパターンです。

パターンをマッチさせるには、docオブジェクトに対してmatcherを呼び出します。

matcherを呼び出すと、マッチの結果がかえってきます。

---

# Matcherをつかう（2）

```python
# matcherをdocに対して呼びだす
doc = nlp("Upcoming iPhone X release date leaked")
matches = matcher(doc)

# 結果をイテレートする
for match_id, start, end in matches:
    # Get the matched span
    matched_span = doc[start:end]
    print(matched_span.text)
```

```out
iPhone X
```

- `match_id`: パターン名のハッシュ値
- `start`: マッチしたスパンの開始インデックス
- `end`: マッチしたスパンの終了インデックス

Notes: matcherをdocオブジェクトに対して呼び出すと、タプルのリストがかえってきます。

それぞれのタプルは、マッチID、マッチしたスパンの開始インデックス、終了インデックスの3つの要素からなります。

この返り値をイテレートし、開始インデックスと終了インデックスで`doc`をスライスすることで、`Span`オブジェクトを作ることができます。

---

# 語彙属性のマッチ

```python
pattern = [
    {"IS_DIGIT": True},
    {"LOWER": "fifa"},
    {"LOWER": "world"},
    {"LOWER": "cup"},
    {"IS_PUNCT": True}
]
```

```python
doc = nlp("2018 FIFA World Cup: France won!")
```

```out
2018 FIFA World Cup:
```

Notes: これは、語彙属性を用いたより複雑なマッチの例です。

次の5つからなるトークン列を探索しています：

数字からなるトークン

3つのトークン「fifa」、「world」、「cup」（ただし大文字小文字を区別しない）

句読点記号

このパターンは、「2018 FIFA World Cup:」というトークンにマッチします。

---

# その他のトークン属性のマッチ

```python
pattern = [
    {"LEMMA": "love", "POS": "VERB"},
    {"POS": "NOUN"}
]
```

```python
doc = nlp("I loved dogs but now I love cats more.")
```

```out
loved dogs
love cats
```

Note: この例では、次の2つのトークンからなる列を探索しています：

見出し語が「love」+名詞

このパターンは「loved dogs」と「love cats」にマッチします。

---

# 演算子と量指定子を使う(1)

```python
pattern = [
    {"LEMMA": "buy"},
    {"POS": "DET", "OP": "?"},  # Optional: 0個か1個にマッチ
    {"POS": "NOUN"}
]
```

```python
doc = nlp("I bought a smartphone. Now I'm buying apps.")
```

```out
bought a smartphone
buying apps
```

Notes: 演算子と量指定子を使うと、マッチするトークンの量を指定することができます。
これらは、「OP」キーによって指定します。

ここで、「?」演算子はトークンのマッチをオプショナルにしています。
つまりこのパターンは、
見出し語の「buy」+冠詞0個か1個+名詞、
にマッチします。

---

# 演算子と量指定子を使う(2)

| Example       | Description                  |
| ------------- | ---------------------------- |
| `{"OP": "!"}` | 否定：0個にマッチ |
| `{"OP": "?"}` | Optional: 0個か1個にマッチ |
| `{"OP": "+"}` | 1個以上にマッチ |
| `{"OP": "*"}` | 0個以上にマッチ |

Notes: 「OP」には以下のいずれかを指定することができます：

「!」トークンの否定。0個にマッチします。

「?」Optional。0個か1個にマッチします。

「+」1個以上にマッチします。

「\*」0個以上にマッチします。

演算子を使えばより強力なパターンを作ることができますが、より複雑になってしまいます。うまく使いましょう。

---

# Let's practice!

Notes: トークンベースのマッチングは、情報抽出の可能性を大きく広げてくれます。
それでは、実際にいくつかのパターンを書いて試してみましょう。
