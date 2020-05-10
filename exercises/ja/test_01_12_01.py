def test():
    assert len(pattern) == 2, "パターンは2つのトークンについて表現している必要があります。（2つの辞書からなります。）"
    assert isinstance(pattern[0], dict) and isinstance(
        pattern[1], dict
    ), "パターンのそれぞれの要素は辞書である必要があります。"
    assert len(pattern[0]) == 1 and len(pattern[1]) == 1, "パターンのそれぞれの要素は１つのキーからなります。"
    assert any(
        pattern[0].get(key) == "iOS" for key in ["text", "TEXT"]
    ), "最初のトークンの文字列のマッチングをしましたか？"
    assert any(
        pattern[1].get(key) == True for key in ["is_digit", "IS_DIGIT"]
    ), "2つめのトークンについて、is_digit属性のマッチングをしましたか？"

    __msg__.good("よくできました！")
