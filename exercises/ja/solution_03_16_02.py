import spacy

nlp = spacy.load("en_core_web_sm")
text = (
    "Chick-fil-A is an American fast food restaurant chain headquartered in "
    "the city of College Park, Georgia, specializing in chicken sandwiches."
)

# taggerとparserを無効化する
with nlp.disable_pipes("tagger", "parser"):
    # テキストを処理する
    doc = nlp(text)
    # docの固有表現をプリントする
    print(doc.ents)
