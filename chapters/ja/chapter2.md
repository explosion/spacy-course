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

- `nlp.vocab.strings`から「ネコ」のハッシュ値を取得してください。
- 逆に、ハッシュ値から文字列を取得してください。

<codeblock id="02_02_01">

- 文字列のデータベース`nlp.vocab.strings`は、Pythonの辞書のように使うことができます。
  例えば、`nlp.vocab.strings["ユニコーン"]`とすればハッシュ値を取得でき、逆にハッシュ値を使うと
  `"ユニコーン"`を再取得することができます。

</codeblock>

### パート2

- `nlp.vocab.strings`から「PERSON」ラベルのハッシュ値を取得してください。
- ハッシュ値から文字列を取得してください。

<codeblock id="02_02_02">

- 文字列のデータベース`nlp.vocab.strings`は、Pythonの辞書のように使うことができます。
  例えば、`nlp.vocab.strings["ユニコーン"]`とすればハッシュ値を取得でき、逆にハッシュ値を使うと
  `"ユニコーン"`を再取得することができます。

</codeblock>

</exercise>

<exercise id="3" title="Vocabとハッシュと語彙素">

さて、なぜこのコードはエラーとなるでしょうか？

```python
from spacy.lang.ja import Japanese
from spacy.lang.de import German

# 日本語とドイツ語のnlpオブジェクトを作る
nlp = Japanese()
nlp_de = German()

# 「ボウイ」のIDを取得
bowie_id = nlp.vocab.strings["ボウイ"]
print(bowie_id)

# vocabから、IDを用いて「ボウイ」を取得
print(nlp_de.vocab.strings[bowie_id])
```

<choice>

<opt correct="true" text='文字列<code>"ボウイ"</code>はドイツ語の語彙データに存在しないため、文字列ストアから取得することができないから。'>

ハッシュ値は復号できません。そのため、テキストを処理したり、文字列をルックアップしたり、同じvocabオブジェクトを使ってハッシュ値から文字列を取得します。

</opt>

<opt text='<code>"ボウイ"</code>は日本語とドイツ語の語彙ではなく、ハッシュ化できないから。'>

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

- `Doc`クラスを`spacy.tokens`からインポートしてください。
- `Doc`オブジェクトを`words`と`spaces`から作成します。vocabオブジェクトを渡すのを忘れないでください！

<codeblock id="02_05_01">

`Doc`クラスは3つの引数をとります。1つめは通常`nlp.vocab`で表される共有語彙データ、
2つめは`words`のリスト、3つめは単語間のスペースの有無をブール値で表した`spaces`のリストです。

</codeblock>

### パート2

- `Doc`クラスを`spacy.tokens`からインポートしてください。
- `Doc`オブジェクトを`words`と`spaces`から作成します。vocabオブジェクトを渡すのを忘れないでください！

<codeblock id="02_05_02">


出力したいテキストの各単語を見て、それがスペースに続いているかどうかを確認します。
もしそうならば`spaces`に`True`を、そうでないならば`False`を追加してください。

</codeblock>

### パート3

- `Doc`クラスを`spacy.tokens`からインポートしてください。
- `Doc`オブジェクトを`words`と`spaces`から作成してください。

<codeblock id="02_05_03">


各トークンを注意深くみてください。
spaCyが普段どのように文字列をトークン化しているかを見るには、試しに `nlp("本当ですか？！")` のトークンをプリントしてみましょう。

</codeblock>

</exercise>

<exercise id="6" title="Doc、スパン、固有表現をゼロから作る">

この演習では、`Doc`と`Span`を手動で作り、固有表現を登録してみましょう。
これはspaCyが普段裏側でやっていることです。
共有`nlp`オブジェクトはすでに作られています。

- `Doc`と`Span`クラスを`spacy.tokens`からインポートしてください。
- `Doc`クラスから直接、単語とスペースリストを用いて`doc`オブジェクトを作ってください。
- 「デヴィッド・ボウイ」の`Span`オブジェクトを`doc`から作り、`"PERSON"`ラベルをつけてください。
- `doc.ents`を「デヴィッド・ボウイ」の`span`からなる固有表現のリストで上書きしてください。

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

nlp = spacy.load("ja_core_news_sm")
doc = nlp("ベルリンはいい街だと思う")

# 全てのトークンと品詞タグを取得
token_texts = [token.text for token in doc]
pos_tags = [token.pos_ for token in doc]

for index, pos in enumerate(pos_tags):
    # 現在のトークンが固有名詞かどうかをチェックする
    if pos == "PROPN":
        # 次のトークンが設置詞(Adposition)かどうかを調べる
        if pos_tags[index + 1] == "ADP":
            result = token_texts[index]
            print("設置詞の前の固有名詞が見つかりました:", result)
