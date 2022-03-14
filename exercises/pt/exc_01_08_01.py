import spacy

# Carregue o fluxo de processamento pequeno do idioma portugues "pt_core_web_sm"
# Faça antes o download do fluxo com o comando: python -m spacy download pt_core_news_sm
nlp = spacy.load("pt_core_news_sm")

text = "É oficial: a Apple é a primeira empresa dos Estados Unidos a ter o valor de mercado acima de 1 trilhão."

# Processar o texto
doc = ____

for token in doc:
    # Selecionar o texto, a classe gramatical e o termo sintático de um token
    token_text = ____.____
    token_pos = ____.____
    token_dep = ____.____
    # Para uma boa formatação da impressão
    print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")
