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
    # Criar uma partição com a etiqueta "GPE" para todas as correspondências 
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

# Processar o texto e imprimir o texto da entidade, etiqueta (label) e a propriedade extendida capital
doc = nlp("Czech Republic may help Slovakia protect its airspace")
print([(____, ____, ____) for ent in doc.ents])
