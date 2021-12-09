def test():
    assert [(ent.text, ent.label_) for ent in doc1.ents] == [
        ("amsterdem", "LOC")
    ], "Überprüfe nochmal die Enitäten im ersten Beispiel."
    assert [(ent.text, ent.label_) for ent in doc2.ents] == [
        ("Paris", "LOC")
    ], "Überprüfe nochmal die Enitäten im zweiten Beispiel."
    assert [(ent.text, ent.label_) for ent in doc3.ents] == [
        ("Paris", "LOC"),
        ("Arkansas", "LOC"),
    ], "Überprüfe nochmal die Enitäten im dritten Beispiel."
    assert [(ent.text, ent.label_) for ent in doc4.ents] == [
        ("Berlin", "LOC")
    ], "Überprüfe nochmal die Enitäten im vierten Beispiel."

    __msg__.good(
        "Gute Arbeit! Sobald das Modell gute Resultate im Erkennen von "
        "LOC-Entitäten in den Reise-Bewertungen erzielt, könntest du "
        "eine regelbasierte Komponente hinzufügen, um zu entscheiden ob eine "
        "Entität ein Touristenziel beschreibt. Du könntest zum Beispiel die "
        "Enitäten mit einer Wissensdatenbank vergleichen oder du schlägst sie "
        "in einem Reise-Wiki nach."
    )
