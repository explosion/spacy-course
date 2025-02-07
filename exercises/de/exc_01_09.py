import spacy

nlp = spacy.load("de_core_news_sm")

text = "Apple bringt neues Modell X Pro im Sommer"

# Verarbeite den Text
doc = ____

# Iteriere über die Entitäten
for ____ in ____.____:
    # Drucke Text und Label der Entität
    print(____.____, ____.____)

# Erstelle eine Span für "X Pro"
x_pro = ____

# Drucke den Text der Span
print("Fehlende Entität:", x_pro.text)
