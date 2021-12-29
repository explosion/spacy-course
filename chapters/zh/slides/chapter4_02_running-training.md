---
type: slides
---

# 配置和运行训练流程

Notes: 我们现在已经学会了如何创建训练数据，我们来看看如何配置和训练流程。本节课中我们会
学习到spaCy的训练配置系统，如何生成我们自己的训练配置，如果使用CLI来训练模型，以及如何
在训练结束后测试我们的流程。

---

# 训练配置(1)

- 所有设定的**唯一真理来源**
- 通常被叫做`config.cfg`
- 定义了如何初始化`nlp`对象
- 包含了关于流程组件和模型实现的所有设定
- 配置了训练过程和超参数
- 使我们的训练过程可复现

Notes: spaCy使用的配置文件通常被叫做`config.cfg`，是所有设定的“唯一真理来源”。这个
配置文件决定了如何初始化`nlp`对象，哪些流程组件被添加，以及如何配置组件内部的模型实现。
配置文件还包含了训练过程的所有设定，包括如何读取数据和超参数等。

由此我们再不需要在命令行提供大量的的参数，或是在代码中记着定义每一个设定。我们只需要把
配置文件传给spaCy的训练指令即可。

配置文件也帮助我们可以更好复现训练过程：所有的设定都在同一个地方，流程训练一目了然。
我们甚至可以将配置文件放到Git仓库中，加入版本控制分享给其他人，这样其他人也可以
用同样的设定训练同样的流程。

---

# 训练配置(2)

```ini
[nlp]
lang = "zh"
pipeline = ["tok2vec", "ner"]
batch_size = 1000
[nlp.tokenizer]
@tokenizers = "spacy.zh.ChineseTokenizer"
segmenter = "char"
[components]
[components.ner]
factory = "ner"
[components.ner.model]
@architectures = "spacy.TransitionBasedParser.v2"
hidden_width = 64
# 以此类推
```

Notes: 这是从训练一个命名实体识别器的流程配置文件中摘取的片段。配置文件分为几个部分，
嵌套部分用一个点来定义。比如，`[components.ner.model]`定义了命名实体识别器
的模型实现的设定。

配置文件也可以用`@`标记来引用Python函数。比如，分词器定义了一个注册过的分词函数。我们
可以用它来定制化`nlp`对象和训练的不同部分 - 从嵌入我们自己的分词器到实现我们自己的模型
架构。但是我们现在先不用担心 - 本章节中我们只是简单使用spaCy提供的开箱可用的默认配置。

---

# 生成一个配置文件

