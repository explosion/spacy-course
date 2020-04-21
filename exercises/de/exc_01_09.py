import spacy

nlp = spacy.load("de_core_news_sm")

text = "Apple: Neues Modell iPhone SE kommt im Sommer"

# Verarbeite den Text
doc = ____

# Iteriere über die Entitäten
for ____ in ____.____:
    # Drucke Text und Label der Entität
    print(____.____, ____.____)

# Erstelle eine Span für "iPhone SE"
iphone_se = ____

# Drucke den Text der Span
print("Fehlende Entität:", iphone_se.text)
