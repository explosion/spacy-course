def test():
    assert (
        "after='ner'" in __solution__ or 'after="ner"' in __solution__
    ), "Fügst du die Komponente explizit nach dem Entity Recognizer hinzu?"
    assert (
        nlp.pipe_names[-1] == "animal_component"
    ), "Hast du die Komponente nach dem Entity Recognizer hinzugefügt?"
    assert len(doc.ents) == 2, "Aktualisierst du die Entitäten korrekt?"
    assert all(
        ent.label_ == "ANIMAL" for ent in doc.ents
    ), "Hast du das Label ANIMAL hinzugefügt?"

    __msg__.good(
        "Gute Arbeit! Du hast gerade deine erste Pipeline-Komponente für "
        "regelbasiertes Entitäten-Matching entwickelt."
    )
