# Importe a biblioteca spaCy
import spacy

# Crie um objeto nlp do Espanhol
nlp = spacy.blank("es")

# Processar o texto em espanhol (equivalente ao português: "Como vai?")
doc = nlp("¿Cómo estás?")

# Imprimir o texto do documento
print(doc.text)
