def test():
    assert (
        "token_text = token.text" in __solution__
    ), "Rufst du den Text des Tokens korrekt auf?"
    assert (
        "token_pos = token.pos_" in __solution__
    ), "Greifst du korrekt auf die Wortart des Tokens zu? Denke daran, das Attribut mit Unterstrich zu verwenden."
    assert (
        "token_dep = token.dep_" in __solution__
    ), "Greifst du korrekt auf die Dependenzrelation des Tokens zu? Denke daran, das Attribut mit Unterstrich zu verwenden."
    __msg__.good("Perfekt!")
