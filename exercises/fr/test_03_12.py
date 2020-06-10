def test():
    assert (
        len(nlp.pipeline) == 1 and nlp.pipe_names[0] == "countries_component"
    ), "Did you add the component correctly?"
    assert Span.has_extension("capital"), "Did you set the extension on the span?"
    ext = Span.get_extension("capital")
    assert ext[2] is not None, "Did you register get_capital as the getter?"
    assert (
        "(ent.text, ent.label_, ent._.capital)" in __solution__
    ), "Are you printing the correct attributes?"
    assert len(doc.ents) == 2, "Looks like the entities didn't get set correctly?"
    assert (
        doc.ents[0]._.capital == "Prague" and doc.ents[1]._.capital == "Bratislava"
    ), "Looks like the capital attribute isn't working correctly."

    __msg__.good(
        "Well done! This is a great example of how you can add structured "
        "data to your spaCy pipeline."
    )
