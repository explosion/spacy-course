---
type: slides
---

# 機械学習モデル

Notes: それでは、`nlp`オブジェクトを強化していきましょう！

この章では、spaCyの機械学習モデルの使い方をみていきます。

---

# 機械学習モデルとは？

- _文脈をもとに_ 言語の特徴を抽出するための手法です
    - 品詞タグ付け
    - 依存構造解析
    - 固有表現抽出
- ラベル付けされたデータを用いて訓練します
- さらにデータを用意することで、予測結果の調整をすることができます

Notes: 言語解析したい対象が文脈に依存することはよくあります。
例えば、ある単語が動詞かどうかの判別や、テキストのある区間が人の名前を示すかどうかの判別などです。

spaCyは機械学習モデルによって、文脈依存の特徴量を抽出することができます。
品詞のタグ付けや依存構造解析、固有表現抽出などがそれに当たります。

機械学習モデルは、大量のラベル付きデータによって訓練されます。

さらにデータを用意することで、予測結果の修正をすることができます。
例えば、特定の分野のデータを用いることで、その分野でのパフォーマンスをあげることができます。

---

# モデルパッケージ

<img src="/package.png" alt="A package with the label en_core_web_sm" width="30%" align="right" />

```bash
$ python -m spacy download en_core_web_sm
```

```python
import spacy

nlp = spacy.load("en_core_web_sm")
```

- バイナリ化されたモデルパラメータ
- 語彙データ
- メタデータ（言語、パイプライン）

Notes: spaCyには、`spacy download`コマンドを使ってダウンロードできる学習済みモデルがたくさんあります。
例えば、"en_core_web_sm"パッケージは、spaCyの中心的な機能が全て詰まった、Web文章で訓練された小さなサイズの英語用モデルです。

`spacy.load`は、モデルパッケジをロードし、`nlp`オブジェクトを返す関数です。

パッケージにはモデルのパラメータが含まれており、spaCyはこれを用いて予測を行います。

モデルパッケージにはこれらの他にも、語彙データやメタデータが含まれています。
メタデータは、spaCyにどの言語クラスを使うかを伝えたり、処理パイプラインの設定方法が記載されています。

---

# 品詞タグの予測

```python
import spacy

# 英語のモデル（小サイズ）をロード
nlp = spacy.load("en_core_web_sm")

# テキストを処理
doc = nlp("She ate the pizza")

# tokenを順に処理
for token in doc:
    # テキストと、品詞タグの予測結果をプリント
    print(token.text, token.pos_)
```

```out
She PRON
ate VERB
the DET
pizza NOUN
```

Notes: それでは、モデルの予測結果をみていきましょう。
この例では、spaCyを使って品詞タグ（文脈に依存した単語のタイプ）を予測しています。

まずはじめに、小サイズの英語モデルをロードし、`nlp`変数に格納します。

次に、"She ate the pizza"というテキストを解析します。

最後に`doc`内のそれぞれの`token`に対して、テキストと、予測結果の品詞タグが格納されている`.pos_`属性をプリントします。

spaCyでは、文字列が格納されている属性の名前は通常、アンダースコア　_ で終わり、
アンダースコアの無い属性はIDを返します。

この例では、モデルは正しく"ate"を動詞、"pizza"を名詞と判断できています。

---

# Predicting Syntactic Dependencies

```python
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)
```

```out
She PRON nsubj ate
ate VERB ROOT ate
the DET det pizza
pizza NOUN dobj ate
```

Notes: In addition to the part-of-speech tags, we can also predict how the words
are related. For example, whether a word is the subject of the sentence or an
object.

The `.dep_` attribute returns the predicted dependency label.

The `.head` attribute returns the syntactic head token. You can also think of it
as the parent token this word is attached to.

---

# Dependency label scheme

<img src="/dep_example.png" alt="Visualization of the dependency graph for 'She ate the pizza'" />

| Label     | Description          | Example |
| --------- | -------------------- | ------- |
| **nsubj** | nominal subject      | She     |
| **dobj**  | direct object        | pizza   |
| **det**   | determiner (article) | the     |

Notes: To describe syntactic dependencies, spaCy uses a standardized label
scheme. Here's an example of some common labels:

The pronoun "She" is a nominal subject attached to the verb – in this case, to
"ate".

The noun "pizza" is a direct object attached to the verb "ate". It is eaten by
the subject, "she".

The determiner "the", also known as an article, is attached to the noun "pizza".

---

# Predicting Named Entities

<img src="/ner_example.png" alt="Visualization of the named entities in 'Apple is looking at buying U.K. startup for $1 billion'" width="80%" />

```python
# Process a text
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

# Iterate over the predicted entities
for ent in doc.ents:
    # Print the entity text and its label
    print(ent.text, ent.label_)
```

```out
Apple ORG
U.K. GPE
$1 billion MONEY
```

Notes: Named entities are "real world objects" that are assigned a name – for
example, a person, an organization or a country.

The `doc.ents` property lets you access the named entities predicted by the
model.

It returns an iterator of `Span` objects, so we can print the entity text and
the entity label using the `.label_` attribute.

In this case, the model is correctly predicting "Apple" as an organization,
"U.K." as a geopolitical entity and "\$1 billion" as money.

---

# Tip: the explain method

Get quick definitions of the most common tags and labels.

```python
spacy.explain("GPE")
```

```out
'Countries, cities, states'
```

```python
spacy.explain("NNP")
```

```out
'noun, proper singular'
```

```python
spacy.explain("dobj")
```

```out
'direct object'
```

Notes: A quick tip: To get definitions for the most common tags and labels, you
can use the `spacy.explain` helper function.

For example, "GPE" for geopolitical entity isn't exactly intuitive – but
`spacy.explain` can tell you that it refers to countries, cities and states.

The same works for part-of-speech tags and dependency labels.

---

# Let's practice!

Notes: Now it's your turn. Let's take a look at spaCy's statistical models and
their predictions.
