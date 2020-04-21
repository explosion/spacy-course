import spacy

nlp = spacy.load("de_core_news_sm")

text = "Apple wurde 1976 von Steve Wozniak, Steve Jobs und Ron Wayne gegründet."

# Verarbeite den Text
doc = nlp(text)

# Iteriere über die vorhergesagten Entitäten
for ent in doc.ents:
    # Drucke den Text und das Label der Entität
    print(ent.text, ent.label_)
