import spacy

nlp = spacy.load("de_core_news_sm")
text = (
    "Chick-fil-A, ein Wortspiel mit der amerikanischen Aussprache von „Filet“, "
    "ist der Name einer 1946 gegründeten amerikanischen Schnellrestaurantkette, "
    "die sich auf den Verkauf von Hühnerfleischprodukten spezialisiert hat."
)

# Wende nur den Tokenizer an
doc = nlp.make_doc(text)
print([token.text for token in doc])
