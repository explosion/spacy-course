from spacy.lang.ja import Japanese

nlp = Japanese()

people = ["デヴィッド・ボウイ", "アンゲラ・メルケル", "レディー・ガガ"]

# PhraseMatcherのパターンのリストを作成
patterns = list(nlp.pipe(people))
