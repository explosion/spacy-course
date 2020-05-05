def test():
    assert len(pattern) == 3, "パターンは3つのトークンについて表現している必要があります。（3つの辞書からなります。）"
    assert (
        isinstance(pattern[0], dict)
        and isinstance(pattern[1], dict)
        and isinstance(pattern[2], dict)
    ), "パターンは2つのトークンについて表現している必要があります。（2つの辞書からなります。）"
    assert len(pattern[0]) == 1 and len(pattern[1]) == 1, "最初の2つのパターンは1つのキーからなります。"
    assert len(pattern[2]) == 2, "3つめのパターンは2つのキーからなります。"
    assert any(
        pattern[0].get(key) == "ADJ" for key in ["pos", "POS"]
    ), "最初のトークンについて、正しい品詞タグでマッチングをしましたか？"
    assert any(
        pattern[1].get(key) == "NOUN" for key in ["pos", "POS"]
    ), "2つめのトークンについて、正しい品詞タグでマッチングをしましたか？"
    assert any(
        pattern[2].get(key) == "NOUN" for key in ["pos", "POS"]
    ), "3つめのトークンについて、正しい品詞タグでマッチングをしましたか？"
    assert pattern[2].get("OP") == "?", "3つめのトークンについて、ただしい演算子を用いていますか？"

    __msg__.good(
        "素晴らしい！この演習では、少し複雑なパターンを出題しました。" "次章に移り、spaCyを使ったより応用的なテキスト解析を見ていきましょう。"
    )
