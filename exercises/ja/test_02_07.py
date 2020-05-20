def test():
    assert "token_texts" not in __solution__, "token_texts変数を削除していませんか？"
    assert "pos_tags" not in __solution__, "pos_tags変数を削除していませんか？"
    assert "token.pos_ ==" in __solution__, "トークンの品詞タグが固有名詞かどうかをチェックしましたか？"
    assert (
        "token.i + 1" in __solution__ or "token.i+1" in __solution__
    ), "トークンのインデックス属性を使って次のトークンをチェックしましたか？"
    __msg__.good(
        "Great work!この解答は、この例ではうまくいきましたが、改善点があります。"
        "例えば、docが固有名詞で終わる場合、doc[token.i + 1]はエラーとなります。"
        "これを避けるためには、token.i + 1 < len(doc) を満たすかどうかチェックする必要があります。"
    )
