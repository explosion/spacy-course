import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

nlp = spacy.load("en_core_web_sm")
animals = ["Golden Retriever", "cat", "turtle", "Rattus norvegicus"]
animal_patterns = list(nlp.pipe(animals))
print("animal_patterns:", animal_patterns)
matcher = PhraseMatcher(nlp.vocab)
matcher.add("ANIMAL", None, *animal_patterns)

# 定义定制化组件
def animal_component(doc):
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
doc = nlp("I have a cat and a Golden Retriever")
print([(____, ____) for ent in ____])
