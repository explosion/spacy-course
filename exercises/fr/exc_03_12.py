import json
import spacy
from spacy.language import Language
from spacy.tokens import Span
from spacy.matcher import PhraseMatcher

with open("exercises/fr/countries.json", encoding="utf8") as f:
    COUNTRIES = json.loads(f.read())

with open("exercises/fr/capitals.json", encoding="utf8") as f:
    CAPITALS = json.loads(f.read())

nlp = spacy.blank("fr")
matcher = PhraseMatcher(nlp.vocab)
matcher.add("COUNTRY", list(nlp.pipe(COUNTRIES)))


@Language.component("countries_component")
def countries_component_function(doc):
    # Crée une entité Span avec le label "GPE" pour toutes les correspondances
    matches = matcher(doc)
    doc.ents = [____(____, ____, ____, label=____) for match_id, start, end in matches]
    return doc


# Ajoute le composant au pipeline
____.____(____)
print(nlp.pipe_names)

# Getter qui recherche le texte du span dans le dictionnaire
# des capitales des pays
get_capital = lambda span: CAPITALS.get(span.text)

# Déclare l'extension d'attribut de Span "capital" avec le getter get_capital
____.____(____, ____)

# Traite le texte et affiche le texte de l'entité,
# ses attributs label et capitale
doc = nlp("La Tchéquie pourrait aider la Slovaquie à protéger son espace aérien")
print([(____, ____, ____) for ent in doc.ents])
