import spacy
from spacy.matcher import Matcher

nlp = spacy.load("zh_core_web_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "我之前有去下载Dota到电脑上面，但是根本打不开游戏，怎么办？"
    "我下载Minecraft，是Windows的版本，下载后是一个'.zip'的文件夹，然后我用了默认软件做了"
    "解压...我是不是还需要去下载Winzip？"
)

# 写一个模板来匹配"下载"加一个代词
pattern = [{"TEXT": "下载"}, {"POS": "PROPN"}]

# 把模板加入到matcher中，然后把matcher应用到doc上面
matcher.add("DOWNLOAD_THINGS_PATTERN", [pattern])
matches = matcher(doc)
print("Total matches found:", len(matches))

# 遍历所有的匹配，打印span的文本
for match_id, start, end in matches:
    print("Match found:", doc[start:end].text)