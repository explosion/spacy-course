def test():
    assert "from spacy.tokens import Doc" in __solution__, "Docクラスをちゃんとインポートしましたか？"
    assert len(spaces) == 4, "Docをちゃんと作成しましたか？"
    assert all(isinstance(s, bool) for s in spaces), "spacesはブール値である必要があります。"
    assert [int(s) for s in spaces] == [0, 0, 0, 0], "スペースは正しいですか？"
    assert doc.text == "さあ、始めよう！", "Docを正しく作成していますか？"
    __msg__.good("Nice!")
