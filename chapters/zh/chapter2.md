---
title: '第二章：使用spaCy进行大规模数据分析'
description:
  "在本章中，我们会用一些新技术来从大量语料中抽取特定信息。
   我们会学习如何利用spaCy的数据结构来结合统计与规则模型进行文本分析。"
prev: /chapter1
next: /chapter3
type: chapter
id: 2
---

<exercise id="1" title="数据结构 (1)" type="slides">

<slides source="chapter2_01_data-structures-1">
</slides>

</exercise>

<exercise id="2" title="从字符串到哈希值">

### Part 1

- 在`nlp.vocab.strings`中查找字符串"猫"来得到哈希值。
- 查找这个哈希值来返回原先的字符串。

<codeblock id="02_02_01">

- 你可以像使用一个普通的Python字典一样使用`nlp.vocab.strings`中存储的字符串。
  举个例子，`nlp.vocab.strings["独角兽"]`会返回哈希值，再查找这个哈希值
  就会返回字符串`"独角兽"`。

</codeblock>

### Part 2

- 在`nlp.vocab.strings`中查找字符串标签"PERSON"来得到哈希值。
- 查找这个哈希值来返回原先的字符串。

<codeblock id="02_02_02">

- 你可以像使用一个普通的Python字典一样使用`nlp.vocab.strings`中存储的字符串。
  举个例子，`nlp.vocab.strings["独角兽"]`会返回哈希值，再查找这个哈希值
  就会返回字符串`"独角兽"`。

</codeblock>

</exercise>

<exercise id="3" title="vocab（词汇表），哈希值和词素">

为什么这段代码抛出了错误信息？

```python
import spacy

# 创建一个英文和德文的nlp实例
nlp = spacy.blank("en")
nlp_de = spacy.blank("de")

# 获取字符串'Bowie'的ID
bowie_id = nlp.vocab.strings["Bowie"]
print(bowie_id)

# 在vocab中查找"Bowie"的ID
print(nlp_de.vocab.strings[bowie_id])
```

<choice>

<opt correct="true" text='The string <code>"Bowie"</code> 不在德语的vocab中，所以我们不能把哈希值转换为原始的字符串。'>

哈希值是不能逆求原始值的。为了解决这个问题，
我们要通过处理文本或者查找字符串把词组加入到新的vocab中，
或者使用同样的vocab把哈希值变回一个字符串。

</opt>

<opt text='<code>"Bowie"</code> 在英语或者德语中都不是一个正常的词语，所以不能被哈希。'>

任何字符串都可以转变为一个哈希值。

</opt>

<opt text="<code>nlp_de</code> 不是一个有效的名字。vocab只有当<code>nlp</code>实例是同样的名字时才可以被共享。">

变量名`nlp`只是一个约定俗成的名字。如果你的代码中用了`nlp`而不是`nlp_de`，
程序会把已经存在的`nlp`实例包括其vocab覆盖掉。

</opt>

</choice>

</exercise>

<exercise id="4" title="数据结构 (2)" type="slides">

<slides source="chapter2_02_data-structures-2">
</slides>

</exercise>

<exercise id="5" title="创建一个Doc">

让我们来从头开始创建`Doc`这种实例。

### 第一部分

- 从`spacy.tokens`中导入`Doc`
- 用`words`和`spaces`创建一个`Doc`。别忘了把vocab传进去！

<codeblock id="02_05_01">

`Doc`类需要3个参数：共享的词汇表，通常是`nlp.vocab`；
一个词组`words`的列表；
一个空格`spaces`的列表，里面是一系列的布尔值表示对应词汇后面是否跟着空格。

</codeblock>

### 第二部分

- 从`spacy.tokens`中导入`Doc`
- 用`words`和`spaces`创建一个`Doc`。别忘了把vocab传进去！

<codeblock id="02_05_02">

检查目标文本输出中的每一个词后面是否跟着一个空格。
如果是spaces的值就是`True`，否则就是`False`。

</codeblock>

### 第三部分

- 从`spacy.tokens`中导入`Doc`
- 完成`words`和`spaces`来匹配目标文本并创建一个`doc`。

<codeblock id="02_05_03">

注意那些单独的词符。
如果想看下spaCy通常是如何对字符串进行分词，你可以试下打印`nlp("Oh, really?!")`的词符。

</codeblock>

</exercise>

