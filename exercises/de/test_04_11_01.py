def test():
    assert (
        len(TRAINING_DATA) == 3
    ), "Irgendetwas scheint mit deinen Daten nicht zu stimmen. Erwartet werden 3 Beispiele."
    assert all(
        len(entry) == 2 and isinstance(entry[1], dict) for entry in TRAINING_DATA
    ), "Die Trainingsdaten haben nicht das richtige Format. Erwartet wird eine Liste von Tuples, bestehend aus Text und einem Dictionary als zweites Element."
    ents = [entry[1].get("entities", []) for entry in TRAINING_DATA]
    assert len(ents[0]) == 2, "Das erste Beispiel sollte zwei Entitäten enhalten."
    ent_0_0 = (0, 6, "WEBSITE")
    ent_0_1 = (11, 18, "WEBSITE")
    assert (
        ents[0][0] == ent_0_0
    ), "Überprüfe nochmal die erste Entität im ersten Beispiel."
    assert (
        ents[0][1] == ent_0_1
    ), "Überprüfe nochmal die zweite Entität im ersten Beispiel."
    assert len(ents[1]) == 1, "Das zweite Beispiel sollte eine Entität enthalten."
    assert ents[1] == [
        (28, 35, "WEBSITE",)
    ], "Überprüfe nochmal die Entität im zweiten Beispiel."
    assert len(ents[2]) == 1, "Das dritte Beispiel sollte eine Entität enthalten."
    assert ents[2] == [
        (15, 21, "WEBSITE",)
    ], "Überprüfe nochmal die Entität im dritten Beispiel."

    __msg__.good("Sehr schön!")
