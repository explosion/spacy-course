from spacy.lang.es import Spanish
from spacy.tokens import Span

nlp = Spanish()

# Define el método
def to_html(span, tag):
    # Envuelve el texto del span en un HTML tag y devuélvelo
    return f"<{tag}>{span.text}</{tag}>"


# Registra la extensión de propiedad del Span, "to_html",
# con el método "to_html"
____.____(____, ____=____)

# Procesa el texto y llama el método "to_html"en el span
# con el nombre de tag "strong"
doc = nlp("Hola mundo, esto es una frase.")
span = doc[0:2]
print(____)
