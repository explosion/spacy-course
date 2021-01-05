---
type: slides
---

# spaCy介绍

Notes: 大家好，我是Ines!我是spaCy的核心开发人员之一。
spaCy是一个先进且广受欢迎的自然语言处理Python库。 

在这门课中，我们会介绍一下spaCy中最重要的几个概念和如何快速上手。

---

# nlp对象

```python
# 导入中文的语言类
from spacy.lang.zh import Chinese

# 创建nlp对象
nlp = Chinese()
```

- 包含了自然语言处理的流程
- 包括了分词等任务的特定语言的规则

Notes: spaCy的核心就是包含了自然语言处理流程的对象。我们通常把这个变量叫做`nlp`。 

举个例子，要创造一个中文的`nlp`的对象，我们要从`spacy.lang.zh`中导入`Chinese`这个语言类
并创建一个实例。我们可以像一个函数一样使用nlp对象来分析文本。

这个nlp对象包含了流程中的所有不同组件。

它还包含了一些特定语言相关的规则，用来将文本分词成为单个的词汇和标点符号。
spaCy支持多种不同语言，包含在`spacy.lang`中。

---

# Doc对象

```python
# 使用nlp对象处理一段文本并生成doc实例
doc = nlp("这是一个句子。")

# 遍历doc实例中的词符
for token in doc:
    print(token.text)
```

```out
这是
一个
句子
。
```

Notes: 当我们用`nlp`对象来处理文本时，spaCy会创建一个`Doc`的对象，这是"document"的缩写。
Doc可以让我们用结构化的方式来读取文本相关的信息，并且不会有信息丢失。

Doc用起来就像一个正常的Python序列，我们可以遍历它的词符，
或者使用索引读取其中一个词符。后面我们会详细介绍！

---

# Token对象

<img src="/doc.png" alt="一个含有四个词符的Doc实例" width="50%" />

```python
doc = nlp("这是一个句子。")

# 使用Doc索引读取单个词符
token = doc[1]

# 使用.text属性读取词符的文本
print(token.text)
```

```out
一个
```

Notes: `Token`实例代表了一个文本中的词符，比如一个词或者一个标点符号。 

要读取某一个位置的词符，我们可以直接使用doc的索引。

`Token`实例同时提供了不同的属性可以让我们读取词符的其它信息。
比如`.text`属性可以返回词符的原始文本。


---

# Span对象

<img src="/doc_span.png" width="50%" alt="一个含有四个词符且其中三个被包装成一个跨度的Doc实例" />

```python
doc = nlp("这是一个句子。")

# 截取Doc的一部分就成为了Span实例
span = doc[1:3]

# 使用.text属性获取span的文本
print(span.text)
```

```out
一个句子
```

Notes: 一个`Span`实例是文本包含了一个或更多的词符的一段截取。
它仅仅是`Doc`的一个视图而不包含实际的数据本身。 

要创建一个span，我们可以使用Python截取的语法。举个例子，`1:3`会创建一个从索引1开始
一直到索引3**之前**（不包括索引3）的词符截取。


---

# 词汇的属性

```python
doc = nlp("这个肉夹馍花了￥5。")
```

```python
print("Index:   ", [token.i for token in doc])
print("Text:    ", [token.text for token in doc])

print("is_alpha:", [token.is_alpha for token in doc])
print("is_punct:", [token.is_punct for token in doc])
print("like_num:", [token.like_num for token in doc])
```

```out
Index:    [0, 1, 2, 3, 4, 5, 6]
Text:     ['这个', '肉夹馍', '花', '了', '￥', '5', '。']

is_alpha: [True, True, True, True, False, False, False]
is_punct: [False, False, False, False, False, False, True]
like_num: [False, False, False, False, False, True, False]
```

Notes: 我们可以看到一些可用的词符属性：

`i`是原始文本中的词符索引值。

`text`返回词符的文本。

`is_alpha`，`is_punct`和`like_num`都会返回一个布尔值，检测词符是否有字母表字符组成、
是否是标点符号或者是否_代表了_一个数字；举个例子，一个包含了1和0的词符"10"，
或者一个包含了T,E,N三个字母的词组"ten"。

这些属性也被叫做词汇属性：他们仅仅代表了词典中元素的特性，而与词符所在的语义情境无关。

---

# 上手练习吧！

Notes: 让我们上手实战，使用spaCy处理你的第一段文本吧。 
