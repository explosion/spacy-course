import spacy

nlp = spacy.load("pt_core_news_md")

doc = nlp("Este é um excelente restaurante. Em seguida fomos a um ótimo bar.")

# Crie partições para "excelente restaurante" e "ótimo bar"
span1 = doc[3:5]
span2 = doc[11:13]
print(span1)
print(span2)

# Obtenha a similaridade das partições
similarity = span1.similarity(span2)
print(similarity)
