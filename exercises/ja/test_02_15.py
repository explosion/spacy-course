def test():
    assert "list(doc.ents) + [span]" in __solution__, "doc.entsにスパンを追加しましたか？"
    assert "span_root_head = span.root.head" in __solution__, "スパンのルートのヘッドトークンを取得しましたか？"
    assert "print(span_root_head.text" in __solution__, "スパンのルートのヘッドトークンをプリントしましたか？"
    ents = [ent for ent in doc.ents if ent.label_ == "GPE"]
    assert len(ents) == 22, "固有表現の数がただしくありません。正しくは22です。"
    __msg__.good(
        "Well done！モデルの予測とルールベースを組み合わせる方法を学びました。" "第3章では、spaCyの処理パイプラインのすべてを教えます。"
    )
