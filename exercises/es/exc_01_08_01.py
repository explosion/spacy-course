import spacy

nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# Procesa el texto
doc = ____

for token in doc:
    # Obtén el texto del token, el part-of-speech tag y el dependency label
    token_text = ____.____
    token_pos = ____.____
    token_dep = ____.____
    # Esto es solo por formato
    print("{:<12}{:<10}{:<10}".format(token_text, token_pos, token_dep))
