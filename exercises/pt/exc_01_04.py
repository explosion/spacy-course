import spacy

nlp = spacy.blank("pt")

# Processar o texto
doc = nlp(
    "Em 1990, mais de 60% da população da Ásia Oriental estava em situação de extrema pobreza."
    "Agora, menos de 4% está nessa situação."
)

# Iterar os tokens de um documento doc 
for token in doc:
    # Checar se o token é composto por algarismos numéricos
    if ____.____:
        # Selecionar o próximo token do documento
        next_token = ____[____]
        # Checar se o texto do proximo token é igual a "%"
        if next_token.____ == "%":
            print("Percentuais encontrados:", token.text)
