def test():
    assert Doc.has_extension(
        "author"
    ), "Did you set up the author extension on the Doc?"
    ext = Doc.get_extension("author")
    assert all(
        v is None for v in ext
    ), "Did you assign the default value to the author extension?"
    assert Doc.has_extension("book"), "Did you set up the book extension on the Doc?"
    ext = Doc.get_extension("book")
    assert all(
        v is None for v in ext
    ), "Did you assign the default value to the book extension?"
    assert (
        "nlp.pipe(DATA, as_tuples=True)" in __solution__
    ), "Did you use nlp.pipe with as_tuples=True?"
    assert (
        'doc._.book = context["book"]' in __solution__
        or "doc._.book = context['book']" in __solution__
    ), "Did you overwrite the doc._.book extension with the context value of 'book'?"
    assert (
        'doc._.author = context["author"]' in __solution__
        or "doc._.author = context['author']" in __solution__
    ), "Did you overwrite the doc._.author extension with the context value of 'author'?"

    __msg__.good(
        "Well done! The same technique is useful for a variety of tasks. For "
        "example, you could pass in page or paragraph numbers to relate the "
        "processed `Doc` back to the position in a larger document. Or you "
        "could pass in other structured data like IDs referring to a "
        "knowledge base."
    )
