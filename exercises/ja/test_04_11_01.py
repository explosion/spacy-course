def test():
    assert len(TRAINING_DATA) == 3, "データがどこかおかしいようです。データの数は正しくは3つです。"
    assert all(
        len(entry) == 2 and isinstance(entry[1], dict) for entry in TRAINING_DATA
    ), "学習データのフォーマットがおかしいです。二番目の要素が辞書となるタプルのリストにしてください。"
    ents = [entry[1].get("entities", []) for entry in TRAINING_DATA]
    assert len(ents[0]) == 2, "最初のデータには2つの固有表現が含まれています。"
    assert ents[0][0] == (0, 6, "WEBSITE"), "最初のデータの1番目の固有表現を確認してください。"
    assert ents[0][1] == (21, 28, "WEBSITE"), "最初のデータの2番目の固有表現を確認してください。"
    assert len(ents[1]) == 1, "2番目のデータには1つの固有表現が含まれています。"
    assert ents[1][0] == (18, 25, "WEBSITE"), "2番目のデータの固有表現を確認してください。"
    assert len(ents[2]) == 1, "3番目のデータには1つの固有表現が含まれています。"
    assert ents[2][0] == (0, 6, "WEBSITE"), "2番目のデータの固有表現を確認してください。"

    __msg__.good("Nice work!")
