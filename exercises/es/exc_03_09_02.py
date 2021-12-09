import spacy
from spacy.tokens import Token

nlp = spacy.blank("es")

# Define la función getter que toma un token y devuelve su texto al revés
def get_reversed(token):
    return token.text[::-1]


# Registra la extensión de propiedad del Token, "reversed", con
# el getter get_reversed
____.____(____, ____=____)

# Procesa el texto e imprime en pantalla el atributo "reversed"
# para cada token
doc = nlp("Todas las generalizaciones son falsas, incluyendo esta.")
for ____ in ____:
    print("invertido:", ____)
