def test():
    assert "from spacy.tokens import Doc" in __solution__, "Docクラスをちゃんとインポートしましたか？"
    assert len(words) == 5, "wordsの数が誤っているようです"
    assert len(spaces) == 5, "spacesの数が誤っているようです"
    assert words == ["本当", "です", "か", "？", "！"], "もう一度wordsをチェックしてみてください！"
    assert all(isinstance(s, bool) for s in spaces), "spacesはブール値である必要があります"
    assert [int(s) for s in spaces] == [0, 0, 0, 0, 0], "spacesは正しいですか？"
    assert doc.text == "本当ですか？！", "Docをきちんと作成しましたか？"
    __msg__.good("Nice work! つぎは、固有表現を作ってみましょう。")
