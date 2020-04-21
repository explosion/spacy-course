def test():
    assert (
        "doc1.similarity(doc2)" or "doc2.similarity(doc1)" in __solution__
    ), "Vergleichst du die Ähnlichkeit der zwei Docs?"
    assert (
        0 <= float(similarity) <= 1
    ), "Der Ähnlichkeitswert muss eine Zahl zwischen 0 und 1 sein. Hast du ihn korrekt berechnet?"
    __msg__.good("Gut gemacht!")
