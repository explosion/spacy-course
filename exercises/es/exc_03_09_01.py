from spacy.lang.en import English
from spacy.tokens import Token

nlp = English()

# Registra la extensión de atributo del Token, "is_country", con el valor por defecto False 
____.____(____, ____=____)

# Procesa el texto y pon True para el atributo "is_country" para el token "Spain"
doc = nlp("I live in Spain.")
____ = True

# Imprime en pantalla el texto del token y el atributo "is_country" para todos los tokens
print([(____, ____) for token in doc])
