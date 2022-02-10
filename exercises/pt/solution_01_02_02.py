# Importe a biblioteca spaCy
import spacy

# Crie um objeto nlp do Alemão
nlp = spacy.blank("de")

# Processe o texto (equivalente ao português: "Atenciosamente")
doc = nlp("Liebe Grüße!")

# Imprima o texto do documento
print(doc.text)
