def test():
    assert Span.has_extension("wikipedia_url"), "スパンに拡張属性を登録しましたか？"
    ext = Span.get_extension("wikipedia_url")
    assert ext[2] is not None, "ゲッターを登録しましたか？"
    assert (
        "getter=get_wikipedia_url" in __solution__
    ), "get_wikipedia_urlをゲッターとして登録しましたか？"
    assert "(ent.text, ent._.wikipedia_url)" in __solution__, "カスタム属性にアクセスしましたか？"
    # XXX The index here is brittle with model updates
    assert (
        doc.ents[-1]._.wikipedia_url
        == "https://ja.wikipedia.org/wiki/デヴィッド・ボウイ"
    ), "ゲッター属性の値が誤っているようです"

    __msg__.good(
        "Nice！モデルによって予測された固有表現を使って、Wikipedia URLを生成し、カスタム属性に追加するコンポーネントを作成しました。"
        "リンクを開いたらどうなるか、試して見ましょう！"
    )
