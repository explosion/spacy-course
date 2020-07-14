# Importe a classe do idioma alemão (German)
from spacy.lang.de import German

# Crie um objeto nlp
nlp = German()

# Processe o texto (equivalente ao português: "Atenciosamente")
doc = nlp("Liebe Grüße!")

# Imprima o texto do documento
print(doc.text)
