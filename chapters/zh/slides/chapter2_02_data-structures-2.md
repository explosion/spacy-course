---
type: slides
---

# 数据结构(2)：Doc、Span和Token

Notes: 我们已经学习了词汇表和字符串库，现在我们可以看下最重要的几个数据结构：
文档`Doc`、其视图词符`Token`以及跨度`Span`。

---

# Doc文档实例

```python
# 创建一个nlp实例
import spacy
nlp = spacy.blank("en")

# 导入Doc类
from spacy.tokens import Doc

# 用来创建doc的词汇和空格
words = ["Hello", "world", "!"]
spaces = [True, False, False]

# 手动创建一个doc
doc = Doc(nlp.vocab, words=words, spaces=spaces)
```

Notes: `Doc`是spaCy的核心数据结构之一。
当我们用`nlp`实例来处理文本时`Doc`就会被自动创建，
当然我们也可以手动初始化这个类。

创建`nlp`实例之后，我们就可以从`spacy.tokens`中导入`Doc`类。

这个例子中我们用了三个词来创建一个doc。空格存储在一个布尔值的列表中，
代表着对应位置的词后面是否有空格。每一个词符都有这个信息，包括最后一个词符！

`Doc`类有三个参数：共享的词汇表，词汇和空格。

---

# Span跨度实例(1)

<img src="/span_indices.png" width="65%" alt="Doc中的一个含有词符索引的Span实例图解" />

Notes: 一个`Span`是doc的一段包含了一个或更多的词符的截取。
`Span`类有最少三个参数：对应的doc以及span本身起始和终止的索引。
注意终止索引代表的词符是不包含在这个span里面的！

---

# Span跨度实例(2)

```python
# 导入Doc和Span类
from spacy.tokens import Doc, Span

# 创建doc所需要的词汇和空格
words = ["Hello", "world", "!"]
spaces = [True, False, False]

# 手动创建一个doc
doc = Doc(nlp.vocab, words=words, spaces=spaces)

# 手动创建一个span
span = Span(doc, 0, 2)

# 创建一个带标签的span
span_with_label = Span(doc, 0, 2, label="GREETING")

# 把span加入到doc.ents中
doc.ents = [span_with_label]
```

Notes: 要手动创建一个`Span`，我们还需要导入`spacy.tokens`中的类，
然后用doc、span的初始和终止索引以及一个可选的标签参数来初始化它。

`doc.ents`是可写的，所以我们可以用一个span列表覆盖它来手动添加一些实体。

---

# 最佳实践

- `Doc`和`Span`是非常强大的类，可以存储词语和句子的参考资料和关系。
  - **不到最后就不要把结果转换成字符串**
  - **尽可能使用词符属性**，比如用`token.i`来表示词符的索引
- 别忘了传入共享词汇表`vocab`

Notes: 在开始之前我们先来看一些小技巧：

`Doc`和`Span`非常强大且为性能做了很多优化，
可以让你获得词汇和句子的所有参考资料和关系。

如果你的应用需要输出字符串，确保到了最后才转换doc实例。
如果太早转换的话你就会丢失所有词符之间的关系。

为了保持一致性，尽量使用原生的词符属性，比如用`token.i`表示词符索引。

还有就是别忘了一定要传入共享词汇表vocab！

---

# 上手练习吧！

Notes: 现在让我们上手练习，从头创建一些doc和span。
