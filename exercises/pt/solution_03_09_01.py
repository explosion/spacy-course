import spacy
from spacy.tokens import Token

nlp = spacy.blank("en")

# Definir o atributo "is_country" com o valor padrão como falso (False)
Token.set_extension("is_country", default=False)

# Processar o texto e atribuir o atributo is_country com valor verdadeiro (True) para o token "Spain"
doc = nlp("I live in Spain.")
doc[3]._.is_country = True

# Imprimir o texto e o atributo is_country para todos os tokens
print([(token.text, token._.is_country) for token in doc])
