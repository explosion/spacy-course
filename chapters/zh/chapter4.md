---
title: '第四章：训练神经网络模型'
description: '本章中，我们要学习更新spaCy的统计模型使其能够为特定的使用场景做出定制化。一个例子是我们想要在网络上的评论中抽取一种新的实体。我们将会学到如何从头训练自己的模型，了解模型训练的基本工作原理，以及一些技巧使得我们自己的定制化自然语言处理项目能够更加成功。'
prev: /chapter3
next: null
type: chapter
id: 4
---

<exercise id="1" title="训练和更新模型" type="slides">

<slides source="chapter4_01_training-updating-models">
</slides>

</exercise>

<exercise id="2" title="训练和评估数据">

要训练一个模型，我们通常需要训练数据 _和_ 用来评估模型的开发数据。这个评估数据是用来做什么的？

<choice>

<opt text="如果训练数据不够的时候用来提供更多的训练例子。">

训练过程中，模型只能由训练数据来进行更新。开发数据只是用来将模型在未见过的数据上预测的结果与真实标注做对比，
来评估模型表现的。准确度分数由此计算而来。

</opt>

<opt text="在未见过的数据上做预测并计算准确度分数。" correct="true">

开发数据只是用来将模型在未见过的数据上预测的结果与真实标注做对比，
来评估模型表现的。准确度分数由此计算而来。

</opt>

<opt text="没有标注数据时来定义训练的例子。">

开发数据只是用来将模型在未见过的数据上预测的结果与真实标注做对比，
来评估模型表现的。准确度分数由此计算而来。

</opt>

</choice>

</exercise>

<exercise id="3" title="创建训练数据(1)">

spaCy的基于规则的`Matcher`可以很好地被用来快速创建一些命名实体模型的训练数据。变量
`TEXTS`中存储着句子的列表，我们可以将其打印出来做检查。我们想要找到所有对应不同iPhone
型号的文本，所以我们可以创建一些训练数据来教会模型把它们识别为电子产品`"GADGET"`。

- 编写一个模板，含有两个词符且它们的小写形式可以匹配到`"iphone"`和`"x"`。
- 编写一个模板，含有两个词符，第一个词符的小写形式匹配到`"iphone"`，第二个词符用`"?"`
  运算符匹配到一个数字。

<codeblock id="04_03">

- 要匹配一个小写形式的词符，我们可以用`"LOWER"`属性，比如`{"LOWER": "apple"}`。
- 要寻找一个数字词符，我们可以用`"IS_DIGIT"`标签，比如`{"IS_DIGIT": True}`。

</codeblock>

</exercise>

<exercise id="4" title="创建训练数据(2)">

在为我们的语料创建数据之后，我们需要将其存放在一个后缀为`.spacy`的文件中。可以参见上一个例子中的代码。

- 使用`docs`的列表初始化`DocBin`。
- 将`DocBin`存储到一个名为`train.spacy`的文件中。

<codeblock id="04_04">

- 我们可以把一个含有多个文档的列表传入关键字参数`docs`中来初始化`DocBin`。
- `DocBin`的`to_disk`方法需要一个参数：二进制文件存储的路径。
  要确保文件的后缀名是`.spacy`.

</codeblock>

</exercise>

<exercise id="5" title="配置和进行训练" type="slides">

<slides source="chapter4_02_running-training">
</slides>

</exercise>

<exercise id="6" title="训练配置">

`config.cfg`文件是使用spaCy训练流程的“唯一真理来源”。下列关于配置的说法哪个是 **错误** 的？

<choice>

<opt text="使我们可以配置训练流程和超参数。">

配置文件含有训练流程的所有设定，包括超参数。

</opt>

<opt text="帮助实现训练流程的可复现。">

配置文件含有 _所有_ 设定，也没有隐藏的默认值，所以可以帮助我们的训练实验更加容易复现。
其他人可以轻松通过相同设定重新跑通我们的实验。

</opt>

<opt text="会为我们的流程创建一个可安装的Python包。" correct="true">

配置文件含有和训练与流程相关的所有设定，但并不能为流程打包。
要创建可安装的Python包，我们可以使用`spacy package`命令。

</opt>

<opt text="定义了流程的组件和各自的设定。">

配置文件中的'[components]'包含了所有流程组件和各自的设定，包括所使用的模型实现。

</opt>

</choice>

</exercise>

<exercise id="7" title="生成一个配置文件">

