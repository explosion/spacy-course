def test():
    assert (
        "from spacy.tokens import Doc" in __solution__
    ), "Você fez a importação da classe Doc corretamente?"
    assert (
        len(spaces) == 5
    ), "Parece que o número de espaços não coincide com o número de palavras..."
    assert all(isinstance(s, bool) for s in spaces), "Os espaços devem ser boleanos."
    assert [int(s) for s in spaces] == [0, 1, 1, 0, 0], "Os espaços estão corretos?"
    assert doc.text == "Go, get started!", "Tem certeza que você criou o Doc corretamente?"
    __msg__.good("Bom!")
