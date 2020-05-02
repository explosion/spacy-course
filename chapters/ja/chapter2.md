---
title: '第2章: spaCyによる大量データの解析'
description:
  "この章では、大量のテキストから特定の情報を抽出する方法をみていきます。
  spaCyのデータ構造の作成方法と、テキスト解析のために機械学習モデルとルールベースモデルを効率的に組み合わせる方法を学びます。"
prev: /chapter1
next: /chapter3
type: chapter
id: 2
---

<exercise id="1" title="データ構造(1)" type="slides">

<slides source="chapter2_01_data-structures-1">
</slides>

</exercise>

<exercise id="2" title="文字列からハッシュへ">

### パート1

- `nlp.vocab.strings`から「cat」のハッシュ値を取得してください。
- 逆に、ハッシュ値から文字列を取得してください。

<codeblock id="02_02_01">

- 文字列のデータベース`nlp.vocab.strings`は、Pythonの辞書のように使うことができます。
  例えば、`nlp.vocab.strings["unicorn"]`とすればハッシュ値を取得でき、逆にハッシュ値を使うと
  `"unicorn"`を再取得することができます。

</codeblock>

### パート2

- `nlp.vocab.strings`から「PERSON」ラベルのハッシュ値を取得してください。
- ハッシュ値から文字列を取得してください。

<codeblock id="02_02_02">

- 文字列のデータベース`nlp.vocab.strings`は、Pythonの辞書のように使うことができます。
  例えば、`nlp.vocab.strings["unicorn"]`とすればハッシュ値を取得でき、逆にハッシュ値を使うと
  `"unicorn"`を再取得することができます。

</codeblock>

</exercise>

<exercise id="3" title="Vocabとハッシュと語彙素">

さて、なぜこのコードはエラーとなるでしょうか？

```python
from spacy.lang.en import English
from spacy.lang.de import German

# 英語とドイツ語のnlpオブジェクトを作る
nlp = English()
nlp_de = German()

# 「Bowie」のIDを取得
bowie_id = nlp.vocab.strings["Bowie"]
print(bowie_id)

# vocabから、IDを用いて「Bowie」を取得
print(nlp_de.vocab.strings[bowie_id])
```

<choice>

<opt correct="true" text='文字列<code>"Bowie"</code>はドイツ語の語彙データに存在しないため、文字列ストアから取得することができないから。'>

ハッシュ値は復号できません。そのため、テキストを処理したり、文字列をルックアップしたり、同じvocabオブジェクトを使ってハッシュ値から文字列を取得します。

</opt>

<opt text='<code>"Bowie"</code>は英語とドイツ語の語彙ではなく、ハッシュ化できないから。'>

いかなる文字列もハッシュ化できます。

</opt>

<opt text="<code>nlp_de</code>は変数名として不正であるから。vocabは<code>nlp</code>という名前の変数でしか共有されない。">

`nlp`という名前はただの慣習です。コード中で`nlp`の代わりに`nlp_de`を用いると、vocabオブジェクトも含めて`nlp`が上書きされてしまいます。

</opt>

</choice>

</exercise>

<exercise id="4" title="データ構造(2)" type="slides">

<slides source="chapter2_02_data-structures-2">
</slides>

</exercise>

<exercise id="5" title="Docオブジェクトを作る">

では、`Doc`オブジェクトをゼロから作ってみましょう。

### パート1

- `Doc`クラスを`spacy.tokens`からインポートして下さい。
- `Doc`オブジェクトを`words`と`spaces`から作成します。vocabオブジェクトを渡すのを忘れないでください！

<codeblock id="02_05_01">

`Doc`クラスは3つの引数をとります。1つめは通常`nlp.vocab`で表される共有語彙データ、
2つめは`words`のリスト、3つめは単語間のスペースの有無をブール値で表した`spaces`のリストです。

</codeblock>

### パート2

- `Doc`クラスを`spacy.tokens`からインポートして下さい。
- `Doc`オブジェクトを`words`と`spaces`から作成します。vocabオブジェクトを渡すのを忘れないでください！

<codeblock id="02_05_02">


出力したいテキストの各単語を見て、それがスペースに続いているかどうかを確認します。
もしそうならば`spaces`に`True`を、そうでないならば`False`を追加してください。

</codeblock>

### パート3

- `Doc`クラスを`spacy.tokens`からインポートして下さい。
- `Doc`オブジェクトを`words`と`spaces`から作成してください。

<codeblock id="02_05_03">


