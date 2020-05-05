def test():
    assert "for doc in nlp.pipe(TEXTS)" in __solution__, "nlp.pipeをTEXTSに対して呼び出しましたか？"
    assert "TRAINING_DATA.append" in __solution__, "TRAINING_DATAに追加しましたか？"
    assert len(TRAINING_DATA) == 6, "学習データの数に誤りがあるようです。正しくは6個です。"
    for entry in TRAINING_DATA:
        assert (
            len(entry) == 2
            and isinstance(entry[0], str)
            and isinstance(entry[1], dict)
            and "entities" in entry[1]
        ), "データの形式が誤っているようです。それぞれのデータは、文字列と'entities'をキーとする辞書のタプルからなります。"
    assert TRAINING_DATA[0][1]["entities"] == [
        (20, 28, "GADGET")
    ], "最初のデータのエンティティをもう一度チェックしてください"
    assert TRAINING_DATA[1][1]["entities"] == [
        (0, 8, "GADGET")
    ], "2番目のデータのエンティティをもう一度チェックしてください"
    assert TRAINING_DATA[2][1]["entities"] == [
        (28, 36, "GADGET")
    ], "3番目のデータのエンティティをもう一度チェックしてください"
    assert TRAINING_DATA[3][1]["entities"] == [
        (4, 12, "GADGET")
    ], "4番目のデータのエンティティをもう一度チェックしてください"
    assert TRAINING_DATA[4][1]["entities"] == [
        (0, 9, "GADGET"),
        (13, 21, "GADGET"),
    ], "5番目のデータのエンティティをもう一度チェックしてください"
    assert TRAINING_DATA[5][1]["entities"] == [], "6番目のデータのエンティティをもう一度チェックしてください"

    __msg__.good(
        "Well done！作成したデータを用いて学習する際、matcherの出力に偽陽性がないかどうか"
        "チェックするのに時間がかかるかもしれませんが、依然としてすべて手動でやるよりは遥かに高速です。"
    )
