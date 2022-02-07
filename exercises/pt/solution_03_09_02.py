import spacy
from spacy.tokens import Token

nlp = spacy.blank("pt")

# Definir a função que recebe um token e retorna seu conteúdo invertido
def get_reversed(token):
    return token.text[::-1]


# Registrar o atributo extendido "reversed" com o argumento getter sendo a função get_reversed
Token.set_extension("reversed", getter=get_reversed)

# Processar o texto e imprimir o atributo "reversed" para cada token
doc = nlp("Todas generalizações são falsas, incluindo esta.")
for token in doc:
    print("reversed:", token._.reversed)
