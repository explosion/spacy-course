def test():
    assert Span.has_extension("to_html"), "スパンに拡張属性を登録しましたか？"
    ext = Span.get_extension("to_html")
    assert ext[1] is not None, "メソッドをきちんと登録しましたか？"
    assert "method=to_html" in __solution__, "to_htmlをメソッドとして登録しましたか？"
    assert 'span._.to_html("strong")' in __solution__, "カスタム属性にアクセスしましたか？"
    assert (
        span._.to_html("strong") == "<strong>おはようございます</strong>"
    ), "メソッドの返り値が誤っているようです"

    __msg__.good("Perfect！次の演習で、拡張属性とカスタムコンポーネントを組み合わせて使ってみましょう。")
