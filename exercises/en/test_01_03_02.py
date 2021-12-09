def test():
    assert (
        doc.text == "I like tree kangaroos and narwhals."
    ), "Are you sure you processed the text correctly?"
    assert (
        tree_kangaroos == doc[2:4]
    ), "Are you sure you selected the right span for tree_kangaroos?"
    assert (
        tree_kangaroos_and_narwhals == doc[2:6]
    ), "Are you sure you selected the right span for tree_kangaroos_and_narwhals?"
    assert 'spacy.blank("en")' in __solution__, 'Are you using spacy.blank("en")?'
    __msg__.good("Good job!")
