def test():
    assert "spacy.load" in __solution__, "spacy.loadを呼び出しましたか?"
    assert nlp.meta["lang"] == "ja", "正しいモデルを呼び出しましたか？"
    assert nlp.meta["name"] == "core_news_sm", "正しいモデルを呼び出しましたか？"
    assert "nlp(text)" in __solution__, "テキストをちゃんと処理しましたか？"
    assert "print(doc.text)" in __solution__, "docのテキストをプリントしましたか？"

    __msg__.good("よくできました！パイプラインのロードのやりかたを学んだので、モデルを用いた解析の方法を見ていきましょう。")
