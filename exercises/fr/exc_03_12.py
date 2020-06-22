import json
from spacy.lang.en import English
from spacy.tokens import Span
from spacy.matcher import PhraseMatcher

with open("exercises/en/countries.json") as f:
    COUNTRIES = json.loads(f.read())

with open("exercises/en/capitals.json") as f:
    CAPITALS = json.loads(f.read())

nlp = English()
matcher = PhraseMatcher(nlp.vocab)
matcher.add("COUNTRY", None, *list(nlp.pipe(COUNTRIES)))


def countries_component(doc):
    # Crée une entité Span avec le libellé "GPE" pour toutes les correspondances
    matches = matcher(doc)
    doc.ents = [____(____, ____, ____, label=____) for match_id, start, end in matches]
    return doc


# Ajoute le composant au pipeline
____.____(____)
print(nlp.pipe_names)

# Getter qui recherche le texte du span dans le dictionnaire des capitales des pays
get_capital = lambda span: CAPITALS.get(span.text)

# Déclare l'extension d'attribut de Span "capital" avec le getter get_capital
____.____(____, ____)

# Traite le texte et affiche le texte de l'entité, ses attributs libellé et capitale
doc = nlp("Czech Republic may help Slovakia protect its airspace")
print([(____, ____, ____) for ent in doc.ents])
