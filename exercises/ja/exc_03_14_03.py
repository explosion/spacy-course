from spacy.lang.en import English

nlp = English()

people = ["David Bowie", "Angela Merkel", "Lady Gaga"]

# PhraseMatcherのパターンのリストを作成
patterns = [nlp(person) for person in people]
