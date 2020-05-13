---
title: '第一章: 词语、短语、名字和概念的检索'
description:
  "本章介绍spaCy文本处理的基础知识。
   你将会学习到数据结构、构造统计模型以及如何用它们来抽取文本中的语言学特征。"
prev: null
next: /chapter2
type: chapter
id: 1
---

<exercise id="1" title="spaCy介绍" type="slides">

<slides source="chapter1_01_introduction-to-spacy">
</slides>

</exercise>

<exercise id="2" title="入门">

让我们来一起开始使用spaCy吧！这个例子中我们会尝试用到55+个[spaCy支持的语言](https://spacy.io/usage/models#languages)中的一些。

### 第一部分: 英语

- 从`spacy.lang.en`中导入`English`类然后创建`nlp`对象。
- 创建`doc`并打印其中的文本。

<codeblock id="01_02_01"></codeblock>

### 第二部分: 德语

- 从`spacy.lang.de`中导入`German`类然后创建`nlp`对象。
- 创建`doc`并打印其中的文本。

<codeblock id="01_02_02"></codeblock>

### 第三部分: 西班牙语

- 从`spacy.lang.es`中导入`Spanish`类然后创建`nlp`对象。
- 创建`doc`并打印其中的文本。

<codeblock id="01_02_03"></codeblock>

</exercise>

<exercise id="3" title="文本(documents), 范围(spans)和词符(tokens) ">

当我们在一段文字上调用`nlp`方法时，spaCy首先会对这段文字分词，然后创建一个文本对象。
在这个练习中我们学习`Doc`及其视图`Token`和`Span`的用法。

### 第一步

- 导入`English`的语言类然后创建`nlp`的对象
- 处理文本，然后在`doc`变量中创建一个`Doc`对象的实例。
- 选取`Doc`中的第一个词符并打印出它的`text`。

<codeblock id="01_03_01">

我们可以像检索Python中的list一样检索`Doc`。
举个例子，`doc[4]`会返回索引为4也就是文本中第五个位置的词符。
要注意Python中的第一个索引是0而不是1。

</codeblock>

### 第二步

- 导入`English`的语言类然后创建`nlp`的对象
- 处理文本，然后在`doc`变量中创建一个`Doc`对象的实例。
- 从`Doc`中截取其部分的词符"tree kangaroos"和"treekangaroos and narwhals"。

<codeblock id="01_03_02">

截取`Doc`中的一部分和截取Python list中的一部分是一样的，都可以使用`:`的标记方法。
要注意最后一个词符的索引是_不被包含在内的_。
举个例子，`0:4`包含了索引0,1,2,3的词符，但并不包含索引为4的词符。

</codeblock>

</exercise>

<exercise id="4" title="词汇属性">

在这个例子中，我们要使用spaCy中的`Doc`和`Token`对象以及一些词汇属性来寻找文本中
表示百分比的部分。我们要寻找两个相邻的词符：一个数字和一个百分比符号。

- 使用词符属性`like_num`来检查一个`doc`中的词符是否构成一个数字。
- 获取文档中_紧接着_当前词符的词符。`doc`中下一个词符的索引是`token.i + 1`。
- 检查下一个词符的`text`属性是否是百分比符号"%"。

<codeblock id="01_04">

要获取某一个索引的词符，我们可以直接用`doc`的索引。
举个例子，`doc[5]`就是索引为5的词符。

</codeblock>

</exercise>

<exercise id="5" title="统计模型" type="slides">

<slides source="chapter1_02_statistical-models">
</slides>

</exercise>

<exercise id="6" title="模型包" type="choice">

spaCy可以读入的模型包中**不包含**以下哪项？

<choice>
<opt text="包含有语言、流程和许可证书的文件">

所以模型都包含一个`meta.json`，定义了启用的语言、调用的流程组件名字以及一些其它的信息，
比如模型名字、版本、许可证书、数据源、作者以及准确率的图标（如果有的话）。

</opt>
<opt text="用来做统计预测的模型二进制权重">

用来做语义标注如词性标注、从属分析或者命名实体识别的模型，包含了二进制的权重

</opt>
<opt correct="true" text="模型训练使用的标注数据">

统计模型可以在训练数据的基础上泛化。
训练好之后模型就可以直接用二进制的权重做预测。
这也是为什么我们不需要把模型当初训练时使用的训练数据也一并包含进来。

</opt>
<opt text="模型的词典字符串以及它们的哈希值">

模型包包含了`string.json`，该文件存储了模型的词典及其对应的哈希值。
这样spaCy在需要的时候可以直接调用哈希值来搜索到对应的词典字符串。

</opt>
</choice>

</exercise>

<exercise id="7" title="调用模型">

这门课中我们需要使用的模型都已经预装好了。
如果你想了解更多关于spaCy的统计模型以及如何在自己的电脑上安装这些模型，
可以参考[这份文档](https://spacy.io/usage/models)。

- 使用`spacy.load`来调用一个比较小的英文模型`"en_core_web_sm"`。
- 处理文档并打印出文档中的文字。

<codeblock id="01_07">

要调用一个模型，我们可以调用`spacy.load`加上模型对应名字的字符串。
模型的名字会因为语言和训练数据的不同而有所变化，所以请确保使用了正确的名字。

</codeblock>

</exercise>

<exercise id="8" title="语言学标注的预测">

我们现在来试试spaCy的一个已经预训练好的模型包看看它在实际预测中的表现。
你完全可以在自己设定的文本中做测试！
如果你对某一个标注或者标签不清楚，可以在代码中调用`spacy.explain`。
举个例子，`spacy.explain("PROPN")`或者`spacy.explain("GPE")`.

### 第一部分

- 使用`nlp`对象来处理文本，创建一个`doc`。
- 对每一个词符，打印出其中的文字、词符的`.pos_`（词性标注）
  以及词符的`.dep_`（从属标注）。

<codeblock id="01_08_01">

如果要创建一个`doc`，我们要对文本中的一个字符串调用`nlp`对象。
要注意我们要在词符属性名后面加一个下划线来拿到字符串的值。

</codeblock>

### Part 2

- 处理文本创建一个`doc`对象。
- 对`doc.ents`做遍历，打印出实体的文本以及`label_`属性。

<codeblock id="01_08_02">

如果要创建一个`doc`，我们要对文本中的一个字符串调用`nlp`对象。
要注意我们要在词符属性名后面加一个下划线来拿到字符串的值。

</codeblock>

</exercise>

<exercise id="9" title="命名实体在情境中的预测">

模型是基于统计学的但并不是_永远_正确。模型的预测是否正确取决于训练数据和我们要处理的文本。
我们来看一个例子：

- 使用`nlp`对象来处理文本
- 对所有实体进行遍历，打印出实体的文本和标注。
- 看上去模型并没有预测出"iPhone X"。为这几个词符创建一个范围（span）。

<codeblock id="01_09">

- 要创建一个`doc`，对文本调用`nlp`对象。命名实体的结果在`doc.ents`这个参数中。
- 创建`Span`对象最简单的方法是使用截取的符号。
  举个例子，`doc[5:10]`可以返回从索引为5的位置一直到索引10_之前_。
  注意最后一个索引是排除在外的。

</codeblock>

</exercise>

<exercise id="10" title="基于规则的匹配抽取" type="slides">

<slides source="chapter1_03_rule-based-matching">
</slides>

</exercise>

<exercise id="11" title="Matcher的使用">

现在我们来试试使用spaCy的基于规则的`Matcher`。
我们继续沿用之前练习中的例子，写一个可以匹配到文本中"iPhone X"这个短语的模版。

- 从`spacy.matcher`中导入`Matcher`。
- 用`nlp`对象中共享的`vocab`来初始化它。
- 创建一个模板使它可以和`"iPhone"`和`"X"`这两个词符的`"TEXT"`值匹配。
- 使用`matcher.add`方法把模板加入到matcher里面。
- 在`doc`上面调用matcher，把结果存储在`matches`变量中。
- 遍历所有的match，得到从索引`start`到索引`end`的匹配结果的范围。

<codeblock id="01_11">

- 共享的词汇表在`nlp.vocab`这个参数里面。
- 一个模板就是一个列表，列表中的每一个元素是以属性名为键值的字典。
  举个例子，`[{"TEXT": "Hello"}]`会匹配到文本是"Hello"的一个词符。
- 每一个匹配的`start`和`end`值代表了被匹配到的范围的起始和终止索引。
  要得到这个范围，你需要用给定的start和end来创建`doc`的一段截取。

</codeblock>

</exercise>

<exercise id="12" title="匹配模板的书写">

这个练习中我们来试着用不同的词符属性和运算符写一些更复杂的匹配模板。

### 第一部分

- 写**一个**模板，只匹配到所有提及_完整_iOS版本的部分：
  "iOS 7"，"iOS 11"和"iOS 10"。

<codeblock id="01_12_01">

- 要精确匹配词符到某一段文字，我们可以使用`TEXT`属性。
  举个例子，`{"TEXT": "Apple"}`会精确匹配到所有文本是"Apple"的词符。
- 要匹配一个数字的词符，我们可以使用`"IS_DIGIT"`属性，
  该属性当目标词符只含有数字时会返回`True`。

</codeblock>

### 第二部分

- 写**一个**模板，只匹配到不同格式的"download"词（词符的原词是"download"），
  后面跟着一个词性是`"PROPN"`（专有名词）的词符。

<codeblock id="01_12_02">

- 要定义一个原词，我们可以在词符模板中使用`"LEMMA"`这个属性。
  举个例子，`{"LEMMA": "be"}`会匹配到如"is", "was"和"being"这样的词符。
- 要找到专有名词，我们可以寻找所有`"POS"`值是`"PROPN"`的词符。

</codeblock>

### 第三部分

- 写**一个**模板，匹配到形容词（`"ADJ"`）
  后面跟着一两个名词`"NOUN"`（一个名词和另一个可能有的名词）。

<codeblock id="01_12_03">

- 要找到形容词我们需要寻找那些`"POS"`值是`"ADJ"`的词符。
  对于名词我们要寻找`"NOUN"`。
- 运算符可以通过`"OP"`这个键值来添加。
  举个例子，`"OP": "?"`可以用来表示0次或1次的匹配。


</codeblock>

</exercise>
