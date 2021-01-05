def test():
    assert len(TRAINING_DATA) == 4, "トレーニングデータの数がおかしいです。正しくは4つです。"
    assert all(
        len(entry) == 2 and isinstance(entry[1], dict) for entry in TRAINING_DATA
    ), "学習データのフォーマットがおかしいです。二番目の要素が辞書となるタプルのリストにしてください。"
    assert all(
        entry[1].get("entities") for entry in TRAINING_DATA
    ), "すべてのデータにentitiesのアノテーションが必要です。"
    assert TRAINING_DATA[0][1]["entities"] == [
        (2, 9, "GPE")
    ], "1番目のデータのentitiesを見直してください。"
    assert TRAINING_DATA[1][1]["entities"] == [
        (6, 8, "GPE")
    ], "2番目のデータのentitiesを見直してください。"

    assert TRAINING_DATA[2][1]["entities"] == [
        (0, 6, "GPE"),
        (8, 10, "GPE"),
    ], "3番目のデータのentitiesを見直してください。"
    assert TRAINING_DATA[3][1]["entities"] == [
        (0, 4, "GPE")
    ], "4番目のデータのentitiesを見直してください。"

    __msg__.good(
        "Great work！モデルがきちんと旅行者のレビューからGPE固有表現を抽出できるようになったら、その地理名称が、文脈的に旅行者の目的地であるかどうかを判断するルールベースコンポーネントをできます。"
        "例えば、抽出された固有表現を知識ベースに照らし合わせたり、トラベルウィキを検索したりすると良いです。"
    )
