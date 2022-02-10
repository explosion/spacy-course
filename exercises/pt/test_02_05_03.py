def test():
    assert (
        "from spacy.tokens import Doc" in __solution__
    ), "Você fez a importação da classe Doc corretamente?"
    assert len(words) == 5, "Parece que há um número errado de palavras."
    assert len(spaces) == 5, "Parece que há um número errado de espaços em branco."
    assert words == ["Oh", ",", "realmente", "?", "!"], "Confira as palavras!"
    assert all(isinstance(s, bool) for s in spaces), "Os espaços em branco devem ser boleanos."
    assert [int(s) for s in spaces] == [0, 1, 0, 0, 0], "Os espaços em branco estão corretos?"
    assert doc.text == "Oh, realmente?!", "Tem certeza que você criou o Doc corretamente?"
    __msg__.good("Bom trabalho! Agora vamos criar algumas entidades.")
