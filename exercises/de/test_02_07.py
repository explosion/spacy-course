def test():
    assert (
        "token_texts" not in __solution__
    ), "Hast du die Variable token_texts gelöscht?"
    assert "pos_tags" not in __solution__, "Hast du die Variable pos_tags gelöscht?"
    assert (
        "token.pos_ ==" in __solution__
    ), "Überprüfst du, ob die Wortart des Tokens ein Eigenname (proper noun) ist?"
    assert (
        "token.i + 1" in __solution__
    ), "Benutzt du das Token-Attribut index, um den nächsten Token auszuwählen?"
    __msg__.good(
        "Gute Arbeit! Auch wenn die Lösung für dieses Beispiel problemos funktioniert, "
        "gibt es noch Dinge, die verbessert werden können. Wenn das Doc auf "
        "einen Eigennamen endet, würde doc[token.i + 1] derzeit fehlschlagen. "
        "Damit der Code besser generalisiert werden kann, solltest du zuerst "
        "testen, ob der Index plus 1 kleiner ist, als die Gesamtlänge des Docs: "
        "if token.i + 1 < len(doc)."
    )
