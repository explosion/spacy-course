import spacy

nlp = spacy.load("de_core_news_sm")

text = "Apple: Modell IPhone SE kommt im Sommer"

# Verarbeite den Text
doc = nlp(text)

# Iteriere über die Entitäten
for ent in doc.ents:
    # Drucke Text und Label der Entität
    print(ent.text, ent.label_)

# Erstelle eine Span für "iPhone SE"
iphone_se = doc[3:5]

# Drucke den Text der Span
print("Fehlende Entität:", iphone_se.text)
