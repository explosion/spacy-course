def test():
    assert 'spacy.blank("ja")' in __solution__, "空の日本語パイプラインを作成しましたか？"
    assert (
        len(nlp.pipe_names) == 1 and nlp.pipe_names[0] == "ner"
    ), "固有表現抽出器をパイプラインに追加しましたか？"
    assert len(ner.labels) == 1 and ner.labels[0] == "GADGET", "固有表現抽出器にラベルを追加しましたか？"

    __msg__.good("Well done！パイプラインの準備が完了たので、学習ループを書いていきましょう。")
