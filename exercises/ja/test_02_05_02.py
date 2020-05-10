def test():
    assert "from spacy.tokens import Doc" in __solution__, "Docクラスをちゃんとインポートしましたか？"
    assert len(spaces) == 5, "Docをちゃんと作成しましたか？"
    assert all(isinstance(s, bool) for s in spaces), "spacesはブール値である必要があります。"
    assert [int(s) for s in spaces] == [0, 1, 1, 0, 0], "スペースは正しいですか？"
    assert doc.text == "Go, get started!", "Docを正しく作成していますか？"
    __msg__.good("Nice!")
