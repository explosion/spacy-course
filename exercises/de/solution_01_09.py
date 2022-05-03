import spacy

nlp = spacy.load("de_core_news_sm")

text = "Apple bringt neues Modell X Pro im Sommer"

# Verarbeite den Text
doc = nlp(text)

# Iteriere über die Entitäten
for ent in doc.ents:
    # Drucke Text und Label der Entität
    print(ent.text, ent.label_)

# Erstelle eine Span für "X Pro"
x_pro = doc[4:6]

# Drucke den Text der Span
print("Fehlende Entität:", x_pro.text)
