def test():
    assert (
        "from spacy.tokens import Doc" in __solution__
    ), "Você fez a importação da classe Doc corretamente?"
    assert (
        len(spaces) == 6
    ), "Parece que o número de espaços não coincide com o número de palavras..."
    assert all(isinstance(s, bool) for s in spaces), "Os espaços devem ser boleanos."
    assert [int(s) for s in spaces] == [1, 0, 1, 1, 0, 0], "Os espaços estão corretos?"
    assert doc.text == "Vamos lá, vamos começar!", "Tem certeza que você criou o Doc corretamente?"
    __msg__.good("Bom!")
