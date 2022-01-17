import spacy
from spacy.tokens import Doc

nlp = spacy.blank("en")

# Definir a função para o atributo getter
def get_has_number(doc):
    # Retornar verdadeiro (True) se algum token do doc for número (token.like_num)
    return any(____ for token in doc)


# Definir a propriedade extendida "has_number" com o getter sendo get_has_number
____.____(____, ____=____)

# Processar o texto e verificar a propriedade has_number
doc = nlp("The museum closed for five years in 2012.")
print("has_number:", ____)
