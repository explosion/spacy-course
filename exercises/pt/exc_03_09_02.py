import spacy
from spacy.tokens import Token

nlp = spacy.blank("pt")

# Definir a função que recebe um token e retorna seu conteúdo invertido
def get_reversed(token):
    return token.text[::-1]


# Registrar o atributo extendido "reversed" com o argumento getter sendo a função get_reversed
____.____(____, ____=____)

# Processar o texto e imprimir o atributo "reversed" para cada token
doc = nlp("Todas generalizações são falsas, incluindo esta.")
for ____ in ____:
    print("reversed:", ____)
