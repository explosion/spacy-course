from spacy.lang.de import German

nlp = German()
doc = nlp("Ich habe eine Katze")

# Schlage den Hash für das Wort "Katze" nach
katze_hash = nlp.vocab.strings["Katze"]
print(katze_hash)

# Schlage katze_hash nach, um den String zu erhalten
katze_string = nlp.vocab.strings[katze_hash]
print(katze_string)
