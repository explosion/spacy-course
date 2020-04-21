import spacy

nlp = spacy.load("de_core_news_sm")

text = "Apple wurde 1976 von Steve Wozniak, Steve Jobs und Ron Wayne gegründet."

# Verarbeite den Text
doc = ____

for token in doc:
    # Greife auf den Text, die Wortart und die Dependenzrelation des Tokens zu
    token_text = ____.____
    token_pos = ____.____
    token_dep = ____.____
    # Dies dient nur zur Formatierung
    print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")