- spaCy可以自动生成一个默认的配置文件
- 文档中有可交互的[快速上手插件](https://spacy.io/usage/training#quickstart)
- 作用于CLI的[`init config`](https://spacy.io/api/cli#init-config)命令

```bash
$ python -m spacy init config ./config.cfg --lang zh --pipeline ner
```

- `init config`: 要运行的命令
- `config.cfg`: 生成的配置文档的输出路径
- `--lang`: 流程的语言类，比如中文是 `zh`
- `--pipeline`: 用逗号分隔的流程组件名称

Notes: 当然了，我们往往不需要手写配置文件，很多情况下我们甚至不需要定制化配置文件。
spaCy会自动帮我们生成。

文档中的快速上手插件可以交互式地帮我们生成配置文件，让我们选择需要的语言和流程组件以及
可选的硬件和优化设定。

另外，我们也可以使用spaCy内建的`init config`命令。该命令的第一个参数是输出文件，我们通常
起名为`config.cfg`. 参数`--lang`定义了流程的语言类，比如`zh`就是中文。`--pipeline`参数
让我们指定一个或多个用逗号分隔的流程组件来加入流程之中。这个例子中，我们创建了一个配置文件，
含有一个命名实体识别的流程组件。

---

# 训练流程(1)

- 我们需要的只是`config.cfg`和训练与测试数据
- 配置的设定可以在命令行中被覆盖

```bash
$ python -m spacy train ./config.cfg --output ./output --paths.train train.spacy --paths.dev dev.spacy
```

- `train`: 要运行的命令
- `config.cfg`: 配置文档的路径
- `--output`: 保存训练流程的输出路径
- `--paths.train`: 覆盖训练数据的路径
- `--paths.dev`: 覆盖测试数据的路径

Notes: 要训练一个流程，我们需要的只是`config.cfg`和训练与测试数据。这些数据都是在之前练习中
我们见到过的`.spacy`文件。

`spaCy train`的第一个参数是配置文件的路径。`--output`参数可以指定保存最终训练好的流程的输出路径。

我们还可以在命令行中覆盖不同的配置设定。在这个例子里面，我们用`train.spacy`文件的路径
覆盖了`paths.train`，用`dev.spacy`文件的路径覆盖了`paths.dev`.

---

# 训练流程(2)

```
============================ Training pipeline ============================
ℹ Pipeline: ['tok2vec', 'ner']
ℹ Initial learn rate: 0.001
E    #       LOSS TOK2VEC  LOSS NER  ENTS_F  ENTS_P  ENTS_R  SCORE
---  ------  ------------  --------  ------  ------  ------  ------
  0       0          0.00     26.50    0.73    0.39    5.43    0.01
  0     200         33.58    847.68   10.88   44.44    6.20    0.11
  1     400         70.88    267.65   33.50   45.95   26.36    0.33
  2     600         67.56    156.63   45.32   62.16   35.66    0.45
  3     800        138.28    134.12   48.17   74.19   35.66    0.48
  4    1000        177.95    109.77   51.43   66.67   41.86    0.51
  6    1200         94.95     52.13   54.63   67.82   45.74    0.55
  8    1400        126.85     66.19   56.00   65.62   48.84    0.56
 10    1600         38.34     24.16   51.96   70.67   41.09    0.52
 13    1800        105.14     23.23   56.88   69.66   48.06    0.57
✔ Saved pipeline to output directory
/path/to/output/model-last
```

Notes: 这是训练过程中和结束时我们会看到的一个屏幕输出的例子。我们还记得之前提到过，我们
通常希望在训练过程中遍历数据多次。每一次遍历数据被叫做一个"epoch"。这就是表中的第一列。

每一个epoch中，spaCy会在每200个数据后输出准确度分数。这是第二列中显示的步骤。我们可以
在配置文件中修改这个频率。每一行显示了训练中的这一步模型损失和计算得到的准确度分数。

我们要留意的最有趣的分数时最后一列的合成分数。这反映了我们的模型在测试数据中预测正确的准确度。

训练过程会一直进行直到模型没有进一步的改进空间了，这时程序就会自动退出。

---

# 读取已经训练好的流程

- 训练后的输出是一个正常的可读取的spaCy流程
  - `model-last`: 最后训练出的流程
  - `model-best`: 表现最好的训练流程
- 用`spacy.load`读取流程

```python
import spacy
nlp = spacy.load("/path/to/output/model-best")
doc = nlp("iPhone 11 vs iPhone 8: 到底有什么区别？")
print(doc.ents)
```

Notes: 训练结束后存储的流程是一个正常的可读取的spaCy流程 - 就像其它spaCy提供的训练好的流程一样，
比如 `zh_core_web_sm`. 最终，最后训练出的流程和最高分的流程都会被存储在输出路径中。

我们可以把路径传给`spacy.load`来读取已经训练好的流程。我们接下来就可以用它来处理和分析文本了。

---

# 小经验：将流程打包

<!-- TODO: illustration of pipeline packages, similar to earlier chapters? -->

- [`spacy package`](https://spacy.io/api/cli#package): 创建一个包含我们流程的可安装的Python包
- 方便版本控制和部署

```bash
$ python -m spacy package /path/to/output/model-best ./packages --name my_pipeline --version 1.0.0
```

```bash
$ cd ./packages/zh_my_pipeline-1.0.0
$ pip install dist/zh_my_pipeline-1.0.0.tar.gz
```

安装后读取和使用流程：

```python
nlp = spacy.load("zh_my_pipeline")
```


Notes: 为了更方便地部署我们的流程，spaCy提供了一系列趁手的命令来将流程打包成Python包。
`spacy package`读取的参数包括我们生成的流程路径和输出路径，然后生成一个含有我们流程的
Python包。这个Python包是`.tar.gz`格式的文件，可以安装到环境中。

我们还可以在命令中提供可选的名字和版本号，这样我们就可以管理同一个流程的多个不同版本，
比如我们想继续定制化我们的流程或者用更多的数据训练它。

使用这个包和使用其它Python包是一样的。安装完后，我们可以用包名来读取流程。注意spaCy会自动把
语言代码加到名字中，所以我们的流程`my_pipeline`最后就成了`zh_my_pipeline`.

---

# 上手练习吧！

Notes: 让我们上手来训练我们的第一个流程！我们会练习生成一个命名实体识别器的配置文件，
然后用之前练习中生成的数据来训练这个流程。