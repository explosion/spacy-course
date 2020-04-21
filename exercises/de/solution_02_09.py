import spacy

# Lade das Modell "en_core_web_md"
nlp = spacy.load("en_core_web_md")

# Verarbeite einen Text
doc = nlp("Two bananas in pyjamas")

# Wähle den Vector des Tokens "bananas" aus
bananas_vector = doc[1].vector
print(bananas_vector)
