import spacy

nlp = spacy.load("pt_core_news_md")

doc = nlp("Visitamos um excelente restaurante. Em seguida fomos a um ótimo bar.")

# Crie partições para "excelente restaurante" e "ótimo bar"
span1 = ____
span2 = ____
print(span1)
print(span2)

# Obtenha a similaridade das partições
similarity = ____.____(____)
print(similarity)
