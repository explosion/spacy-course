def test():
    assert (
        'with nlp.select_pipes(disable=["parser"])' in __solution__
    ), "正しいコンポーネントに対して、nlp.select_pipesを呼び出しましたか？"

    __msg__.good(
        "Perfect！最適化のためのヒントや工夫について練習しました。" 
        "次章では、spaCyのニューラルネットワークモデルのトレーニングを行います。"
    )
