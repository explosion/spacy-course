from spacy.lang.es import Spanish
from spacy.tokens import Token

nlp = Spanish()

# Registra la extensión de atributo del Token, "is_country",
# con el valor por defecto False
Token.set_extension("is_country", default=False)

# Procesa el texto y pon True para el atributo "is_country"
# para el token "España"
doc = nlp("Vivo en España.")
doc[2]._.is_country = True

# Imprime en pantalla el texto del token y el atributo "is_country"
# para todos los tokens
print([(token.text, token._.is_country) for token in doc])
