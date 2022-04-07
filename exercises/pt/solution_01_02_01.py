# Importar a biblioteca spaCy
import spacy

# Crie um objeto nlp do Inglês
nlp = spacy.blank("en")

# Processe o texto
doc = nlp("This is a sentence.")

# Imprima o texto do documento
print(doc.text)
