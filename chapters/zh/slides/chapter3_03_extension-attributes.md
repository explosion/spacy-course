---
type: slides
---

# 扩展属性

Notes: 本节课中我们会学习如何添加定制化属性到`Doc`、`Token`和`Span`实例中
来储存一些定制化的数据。

---

# 设置定制化属性

- 添加定制化元数据到文档document、词符token和跨度span中
- 通过`._`属性来读取


```python
doc._.title = "My document"
token._.is_color = True
span._.has_color = False
```

- 使用`set_extension`方法在全局的`Doc`、`Token`或`Span`上注册。

```python
# 导入全局类
from spacy.tokens import Doc, Token, Span

# 在Doc、Token和Span上设置扩展属性
Doc.set_extension("title", default=None)
Token.set_extension("is_color", default=False)
Span.set_extension("has_color", default=False)
```

Notes: 定制化属性可以让我们添加任何的元数据到doc、token和span中。
这些数据可以一次性添加，也可以动态被计算出来。

定制化属性通过`._`（点加下划线）属性来读取，这样我们可以很清楚看到这些属性是
被用户添加的而不是spaCy的内建属性如`token.text`。

属性需要注册在从`spacy.tokens`导入的全局`Doc`、`Token`和`Span`类上。我们已经在
前面几个章节中使用过它们。我们用`set_extension`方法将一个定制化属性注册到
`Doc`、`Token`和`Span`上。

第一个参数是属性名字。关键词参数让我们可以定义其值是如何被计算出来的。
在这个例子中这些定制化参数有默认值，也可以被覆盖重写。

---

# 扩展属性类别

1. 特性（Attribute）扩展
2. 属性（Property）扩展
3. 方法（Method）扩展

Notes: 有三种扩展类别：特性扩展，属性扩展和方法扩展。

---

# 特性（Attribute）扩展

- 设置一个可以被覆盖的默认值。

```python
from spacy.tokens import Token

# 为Token设置一个有默认值的扩展
Token.set_extension("is_color", default=False)

doc = nlp("The sky is blue.")

# 覆盖默认扩展特性的值
doc[3]._.is_color = True
```

Notes: 特性扩展设置一个可被覆盖的默认值。

举个例子，我们可以为词符设置一个定制化的`is_color`特性，默认值是`False`。

对词符个体，其扩展特性值可以被覆盖重写。在这个例子中，"blue"词符的扩展特性值被写为True。

---

# 属性（Property）扩展 (1)

- 设置一个取值器（getter）和一个可选的赋值器（setter）函数。
- 取值器只有当你 _提取_ 属性值的时候才会被调用。

```python
from spacy.tokens import Token

# 定义取值器函数
def get_is_color(token):
    colors = ["red", "yellow", "blue"]
    return token.text in colors

# 为词符设置有取值器的扩展
Token.set_extension("is_color", getter=get_is_color)

doc = nlp("The sky is blue.")
print(doc[3]._.is_color, "-", doc[3].text)
```

```out
True - blue
```

Notes: 属性扩展的工作方式和Python中的属性（property）一样：它们可以定义一个
取值器（getter）和一个可选的赋值器（setter）。

取值器只有当我们提取属性值的时候才会被调用。这样我们可以动态计算属性值，甚至可以考虑
到其它定制化属性的值。

取值函数有一个参数：其对应的实例，在这里就是词符本身。这个例子中，函数返回该词符的文字
是否在我们的颜色表中。

我们注册扩展的时候就可以通过`getter`关键字参数来提供这个函数。

词符"blue"现在调用`._.is_color`就会返回`True`了。

---

# 属性（Property）扩展 (2)

- `Span`扩展大部分情况下总是需要有一个取值器。

```python
from spacy.tokens import Span

# 定义取值器函数
def get_has_color(span):
    colors = ["red", "yellow", "blue"]
    return any(token.text in colors for token in span)

# 为Span设置一个带有取值器getter的扩展
Span.set_extension("has_color", getter=get_has_color)

doc = nlp("The sky is blue.")
print(doc[1:4]._.has_color, "-", doc[1:4].text)
print(doc[0:2]._.has_color, "-", doc[0:2].text)
```

```out
True - sky is blue
False - The sky
```

Notes: 如果我们想给span设置一个拓展属性，大部分时间我们应该用一个带取值函数
的属性拓展。否则为了设置所有的span值我们需要手动更新 _每一个可能出现的span_。

本例中，`get_has_color`函数读入span然后返回其中是否有任一个词符的文本出现在颜色表中。

处理doc之后，我们要检查doc的各种不同截取，而定制化的`._.has_color`属性则会返回这个
span中是否包含了一个颜色的词符。

---

# 方法（Method）扩展

- 作为一个实例的方法引入一个**函数**
- 可以向扩展函数中传入**参数**

```python
from spacy.tokens import Doc

# 定义含有参数的方法
def has_token(doc, token_text):
    in_doc = token_text in [token.text for token in doc]
    return in_doc

# 在doc上设置方法扩展
Doc.set_extension("has_token", method=has_token)

doc = nlp("The sky is blue.")
print(doc._.has_token("blue"), "- blue")
print(doc._.has_token("cloud"), "- cloud")
```

```out
True - blue
False - cloud
```

Notes: 方法扩展使扩展属性变为一个可调用的方法。

我们可以向方法扩展中传入一个或多个参数然后动态计算属性值，基于比如某一个特定
的参数或者设定。

本例中，方法函数检查doc中是否含有一个给定文本的词符。方法的第一个参数永远是实例本
身，本例中就是这个doc。方法被调用时该doc就会被自动传入。其它所有的函数参数都是这个
方法扩展的参数，在这里这个参数就是`token_text`。

定制化的`._.has_token`方法会为词语"blue"返回`True`，为词语"cloud"返回`False`。

---

# 上手练习吧

Notes: 轮到你上手了，试着添加一些定制化的扩展吧！
