def test():
    assert (
        "token1.similarity(token2)" or "token2.similarity(token1)" in __solution__
    ), "Vergleichst du die Ähnlichkeit der zwei Tokens?"
    assert (
        0 <= float(similarity) <= 1
    ), "Der Ähnlichkeitswert muss eine Zahl zwischen 0 und 1 sein. Hast du ihn korrekt berechnet?"
    __msg__.good("Prima!")
