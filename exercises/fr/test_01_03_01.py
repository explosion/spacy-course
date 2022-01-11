def test():
    assert (
        doc.text == "La forêt est peuplée de loups gris et renards roux."
    ), "Es-tu certain d'avoir traité correctement le texte ?"
    assert first_token == doc[0], "Es-tu certain d'avoir sélectionné le premier token ?"
    assert "print(first_token.text)" in __solution__, "Affiches-tu le texte du token ?"
    assert 'spacy.blank("fr")' in __solution__, 'Utilises-tu spacy.blank avec la bonne langue ?'
    __msg__.good("Bien joué !")
