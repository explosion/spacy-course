def test():
    assert (
        'spacy.blank("de")' in __solution__ or "spacy.blank('de')" in __solution__
    ), "Hast du das leere deutsche Modell erstellt?"
    assert (
        len(nlp.pipe_names) == 1 and nlp.pipe_names[0] == "ner"
    ), "Hast du den Entity Recognizer zur Pipeline hinzugefügt?"
    assert (
        len(ner.labels) == 1 and ner.labels[0] == "GADGET"
    ), "Hast du das Label zum Entity Recognizer hinzugefügt?"

    __msg__.good(
        "Prima! Die Pipeline ist jetzt fertig und wir können mit der "
        "Trainingsschleife beginnen."
    )
