---
type: slides
---

# 定制化流程组件

Notes: 现在我们知道了spaCy的流程如何运作，我们来看看另一个非常强大的
功能：定制化流程组件。

定制化流程组件让我们可以在spaCy的流程中加入我们自己的函数，当我们在一段文本上调
用`nlp`时，这些函数就会被调用来完成比如修改doc为其增加更多数据的任务。

---

# 为什么要用定制化组件？

<img src="/pipeline.png" alt="spaCy流程图示" width="90%" />

- 使得一个函数在我们调用`nlp`时被自动执行
- 为文档document和词符token增加我们自己的元数据
- 更新一些原生的属性比如`doc.ents`

Notes: 当一短文本已经被分词且`Doc`实例被创建后，流程组件会依次被应用。
spaCy支持一系列的原生组件，但也允许我们定义自己的组件。

定制化组件当我们在一段文字上调用`nlp`时会被自动执行。

当我们想要给文档和词符添加我们自己定制化的元数据时，定制化组件就尤其有用。

我们还可以用定制化组件来更新原生的属性，比如命名实体识别的结果。

---

# 解构组件(1)

- 函数用来读取一个`doc`，修改和返回它。
- 我们可以用`nlp.add_pipe`来添加组件。

```python
def custom_component(doc):
    # 对doc做一些处理
    return doc

nlp.add_pipe(custom_component)
```

Notes: 根本上来讲，一个流程组件就是一个函数或者callable，它读取一个doc，修改
和返回这个doc，作为下一个流程组件的输入。

我们可以用`nlp.add_pipe`方法来为流程添加组件。这个方法需要至少一个参数：组件函数。

---

# 解构组件(2)

```python
def custom_component(doc):
    # 对doc做一些处理
    return doc

nlp.add_pipe(custom_component)
```

| 参数 | 说明          | 例子                                   |
| -------- | -------------------- | ----------------------------------------- |
| `last`   | 如果为`True`则加在最后面  | `nlp.add_pipe(component, last=True)`      |
| `first`  | 如果为`True`则加在最前面 | `nlp.add_pipe(component, first=True)`     |
| `before` | 加在指定组件之前 | `nlp.add_pipe(component, before="ner")`   |
| `after`  | 加在指定组件之后  | `nlp.add_pipe(component, after="tagger")` |

Notes: 我们可以用下面这些关键字参数来指定在流程的 _什么位置_ 添加组件： 

将`last`设定为`True`会把组件加在流程的最后面。这也是默认的方法。

将`first`设定为`True`会把组件加在流程的最前面，紧紧跟在分词器之后。

`before`和`after`让我们可以定义新组件放置位置之前或者之后的已有组件名字。
比如`before="ner"`就会把新组建添加到命名实体识别器之前。

新组件位置之前或者之后的那个组件必须存在，不然spaCy就会报错。

---

# 举例: 一个简单的组件(1)

```python
# 创建nlp实例
nlp = spacy.load("zh_core_web_sm")

# 定义一个定制化组件
def custom_component(doc):
    # 打印doc的长度
    print("Doc length:", len(doc))
    # 返回doc
    return doc

# 把组件添加到流程的最前面
nlp.add_pipe(custom_component, first=True)

# 打印流程的组件名
print("Pipeline:", nlp.pipe_names)
```

```out
Pipeline: ['custom_component', 'tagger', 'parser', 'ner']
```

Notes: 我们来看看一个简单的流程组件的例子。

我们从一个小的英文模型开始。

然后定义组件，也就是一个函数，读取`Doc`实例然后再把它返回出来。

我们简单把要走流程的doc的长度打印出来。

别忘了把这个doc返回出来，因为它还要被流程后面的组件处理！
分词器创建的doc会走完全部的流程组件，所以每个组件都一定要返回其处理过的doc，这点很重要。

我们现在可以把组件加入到流程中了。我们设置`first=True`把它加到流程的最前面，紧跟着分词器。

我们打印流程组件名，可以看到定制化组件现在出现在起始位置。这意味着我们处理一个doc
的时候这个组件会先被调用。

---

# 举例: 一个简单的组件(2)

```python
# 创建nlp实例
nlp = spacy.load("zh_core_web_sm")

# 定义一个定制化组件
def custom_component(doc):

    # 打印doc的长度
    print("Doc length:", len(doc))

    # 返回doc
    return doc

# 把组件添加到流程的最前面
nlp.add_pipe(custom_component, first=True)

# 处理一段文本
doc = nlp("这是一个句子。")
```

```out
Doc length: 4
```

Notes: 当我们用`nlp`实例处理一段文本的时候，自定义组件会被应用到doc上，打印出
这个文档的长度。

---

# 上手练习吧！

Notes: 是时候上手练习，编写你自己的第一个流程组件了！
