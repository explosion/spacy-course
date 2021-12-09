def test():
    assert nlp.meta["name"] == "core_news_sm", "正しいパイプラインをロードしましたか？"
    assert nlp.meta["lang"] == "ja", "正しいパイプラインをロードしましたか？"
    assert "print(nlp.pipe_names)" in __solution__, "パイプラインの名前をプリントしましたか？"
    assert "print(nlp.pipeline)" in __solution__, "パイプラインをプリントしましたか？"

    __msg__.good(
        "Well done！今あるパイプラインについて調べたくなったときは、nlp.pipe_namesやnlp.pipelineを使ってプリントしましょう。"
    )
