import spacy

nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# Processar o texto
doc = ____

for token in doc:
    # Selecionar o texto, s classe gramatical e o termo sintático de um token
    token_text = ____.____
    token_pos = ____.____
    token_dep = ____.____
    # Para uma boa formatação da impressão
    print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")
