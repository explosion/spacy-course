def test():
    assert len(TRAINING_DATA) == 3, "トレーニングデータの数がおかしいです。正しくは4つです。"
    assert all(
        len(entry) == 2 and isinstance(entry[1], dict) for entry in TRAINING_DATA
    ), "学習データのフォーマットがおかしいです。二番目の要素が辞書となるタプルのリストにしてください。"
    ents = [entry[1].get("entities", []) for entry in TRAINING_DATA]
    assert all(len(e) == 2 for e in ents), "すべてのデータは、それぞれ固有表現を2つ含みます。"
    assert any(e == (0, 9, "PERSON") for e in ents[1]), "PERSONラベルをちゃんと付けましたか？"
    assert any(e == (15, 29, "PERSON") for e in ents[2]), "PERSONラベルをちゃんと付けましたか？"

    __msg__.good(
        "Good job！新しいラベルであるWEBSITEのデータと、すでにあったPERSONのデータを用意したので、モデルの性能はもっとよくなるでしょう。"
    )