<exercise id="6" title="从头开始练习Docs（文档）, spans（跨度）和entities（实体）">

在这个练习中，我们要手动创建`Doc`和`Span`实例，然后更新命名实体。
实际中spaCy在后台也就是这么做的。
一个共享的`nlp`实例已经创建好了。

- 从`spacy.tokens`中导入`Doc`和`Span`。
- 用`Doc`类使用词组和空格直接创建一个`doc`实例。
- 用`doc`实例创建一个"David Bowie"的`Span`，赋予它`"PERSON"`的标签。
- 用一个实体的列表，也就是"David Bowie" `span`，来覆盖`doc.ents`。

<codeblock id="02_06">

- `Doc`类用三个参数来初始化：共享的词汇表比如`nlp.vocab`，一个词组的列表
  以及一个布尔值的列表代表了每个词后面是否跟着一个空格。
- `Span`类用四个参数来初始化：一个`doc`的引用，起始词符索引，终止词符索引，
  以及一个可选的标签。
- `doc.ents`属性是可写的，所以我们可以赋予它任何含有`Span`实例的可遍历的数据结构。

</codeblock>

</exercise>

<exercise id="7" title="数据结构最佳实践">


```python
import spacy

nlp = spacy.load("zh_core_web_sm")
doc = nlp("北京是一座美丽的城市")

# 获取所有的词符和词性标注
token_texts = [token.text for token in doc]
pos_tags = [token.pos_ for token in doc]

for index, pos in enumerate(pos_tags):
    # 检查当前词符是否是专有名词
    if pos == "PROPN":
        # 检查下一个词符是否是动词
        if pos_tags[index + 1] == "VERB":
            result = token_texts[index]
            print("Found proper noun before a verb:", result)
```

### 第一部分

这段代码哪里不对？

<choice>

<opt text="<code>result</code>词符应该要转变回一个<code>Token</code>实例，这样我们就可以在spaCy中重用它了。 ">

我们并不需要把字符串变回`Token`实例。
实际上我们应该要避免把词符变成字符串，因为这样的话
我们就不能够读取其属性和关系了。

</opt>

<opt correct="true" text="代码使用了一个字符串的列表而不是原生的词符属性。这样通常会影响效率，也不能表达复杂的关系。">

一般来说我们到了最后才会考虑将结果转成字符串。
使用原生的词符属性也能保证前后一致。

</opt>

<opt text='不应该用<code>pos_</code>来做专有名词提取，而应该使用<code>tag_</code>、<code>"NNP"</code>和<code>"NNS"</code>这几个标签。'>

`.pos_`属性返回的是粗粒度的词性标注结果，
`"PROPN"`才是正确的专有名词标签。

</opt>

</choice>

### 第二部分

- 用原生的词符属性而不是`token_texts`和`pos_tags`的列表来重写代码。
- 在`doc`中遍历每一个`token`并检查其`token.pos_`属性。
- 用`doc[token.i + 1]`来检查下一个词符及其`.pos_`属性
- 如果找到一个处于动词前的专有名词，我们就打印其`token.text`。

<codeblock id="02_07">

- 删除`token_texts`和`pos_tags`因为我们并不需要提前编译一个字符串的列表。
- 我们不应该遍历`pos_tags`，而应该是在`doc`中遍历每一个`token`并且获取其`token.pos_`属性。
- 读取`doc[token.i + 1].pos_`来检查下一个词符是否是动词。

</codeblock>

</exercise>

<exercise id="8" title="词向量和语义相似度" type="slides">

<slides source="chapter2_03_word-vectors-similarity">
</slides>

</exercise>

<exercise id="9" title="检查词向量">

