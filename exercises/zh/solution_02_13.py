import spacy
from spacy.matcher import Matcher

nlp = spacy.load("zh_core_web_sm")

doc = nlp("荣耀将于7月16日发布新一代 MagicBook 锐龙笔记本，显然会配备7nm工艺、Zen2 架构的"
          "全新锐龙4000系列，但具体采用低功耗的锐龙4000U 系列，还是高性能的锐龙4000H 系列，"
          "目前还没有官方消息。今天，推特曝料大神公布了全新 MagicBook Pro 锐龙本的配置情况。"
         )

# 创建匹配模板
pattern1 = [{"POS": "ADJ"},{"TEXT": "笔记本"}]
pattern2 = [{"TEXT": "锐龙"}, {"LIKE_NUM": True}, {"IS_ASCII": True}]

# 初始化matcher并加入模板
matcher = Matcher(nlp.vocab)
matcher.add("PATTERN1", [pattern1])
matcher.add("PATTERN2", [pattern2])

# 遍历匹配结果
for match_id, start, end in matcher(doc):
    # 打印匹配到的字符串名字及匹配到的span的文本
    print(doc.vocab.strings[match_id], doc[start:end].text)
