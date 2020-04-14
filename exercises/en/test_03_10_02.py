def test():
    assert Span.has_extension("to_html"), "Did you register the extension on the span?"
    ext = Span.get_extension("to_html")
    assert ext[1] is not None, "Did you set the method correctly?"
    assert "method=to_html" in __solution__, "Did you assign to_html as the method?"
    assert (
        'span._.to_html("strong")' in __solution__
        or "span._.to_html('strong')" in __solution__
    ), "Are you accessing the custom attribute?"
    assert (
        span._.to_html("strong") == "<strong>Hello world</strong>"
    ), "Looks like the method is returning the wrong value."

    __msg__.good(
        "Perfect! In the next exercise, you'll get to combine custom "
        "attributes with custom pipeline components."
    )
