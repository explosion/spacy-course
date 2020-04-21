import spacy

# Lade das Modell "de_core_news_sm"
nlp = spacy.load("de_core_news_sm")

text = "Apple wurde 1976 von Steve Wozniak, Steve Jobs und Ron Wayne gegründet."

# Verarbeite den Text
doc = nlp(text)

# Drucke den Text des Dokuments
print(doc.text)
