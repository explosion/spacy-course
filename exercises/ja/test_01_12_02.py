def test():
    assert len(pattern) == 2, "パターンは2つのトークンについて表現している必要があります。（2つの辞書からなります。）"
    assert isinstance(pattern[0], dict) and isinstance(
        pattern[1], dict
    ), "パターンのそれぞれの要素は辞書である必要があります。"
    assert len(pattern[0]) == 1 and len(pattern[1]) == 1, "パターンのそれぞれの要素は１つのキーからなります。"
    assert any(
        pattern[0].get(key) == "download" for key in ["lemma", "LEMMA"]
    ), "最初のトークンの見出し語にマッチングをしましたか？"
    assert any(
        pattern[1].get(key) == "PROPN" for key in ["pos", "POS"]
    ), "2つめのトークンについて、固有名詞の品詞タグを用いてマッチングをしましたか？"

    __msg__.good("Good job!")
