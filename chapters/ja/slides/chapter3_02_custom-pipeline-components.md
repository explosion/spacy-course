---
type: slides
---

# カスタムのパイプラインコンポーネント

Notes: さて、spaCyのパイプラインがどのように動いているかをみてきました。それでは新しい強力な機能である、カスタムのパイプラインコンポーネント作成法をみていきましょう。

カスタムパイプラインコンポーネントとは、テキストに対して `nlp` オブジェクトを呼び出したときに実行されるspaCyパイプラインに追加できる、独自の機能のことです。

---

# なぜカスタムコンポーネントが必要？

<img src="/pipeline.png" alt="spaCyのパイプラインの図解" width="90%" />

- `nlp` を呼び出したときに関数が自動的に実行されるようにする
- `Doc` や `Token` に独自のメタデータを追加する
- `Doc.ents` のような備え付けの属性を更新する

Notes: テキストがトークン化されて `Doc` オブジェクトが作成された後、パイプラインコンポーネントが順番に適用されます。

カスタムコンポーネントは、テキストに対して `nlp` オブジェクトを呼び出すと自動的に実行されます。

これらは、`Doc` やトークンに独自のカスタムメタデータを追加するのに特に便利です。

また、固有表現スパンのような備え付けの属性を更新するのにも使えます。

---

# コンポーネントを解剖する(1)

- `Doc` を受け取り、それを更新して返す関数
- `Language.component` デコレータで登録
- `nlp.add_pipe` メソッドを使って追加することができます

```python
from spacy.language import Language

@Language.component("custom_component")
def custom_component_function(doc):
    # ここでdocに対して何か処理をする
    return doc

nlp.add_pipe("custom_component")
```

Notes: 基本的にパイプラインコンポーネントとは、 `Doc` を受け取り、それを更新して返し、パイプライン内の次のコンポーネントで処理できるようにする関数または呼び出し可能なオブジェクトです。

  spaCy に自作のコンポーネントを使うため、`@Language.component`デコレータでコンポーネントを登録します。デコレータを関数の前の行に書き足します。

登録済みのコンポーネントは`nlp.add_pipe`を使ってパイプラインに追加します。このメソッドを呼び出すとき、少なくともコンポーネントの名前を指定する必要があります。

---

# コンポーネントを解剖する(2)

```python
from spacy.language import Language

@Language.component("custom_component")
def custom_component_function(doc):
    # ここでdocに対して何か処理をする
    return doc

nlp.add_pipe("custom_component")
```

| 引数 | 説明 | 例 |
| -------- | -------------------- | ----------------------------------------- |
| `last`   | `True`の場合、最後に追加  | `nlp.add_pipe("component", last=True)`      |
| `first`  | `True`の場合、最初に追加 | `nlp.add_pipe("component", first=True)`     |
| `before` | 特定のコンポーネントの前に追加 | `nlp.add_pipe("component", before="ner")`   |
| `after`  | 特定のコンポーネントのあとに追加 | `nlp.add_pipe("component", after="tagger")` |

Notes: コンポーネントをパイプラインに追加する**場所**を指定するには、以下のキーワード引数を使用します。

`last`を`True`に設定すると、パイプラインの最後にコンポーネントが追加されます。これがデフォルトの動作です。

`first`を`True`に設定すると、パイプラインの最初、つまりトークナイザの直後に追加されます。

`before`および`after`引数に既存のコンポーネントの名前を指定すると、その前または後に追加されます。
例えば、`before="ner"` とすると、固有表現抽出器の前に追加されます。

ただし、前または後にそのコンポーネントが存在する必要があります。そうでない場合はspaCyがエラーを発生させます。

---

# 例: 簡単なコンポーネント(1)

```python
# nlpオブジェクトを作成
nlp = spacy.load("ja_core_news_sm")

# カスタムコンポーネントを定義
@Language.component("custom_component")
def custom_component_function(doc):
    # docの長さをプリント
    print("docの長さ:", len(doc))
    # docオブジェクトを返す
    return doc

# パイプラインの最初にコンポーネントを追加
nlp.add_pipe("custom_component", first=True)

# パイプラインのコンポーネント名をプリント
print("Pipeline:", nlp.pipe_names)
```

```out
Pipeline: ['custom_component', 'tok2vec', 'morphologizer', 'parser', 'attribute_ruler', 'ner']
```

Notes: 簡単なコンポーネントの例をみていきます。

まずは小サイズの日本語パイプラインから始めます。

次にコンポーネントを定義します。 `Doc` オブジェクトを受け取り、それを返す関数を書きます。

簡単に、パイプラインを通過する `doc` の長さを表示してみましょう。

パイプラインの次のコンポーネントで処理する必要があるので、docを返すことを忘れないでください。
トークン化によって作成された `doc` はすべてのコンポーネントに渡されるので、すべてのコンポーネントが更新されたdocを返すことが重要です。

spaCy に新しいコンポーネントを登録するために、`@Language.component`デコレータを使って、関数を`custom_component`として登録します。

これで、パイプラインにコンポーネントを追加することができるようになりました。 `first=True` を設定して、トークナイザの直後に追加してみましょう。

パイプラインのコンポーネント名を表示すると、カスタムコンポーネントが最初に表示されます。これは、 `doc` を処理するときに最初に適用されることを意味します。

---

# 例: 簡単なコンポーネント (2)

```python
# nlpオブジェクトを作成
nlp = spacy.load("ja_core_news_sm")

# カスタムコンポーネントを定義
@Language.component("custom_component")
def custom_component_function(doc):

    # docの長さをプリント
    print("docの長さ:", len(doc))

    # docオブジェクトを返す
    return doc

# コンポーネントをパイプラインの先頭に追加
nlp.add_pipe("custom_component", first=True)

# テキストを処理
doc = nlp("よろしくお願いします！")
```

```out
docの長さ: 6
```

Notes: これで、テキストを`nlp`オブジェクトで処理すると、カスタムコンポーネントが適用され、 `doc` の長さがプリントされます。

---

# Let's practice!

Notes: ここで学んだことを実践し、最初のパイプラインコンポーネントを書いてみましょう！
