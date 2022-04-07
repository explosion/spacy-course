import spacy

# Carregue o fluxo de processamento pequeno do idioma portugues "pt_core_web_sm"
# Faça antes o download do fluxo com o comando: python -m spacy download pt_core_news_sm
nlp = spacy.load("pt_core_news_sm")

text = "Vazou a data de lançamento do novo iPhone X após a Apple revelar a existência de compras antecipadas."

# Processar o texto
doc = ____

# Iterar nas entidades previstas
for ____ in ____.____:
    # Imprimir o texto e etiqueta (label) da entidade
    print(____.____, ____.____)

# Selecionar a partição para "iPhone X"
iphone_x = ____

# Imprimir o texto da partição
print("Missing entity:", iphone_x.text)
