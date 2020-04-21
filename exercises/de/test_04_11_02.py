def test():
    assert (
        len(TRAINING_DATA) == 3
    ), "Irgendetwas scheint mit deinen Daten nicht zu stimmen. Erwartet werden 3 Beispiele."
    assert all(
        len(entry) == 2 and isinstance(entry[1], dict) for entry in TRAINING_DATA
    ), "Die Trainingsdaten haben nicht das richtige Format. Erwartet wird eine Liste von Tuples, bestehend aus Text und einem Dictionary als zweites Element."
    ents = [entry[1].get("entities", []) for entry in TRAINING_DATA]
    assert all(
        len(e) == 2 for e in ents
    ), "Alle Beispiele sollten zwei Entitäten enthalten."
    assert any(
        e == (0, 9, "PER") for e in ents[1]
    ), "Hast du das Label PER korrekt zugeordnet?"
    assert any(
        e == (23, 37, "PER") for e in ents[2]
    ), "Hast du das Label PER korrekt zugeordnet?"

    __msg__.good(
        "Bravo! Nachdem wir sowohl Beispiele der neuen WEBSITE-Entitäten, "
        "als auch vorhandene Entitäten wie PERSON in unsere Daten "
        "mitaufgenommen haben, erzielt das Modell nun deutlich bessere Ergebnisse."
    )