```

### パート1

このコードはなぜよくないでしょうか？

<choice>

<opt text="<code>result</code>トークンを<code>Token</code>オブジェクトに再変換すべきであるから。そうすれば、spaCyで再利用できるようになります。">

文字列を`Token`オブジェクトに変換し直す必要はありません。ただこれ以降も文字列以外の情報を使う必要があるのならば、
トークンを文字列にしないほうが賢明でしょう。

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
- 次のトークンが動詞かどうかをチェックするために、`doc[token.i + 1].pos_`を確認してください。

</codeblock>

</exercise>

<exercise id="8" title="単語ベクトルと意味的類似度" type="slides">

<slides source="chapter2_03_word-vectors-similarity">
</slides>

</exercise>

<exercise id="9" title="単語ベクトルの検査">

この演習では、35,000個の単語ベクトルが含まれている中サイズの[日本語モデル](https://spacy.io/models/ja)を使います。
このモデルは既にインストールされています。

- 単語ベクトルの入っている中サイズモデル`"ja_core_news_md"`をロードしてください。
- `token.vector`属性を使って、`"バナナ"`の単語ベクトルをプリントしてください。

<codeblock id="02_09">

- `spacy.load`関数を呼びだし、機械学習モデルをロードしてください。
- docに含まれるトークンを取得するには、インデックスを使ってください。例えば`doc[4]`とします。

</codeblock>

</exercise>

<exercise id="10" title="類似度の比較">

この演習では、spaCyの`similarity`メソッドを使って、`Doc`と`Token`と`Span`オブジェクトの比較をし、類似度を算出していきます。

### パート1

- `doc.similarity`メソッドを使って、`doc1`と`doc2`を比較し、結果をプリントしてください。

<codeblock id="02_10_01">

`doc.similarity`メソッドは引数を1つとります。比較対象のオブジェクトです。

</codeblock>

### パート2

- `token.similarity`メソッドを使って、`token1`と`token2`を比較し、結果を出力してください。

<codeblock id="02_10_02">

- `token.similarity`メソッドは引数を1つとります。比較対象のオブジェクトです。

</codeblock>

### パート3

- 「素晴らしいレストラン」と「とても素敵なバー」のスパンを作ってください。
- `span.similarity`を使ってこれらを比較し、結果をプリントしてください。

<codeblock id="02_10_03"></codeblock>

</exercise>

<exercise id="11" title="モデルとルールの組み合わせ" type="slides">

<slides source="chapter2_04_models-rules">
</slides>

</exercise>

<exercise id="12" title="パターンのデバッグ(1)">

なぜこのパターンは`doc`中の「Silicon Valley」にマッチしないでしょうか？

```python
pattern = [{'LOWER': 'silicon'}, {'TEXT': ' '}, {'LOWER': 'valley'}]
```

```python
doc = nlp("Silicon Valleyの労働者は内部からビッグテックを抑制することができるか？")
```

<choice>

<opt text='「Silicon」と「Valley」は小文字ではないので、<code>"LOWER"</code>はマッチしないから'>

パターン中の`"LOWER"`属性は、トークンを小文字化したらその値にマッチする、ということを示しています。
つまり、`{"LOWER": "valley"}`は「Valley」や「VALLEY」、「valley」等にマッチします。

</opt>

<opt correct="true" text='トークナイザは単一のスペースについてトークンを作らないので、<code>" "</code>というトークンがないから'>

トークナイザは既にスペースを区切っており、それぞれの辞書はトークンについて表しています。

</opt>

<opt text='各トークンが一度だけマッチすることを示す<code>"OP"</code>属性がかけているから'>

パターン中のトークンは、デフォルトで一度だけマッチします。
演算子は、この挙動を変えたいときだけ用います。例えば、0回以上マッチさせたいときなどです。

</opt>

</choice>

</exercise>

<exercise id="13" title="パターンのデバッグ(2)">

この演習中のパターンは両方とも誤っており、期待した通りには動きません。
正しく修正できますか？
もし躓いてしまったら、`doc`のトークンを全てプリントしてみて、トークンがどのように分割されているかを確認し、
パターン中の各辞書が1つのトークンに対応するように調整してみましょう。

- `pattern1`を修正し、大文字小文字によらず`"Amazon"`にマッチし、また、タイトルケースの固有名詞にマッチするようにしてください。
- `pattern2`を修正し、大文字小文字によらない`"ad-free"`と、名詞の組にマッチするようにしてください。

<codeblock id="02_13">

- `nlp`オブジェクトにマッチする文字列を処理してみてください。例えば、`[token.text for token in nlp("ad-free視聴")]`のように。
- トークンを検査し、パターン内の各辞書が1つのトークンを正しく記述していることを確認してください。

</codeblock>

</exercise>

<exercise id="14" title="効率的なフレーズマッチング">

個々のトークンを記述するパターンを書くよりも、正確な文字列をマッチさせた方が効率的な場合もあります。これは特に、世界のすべての国のような数に限りのある場合に当てはまります。
すでに国のリストがあるので、これを使って情報抽出スクリプトを作りましょう。
国名のリストは、`COUNTRIES`変数に入っています。

- `PhraseMatcher`をインポートし、共有の`vocab`で初期化し、`matcher`変数に格納してください。
- フレーズのパターンを追加し、matcherを`doc`に対して呼び出してください。

<codeblock id="02_14">

共有の`vocab`は、`nlp.vocab`にあります。

</codeblock>

</exercise>

<exercise id="15" title="国名と関係の抽出">

前の演習では、`PhraseMatcher`を使って国名を抽出するスクリプトを作りました。
長いテキストで国別マッチツールを使用し、構文を分析して、一致した国でdocの固有表現を更新してみましょう。

- マッチの結果をイテレートし、ラベル `"GPE"` (地理的実体) を持つ `Span` を作成します。
- `doc.ents` を上書きし、マッチしたスパンを追加します。
- マッチしたスパンのルートのヘッドトークンを取得します。
- そのヘッドトークンとスパンのテキストをプリントします。

<codeblock id="02_15">

- テキストは変数 `text` として利用できます。
- スパンのルートトークンは `span.root` で取得できます。トークンのヘッドは `token.head` 属性で取得できます。

</codeblock>

</exercise>
