import spacy
from spacy.language import Language
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

nlp = spacy.load("ja_core_news_sm")
animals = ["ゴールデンレトリバー", "ネコ", "カメ", "ドブネズミ"]
animal_patterns = list(nlp.pipe(animals))
print("動物の一覧: ", animal_patterns)
matcher = PhraseMatcher(nlp.vocab)
matcher.add("ANIMAL", None, *animal_patterns)

# カスタムコンポーネントを定義
@Language.component("animal_component")
def animal_component_function(doc):
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

# テキストを処理し、doc.entsの文字列とラベルを表示
doc = nlp("私はネコとゴールデンレトリバーを飼っている。")
print([(____, ____) for ent in ____])
