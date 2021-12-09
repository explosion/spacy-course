import spacy

nlp = spacy.blank("ja")

people = ["デヴィッド・ボウイ", "アンゲラ・メルケル", "レディー・ガガ"]

# PhraseMatcherのパターンのリストを作成
patterns = [nlp(person) for person in people]
