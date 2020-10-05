---
type: slides
---

# 拡張属性

Notes: このレッスンでは、カスタムデータを保存するために `Doc` 、 `Token` 、 `Span` オブジェクトに拡張属性を追加する方法を学びます。

---

# 拡張属性のセッティング

- カスタムのメタデータを `Doc` 、 `Token` 、 `Span` に追加
- `._`プロパティから 取得

```python
doc._.title = "サンプル文書"
token._.is_color = True
span._.has_color = False
```

- グローバルな`Doc`、`Token`、`Span` に `set_extension` メソッドを使って登録

```python
# グローバルなクラスをインポート
from spacy.tokens import Doc, Token, Span

# Doc, Token, Spanに拡張をセット
Doc.set_extension("title", default=None)
Token.set_extension("is_color", default=False)
Span.set_extension("has_color", default=False)
```

Notes: 拡張属性を使用すると、任意のメタデータを `Doc` 、 `Token` 、 `Span` に追加することができます。
データは手動で追加したり、動的に計算したりできます。

拡張属性は `._` (ドットアンダースコア) プロパティで使用できます。これにより、それらがユーザによって追加されたものであり、`token.text`のようにspaCyのビルトインのものではないことが明確になります。

属性は `spacy.tokens` からインポートできるグローバルな `Doc` 、 `Token` 、 `Span` クラスに登録する必要があります。
これらのクラスについては、前の章で説明した通りです。
拡張属性を `Doc` 、 `Token` 、 `Span` に登録するには、 `set_extension` メソッドを使ってください。

最初の引数は属性名です。キーワード引数は、値の計算方法を定義することができます。
この場合、デフォルト値を持ち、上書きすることができる、という意味です。

---

# 拡張属性のタイプ

1. 属性拡張
2. プロパティ拡張
3. メソッド拡張

Notes: 拡張には3つのタイプがあります。属性拡張、プロパティ拡張、メソッド拡張です。

---

# 属性拡張

- 上書き可能なデフォルト値をセット

```python
from spacy.tokens import Token

# Tokenに拡張をセットし、デフォルト値を与える
Token.set_extension("is_color", default=False)

doc = nlp("むこうの空は青い。")

# 拡張属性の値を上書き
doc[4]._.is_color = True
```

Notes: 属性拡張を使うには、上書き可能なデフォルト値をセットします。

例えば、トークンにカスタムの`is_color`属性を設定し、デフォルトは`False`とします。

個々のトークンについては、その値を上書きできます。この場合、トークン「青い」は `True` となります。

---

# プロパティ拡張(1)

- ゲッターと、必要ならばセッターを定義
- ゲッターは、属性値を取得したときにのみ呼び出されます。

```python
from spacy.tokens import Token

# ゲッターを定義
def get_is_color(token):
    colors = ["赤", "白", "青"]
    return any(color in token.text for color in colors)

# ゲッターをTokenの拡張にセット
Token.set_extension("is_color", getter=get_is_color)

doc = nlp("むこうの空は青い。")
print(doc[4]._.is_color, "-", doc[4].text)
```

```out
True - 青い
```

Notes: プロパティ拡張機能はPythonのプロパティと似ています。ゲッターと、オプショナルなセッターを定義できます。

ゲッターは、属性を取得したときに呼び出されます。
これにより、値を動的に計算したり、他の拡張属性を用いることができます。

ゲッターは1つの引数を取ります。この例では、ゲッターは `Token` のテキストが色のリストに含まれているかどうかを返します。

拡張を登録する際に、`getter`キーワード引数でゲッターを登録します。

トークン「青い」の`._.is_color`プロパティは`True`を返すようになりました。

---

# プロパティ拡張(2)

- `Span`拡張はほぼ全ての場合でゲッターを用いるべきです

```python
from spacy.tokens import Span

# ゲッターを定義
def get_has_color(span):
    colors = ["赤", "白", "青"]
    return any(color in token.text for token in span for color in colors)

# Spanにゲッターを登録
Span.set_extension("has_color", getter=get_has_color)

doc = nlp("むこうの空は青い。")
print(doc[2:5]._.has_color, "-", doc[2:5].text)
print(doc[0:3]._.has_color, "-", doc[0:3].text)
```

```out
True - 空は青い
False - むこうの空
```

Notes: `Span` に拡張を登録する際は、ほとんどの場合ゲッターによるプロパティ属性を使うべきです。
もしこれ以外を使うならば、とりうる全ての `Span` を手作業で更新しなければなりません。

この例では、関数`get_has_color`は `Span` を受け取り、`Token` のいずれかのテキストが色のリストに含まれているかどうかを返します。

`doc` の処理した後、 `doc` のスライスをチェックすると、カスタムの`._.has_color`プロパティはスパンに色を示す `Token` が含まれているかどうかを返すようになります。

---

# メソッド拡張

- 関数をアサインすると、オブジェクトのメソッドとして使えるようになります
- 拡張メソッドには、**引数**を渡すことができます

```python
from spacy.tokens import Doc

# 引数をとるメソッドを定義
def has_token(doc, token_text):
    in_doc = token_text in [token.text for token in doc]
    return in_doc

# メソッドを拡張にセット
Doc.set_extension("has_token", method=has_token)

doc = nlp("むこうの空は青い。")
print(doc._.has_token("青い"), "- 青い")
print(doc._.has_token("雲"), "- 雲")
```

```out
True - 青い
False - 雲
```

Notes: メソッド拡張を使うと、拡張属性を呼び出し可能なメソッドにすることができます。

拡張属性に1つ以上の引数を渡して、属性値を動的に計算することができます。

この例では、メソッドは `doc` に指定されたテキストを含むトークンが含まれているかどうかをチェックします。
メソッドの最初の引数は常にオブジェクトで、この場合は `doc` です。
これは、メソッドが呼び出されたときに自動的に渡されます。他のすべての関数の引数は拡張メソッドの引数になります。この場合は `token_text` です。

ここでは、`._.has_token`メソッドは「青い」に対して`True`を返し、「雲」に対しては`False`を返します。

---

# Let's practice!

Notes: それでは、演習に入ります。カスタム拡張を追加してみましょう！
