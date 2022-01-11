---
title: '第三章：处理流程'
description:
  "本章会介绍spaCy的处理流程。我们会学到当spaCy在处理文本的时候背后的机制是什么，
  如何编写定制化的组件并加入流程中，以及如何在documents、spans和tokens中通过
  编写定制化属性来添加我们自己的元数据。"
prev: /chapter2
next: /chapter4
type: chapter
id: 3
---

<exercise id="1" title="处理流程" type="slides">

<slides source="chapter3_01_processing-pipelines">
</slides>

</exercise>

<exercise id="2" title="调用nlp时会发生什么？">

当我们在一个文本的字符串上面调用`nlp`时spaCy会做什么？

```python
doc = nlp("这是一个句子。")
```

<choice>

<opt text="运行词性标注器、依存关系解析器、实体识别器然后运行分词器。">

分词器永远是在其它所有流程组件 _之前_ 运行的，因为分词器会将文本的字符串转化为一个
`Doc`实例。流程也不一定需要包括词性标注器、依存关系解析器和实体识别器。

</opt>

<opt text="对文本进行分词然后依次运行流程中的每一个组件。" correct="true">

分词器会将文本的字符串转化为一个`Doc`实例。然后spaCy会按照顺序在文档上运行
流程中的每一个组件。

</opt>

<opt text="连接spaCy服务器计算和返回结果。">

spaCy的所有运算都在本机，并不需要连接任何远端服务器。

</opt>

<opt text="初始化相应的语言，加入流程并读取模型中的二进制权重。">

当我们调用`spacy.load()`来读取流程时，spaCy会初始化相应语言，加入流程并读取
模型的二进制权重。当我们在文本上调取`nlp`之前流程就已经被读取了。

</opt>

</exercise>

<exercise id="3" title="流程的检查">

让我们一起检查一下小规模的中文流程。

- 读取`zh_core_web_sm`流程并创建`nlp`实例。
- 用`nlp.pipe_names`来打印流程组件的名字。
- 用`nlp.pipeline`来打印`(name, component)`元组的完整流程。

<codeblock id="03_03">

组件的名字列表存储在`nlp.pipe_names`属性中。由`(name, component)`元组组成的
完整流程存储在`nlp.pipeline`中。

</codeblock>

</exercise>

<exercise id="4" title="定制化模型组件" type="slides">

<slides source="chapter3_02_custom-pipeline-components">
</slides>

</exercise>

<exercise id="5" title="定制化组件的应用场景">

下面这些问题中那些可以用定制化组件来解决？请选择所有正确的答案。

1. 更新训练好的流程来改进其性能
2. 基于词符及其属性来计算我们自己定义的变量
3. 基于比如一个词典来增加新的命名实体
4. 编写对某种新语种的支持

<choice>

<opt text="1和2">

定制化组件只能修改`Doc`，并不能用来直接更新其它组件的模型权重。

</opt>

<opt text="1和3">

定制化组件只能修改`Doc`，并不能用来直接更新其它组件的模型权重。

</opt>

<opt text="1和4">

定制化组件只能修改`Doc`，并不能用来直接更新其它组件的模型权重。
定制化组件只有在语言类被初始化和流程中的分词步骤结束后才能被加入到流程中，
所以定制化组件不适用于增加新的语种。

</opt>

<opt text="2和3" correct="true">

定制化组件可以很方便地用来对documents、tokens和spans增加定制化变量，
以及定制化`doc.ents`。

</opt>

<opt text="2和4">

定制化组件只有在语言类被初始化和流程中的分词步骤结束后才能被加入到流程中，
所以定制化组件不适用于增加新的语种。

</opt>

<opt text="3和4">

定制化组件只有在语言类被初始化和流程中的分词步骤结束后才能被加入到流程中，
所以定制化组件不适用于增加新的语种。

</opt>

</choice>

</exercise>

<exercise id="6" title="简单组件">

这个例子中我们想要用一个定制化组件来打印文档的词符长度。
你能完成这段代码吗？

- 用`doc`长度来完成组件函数。
- 加入`"length_component"`到现有的流程中，作为其**第一个**组件。
- 试用这个新的流程，用`nlp`实例来处理一段任意的文本，比如"这是一个句子。"。

<codeblock id="03_06">