各トークンを注意深くみてください。
spaCyが普段どのように文字列をトークン化しているかを見るには、試しに `nlp("Oh, really?!")` のトークンをプリントしてみましょう。

</codeblock>

</exercise>

<exercise id="6" title="Doc、スパン、固有表現をゼロから作る">

この演習では、`Doc`と`Span`を手動で作り、固有表現を登録してみましょう。
これはspaCyが普段裏側でやっていることです。
共有`nlp`オブジェクトはすでに作られています。

- `Doc`と`Span`クラスを`spacy.tokens`からインポートしてください。
- `Doc`クラスから直接、単語とスペースリストを用いて`doc`オブジェクトを作ってください。
- 「David Bowie」の`Span`オブジェクトを`doc`から作り、`"PERSON"`ラベルをつけてください。
- `doc.ents`を「David Bowie」の`span`からなる固有表現のリストで上書きしてください。

<codeblock id="02_06">

- `Doc`クラスは3つの引数で初期化します。1つめは例えば`nlp.vocab`で表される共有語彙データ、
  2つめは`words`のリスト、3つめは単語間のスペースの有無をブール値で表した`spaces`のリストです。
- `Span`クラスは4つの引数をとります。1つめは`doc`への参照、2つめは開始トークンのインデックス、3つめは終了トークンのインデックス、4つめはオプショナルで、固有表現ラベルです。
- `doc.ents`プロパティは、任意の`Span`からなるイテレート可能タイプ（iterable）を書き込むことができます。

</codeblock>

</exercise>

<exercise id="7" title="データ構造のベストプラクティス">

この例では、テキストを解析し、動詞が続く固有名詞を全て抽出しようとしています。

```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Berlin is a nice city")

# 全てのトークンと品詞タグを取得
token_texts = [token.text for token in doc]
pos_tags = [token.pos_ for token in doc]

for index, pos in enumerate(pos_tags):
    # 現在のトークンが固有名詞かどうかをチェックする
    if pos == "PROPN":
        # 次のトークンが動詞かどうかを調べる
        if pos_tags[index + 1] == "VERB":
            result = token_texts[index]
            print("Found proper noun before a verb:", result)
```

### パート1

このコードはなぜよくないでしょうか？

<choice>

<opt text="<code>result</code>トークンを<code>Token</code>オブジェクトに再変換すべきであるから。そうすれば、spaCyで再利用できるようになります。">

文字列を`Token`オブジェクトに変換し直す必要はありません。ただ、これ以降も文字列以外の情報を使う必要があるのならば、
トークンを文字列に避けるのは賢明でしょう。

</opt>

<opt correct="true" text="ネイティブなトークン属性ではなく、文字列のリストを使っているから。大抵の場合このやり方は効率が悪く、複雑な関係を表現できません。">

結果を文字列として出力するのはなるべく後にし、一貫性を保つためにネイティブなトークン属性を使うのが良いです。

</opt>

<opt text='<code>pos_</code>は固有表現を抽出するため属性ではないから。代わりに、<code>tag_</code>属性と、<code>"NNP"</code>と<code>"NNS"</code>ラベルを使うべきです。'>

`.pos_`属性は粗視化された品詞タグを返し、`"PROPN"`は固有名詞をチェックするための正しいタグです。

</opt>

</choice>

### パート2

- 2つのリスト`token_texts`と`pos_tags`を使う代わりに、トークンのネイティブ属性を使ってコードを書き直してください。
- `doc`に入っているそれぞれの`token`についてループし、`token.pos_`属性をチェックしてください。
- `doc[token.i+1]`を使って次のトークンを取得し、その`.pos_`属性をチェックしてください。
- 動詞の前に固有名詞が見つかったら、その`token.text`をプリントしてください。

<codeblock id="02_07">

- 事前に文字列を取得する必要はないので、`token_texts`と`pos_tags`を削除してください。
- `pos_tags`をイテレートする代わりに、`doc`に入っている各`token`をループし、`token.pos_`属性を取得してください。
- 次のトークンが同志かどうかをチェックするために、`doc[token.i + 1].pos_`を確認してください。

</codeblock>

</exercise>

<exercise id="8" title="単語ベクトルと意味的類似度" type="slides">

<slides source="chapter2_03_word-vectors-similarity">
</slides>

</exercise>

<exercise id="9" title="Inspecting word vectors">

