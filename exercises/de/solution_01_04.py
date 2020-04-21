from spacy.lang.de import German

nlp = German()

# Verarbeite den Text
doc = nlp(
    "Im Jahr 1990 lebten über 60% der Menschen in Ostasien in äußerster Armut. "
    "Heute sind es nur noch 4%."
)

# Iteriere über die Tokens im Doc
for token in doc:
    # Teste ob der Token einer Zahl ähnelt
    if token.like_num:
        # Wähle den nächsten Token im Doc aus
        next_token = doc[token.i + 1]
        # Überprüfe ob der Text des nächsten Tokens "%"" ist
        if next_token.text == "%":
            print("Prozentzahl gefunden:", token.text)