- 我们可以调用Python原生的`len()`方法来获取`Doc`实例的长度。
- 使用`nlp.add_pipe`方法把组件加入到流程中。记住要使用组件的字符串名字并且把`first`关键词参数设置为
  `True`来保证这个组件是被添加到其它所有组件之前的。
- 调用`nlp`实例来处理一段本文。

</codeblock>

</exercise>

<exercise id="7" title="复杂组件">

这个练习中我们要编写一个定制化组件，使用`PhraseMatcher`在文本中寻找动物名字，
然后把匹配到的名字加入到`doc.ents`中。我们已经在变量`matcher`中创建了含有匹配
动物名模板的`PhraseMatcher`。

- 定义这个定制化组件，在`doc`上面应用`matcher`。
- 给每一个匹配结果创建一个`Span`，添加`"ANIMAL"`的标签ID，然后
  用这些新的span覆盖`doc.ents`。
- 处理文本，打印`doc.ents`中所有实体的实体文本和实体标签。

<codeblock id="03_07">

- 注意所有的匹配结果是在一个`(match_id, start, end)`元组的列表中。
- `Span`类有四个参数：产生它的原始`doc`、起始索引、终止索引和标签。
- 在`nlp.add_pipe`上使用`after`关键词参数来把组件添加到另一个组件后面。
  记住要使用组件的字符串名字。

</codeblock>

</exercise>

<exercise id="8" title="扩展属性" type="slides">

<slides source="chapter3_03_extension-attributes">
</slides>

</exercise>

<exercise id="9" title="设置扩展属性(1)">

我们来练习设置一些扩展属性。

### 第一部分

- 用`Token.set_extension`来注册`"is_country"`（默认是`False`）。
- 对`"Spain"`更新该扩展属性，然后对所有词符打印这个属性。

<codeblock id="03_09_01">

注意扩展属性是在挂靠在`._`特性中，比如`doc._.has_color`。

</codeblock>

### 第二部分

- 用`Token.set_extension`来注册`"reversed"`（取值函数是`get_reversed`）。
- 对所有词符打印这个属性的值。

<codeblock id="03_09_02">

注意扩展属性是在挂靠在`._`特性中，比如`doc._.has_color`。

</codeblock>

</exercise>

<exercise id="10" title="设置扩展属性(2)">

我们来练习使用取值函数和方法扩展设置一些更复杂的属性。

### 第一部分

- 完成`get_has_number`函数。
- 用`Doc.set_extension`来注册`"has_number"`（取值函数是`get_has_number`）
  并打印这个属性的值。

<codeblock id="03_10_01">

- 注意扩展属性是在挂靠在`._`特性中，比如`doc._.has_color`。
- 如果`token.like_num`（词符是否组成一个数字）对`doc`中的任意一个词符返回`True`，
  那么`get_has_number`对该`doc`就应该返回`True`。

</codeblock>

### 第二部分

- 用`Span.set_extension`来注册`"to_html"`（`to_html`方法）。
- 在`doc[0:2]`上用标签`"strong"`来调用它。

<codeblock id="03_10_02">

- 扩展方法可以有一个或者多个输入参数。比如`doc._.some_method("argument")`。
- 传入方法的第一个参数一定是该方法要作用于的`Doc`、`Token`或者`Span`实例。

</codeblock>

</exercise>

<exercise id="11" title="实体和扩展">

在这个练习中，我们要结合定制化属性扩展和统计预测结果，创建一个属性取值函数，当
span为一个人、组织或者位置时返回其维基百科的查询URL。

- 完成`get_wikipedia_url`这个取值函数，使其只有在span的标签在标签列表中时
  才返回URL。
- 用取值函数`get_wikipedia_url`设置`Span`的扩展`"wikipedia_url"`。
- 遍历`doc`中的实体，输出它们的维基百科URL。

<codeblock id="03_11">

- 使用`span.label_`属性来获得span的字符串标签。如果span是一个实体的话这个标签
  就是实体识别器预测的结果。
- 记住扩展属性是在挂靠在`._`特性中，比如`doc._.has_color`。

</codeblock>

</exercise>

<exercise id="12" title="含有扩展的组件">

把扩展参数和定制化流程组件结合在一起会发挥很大的作用。在这个练习中，我们要写一个
流程组件，寻找国家名和一个返回国家首都（如果存在的话）的定制化属性。

