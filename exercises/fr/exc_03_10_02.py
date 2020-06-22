from spacy.lang.en import English
from spacy.tokens import Span

nlp = English()

# Définis la méthode
def to_html(span, tag):
    # Entoure le texte du span avec une balise HTML et retourne l'ensemble
    return f"<{tag}>{span.text}</{tag}>"


# Déclare l'extension de méthode de Span "to_html" avec la méthode to_html
____.____(____, ____=____)

# Traite le texte et applique la méthode to_html sur le span avec la balise "strong"
doc = nlp("Hello world, this is a sentence.")
span = doc[0:2]
print(____)
