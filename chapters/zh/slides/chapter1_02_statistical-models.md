---
type: slides
---

# 统计模型

Notes: 让我们来看看`nlp`对象更多强大的功能。

这门课中我们会学习spaCy的统计模型。 

---

# 什么是统计模型？

- 使spaCy可以_从语境中_抽取到语言学属性
  - 词性标注
  - 依存关系解析
  - 命名实体识别
- 从标注过的文本中训练而来
- 可以用更多的标注数据来更新模型，优化抽取结果

Notes: 很多非常有趣的分析是基于语境的：
比如一个词是否是动词，或者文本的一段跨度是否是人名。

统计模型让spaCy可以通过语境来做抽取。抽取结果通常包括了词性标注、依存关系和命名实体。

模型是由大量标注过的文本例子训练而成。

模型可以输入更多的标注数据来优化结果，常见的应用是用特定数据优化用户需要的特定场景。

---

# 模型包

<img src="/package.png" alt="名字为en_core_web_sm的模型包" width="30%" align="right" />

```bash
$ python -m spacy download zh_core_web_sm
```

```python
import spacy

nlp = spacy.load("zh_core_web_sm")
```

- 二进制权重
- 词汇表
- 元信息 (语言、流程)

Notes: spaCy提供了很多预训练好的模型包，我们可以用`spacy download`命令来下载。
比如"zh_core_web_sm"这个模型包就是一个小的中文模型，它有所有核心功能，是从网上的文本训练而来。

`spacy.load`方法可以通过包名读取一个模型包并返回一个`nlp`实例。

模型包含有二进制权重，spaCy用这些权重可以做出模型预测实现信息抽取。

模型包也含有词汇表以及一些元信息，配置了spaCy的语言类以及相应的处理流程组件。

---

# 词性标注

```python
import spacy

# 读取小版本的英文模型
nlp = spacy.load("zh_core_web_sm")

# 处理文本
doc = nlp("我吃了个肉夹馍")

# 遍历词符
for token in doc:
    # Print the text and the predicted part-of-speech tag
    print(token.text, token.pos_)
```

```out
我 PRON
吃 VERB
了 PART
个 NUM
肉夹馍 NOUN
```

Notes: 我们来看下模型的预测结果。这个例子中我们使用spaCy来获得词性标注的结果，
为每个词在其所在语境中标注种类。

首先我们读入小版本的中文模型得到一个`nlp`的实例。

然后我们处理"我吃了个肉夹馍"这个文本。

对于这段文本中的每一个词符我们可以打印其文字和`.pos_`属性，这个属性就是词性标注的结果。

在spaCy中，返回字符串的属性名一般结尾会有下划线；没有下划线的属性会返回一个整型的ID值。

这里我们看到模型正确地标注"吃"为一个动词，而"肉夹馍"为一个名词。

---

# 依存关系解析

```python
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)
```

```out
我 PRON nsubj 吃
吃 VERB ROOT 吃
了 PART aux:asp 吃
个 NUM nummod 肉夹馍
肉夹馍 NOUN dobj 吃
```

Notes: 除了词性分析以外，我们还可以预测词与词之间的关系。比如一个词是某一个句子或者物体的主语。

`.dep_`属性返回预测的依存关系标注。

`.head`属性返回句法头词符。你可以认为这是词在句子中所依附的母词符。

---

# 依存关系的定义

<img src="/dep_example.png" alt="'She ate the pizza'的依存关系可视化" />

| Label     | Description          | Example |
| --------- | -------------------- | ------- |
| **nsubj** | 名词主语      | 我     |
| **dobj**  | 目的语        | 肉夹馍   |

Notes: spaCy使用了一系列标准化的标注方法来描述依存关系：

代词"我"是一个依附在动词（这里是"吃"）上的名词主语。

名词"肉夹馍"是一个依附在动词"吃"上面的目的语。这个肉夹馍被主语"我"吃掉了。

---

# 命名实体识别

<img src="/ner_example.png" alt="'Apple is looking at buying U.K. startup for $1 billion'中命名实体的可视化" width="80%" />

```python
# 处理文本
doc = nlp("微软准备用十亿美金买下这家英国的创业公司。")

# 遍历识别出的实体
for ent in doc.ents:
    # 打印实体文本及其标注
    print(ent.text, ent.label_)
```

```out
微软 ORG
十亿美金 MONEY
英国 GPE
```

Notes: 命名实体是那些被赋予了名字的真实世界的物体，比如一个人、一个组织或者一个国家。

从`doc.ents`中可以读取模型预测出的所有命名实体。

它会返回一个`Span`实例的遍历器，我们可以打印出实体文本和用`.label_`属性来打印出实体标注。

这个例子里模型正确地将"微软"识别为一个组织，将"英国"识别为一个地理政治实体，
将"十亿美金"预测为钱。

---

# Tip: spacy.explain方法

快速获得大部分常见的标注和标签定义

```python
spacy.explain("GPE")
```

```out
'Countries, cities, states'
```

```python
spacy.explain("NNP")
```

```out
'noun, proper singular'
```

```python
spacy.explain("dobj")
```

```out
'direct object'
```

Notes: 一个小诀窍是可以用`spacy.explain`这个帮手函数
来快速获得大部分常见的标注和标签定义。

举个例子，可能很多人不知道"GPE"代表的地理政治实体（geopolitical entity）的意思，
但调用`spacy.explain`我们就知道这是指国家、城市和州省。

同样这个方法也适用于词性标注和依存关系标注。


---

# 上手练习吧！

Notes: 轮到你自己来试试spaCy的统计模型和用它来预测一些信息了。
