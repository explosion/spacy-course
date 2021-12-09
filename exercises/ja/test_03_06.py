def test():
    assert "len(doc)" in __solution__, "docの長さを取得しましたか？"
    assert "return doc" in __solution__, "docを返しましたか？"
    assert "nlp.add_pipe" in __solution__, "コンポーネントを返しましたか？"
    assert "first=True" in __solution__, "パイプラインの最初にコンポーネントを追加しましたか？"
    assert nlp.pipe_names[0] == "length_component", "パイプラインの名前が正しくないようです！"

    __msg__.good("Perfect！もう少し複雑なコンポーネントを見ていきましょう！")
