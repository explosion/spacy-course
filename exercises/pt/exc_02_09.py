import spacy

# Carregue o fluxo de processamento en_core_web_md
# para fazer o download do fluxo: python -m spacy download pt_core_news_md
nlp = ____

# Processe um texto 
doc = nlp("Duas bananas de pijamas")

# Imprima o vetor para "bananas"
bananas_vector = ____.____
print(bananas_vector)
