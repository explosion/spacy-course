from spacy.lang.es import Spanish
from spacy.tokens import Token

nlp = Spanish()

# Define la función getter que toma un token y devuelve su texto al revés
def get_reversed(token):
    return token.text[::-1]


# Registra la extensión de propiedad del Token, "reversed", con
# el getter get_reversed
Token.set_extension("reversed", getter=get_reversed)

# Procesa el texto e imprime en pantalla el atributo "reversed"
# para cada token
doc = nlp("Todas las generalizaciones son falsas, incluyendo esta.")
for token in doc:
    print("invertido:", token._.reversed)
