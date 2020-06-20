def test():
    assert "in doc.ents" in __solution__, "Iterierst du über die Entitäten?"
    assert (
        iphone_se.text == "IPhone SE"
    ), "Bist du dir sicher, dass iphone_se die richtigen Tokens erfasst?"

    __msg__.good(
        "Super! Natürlich musst du das hier nicht immer von Hand machen. In der "
        "nächsten Lektion lernst du spaCys regelbasierten Matcher kennen, der "
        "dir dabei helfen kann, bestimmte Wörter und Ausdrücke im Text zu finden."
    )
