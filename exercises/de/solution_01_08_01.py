import spacy

nlp = spacy.load("de_core_news_sm")

text = "Apple wurde 1976 von Steve Wozniak, Steve Jobs und Ron Wayne gegründet."

# Verarbeite den Text
doc = nlp(text)

for token in doc:
    # Greife auf den Text, die Wortart und die Dependenzrelation des Tokens zu
    token_text = token.text
    token_pos = token.pos_
    token_dep = token.dep_
    # Dies dient nur zur Formatierung
    print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")
