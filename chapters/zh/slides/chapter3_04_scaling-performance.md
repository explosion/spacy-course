---
type: slides
---

# 规模化和性能

Notes: 本节课中我们来学习一些技巧，让spaCy流程可以运作得尽可能快速，并且
能够高效处理大规模语料。

---

# 处理大规模语料

- 使用`nlp.pipe`方法
- 用流模式来处理文本，生成`Doc`实例
- 这比直接在每段文本上面调用`nlp`快得多

**不好的方法：**

```python
docs = [nlp(text) for text in LOTS_OF_TEXTS]
```

**好的方法：**

```python
docs = list(nlp.pipe(LOTS_OF_TEXTS))
```

Notes: 如果我们要处理很多段文本然后创建一系列的`Doc`实例，使用`nlp.pipe`方法
可以极大地加速这一过程。

这个方法用流模式来处理文本生成`Doc`实例。

这种方法大大快过在每段文本上调用nlp，原因是它对目标文本集进行了打包。

`nlp.pipe`是一个产生`Doc`实例的生成器，所以要获得doc的列表记住要对其调用`list`方法。

---

# 传入语境(1)

- 在`nlp.pipe`设置`as_tuples=True`，这样我们可以传入一些列形式为
`(text, context)`的元组。
- 产生一系列`(doc, context)`元组。
- 当我们要把`doc`关联到一些元数据时这种方法就很有用。

```python
data = [
    ("这是一段文本", {"id": 1, "page_number": 15}),
    ("以及另一段文本", {"id": 2, "page_number": 16}),
]

for doc, context in nlp.pipe(data, as_tuples=True):
    print(doc.text, context["page_number"])
```

```out
这是一段文本 15
以及另一段文本 16
```

Notes: `nlp.pipe`支持传入文本/语境的元组，我们只需要设置`as_tuples`为`True`。

然后该方法会生成文档/语境的元组。

当我们想要传入新增的元数据时这就很有用，比如我们想要添加文本对应的ID或是一个页码。

---

# 传入语境(2)

```python
from spacy.tokens import Doc

Doc.set_extension("id", default=None)
Doc.set_extension("page_number", default=None)

data = [
    ("这是一段文本", {"id": 1, "page_number": 15}),
    ("以及另一段文本", {"id": 2, "page_number": 16}),
]

for doc, context in nlp.pipe(data, as_tuples=True):
    doc._.id = context["id"]
    doc._.page_number = context["page_number"]
```

Notes: 我们甚至可以把语境的元数据加入到定制化的属性中。

本例中我们要注册两个扩展属性，`id`和`page_number`。它们的默认值都是`None`。

处理文本和传入语境之后，我们就可以用我们的语境元数据来重写doc的扩展属性。

---

# 只用分词器(1)

<img src="/pipeline.png" width="90%" alt="spaCy流程图解">

- 不要跑整个流程！

Notes: 另一种常见的情况是，有时候我们已经读入了一个模型来做一些其它的处理，
但是对某一个特定的文本我们只需要运行分词器。

我们没有必要跑完整个流程因为这会比较慢，我们还会拿到很多我们并不需要的
模型预测结果。

---

# 只用分词器(2)

- 用`nlp.make_doc`将一段文本变成`Doc`实例

**不好的方法：**

```python
doc = nlp("Hello world")
```

**好的方法：**

```python
doc = nlp.make_doc("Hello world!")
```

Notes: 如果我们只是需要一个分词过的`Doc`实例，我们可以用`nlp.make_doc`方法
读入一段文本并返回一个doc。

这也是spaCy后台所做的事情：流程组件在被调用之前，`nlp.make_doc`会先把文本变
成一个doc。

---

# 关闭流程组件

- 使用`nlp.disable_pipes`来暂时关闭一个或多个流程组件。

```python
# 关闭词性标注器tagger和依存关系标注器parser
with nlp.disable_pipes("tagger", "parser"):
    # 处理文本并打印实体结果
    doc = nlp(text)
    print(doc.ents)
```

- `with`代码块之后这些组件会重新启用
- 这些组件关闭后spaCy流程只会跑剩余的未被关闭的组件

Notes: spaCy允许我们暂时关闭一些流程组件，方法是用`nlp.disable_pipes`
这个管理器。

这个方法需要一个可变长的参数，包含了需要关闭的一个或多个流程组件的名字。
比如我们只想要用实体识别器来处理文档，我们就可以暂时关闭词性标注器tagger
和依存关系标注器parser。

在`with`代码块之后，那些被关闭的流程组件会被自动重新启用。

在`with`代码块里面，spaCy只会跑未被关闭的剩余组件。

---

# 上手练习吧！

Notes: 轮到你来上手了。我们来试试这些新方法，优化一些代码使其更快更高效。