In this exercise, you'll use a larger
[English model](https://spacy.io/models/en), which includes around 20.000 word
vectors. The model is already pre-installed.

- Load the medium `"en_core_web_md"` model with word vectors.
- Print the vector for `"bananas"` using the `token.vector` attribute.

<codeblock id="02_09">

- To load a statistical model, call `spacy.load` with its string name.
- To access a token in a doc, you can index into it. For example, `doc[4]`.

</codeblock>

</exercise>

<exercise id="10" title="Comparing similarities">

In this exercise, you'll be using spaCy's `similarity` methods to compare `Doc`,
`Token` and `Span` objects and get similarity scores.

### パート1

- Use the `doc.similarity` method to compare `doc1` to `doc2` and print the
  result.

<codeblock id="02_10_01">

The `doc.similarity` method takes one argument: the other object to compare the
current object to.

</codeblock>

### パート2

- Use the `token.similarity` method to compare `token1` to `token2` and print
  the result.

<codeblock id="02_10_02">

- The `token.similarity` method takes one argument: the other object to compare
  the current object to.

</codeblock>

### パート3

- Create spans for "great restaurant"/"really nice bar".
- Use `span.similarity` to compare them and print the result.

<codeblock id="02_10_03">
</codeblock>

</exercise>

<exercise id="11" title="Combining models and rules" type="slides">

<slides source="chapter2_04_models-rules">
</slides>

</exercise>

<exercise id="12" title="Debugging patterns (1)">

Why does this pattern not match the tokens "Silicon Valley" in the `doc`?

```python
pattern = [{'LOWER': 'silicon'}, {'TEXT': ' '}, {'LOWER': 'valley'}]
```

```python
doc = nlp("Can Silicon Valley workers rein in big tech from within?")
```

<choice>

<opt text='The tokens "Silicon" and "Valley" are not lowercase, so the <code>"LOWER"</code> attribute won’t match.'>

The `"LOWER"` attribute in the pattern describes tokens whose _lowercase form_
matches a given value. So `{"LOWER": "valley"}` will match tokens like "Valley",
"VALLEY", "valley" etc.

</opt>

<opt correct="true" text='The tokenizer doesn’t create tokens for single spaces, so there’s no token with the value <code>" "</code> in between.'>

The tokenizer already takes care of splitting off whitespace and each dictionary
in the pattern describes one token.

</opt>

<opt text='The tokens are missing an operator <code>"OP"</code> to indicate that they should be matched exactly once.'>

By default, all tokens described by a pattern will be matched exactly once.
Operators are only needed to change this behavior – for example, to match zero
or more times.

</opt>

</choice>

</exercise>

<exercise id="13" title="Debugging patterns (2)">

Both patterns in this exercise contain mistakes and won't match as expected. Can
you fix them? If you get stuck, try printing the tokens in the `doc` to see how
the text will be split and adjust the pattern so that each dictionary represents
one token.

- Edit `pattern1` so that it correctly matches all case-insensitive mentions of
  `"Amazon"` plus a title-cased proper noun.
- Edit `pattern2` so that it correctly matches all case-insensitive mentions of
  `"ad-free"`, plus the following noun.

<codeblock id="02_13">

- Try processing the strings that should be matched with the `nlp` object – for
  example `[token.text for token in nlp("ad-free viewing")]`.
- Inspect the tokens and make sure each dictionary in the pattern correctly
  describes one token.

</codeblock>

</exercise>

<exercise id="14" title="Efficient phrase matching">

Sometimes it's more efficient to match exact strings instead of writing patterns
describing the individual tokens. This is especially true for finite categories
of things – like all countries of the world. We already have a list of
countries, so let's use this as the basis of our information extraction script.
A list of string names is available as the variable `COUNTRIES`.

- Import the `PhraseMatcher` and initialize it with the shared `vocab` as the
  variable `matcher`.
- Add the phrase patterns and call the matcher on the `doc`.

<codeblock id="02_14">

The shared `vocab` is available as `nlp.vocab`.

</codeblock>

</exercise>

<exercise id="15" title="Extracting countries and relationships">

In the previous exercise, you wrote a script using spaCy's `PhraseMatcher` to
find country names in text. Let's use that country matcher on a longer text,
analyze the syntax and update the document's entities with the matched
countries.

- Iterate over the matches and create a `Span` with the label `"GPE"`
  (geopolitical entity).
- Overwrite the entities in `doc.ents` and add the matched span.
- Get the matched span's root head token.
- Print the text of the head token and the span.

<codeblock id="02_15">

- Remember that the text is available as the variable `text`.
- The span's root token is available as `span.root`. A token's head is available
  via the `token.head` attribute.

</codeblock>

</exercise>
