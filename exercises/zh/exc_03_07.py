import spacy
from spacy.language import Language
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

nlp = spacy.load("zh_core_web_sm")
animals = ["金毛犬", "猫", "乌龟", "老鼠"]
animal_patterns = list(nlp.pipe(animals))
print("animal_patterns:", animal_patterns)
matcher = PhraseMatcher(nlp.vocab)
matcher.add("ANIMAL", animal_patterns)

# 定义定制化组件
@Language.component("animal_component")
def animal_component_function(doc):
    # 把matcher应用到doc上
    matches = ____
    # 为每一个匹配结果生成一个Span并赋予标签"ANIMAL"
    spans = [Span(____, ____, ___, label=____) for match_id, start, end in matches]
    # 用匹配到的span覆盖doc.ents
    doc.ents = spans
    return doc


# 把组件加入到流程中，紧跟在"ner"组件后面
____.____(____, ____=____)
print(nlp.pipe_names)

# 处理文本，打印doc.ents的文本和标签
doc = nlp("我养了一只猫和一条金毛犬。")
print([(____, ____) for ent in ____])
