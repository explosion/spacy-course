def test():
    assert Doc.has_extension("author"), "Docにauthor属性を登録しましたか？"
    ext = Doc.get_extension("author")
    assert all(v is None for v in ext), "author属性にデフォルト値を設定しましたか？"
    assert Doc.has_extension("book"), "Docにbook属性を登録しましたか？"
    ext = Doc.get_extension("book")
    assert all(v is None for v in ext), "book属性にデフォルト値を設定しましたか？"
    assert (
        "nlp.pipe(DATA, as_tuples=True)" in __solution__
    ), "nlp.pipeを呼び出すときに、as_tuple=Trueとしましたか？"
    assert (
        'doc._.book = context["book"]' in __solution__
    ), "doc._.book属性を、コンテキスト中の'book'を用いて更新しましたか？"
    assert (
        'doc._.author = context["author"]' in __solution__
    ), "doc._.author属性を、コンテキスト中の'author'を用いて更新しましたか？"

    __msg__.good(
        "Well done！このテクニックは、様々なタスクで役に立ちます！"
        "たとえば、大量の文章に対して、ページ番号や段落番号をコンテキストに渡し、処理されたdocの位置を復元することができます。"
        "他にも、知識ベースのIDなど、構造化されたデータを渡すこともできます。"
    )
