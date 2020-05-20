def test():
    assert 'after="ner"' in __solution__, "明示的に固有表現抽出器のあとにコンポーネントを追加しましたか？"
    assert nlp.pipe_names[-1] == "animal_component", "固有表現抽出器のあとにコンポーネントを追加しましたか？"
    assert len(doc.ents) == 2, "きちんと固有表現を追加しましたか？"
    assert all(ent.label_ == "ANIMAL" for ent in doc.ents), "ANIMALのラベルを追加しましたか？"

    __msg__.good("Good job！はじめてのカスタムパイプラインコンポーネントとしてルールベースの固有表現抽出器を作ることができましたね。")
