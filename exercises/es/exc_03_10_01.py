from spacy.lang.es import Spanish
from spacy.tokens import Doc

nlp = Spanish()

# Define la función getter
def get_has_number(doc):
    # Devuelve si alguno de los tokens en el doc devuelve True
    # para token.like_num
    return any(____ for token in doc)


# Registra la extensión de propiedad del Doc, "has_number",
# con el getter get_has_number
____.____(____, ____=____)

# Procesa el texto y revisa el atributo personalizado "has_number"
doc = nlp("El museo cerró por cinco años en el 2012.")
print("has_number:", ____)
