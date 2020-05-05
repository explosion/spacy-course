def test():
    assert 'spacy.load("en_core_web_md")' in __solution__, "中サイズのモデルをロードしましたか？"
    assert "doc[1].vector" in __solution__, "正しいベクトルを取得しましたか？"
    __msg__.good("Well done！次章では、単語ベクトルを用いたdoc、スパン、トークン間の類似度の予測を行います。")
