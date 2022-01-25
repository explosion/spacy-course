def test():
    assert (
        "from spacy.tokens import Doc" in __solution__
    ), "Você fez a importação da classe Doc corretamente?"
    assert doc.text == "spaCy é bem legal!", "Você tem certeza que criou o Doc corretamente?"
    assert "print(doc.text)" in __solution__, "Você está imprimindo o texto do Doc?"
    __msg__.good("Muito bom!")
