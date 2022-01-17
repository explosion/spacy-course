---
type: slides
---

# 流程和规则的结合

Notes: 将统计模型的预测结果与规则系统结合使用，是自然语言处理工具箱里面最强大的方法之一。

本节课中我们看下如何用spaCy来做这件事。

---

# 统计模型vs规则

|                         | **统计模型**                                      | **规则系统**            |
| ----------------------- | ----------------------------------------------------------- | --------------------------------- |
| **应用场景**           | 需要根据例子来 _泛化_ 的应用        | ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀ |
| **真实范例** | 产品名、人名、主语宾语关系   |                                   |
| **spaCy功能**      | 实体识别器、依存句法识别器、词性标注器 |                                   |

Notes: 如果你的应用需要能够根据一些例子而进行泛化，那么统计模型会很有用。

举个例子，训练好的流程通常可以优化产品和人名的识别。
相比于给出一个所有曾经出现过的人名库，你的应用可以判断一段文本中的几个词符是否是人名。
相类似的你也可以预测依存关系标签从而得到主宾关系。

我们可以使用spaCy的实体识别器、依存句法识别器或者词性标注器来完成这些任务。

---

# 统计预测vs规则

|                         | **统计模型**                                      | **规则系统**                                 |
| ----------------------- | ----------------------------------------------------------- | ------------------------------------------------------ |
| **使用场景**           | 需要根据例子来 _泛化_ 的应用         | 有限个例子组成的字典              |
| **真实范例** | 产品名、人名、主宾关系   | 世界上的国家、城市、药品名、狗的种类 |
| **spaCy功能**      | 实体识别器、依存句法识别器、词性标注器 | 分词器, `Matcher`, `PhraseMatcher`                  |

Notes: 当我们要查找的例子差不多是有限个的时候，基于规则的方法就变得很有用。比如世界上所有的国家名或者城市名、药品名或者甚至狗的种类。

在spaCy中我们可以用定制化的分词规则以及matcher和phrase matcher这样的匹配器来完成这些任务。

---

# 回顾：基于规则的匹配

```python
# 用共享词汇表初始化
from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)

# 模板是一个代表词符的字典组成的列表
pattern = [{"LEMMA": "love", "POS": "VERB"}, {"LOWER": "cats"}]
matcher.add("LOVE_CATS", [pattern])

# 运算符可以定义一个词符应该被匹配多少次
pattern = [{"TEXT": "very", "OP": "+"}, {"TEXT": "happy"}]
matcher.add("VERY_HAPPY", [pattern])

# 在doc上面调用matcher来返回一个(match_id, start, end)元组的列表
doc = nlp("I love cats and I'm very very happy")
matches = matcher(doc)
```

Notes: 在上一章中，我们学过如何用spaCy的基于规则的匹配器matcher来查找文本中的复杂模板。
这里我们简单回顾一下。

matcher由一个共享词汇表（通常是`nlp.vocab`）来初始化。

模板是一个元素为字典的列表，每个字典代表了一个词符及其属性。
模板可以用`matcher.add`添加到matcher中。

运算符可以定义一个词符应该被匹配多少次，比如"+"表示可以匹配一次或者更多次。

在doc实例上调用matcher会返回一个匹配结果的列表。每一个匹配结果是一个元组，
其中包括一个ID以及文档中的词符的起始和终止索引。

---

# 统计预测的加成

```python
matcher = Matcher(nlp.vocab)
matcher.add("DOG", [[{"LOWER": "golden"}, {"LOWER": "retriever"}]])
doc = nlp("I have a Golden Retriever")

for match_id, start, end in matcher(doc):
    span = doc[start:end]
    print("Matched span:", span.text)
    # 获取span的根词符和根头词符
    print("Root token:", span.root.text)
    print("Root head token:", span.root.head.text)
    # 获取前一个词符及其词性标注的POS标签
    print("Previous token:", doc[start - 1].text, doc[start - 1].pos_)
```

```out
Matched span: Golden Retriever
Root token: Retriever
Root head token: have
Previous token: a DET
```

Notes: 这个例子是一个"golden retriever"的匹配规则。

如果我们遍历matcher返回的匹配结果，将得到匹配ID以及匹配到的span的起始和终止索引。
我们就可以用它来得到更多的信息。`Span`实例让我们可以读取原始文档以及所有其它
模型预测出来的词符属性和语言学特征。

比如，我们可以得到span的根词符。如果这个span有多个词符，那跟词符就决定了这个短语的类别。举个例子，"Golden Retriever"的根词符是"Retriever"。
我们还能找到根词符的头词符，这是这个短语中管着它的语言学“父词符”，本例中就是动词"have"。

最后我们还能得到前一个词符及其属性。在这里它是一个限定词，也就是冠词"a"。

---

# 高效短语匹配(1)

- `PhraseMatcher`和普通正则表达式或者关键词搜索类似，但是可以直接读取词符！
- 将`Doc`实例作为模板
- 比`Matcher`更快更高效
- 适用于大规模词表的匹配

Notes: 短语匹配器phrase matcher是另一个在数据中查找词语序列的非常有用的工具。

短语匹配器也是在文本中做关键词查询，但不同于仅仅寻找字符串，短语匹配器可以直接读取语义中的词符。

短语匹配器将`Doc`实例作为模板。

短语匹配器也非常快。

所以当我们要在大规模语料中匹配一个很大的字典和词库时这就很有用。

---

# 高效短语匹配(2)

```python
from spacy.matcher import PhraseMatcher

matcher = PhraseMatcher(nlp.vocab)

pattern = nlp("Golden Retriever")
matcher.add("DOG", [pattern])
doc = nlp("I have a Golden Retriever")

# 遍历匹配结果
for match_id, start, end in matcher(doc):
    # 获取匹配到的span
    span = doc[start:end]
    print("Matched span:", span.text)
```

```out
Matched span: Golden Retriever
```

Notes: 让我们来看这个例子。

短语匹配器phrase matcher可以从`spacy.matcher`中导入，和普通的matcher是一样的API。

我们传进一个`Doc`实例而不是字典列表作为模板。

然后我们就可以遍历文本中的匹配结果，这些结果中有匹配的ID和匹配的起始和终止索引。
同时也可以让我们可以创建一个匹配到的词符"Golden Retriever"的`Span`实例使我们可以做情景中的分析。

---

# 上手练习吧！

Notes: 让我们来试试这些结合了规则和预测结果的新技术。
