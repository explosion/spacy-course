---
type: slides
---

# 機械学習モデル

Notes: それでは、`nlp`オブジェクトを強化していきましょう！

この章では、spaCyの機械学習モデルの使い方をみていきます。

---

# 機械学習モデルとは？

- _文脈をもとに_ 言語の特徴を抽出するための手法
    - 品詞タグ付け
    - 統語的依存関係解析
    - 固有表現抽出
- ラベル付けされたデータを用いて訓練します
- データを追加することで、予測結果の調整をすることができます

Notes: 解析の対象が文脈に依存することはよくあります。
例えば、ある単語が動詞かどうかの判別や、テキストのある区間が人の名前を示すかどうかの判別などです。

spaCyは機械学習モデルによって、文脈依存の特徴量を抽出することができます。
品詞のタグ付けや依存関係解析、固有表現抽出などがそれに当たります。

機械学習モデルは、大量のラベル付きデータによって訓練されます。

データを追加することで、予測結果の修正をすることができます。
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
例えば、「en_core_web_sm」パッケージは、spaCyの中心的な機能が全て詰まった、Web文章で訓練された小サイズの英語用モデルです。

`spacy.load`は、モデルパッケージをロードし、`nlp`オブジェクトを返す関数です。

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

次に、「She ate the pizza」というテキストを解析します。

最後に`doc`内のそれぞれの`token`に対して、テキストと、予測結果の品詞タグが格納されている`.pos_`属性をプリントします。

spaCyでは、文字列が格納されている属性の名前は通常、アンダースコア「_」で終わり、
アンダースコアの無い属性は数字からなるIDを返します。

この例では、モデルは「ate」を動詞、「pizza」を名詞と正しく判断できています。

---

# 依存関係の解析

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

Notes: 品詞タグづけに加えて、単語間の依存関係の解析もできます。
例えば、文章中のある単語が主語か目的語かなどを予測することができます。

依存関係ラベルの予測結果は、`.dep_`属性で取得することができます。

`.head`属性は、係り先のトークン、つまり構文木における親のトークンを表しています。

---

# 依存関係ラベルの定義

<img src="/dep_example.png" alt="'She ate the pizza'という文の構文木のグラフ" />

| Label     | Description          | Example |
| --------- | -------------------- | ------- |
| **nsubj** | 名詞句主語 | She     |
| **dobj**  | 目的語 | pizza   |
| **det**   | 限定詞（冠詞） | the     |

Notes: 依存関係解析の結果は、標準化されたラベルで表現されます。
ここに記載されているのは、よく使われるラベルのうちいくつかの例です。

「She」という代名詞は、動詞「ate」に係る名詞句主語です。

「pizza」は動詞「ate」に係る目的語です。「pizza」は、主語である「She」によって食べれられます。

限定詞もしくは冠詞「the」は、名詞「pizza」に係ります。

---

# 固有表現抽出

<img src="/ner_example.png" alt="'Apple is looking at buying U.K. startup for $1 billion'という文の固有表現抽出結果" width="80%" />

```python
# テキストを処理
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

# 抽出された固有表現をイテレート
for ent in doc.ents:
    # 固有表現のテキストとラベルをプリント
    print(ent.text, ent.label_)
```

```out
Apple ORG
U.K. GPE
$1 billion MONEY
```

Notes: 固有表現とは、例えば人、国、組織のような、名前のついた実世界の実体のことです。

固有表現抽出の解析結果は、`doc.ents`プロパティから取得できます。

`doc.ents`プロパティは`Span`オブジェクトのイテレータを返します。
そしてそれぞれの`Span`に対して、`.text`でテキストを、`.label_`で固有表現のラベルを取得できます。

このケースでは、「Apple」を組織、「U.K.」を地理名称、「\$1 billion」を金額、と正しく解析されています。

---

# Tip：explain関数

よく使われるタグやラベルの定義を確認してみましょう。

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

Notes: よく使われるタグやラベルの定義を確認したいときは、`spacy.explain`ヘルパー関数が便利です。

例えば、「GPE」は地理的な実体を示しますが、ちょっとわかりづらいです。
そこで、`spacy.explain`を使えば、国や町を意味していることをすぐに確認できます。

この関数は品詞タグや依存関係ラベルにも使えます。

---

# Let's practice!

Notes: さて、ここからは手を動かしていきましょう。
spaCyの機械学習モデルと、解析結果を実際にみていきます。
