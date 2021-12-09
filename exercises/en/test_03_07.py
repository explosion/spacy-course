def test():
    assert (
        'after="ner"' in __solution__
    ), "Are you adding the component explicitly after the entity recognizer?"
    assert (
        nlp.pipe_names[6] == "animal_component"
    ), "Did you add the component after the entity recognizer?"
    assert len(doc.ents) == 2, "Are you adding the entities correctly?"
    assert all(
        ent.label_ == "ANIMAL" for ent in doc.ents
    ), "Did you assign the label ANIMAL?"

    __msg__.good(
        "Good job! You've built your first pipeline component for "
        "rule-based entity matching."
    )
