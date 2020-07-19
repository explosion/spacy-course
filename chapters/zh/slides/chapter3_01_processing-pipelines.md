---
type: slides
---

# 处理流程

Notes: 欢迎回来！本章专门介绍处理流程：一系列应用在doc上面的函数来添加其属性，
如词性标注、依存关系或者命名实体等。

这一节我们了解一下spaCy提供的流程组件，看看当我们在一个文本的字符串上面调用nlp
的时候spaCy在后台都做了什么。

---

# 调用nlp时会发生什么？

<img src="/pipeline.png" alt="spaCy流程将文本变为处理过的doc的图示" width="90%" />

```python
doc = nlp("This is a sentence.")
```

Notes: 我们到现在已经写过很多遍了：给`nlp`实例传入一个文本的字符串，然后
返回一个`Doc`实例。

但`nlp`实例 _实际中_ 到底做了什么？

首先，应用分词器将一段文本的字符串变成一个`Doc`实例。
然后，一系列的流程组件会依次作用在这个doc上面。
这个例子中这些组件依次是词性标注器tagger、依存关系标注器parser、以及实体识别器entity recognizer。
最后返回被处理过的doc，我们就可以在这个上面开展后续工作了。

---

# 原生的流程组件

| 名字        | 描述             | 创建结果                                                   |
| ----------- | :---------------------- | :-------------------------------------------------------- |
| **tagger**  | 词性标注器   | `Token.tag`, `Token.pos`                                  |
| **parser**  | 依存关系标注器       | `Token.dep`, `Token.head`, `Doc.sents`, `Doc.noun_chunks` |
| **ner**     | 命名实体识别器 | `Doc.ents`, `Token.ent_iob`, `Token.ent_type`             |
| **textcat** | 文本分类器         | `Doc.cats`                                                |

Notes: spaCy原生提供了下面的流程组件：

词性标注器设定了`token.tag`和`token.pos`这两个属性。

依存关系标注器添加了`token.dep`和`token.head`属性，同时也负责检测句子和基础的名词
短语，也被称作名词块。

命名实体识别器将检测到的实体添加到`doc.ents`属性中，同时对词符设定了实体类别的属性，
表明该词符是否是一个实体的一部分。

最后，文本分类器设定适用于整个文本的类别，将其加入`doc.cats`属性中。

因为文本的类别往往是特定的，所以默认文本分类器不包含在任何一个预训练好的模型里面。
但我们可以用它来训练自己的系统。

---

# 解构后台

<img src="/package_meta_zh.png" alt="标注为zh_core_web_sm的包、文件夹、文件及meta.json的图示" />

- 流程是依次定义在模型的`meta.json`文件里。
- 原生组件需要二进制数据来做预测。

Notes: 所有我们能读进spaCy的模型都包含了一些文件和一个`meta.json`。

这个元数据定义了语种和流程等等，告诉spaCy应该去初始化那些组件。

原生的组件如果要做预测也要需要二进制数据。这些数据都保存在模型包中，当我们读取模型
的时候这些数据就被读取到组件中。

---

# 流程属性

- `nlp.pipe_names`: 流程组件名的列表

```python
print(nlp.pipe_names)
```

```out
['tagger', 'parser', 'ner']
```

- `nlp.pipeline`: `(name, component)`元组的列表

```python
print(nlp.pipeline)
```

```out
[('tagger', <spacy.pipeline.Tagger>),
 ('parser', <spacy.pipeline.DependencyParser>),
 ('ner', <spacy.pipeline.EntityRecognizer>)]
```

Notes: 我们可以使用`nlp.pipe_names`属性来读取当前nlp实例中流程组件的名字。

我们可以使用`nlp.pipeline`属性来读取一个组件名与组件函数构成的元组的列表。

组件函数就是那些作用在doc上面处理文本并设置属性的函数，比如词性标注器或者命名实体
识别器。

---

# 上手练习吧！

Notes: 让我们试一试spaCy的几种流程，看看后台都发生了什么。
