import spacy

# Carregue o fluxo de processamento pequeno do idioma portugues "pt_core_web_sm"
# Faça antes o download do fluxo com o comando: python -m spacy download pt_core_news_sm
nlp = spacy.load("pt_core_news_sm")

text = "É oficial: a Apple é a primeira empresa dos Estados Unidos a ter o valor de mercado acima de 1 trilhão."

# Processar o texto
doc = ____

# Iterar nas entidades previstas
for ent in ____.____:
    # Imprimir o texto e a etiqueta da entidade
    print(ent.____, ____.____)
