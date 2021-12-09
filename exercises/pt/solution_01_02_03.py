# Importar a classe da língua espanhola (Spanish) 
from spacy.lang.es import Spanish

# Crie um objeto nlp
nlp = Spanish()

# Processar o texto em espanhol (equivalente ao português: "Como vai?")
doc = nlp("¿Cómo estás?")

# Imprimir o texto do documento
print(doc.text)
