import spacy
from spacy.language import Language

# Definiere die benutzerdefinierte Komponente
@Language.component("length_component")
def length_component_function(doc):
    # Berechne die Länge des Dokuments
    doc_length = ____
    print(f"Dieses Dokument ist {doc_length} Tokens lang.")
    # Gib das Doc zurück
    ____


# Lade die kleine deutsche Pipeline
nlp = spacy.load("de_core_news_sm")

# Füge die Komponente am Anfang der Pipeline hinzu und drucke die Namen der Komponenten
____.____(____, ____=____)
print(nlp.pipe_names)

# Verarbeite einen Text
doc = ____
