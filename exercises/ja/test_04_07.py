def test():
    assert "nlp.begin_training()" in __solution__, "nlp.begin_trainingを呼び出しましたか？"
    assert "range(10)" in __solution__, "正しい回数のループを書きましたか？"
    assert (
        "spacy.util.minibatch(TRAINING_DATA" in __solution__
    ), "学習データをバッチ化するためにminibatchヘルパー関数を使いましたか？"
    assert (
        "text for text" in __solution__ and "entities for text" in __solution__
    ), "テキストとアノテーションをちゃんと分けましたか？"
    assert "nlp.update" in __solution__, "モデルを更新しましたか？"

    __msg__.good(
        "Good job！spaCyのモデルを学習させることに成功しました。"
        "シェルに出力された数字は損失量であり、オプティマイザーにとって残った仕事の量を示しています。"
        "低いほどよいです。"
        "実際に学習する際は、**非常に沢山の**データを使うことが普通です。理想的には、少なくとも数百から、数千程度のデータが必要となるでしょう。"
    )
