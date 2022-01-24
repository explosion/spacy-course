# Importar spaCy e o objeto nlp do Português
import spacy
nlp = spacy.blank("pt")

# Processar o texto
doc = nlp("Eu tenho três cachorros e dois gatos.")

# Uma partição do Doc para "três cachorros"
tres_cachorros = doc[2:4]
print(tres_cachorros.text)

# Uma partição do Doc para "três cachorros e dois gatos" (sem incluir o ".")
tres_cachorros_dois_gatos = doc[2:7]
print(tres_cachorros_dois_gatos.text)
