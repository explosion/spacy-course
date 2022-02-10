import json
import spacy
from spacy.language import Language
from spacy.tokens import Span
from spacy.matcher import PhraseMatcher

with open("exercises/pt/countries.json", encoding="utf8") as f:
    COUNTRIES = json.loads(f.read())

with open("exercises/pt/capitals.json", encoding="utf8") as f:
    CAPITALS = json.loads(f.read())

nlp = spacy.blank("pt")
matcher = PhraseMatcher(nlp.vocab)
matcher.add("COUNTRY", list(nlp.pipe(COUNTRIES)))


@Language.component("countries_component")
def countries_component_function(doc):
    # Criar uma partição com o rótulo "GPE" para todas as correspondências
    matches = matcher(doc)
    doc.ents = [____(____, ____, ____, label=____) for match_id, start, end in matches]
    return doc


# Adicionar o componente ao fluxo de processamento (pipeline)
____.____(____)
print(nlp.pipe_names)

# Criar uma função getter que compara o texto com um dicionário com países e suas capitais
get_capital = lambda span: CAPITALS.get(span.text)

# Definir a propriedade extendida "capital" com o atributo getter get_capital
____.____(____, ____)

# Processar o texto e imprimir o texto da entidade, rótulo (label) e a propriedade extendida capital
doc = nlp("A República Tcheca pode ajudar a Eslováquia a proteger seu espaço aéreo.")
print([(____, ____, ____) for ent in doc.ents])
