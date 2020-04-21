from spacy.lang.de import German
from spacy.tokens import Span

nlp = German()

# Definiere die Methode
def to_html(span, tag):
    # Verpacke den Text der Span in einem HTML-Tag und gebe ihn zurück
    return f"<{tag}>{span.text}</{tag}>"


# Registriere die Span-Erweiterung "to_html" mit der Methode to_html
____.____(____, ____=____)

# Verarbeite den Text und rufe die Methode to_html mit dem Tag "strong" auf
doc = nlp("Hallo Welt, dies ist ein Satz.")
span = doc[0:2]
print(____)
