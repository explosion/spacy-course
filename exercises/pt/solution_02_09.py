import spacy

# Carregue o fluxo de processamento en_core_web_md
nlp = spacy.load("en_core_web_md")

# Processe um texto 
doc = nlp("Two bananas in pyjamas")

# Imprima o vetor para "bananas"
bananas_vector = doc[1].vector
print(bananas_vector)
