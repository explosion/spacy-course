def test():
    assert (
        len(TRAINING_DATA) == 4
    ), "Die Anzahl der Trainingsdaten scheint nicht zu passen – erwartet werden 4 Beispiele."
    assert all(
        len(entry) == 2 and isinstance(entry[1], dict) for entry in TRAINING_DATA
    ), "Die Trainingsdaten haben nicht das richtige Format. Erwartet wird eine Liste von Tuples, bestehend aus Text und einem Dictionary als zweites Element."
    assert all(
        entry[1].get("entities") for entry in TRAINING_DATA
    ), "Alle Annotationen in den Trainingsdaten sollten Entitäten enthalten."
    assert TRAINING_DATA[0][1]["entities"] == [
        (24, 33, "LOC")
    ], "Überprüfe nochmal die Entitäten im ersten Beispiel."
    assert TRAINING_DATA[1][1]["entities"] == [
        (28, 33, "LOC")
    ], "Überprüfe nochmal die Entitäten im zweiten Beispiel."
    assert TRAINING_DATA[2][1]["entities"] == [
        (17, 22, "LOC"),
        (26, 34, "LOC"),
    ], "Überprüfe nochmal die Entitäten im dritten Beispiel.."
    assert TRAINING_DATA[3][1]["entities"] == [
        (0, 6, "LOC")
    ], "Überprüfe nochmal die Entitäten im vierten Beispiel."

    __msg__.good(
        "Super Arbeit! Sobald das Modell gute Ergebnisse erzielt und das Label "
        "LOC zuverlässig erkennt, könntest du eine regelbasierte Komponente "
        "hinzufügen, um herauszufinden, ob die Entität in diesem Kontext ein "
        "Touristenziel beschreibt. Hierfür könntest du die Entitäten zum Beispiel "
        "in einer Wissensdatenbank oder in einem Reise-Wiki nachschlagen."
    )