[`init config`命令](https://spacy.io/api/cli#init-config) 自动生成一个使用默认设定的训练配置文件。
我们想要训练一个命名实体识别器，所以我们要生成一个含有一个流程组件`ner`的配置文件。
因为我们在本课程中是在Jupyter环境中运行命令，所以加上前缀`!`。
如果是在本地终端中运行则不需要加这个前缀。

### 第一部分

- 使用spaCy的`init config`命令来自动生成一个中文流程的配置。
- 将配置保存到文件`config.cfg`中。
- 使用`--pipeline`参数指明一个流程组件`ner`。

<codeblock id="04_07_01">

- `--lang`参数定义了语言类，比如`zh`指中文。

</codeblock>

### 第二部分

我们来看看spaCy刚刚生成的配置文件！
我们可以运行下面的命令将配置打印到屏幕上。

<codeblock id="04_07_02"></codeblock>

</exercise>

<exercise id="8" title="使用训练客户端">

让我们用前面练习中生成的配置文件和训练语料来训练一个命名实体识别器!

使用[`train`](https://spacy.io/api/cli#train) 命令来调取训练配置文件来训练一个模型。
一个名为`config_gadget.cfg`的文件已经在`exercise/zh`中了，
同时还有一个名为`train_gadget.spacy`的文件包含了一些训练数据，`dec_gadget.spacy`文件包含了测试数据。
因为我们在本课程中是在Jupyter环境中运行命令，所以加上前缀`!`。
如果是在本地终端中运行则不需要加这个前缀。

- 在文件`exercises/zh/config_gadget.cfg`上面运行`train`命令。
- 将训练好的流程保存在`output`文件夹中。
- 传入路径`exercises/zh/train_gadget.spacy` 和 `exercises/zh/dev_gadget.spacy`

<codeblock id="04_08">

- 命令`spacy train`的第一个参数是配置文件的路径。

</codeblock>

</exercise>

<exercise id="9" title="检测模型">

让我们来看看模型在未出现过的新数据上表现如何！为了节省时间，我们已经在一些文本上面
训练好了一个带有标签`"GADGET"`的流程。这里是一些结果：


| 文本                                                                                                              | 实体              |
| ----------------------------------------------------------------------------------------------------------------- | ---------------------- |
| 苹果已经开始让iPhone 8和iPhone X变得越来越慢了，怎么办                                                              | `(iPhone 8, iPhone X)` |
| 我终于明白iPhone X的“刘海”是干嘛的了                                                                               | `(iPhone X,)`          |
| 关于Samsung Galaxy S9你需要了解的一切                                                                              | `(Samsung Galaxy,)`    |
| 想要比较不同的iPad型号？这里是2020年所有的产品线对比。                                                              | `(iPad,)`              |
| iPhone 8和iPhone 8 Plus是苹果公司设计、研发和销售的智能手机                                                         | `(iPhone 8, iPhone 8)` |
| 那个型号ipad是最便宜的，尤其是ipad pro里面的？？                                                                    | `(ipad, ipad)`         |
| Samsung Galaxy是三星电子公司设计、生产并退出市场的一系列移动计算设备                                                 | `(Samsung Galaxy,)`    |

在模型从文本中抽取的所有实体中，**有多少实体模型的判断是正确的**？
注意如果实体的跨度span不完整的话也被认为是一个错误！
小技巧：数一数模型 _应该_ 抽取出的实体数目，然后数一数模型 _实际中_ 抽取正确的实体数目，
把后者除以前者也就是全部正确实体的数目就可以得到准确率。

<choice>

<opt text="45%">
试着数数模型正确抽取的实体数目，然后除以模型 _应该_ 抽取出的全部正确实体的数目。

</opt>

<opt text="60%">

试着数数模型正确抽取的实体数目，然后除以模型 _应该_ 抽取出的全部正确实体的数目。

</opt>

<opt text="70%" correct="true">

在我们的测试数据上模型的准确率是70%。

</opt>

<opt text="90%">

试着数数模型正确抽取的实体数目，然后除以模型 _应该_ 抽取出的全部正确实体的数目。

</opt>

</choice>

</exercise>

<exercise id="10" title="模型训练最佳实践" type="slides">

<slides source="chapter4_03_training-best-practices">
</slides>

</exercise>

<exercise id="11" title="好数据vs烂数据">

这是一段摘抄，来自于一个训练集试图在旅行者的评论中标注实体类型
`TOURIST_DESTINATION`（游客目的地）。

```python
doc1 = nlp("我去年去了西安，那里的城墙很壮观！")
doc1.ents = [Span(doc1, 4, 5, label="TOURIST_DESTINATION")]

doc2 = nlp("人一辈子一定要去一趟爸黎，但那里的埃菲尔铁塔有点无聊。")
doc2.ents = [Span(doc2, 5, 6, label="TOURIST_DESTINATION")]

doc3 = nlp("深圳也有个巴黎的埃菲尔铁塔，哈哈哈")
doc3.ents = []

doc4 = nlp("北京很适合暑假去：长城、故宫，还有各种好吃的小吃！")
doc4.ents = [Span(doc4, 0, 1, label="TOURIST_DESTINATION")]
```

### 第一部分

为什么这段数据和标注方法有问题？

<choice>

<opt text="一个地方是不是游客目的地是一个主观看法而不是客观绝对的，所以实体识别器很难学习到。" correct="true">

一个更好的方法应该是只标注`"GPE"`（地理政治实体）或者是`"LOCATION"`（位置实体），然后用基于规则的系统
来判断这个实体在语境中是不是游客目的地，比如我们可以在知识库中寻找该实体类别或者在旅行百科
中查询这些实体。

</opt>

<opt text="埃菲尔铁塔为了保持一致也应该被标注为游客目的地，不然扰乱模型的判断。">

虽然Paris确实有可能是一个游客目的地，但这恰恰表明了这种标注的方法有多么主观，
以及决定标签是否符合这个实体有多么困难。结果就是我们的实体识别器也很难学习到这种区别。

</opt>

<opt text="像拼写错误的'爸黎'这种非常罕见的词库以外的词就不应该被标注为实体。">

就算是不常见的或者拼写错误的词也是可以被标注为实体的。实际上基于语境来判断拼写错误的文本
的类别恰恰是统计实体识别模型的一大优势。

</opt>

</choice>

### 第二部分

- 重写`doc.ents`使其跨度span的标签为`"GPE"`（城市、州省、国家）而非`"TOURIST_DESTINATION"`。
- 别忘了添加那些数据中本来未被标注为`"GPE"`的实体的跨度span。

<codeblock id="04_11">

- 对于那些已经标注过的span，我们只需要将其标签名从`"TOURIST_DESTINATION"`换为`"GPE"`。
- 有一段文本包含了城市和州省实体但还没有被标注。要加入实体的跨度span，我们需要数一数词符token
  来找出实体的span是从哪里开始和从哪里结束。注意最后一个词符的索引是 _不包含的_！
  然后把新的`Span`加入到`doc.ents`中。
- 注意分词！如果不确定可以把`Doc`中的词符打印出来。

</codeblock>

</exercise>

<exercise id="12" title="训练多个标签">

这里是某个数据集的一个样品，我们创建它来训练一个新的实体种类`"WEBSITE"`。
原始的数据集包含了几千个句子。这个练习中我们要手动做标注。实际工作中我们
很可能想要用一些标注工具来自动化这一步，比如[Brat](http://brat.nlplab.org/)，
一个很流行的开源方案，或者[Prodigy](https://prodi.gy)，我们自己开发的整合
了spaCy的标注工具。

### 第一部分

- 完成数据中所有`"WEBSITE"`实体的位置参数。

<codeblock id="04_12_01">

- 要注意终止词符的span是不包含的。
  所以如果一个实体从位置2开始而从位置3结束，那么start就是`2`，而end是`4`.

</codeblock>

### 第二部分

我们已经用刚才标注好的数据和其它几千个类似的例子训练了一个模型。训练完成之后，这个模型
对`"WEBSITE"`的抽取表现很好，但却识别不了`"PERSON"`了。这是怎么回事？

<choice>

<opt text='对模型来说很难学习到如<code>"PERSON"</code>和<code>"WEBSITE"</code>这样不同的类别。'>

让模型学习到不同类别是完全可能的。比如spaCy的预训练英文模型就可以识别人名、组织名或者
百分数。

</opt>

<opt text='训练数据中没有任何<code>"PERSON"</code>的例子了，所以模型学习到这个标签本身是错误的。' correct="true">

如果`"PERSON"`实体在训练数据中出现但并未被标注，模型就会学到这些实体不应该被抽取出来。
类似的如果一个已有的实体类别没有出现在训练数据中，模型就会 \"忘记\" 它而停止抽取。

</opt>

<opt text="我们需要返回模型超参数来让两种实体类别都被识别出来。">

超参数确实对模型准确度有影响，但不是这里的问题所在。

</opt>

</choice>

### 第三部分

- 更新训练数据，加入对`"PERSON"`实体"李子柒"和"马云"的标注。

<codeblock id="04_12_02">

- 要添加更多的实体，给`doc.ents`增加一个`Span`就行。
- 要注意终止词符的span是不包含的。
  所以如果一个实体从位置2开始而从位置3结束，那么start就是`2`，而end是`4`.

</codeblock>

</exercise>

<exercise id="13" title="总结" type="slides">

<slides source="chapter4_04_wrapping-up">
</slides>

</exercise>
