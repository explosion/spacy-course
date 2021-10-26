def test():
    assert (
        doc.text == "I like tree kangaroos and narwhals."
    ), "Are you sure you processed the text correctly?"
    assert first_token == doc[0], "Are you sure you selected the first token?"
    assert "print(first_token.text)" in __solution__, "Are you printing the token text?"
    assert 'spacy.blank("en")' in __solution__, 'Are you using spacy.blank("en")?'
    __msg__.good("Nicely done!")
