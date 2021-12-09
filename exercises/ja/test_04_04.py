def test():
    assert (
        'spacy.blank("ja")' in __solution__
    ), "日本語のパイプラインを作成しましたか？"
    assert (
        "DocBin(docs=docs)" in __solution__
    ), "DocBin を正しく初期化していないようです。"
    assert "doc_bin.to_disk(" in __solution__, "`to_disk` メソッドを呼び出しましたか？"
    assert "train.spacy" in __solution__, "出力のファイル名を確認してください。"

    __msg__.good(
        "Well done! 学習データを作成できましたので、さっそくトレーニングしてみましょう。"
    )
