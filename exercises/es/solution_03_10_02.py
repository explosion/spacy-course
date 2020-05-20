from spacy.lang.en import English
from spacy.tokens import Span

nlp = English()

# Define el método
def to_html(span, tag):
    # Envuelve el texto del span en un HTML tag y devuélvelo
    return f"<{tag}>{span.text}</{tag}>"


# Registra la extensión de propiedad del Span, "to_html", con el método "to_html"
Span.set_extension("to_html", method=to_html)

# Procesa el texto y llama el método "to_html" en el span con el nombre de tag "strong"
doc = nlp("Hello world, this is a sentence.")
span = doc[0:2]
print(span._.to_html("strong"))
