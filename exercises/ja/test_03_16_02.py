def test():
    assert (
        'with nlp.disable_pipes("tagger", "parser")' in __solution__
        or 'with nlp.disable_pipes("parser", "tagger")' in __solution__
    ), "正しいコンポーネントに対して、nlp.disable_pipeを呼び出しましたか？"

    __msg__.good(
        "Perfect！最適化のためのヒントや工夫について練習しました。" "次章では、spaCyのニューラルネットワークモデルのトレーニングを行います。"
    )
