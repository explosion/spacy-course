def test():
    assert (
        len(nlp.pipeline) == 1 and nlp.pipe_names[0] == "countries_component"
    ), "コンポーネントを追加しましたか？"
    assert Span.has_extension("capital"), "スパンに拡張属性を登録しましたか？"
    ext = Span.get_extension("capital")
    assert ext[2] is not None, "get_capitalをゲッターとして登録しましたか？"
    assert "(ent.text, ent.label_, ent._.capital)" in __solution__, "正しい属性をプリントしましたか？"
    assert len(doc.ents) == 2, "固有表現が正く登録されていないようです"
    assert (
        doc.ents[0]._.capital == "プラハ" and doc.ents[1]._.capital == "ブラチスラヴァ"
    ), "capital属性がちゃんと働いていないようです"

    __msg__.good("Well done！これは構造化されたデータをspaCyのパイプラインに追加する非常に良い例です。")
