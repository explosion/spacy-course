def test():
    assert len(pattern1) == 2, "pattern1は2つのトークンについて表します"
    assert len(pattern2) == 2, "pattern2は2つのトークンについて表します"
    assert len(pattern1[0]) == 1, "pattern1の最初のトークンの属性の数は1です。"
    assert any(
        pattern1[0].get(l) == "iphone" for l in ("LOWER", "lower")
    ), "pattern1の最初のトークンは、小文字が'iphone'にマッチするようにします"
    assert len(pattern1[1]) == 1, "pattern1の2番目トークンの属性の数は1です。"
    assert any(
        pattern1[1].get(l) == "x" for l in ("LOWER", "lower")
    ), "pattern1の2番目のトークンは、小文字が'x'にマッチするようにします"
    assert len(pattern2[0]) == 1, "pattern2の最初のトークンは、小文字が'iphone'にマッチするようにします"
    assert any(
        pattern2[0].get(l) == "iphone" for l in ("LOWER", "lower")
    ), "pattern1の最初のトークンは、小文字が'iphone'にマッチするようにします"
    assert len(pattern2[1]) == 1, "pattern2の2番目トークンの属性の数は1です。"
    assert any(
        pattern2[1].get(l) == True for l in ("IS_DIGIT", "is_digit")
    ), "pattern2の2番目のトークンは、数字にマッチするようにします"

    __msg__.good("Nice！これらのパターンを使って、モデルの学習データを増強しましょう。")
