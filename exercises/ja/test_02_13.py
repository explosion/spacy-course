def test():
    assert len(pattern1) == 2, "pattern1の要素の数がただしくありません。"
    assert len(pattern2) == 4, "pattern2の要素の数がただしくありません。"
    # Pattern 1 validation
    assert len(pattern1[0]) == 1, "pattern1の最初のトークンのキーの数がただしくありません。"
    assert any(
        pattern1[0].get(attr) == "amazon" for attr in ("lower", "LOWER")
    ), "pattern1の最初のトークンのキーと値をチェックしてください"
    assert len(pattern1[1]) == 2, "pattern1の2つめのトークンは、2つのキーからなります。"
    assert any(
        pattern1[1].get(attr) == True for attr in ("is_title", "IS_TITLE")
    ), "pattern2の最初のトークンのキーと値をチェックしてください"
    assert any(
        pattern1[1].get(attr) == "NOUN" for attr in ("pos", "POS")
    ), "pattern2の最初のトークンのキーと値をチェックしてください"

    # Pattern 2 validation
    assert any(
        pattern2[0].get(attr) == "ad" for attr in ("lower", "LOWER")
    ), "pattern2の最初のトークンのキーと値をチェックしてください"
    assert any(
        pattern2[2].get(attr) == "free" for attr in ("lower", "LOWER")
    ), "pattern2の3番目のトークンのキーと値をチェックしてください"
    assert any(
        pattern2[3].get(attr) == "NOUN" for attr in ("pos", "POS")
    ), "pattern2の4番目のトークンのキーと値をチェックしてください"
    assert len(matcher(doc)) == 6, "マッチ数がただしくありません。正しくは6です。"

    __msg__.good(
        "Well done！トークン'-'については、'TEXT'か'LOWER'か'SHAPE'を用いてマッチすることができます。"
        "どれを使っても良いです。トークンを注意深く観察することは、トークンベースのMatcherを使うのにとても重要です。"
        "単に文字列にマッチさせるほうがかんたんな場合がありますが、その場合はPhraseMatcherを使いましょう。これは次の演習で見ていきます。"
    )
