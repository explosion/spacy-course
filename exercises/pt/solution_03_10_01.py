import spacy
from spacy.tokens import Doc

nlp = spacy.blank("pt")

# Definir a função para o atributo getter
def get_has_number(doc):
    # Retornar verdadeiro (True) se algum token do doc for número (token.like_num)
    return any(token.like_num for token in doc)


# Definir a propriedade extendida "has_number" com o getter sendo get_has_number
Doc.set_extension("has_number", getter=get_has_number)

# Processar o texto e verificar a propriedade has_number
doc = nlp("O museu esteve fechado por cinco anos em 2012.")
print("has_number:", doc._.has_number)
