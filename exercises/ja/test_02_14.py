def test():
    assert (
        "from spacy.matcher import PhraseMatcher" in __solution__
    ), "PhraseMatcherをちゃんとインポートしましたか？"
    assert "PhraseMatcher(nlp.vocab)" in __solution__, "PhraseMatcherをきちんと初期化しましたか？"
    assert "matcher(doc)" in __solution__, "docに対してMatcherを呼び出しましたか？"
    assert len(matches) == 2, "matchesの数がただしくありません。正しくは2です。"
    __msg__.good("Well done！このmatcherを使って、カスタムの固有表現を追加してみましょう。")
