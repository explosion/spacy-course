# Importe a classe do idioma inglês
from spacy.lang.en import English

# Crie um objeto nlp
nlp = English()

# Processe o texto
doc = nlp("This is a sentence.")

# Imprima o texto do documento
print(doc.text)
