def test():
    assert "nlp.begin_training()" in __solution__, "Hast du nlp.begin_training aufgerufen?"
    assert (
        "range(10)" in __solution__
    ), "Trainierst du mit der richten Anzahl an Iterationen?"
    assert (
        "spacy.util.minibatch(TRAINING_DATA" in __solution__
    ), "Verwendest du die minibatch Hilfsfunktion, um Batches zu erstellen?"
    assert (
        "text for text" in __solution__ and "entities for text" in __solution__
    ), "Teilst du die Texte und Annotationen korrekt auf?"
    assert "nlp.update" in __solution__, "Aktualisierst du das Modell mit den Beispielen?"

    __msg__.good(
        'Gut gemacht – du hast erfolgreich dein erstes spaCy-Modell trainiert. '
        'Die Zahlen, die du hier siehst werden auch "loss" genannt und bezeichnen '
        'quasi die Arbeit, die der Optimizer noch zu erledigen hat. Je niedriger '
        'die Zahl, desto besser. Im echten Leben würdest du normalerweise *viel '
        'mehr* Daten verwenden als hier, idealerweise ein paar Hundert oder sogar '
        'ein paar Tausend Beispiele.'
    )