`matcher`变量中已经有一个匹配所有国家的短语匹配器。`CAPITALS`变量中则有一个把国家名
映射到其首都城市的字典。

- 完成`countries_component_function`，为所有匹配结果创建一个含有标签`"GPE"`（地理政治实体）
  的`Span`。
- 把组件加入到流程中。
- 使用取值函数`get_capital`注册Span的扩展属性`"capital"`。
- 处理文本，对每一个`doc.ents`中的实体打印其实体文本、实体标签和实体的首都城市。

<codeblock id="03_12">

- `Span`类有四个参数：`doc`文档，span中词符的`start`和`end`索引以及标签`label`。
- 在`doc`上调用`PhraseMatcher`会返回一个`(match_id, start, end)`的元组表。
- 要注册一个新的扩展属性，在全局类如`Doc`、`Token`或者`Span`上面使用`set_extension`
  方法。要定义一个取值函数，使用`getter`这个关键字参数。
- 记住扩展属性是在挂靠在`._`特性中，比如`doc._.has_color`。

</codeblock>

</exercise>

<exercise id="13" title="规模化性能" type="slides">

<slides source="chapter3_04_scaling-performance">
</slides>

</exercise>

<exercise id="14" title="处理流">

在这个练习中，我们要使用`nlp.pipe`来做一些更高效的文本处理。
`nlp`实例已经为我们创建好了。在变量`TEXTS`中有一个关于流行美国快餐连锁的推特列表。

### 第一部分

- 用`nlp.pipe`重写这个例子。不要直接遍历文本来处理它们，而是遍历`nlp.pipe`产生的
  `doc`实例。

<codeblock id="03_14_01">

- `nlp.pipe`使我们可以把前两行代码合并为一行。
- `nlp.pipe`读入`TEXTS`然后产生一系列我们可以遍历的`doc`实例。

</codeblock>

### 第二部分

- 用`nlp.pipe`重写这个例子。记着对结果调用`list()`来把它变为一个列表。

<codeblock id="03_14_02"></codeblock>

### 第三部分

- 用`nlp.pipe`重写这个例子。记着对结果调用`list()`来把它变为一个列表。

<codeblock id="03_14_03"></codeblock>

</exercise>

<exercise id="15" title="在语境中处理数据">

在这个练习中，我们要用定制化属性将作者和书的一些信息加入到引用中。

变量`DATA`里有一个`[text, context]`的示例列表。文本text是一些有名书籍的引用，
而语境context是一些键值为`"author"`和`"book"`的字典。

- 使用`set_extension`方法在`Doc`上注册定制化属性`"author"`和`"book"`，其默认值
  为`None`。
- 使用`nlp.pipe`，设置`as_tuples=True`，处理`DATA`中的`[text, context]`对。
- 使用传入的对应信息作为语境覆盖`doc._.book`和`doc._.author`。

<codeblock id="03_15">

- `Doc.set_extension`方法有两个参数：一个是属性的字符串名字，另一个是一个
  关键字参数用来表示默认default、取值函数getter、赋值函数setter或者方法，比如
  我们可以设置`default=True`。
- 如果`as_tuples`被设置为`True`，那么`nlp.pipe`方法会读取一个`(text, context)`
  的元组列表然后产生一系列`(doc, context)`元组。

</codeblock>

</exercise>

<exercise id="16" title="选择性处理">

在这个练习中，我们使用`nlp.make_doc`和`nlp.select_pipes`方法只运行我们选择的
组件来处理文本。

### 第一部分

- 用`nlp.make_doc`重写代码使其只对文本做分词。

<codeblock id="03_16_01">

`nlp.make_doc`方法作用在一短文本上返回一个`Doc`，和`nlp`实例一样。

</codeblock>

### 第二部分

- 用`nlp.select_pipes`方法关闭词性标注(tagger)和词性还原(lemmatizer)的组件。
- 处理文本，将所有`doc`中的结果实体打印出来。

<codeblock id="03_16_02">

`nlp.select_pipes`方法可以接收关键字参数`enbale`或者`disable`，
读入一个组件名的列表来启用或者关闭相应的流程组件。
比如`nlp.select_pipes(disable="ner")`就会把命名实体识别器关掉。

</codeblock>

</exercise>
