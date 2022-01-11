import spacy
from spacy.tokens import Span

nlp = spacy.blank("fr")

# Définis la méthode
def to_html(span, tag):
    # Entoure le texte du span avec une balise HTML et retourne l'ensemble
    return f"<{tag}>{span.text}</{tag}>"


# Déclare l'extension de méthode de Span "to_html" avec la méthode to_html
____.____(____, ____=____)

# Traite le texte et applique la méthode to_html sur le span
# avec la balise "strong"
doc = nlp("Bonjour monde, ceci est une phrase.")
span = doc[0:2]
print(____)
