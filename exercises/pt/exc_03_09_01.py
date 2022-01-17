import spacy
from spacy.tokens import Token

nlp = spacy.blank("en")

# Definir o atributo "is_country" com o valor padrão como falso (False)
____.____(____, ____=____)

# Processar o texto e atribuir o atributo is_country com valor verdadeiro (True) para o token "Spain"
doc = nlp("I live in Spain.")
____ = True

# Imprimir o texto e o atributo is_country para todos os tokens
print([(____, ____) for token in doc])
