import spacy

nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# Processar o texto
doc = nlp(text)

for token in doc:
    # Selecionar o texto, s classe gramatical e o termo sintático de um token
    token_text = token.text
    token_pos = token.pos_
    token_dep = token.dep_
    # Para uma boa formatação da impressão
    print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")
