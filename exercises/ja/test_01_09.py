def test():
    assert "for ent in doc.ents" in __solution__, "Are you iterating over the entities?"
    assert iphone_x.text == "iPhone X", "Are you sure iphone_x covers the right tokens?"

    __msg__.good(
        "Perfect! Of course, you don't always have to do this manually. In "
        "the next exercise, you'll learn about spaCy's rule-based matcher, "
        "which can help you find certain words and phrases in text."
    )
