import spacy

nlp = spacy.load("pt_core_news_md")

doc = nlp("Visitamos um excelente restaurante. Em seguida fomos a um ótimo bar.")

# Crie partições para "excelente restaurante" e "ótimo bar"
span1 = doc[2:4]
span2 = doc[10:12]
print(span1)
print(span2)

# Obtenha a similaridade das partições
similarity = span1.similarity(span2)
print(similarity)
