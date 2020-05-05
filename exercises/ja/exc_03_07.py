import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

nlp = spacy.load("en_core_web_sm")
animals = ["Golden Retriever", "cat", "turtle", "Rattus norvegicus"]
animal_patterns = list(nlp.pipe(animals))
print("animal_patterns:", animal_patterns)
matcher = PhraseMatcher(nlp.vocab)
matcher.add("ANIMAL", None, *animal_patterns)

# カスタムコンポーネントを定義
def animal_component(doc):
    # matcherをdocに適用
    matches = ____
    # マッチした結果に対してSpanを作り、"ANIMAL"のラベルを付ける
    spans = [Span(____, ____, ___, label=____) for match_id, start, end in matches]
    # doc.entsにマッチ結果のスパンを追加
    doc.ents = spans
    return doc


# 「ner」コンポーネントのあとに追加
____.____(____, ____=____)
print(nlp.pipe_names)

# テキストを処理し、doc.entsの文字列とラベルをプリント
doc = nlp("I have a cat and a Golden Retriever")
print([(____, ____) for ent in ____])
