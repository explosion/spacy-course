import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

nlp = spacy.load("de_core_news_sm")
animals = ["Golden Retriever", "Katze", "Schildkröte", "Rattus norvegicus"]
animal_patterns = list(nlp.pipe(animals))
print("animal_patterns:", animal_patterns)
matcher = PhraseMatcher(nlp.vocab)
matcher.add("ANIMAL", None, *animal_patterns)

# Definiere die benutzerdefinierte Komponente
def animal_component(doc):
    # Wende den Matcher auf das Doc an
    matches = matcher(doc)
    # Erstelle eine Span für jedes Resultat und weise das Label "ANIMAL" zu
    spans = [Span(doc, start, end, label="ANIMAL") for match_id, start, end in matches]
    # Überschreibe die doc.ents mit den gefundenen Spans
    doc.ents = spans
    return doc


# Füge die Komponente nach der Komponente "ner" hinzu
nlp.add_pipe(animal_component, after="ner")
print(nlp.pipe_names)

# Verarbeite den Text und drucke Text und Label der doc.ents
doc = nlp("Ich habe eine Katze und einen Golden Retriever")
print([(ent.text, ent.label_) for ent in doc.ents])