在这个练习中我们要用到一个更大的[中文流程](https://spacy.io/models/zh)，
该模型有大概两万个词向量。这里模型已经提前安装好了。

- 读取中等大小的`"zh_core_web_md"`流程，该流程含有词向量
- 用`token.vector`属性来打印`"老虎"`的向量。

<codeblock id="02_09">

- 用`spacy.load`调用流程名字来读取训练好的流程。
- 可以直接用索引来读取doc中的一个词符token，比如`doc[4]`。

</codeblock>

</exercise>

<exercise id="10" title="比对相似度">

在这个练习中我们要用spaCy的`similarity`方法来比较
`Doc`、`Token`和`Span`实例，得到相似度分数。

### 第一部分

- 使用`doc.similarity`方法来比较`doc1`和`doc2`的相似度并打印结果。

<codeblock id="02_10_01">

- `doc.similarity`方法需要一个参数：需要和当前实例计算相似度的另一个实例。

</codeblock>

### 第二部分

- 使用`token.similarity`方法来比较`token1`和`token2`的相似度并打印结果。

<codeblock id="02_10_02">

- `token.similarity` 方法需要一个参数：需要和当前实例计算相似度的另一个实例。

</codeblock>

### 第三部分

- 为"不错的餐厅"/"很好的酒吧"创建跨度(span)。
- 使用`span.similarity`来比较它们并打印结果。

<codeblock id="02_10_03"></codeblock>

</exercise>

<exercise id="11" title="结合流程与规则" type="slides">

<slides source="chapter2_04_models-rules">
</slides>

</exercise>

<exercise id="12" title="模板调试 (1)">

为什么这个模板不能匹配到`doc`中的词符"Silicon Valley"？

```python
pattern = [{"LOWER": "silicon"}, {"TEXT": " "}, {"LOWER": "valley"}]
```

```python
doc = nlp("Can Silicon Valley workers rein in big tech from within?")
```

<choice>

<opt text='词符"Silicon"和"Valley"不全是小写字母, 所以<code>"LOWER"</code>属性匹配不到。'>

模板中的`"LOWER"`属性描述了那些_小写字母形式_能匹配到指定值的词符。
所以`{"LOWER": "valley"}`是可以匹配到诸如"Valley","VALLEY", "valley"
这样的词符的。

</opt>

<opt correct="true" text='分词器不能为单空格创建词符，所以文本中的空格<code>" "</code>并没有变为词符。'>

分词器已经自动用空格来分割文本了，模板中的每一个字典描述了一个词符。

</opt>

<opt text='词符少了一个<code>"OP"</code>运算符来表示它们只能被匹配到刚好1次。'>

所有词符默认被模板匹配刚好1次。
运算符是用来改变这种情况的，比如要匹配0次或者多于1次。

</opt>

</choice>

</exercise>

<exercise id="13" title="模板调试 (2)">

这个练习中的两个模板都出错了，匹配不到我们想要的结果。
你能改正它们吗？要是你卡住了，可以尝试把`doc`中的词符打印出来，
看看这些文本应该怎样被分割，然后调整你的模板保证每个字典表示一个词符。

- 编辑`pattern1`使其可以正确匹配到所有的形容词后面跟着`"笔记本"`。
- 编辑`pattern2`使其可以正确匹配到`"锐龙"`加上后面的数字 (LIKE_NUM) 和符号 (IS_ASCII) 。

<codeblock id="02_13">

- 试着处理那些能匹配到`nlp`实例的字符串，比如`[token.text for token in nlp("锐龙4000U")]`。
- 检查这些词符，确保模板中的每个字典正确描述了一个词符。

</codeblock>

</exercise>

<exercise id="14" title="高效率的短语匹配">

有时候相比起写一些描述单个词符的模板，直接精确匹配字符串可能更高效。
在面对有限个种类的东西时尤其如此，比如世界上的所有国家。
我们已经有一个国家的列表，所以我们用它作为我们信息提取代码的基础。
变量`COUNTRIES`中存取了这些字符串名字的列表。

- 导入`PhraseMatcher`并用含有共享`vocab`的变量`matcher`来初始化。
- 加入短语模板并在'doc'上面调用matcher

<codeblock id="02_14">

共享`vocab`在`nlp.vocab`中。

</codeblock>

</exercise>

<exercise id="15" title="提取国家和关系">

在上一个练习中，我们写了一段代码用spaCy的`PhraseMatcher`来寻找文本中的国家名。
我们现在用这个国家匹配器来匹配一段更长的文本，分析句法，
并用匹配到的国家名更新文档中的实体。

- 对匹配结果进行遍历，
  创建一个标签为`"GPE"`(geopolitical entity，地理政治实体)的`Span`。
- 覆盖`doc.ents`中的实体，加入匹配到的跨度span。
- 获取匹配到的跨度span中的根词符的头。
- 打印出词符头和跨度span的文本。

<codeblock id="02_15">

- 记住文本信息是在变量`text`中。
- 跨度span的根词符是在`span.root`中。一个词符的头是在`token.head`属性中。

</codeblock>

</exercise>
