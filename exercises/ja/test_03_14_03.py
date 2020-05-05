def test():
    assert (
        "patterns = list(nlp.pipe(people))" in __solution__
    ), "nlp.pipeの結果に対してリストを呼び出しましたか？"

    __msg__.good("Good job！追加のメタデータとともにnlp.pipeを呼びだす実践的な例を見ていきましょう。")
