def test():
    assert Doc.has_extension("has_number"), "Did you register the extension on the doc?"
    ext = Doc.get_extension("has_number")
    assert ext[2] is not None, "Did you set the getter correctly?"
    assert (
        "getter=get_has_number" in __solution__
    ), "Did you assign get_has_number as the getter?"
    assert "doc._.has_number" in __solution__, "Are you accessing the custom attribute?"
    assert doc._.has_number, "Looks like the getter is returning the wrong value."

    __msg__.good("Nice work!")
