def test():
    import spacy.matcher

    assert isinstance(matcher, spacy.matcher.Matcher), "matcherをちゃんと初期化しましたか？"
    assert "Matcher(nlp.vocab)" in __solution__, "共有語彙データを用いてmatcherを初期化しましたか？"
    assert len(pattern) == 2, "パターンは2トークンについて表現している必要があります。（2つの辞書からなります）"
    assert isinstance(pattern[0], dict) and isinstance(
        pattern[1], dict
    ), "パターンのそれぞれの要素は辞書である必要があります。"
    assert len(pattern[0]) == 1 and len(pattern[1]) == 1, "パターンのそれぞれの要素は１つのキーからなります。"
    assert any(
        pattern[0].get(key) == "iPhone" for key in ["text", "TEXT"]
    ), "トークンの文字列に対してマッチングを行いましたか？"
    assert any(
        pattern[1].get(key) == "X" for key in ["text", "TEXT"]
    ), "トークンの文字列に対してマッチングを行いましたか？"
    assert 'matcher.add("IPHONE_X_PATTERN"' in __solution__, "パターンをmatcherにきちんと追加しましたか？"
    assert "matches = matcher(doc)" in __solution__, "matcherをdocに対して呼び出しましたか？"

    __msg__.good("よくできました！doc[2:4]からなるパターン「iPhone X」を見つけることに成功しました。")
