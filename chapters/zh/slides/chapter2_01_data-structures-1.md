---
type: slides
---

# 数据结构 (1): Vocab, Lexemes和StringStore

Notes: 欢迎回来！现在你已经有一些spaCy实例的实战经验了，
是时候学习一下spaCy背后到底是怎么工作的了。

在这门课中，我们要看下共享词汇表以及spaCy如何处理字符串。

---

# 共享词汇表和字符串库 (1)

- `Vocab`: 存储那些多个文档共享的数据
- 为了节省内存使用，spaCy将所有字符串编码为**哈希值**。
- 字符串只在`StringStore`中通过`nlp.vocab.strings`存储一次。
- 字符串库：双向的**查询表**

```python
nlp.vocab.strings.add("咖啡")
coffee_hash = nlp.vocab.strings["咖啡"]
coffee_string = nlp.vocab.strings[coffee_hash]
```
- 哈希是不能逆求解的，所以我们要提供共享词汇表。

```python
# 如果该字符串从未出现过则会报错
string = nlp.vocab.strings[7962530705879205333]
```

Notes: spaCy把所有共享数据都存在一个词汇表里，也就是Vocab。

这里面除了有很多词汇，还包括了标注和实体的标注方案。

为了节省内存，所有的字符串都被编码成哈希ID。
如果一个词出现多过一次，我们就不需要每次都多存储一次。

相反，spaCy使用哈希方程生成一个ID，和对应的字符串一起在字符串库中仅存储一次。
`nlp.vocab.strings`这个字符串库就在`nlp.vocab.strings`里。

这是一个双向的查询表。你可以查找一个字符串获得其哈希值，
也可以查找一个哈希值获得其字符串值。
spaCy内部的信息交流都是通过哈希ID进行的。

然而哈希ID不能逆求解。如果一个词不在词汇表里，那我们也没法办拿到它的字符串。
这也是为什么我们每次都要把共享词汇表传进来。

---

# 共享词汇表和字符串库 (2)

- 在`nlp.vocab.strings`中查找字符串和哈希值

```python
doc = nlp("我爱喝咖啡。")
print("hash value:", nlp.vocab.strings["咖啡"])
print("string value:", nlp.vocab.strings[7962530705879205333])
```

```out
hash value: 7962530705879205333
string value: 咖啡
```
- `doc`也会暴露出词汇表和字符串

```python
doc = nlp("我爱喝咖啡。")
print("hash value:", doc.vocab.strings["咖啡"])
```

```out
hash value: 7962530705879205333
```

Notes: 要拿到字符串的哈希值，我们要在`nlp.vocab.strings`中查找。

要拿到一个哈希值的字符串形式，我们可以查询哈希值。

一个`Doc`实例也可以暴露出它的词汇表和字符串。

---

# Lexemes: 词汇表中的元素

- 一个`Lexeme`实例是词汇表中的一个元素

```python
doc = nlp("我爱喝咖啡。")
lexeme = nlp.vocab["咖啡"]

# 打印词汇的属性
print(lexeme.text, lexeme.orth, lexeme.is_alpha)
```

```out
咖啡 7962530705879205333 True
```

- 包含了一个词的**和语境无关**的信息
  - 词组的文本：`lexeme.text`和`lexeme.orth`（哈希值）
  - 词汇的属性如`lexeme.is_alpha`
  - **并不包含**和语境相关的词性标注、依存关系和实体标签

Notes: Lexeme（语素）是词汇表中和语境无关的元素。

在词汇表中查询一个字符串或者一个哈希ID就会获得一个lexeme。

Lexeme可以暴露出一些属性，就像词符一样。

它们代表着一个词的和语境无关的信息，比如文本本身，或者是这个词是否包含了英文字母。

Lexeme中没有词性标注、依存关系或者实体标签这些和语境关联的信息。

---

# Vocab, 哈希值和语素

<img src="/vocab_stringstore_zh.png" width="70%" alt="'I'、'love'和'coffee'三个词在Doc、Vocab和StringStore中的图解" />

Notes: 我们来看一个例子。

`Doc`包含了语境中的词汇，在这个例子里面就是指"I"、"love"、"coffee"这三个词符
以及它们的词性标注和依存关系。

每个词符对应一个语素lexeme，里面保存着词汇的哈希ID。
要拿到这个词的文本表示，spaCy要在字符串库里面查找它的哈希值。

---

# 上手练习吧！

Notes: 可能这些都听上去有些抽象，
所以让我们上手看下实际中的词汇表和字符串库。
