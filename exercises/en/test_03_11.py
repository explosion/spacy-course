def test():
    assert Span.has_extension(
        "wikipedia_url"
    ), "Did you register the extension on the span?"
    ext = Span.get_extension("wikipedia_url")
    assert ext[2] is not None, "Did you set the getter correctly?"
    assert (
        "getter=get_wikipedia_url" in __solution__
    ), "Did you assign get_wikipedia_url as the getter?"
    assert (
        "(ent.text, ent._.wikipedia_url)" in __solution__
    ), "Are you accessing the custom attribute?"
    assert (
        doc.ents[-1]._.wikipedia_url
        == "https://en.wikipedia.org/w/index.php?search=David_Bowie"
    ), "Looks like the value of the attribute isn't correct."

    __msg__.good(
        "Nice! You now have a pipeline component that uses named entities "
        "predicted by the model to generate Wikipedia URLs  and adds them as "
        "a custom attribute. Try opening the link in your browser to see what "
        "happens!"
    )
