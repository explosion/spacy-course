def test():
    assert (
        "for doc in nlp.pipe(TEXTS)" in __solution__
    ), "Verwendest du nlp.pipe, um die Texte zu verarbeiten?"
    assert (
        "TRAINING_DATA.append" in __solution__
    ), "Verwendest du die Methode append, um das Beispiel zu TRAINING_DATA hinzuzufügen?"
    assert (
        len(TRAINING_DATA) == 6
    ), "Die Trainingsdaten sehen nicht korrekt aus. Erwartet werden 6 Beispiele."
    for entry in TRAINING_DATA:
        assert (
            len(entry) == 2
            and isinstance(entry[0], str)
            and isinstance(entry[1], dict)
            and "entities" in entry[1]
        ), "Es scheint, als haben die Daten das falsche Format. Es sollte Tuples mit einem Text und einem Dictionary mit dem Schlüssel 'entities' sein."
    assert TRAINING_DATA[0][1]["entities"] == [
        (0, 8, "GADGET")
    ], "Schau dir die Entitäten in Beispiel 1 nochmal an."
    assert TRAINING_DATA[1][1]["entities"] == [
        (4, 12, "GADGET")
    ], "Schau dir die Entitäten in Beispiel 2 nochmal an."
    assert TRAINING_DATA[2][1]["entities"] == [
        (29, 37, "GADGET")
    ], "Schau dir die Entitäten in Beispiel 3 nochmal an."
    assert TRAINING_DATA[3][1]["entities"] == [
        (21, 29, "GADGET")
    ], "Schau dir die Entitäten in Beispiel 4 nochmal an."
    assert TRAINING_DATA[4][1]["entities"] == [
        (0, 9, "GADGET"),
        (13, 21, "GADGET"),
    ], "Schau dir die Entitäten in Beispiel 5 nochmal an."
    assert (
        TRAINING_DATA[5][1]["entities"] == []
    ), "Schau dir die Entitäten in Beispiel 6 nochmal an."

    __msg__.good(
        "Gut gemacht! Bevor du ein Modell mit den Daten trainierst, solltest du "
        "immer nochmals überprüfen, dass dein Matcher keine falschpositiven Spans "
        "gefunden hat. Aber dieser Prozess ist immer noch viel schneller, als "
        "*alles* von Hand zu erledigen."
    )
