def test():
    assert (
        "span1.similarity(span2)" or "span2.similarity(span1)" in __solution__
    ), "2つのスパンの類似度を比較しましたか？"
    assert span1.text == "素晴らしいレストラン", "span1をきちんと作成しましたか？"
    assert span2.text == "とても素敵なバー", "span2をきちんと作成しましたか？"
    assert 0 <= float(similarity) <= 1, "simirlarityは浮動小数点数である必要があります。きちんと計算しましたか？"
    __msg__.good(
        "Well done！お気軽に別のオブジェクトの比較をしてみてください！"
        "類似度は、いつもこのように決定的にはなりません。"
        "きちんとNLPアプリケーションを作ると、ご自身のデータで単語ベクトルを訓練し直したり、類似度アルゴリズムを弄ってみたりしたくなるでしょう。"
    )
