import spacy

nlp = spacy.blank("pt")

# Importe as classes Doc e Span 
from spacy.tokens import Doc, Span

words = ["Eu", "adoro", "David", "Bowie"]
spaces = [True, True, True, False]

# Crie um doc Doc a partir das palavras words e espaçamento spaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)

# Crie uma partição para "David Bowie" a partir do doc e atribua o marcador "PERSON"
span = Span(doc, 2, 4, label="PERSON")
print(span.text, span.label_)

# Adicione a partição às entidades do doc.
doc.ents = [span]

# Imprima o texto e os marcadores das entidades
print([(ent.text, ent.label_) for ent in doc.ents])