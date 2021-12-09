def test():
    assert [(ent.text, ent.label_) for ent in doc1.ents] == [
        ("アスムテルダム", "GPE")
    ], "doc1の固有表現は正しくないようです！"
    assert [(ent.text, ent.label_) for ent in doc2.ents] == [
        ("パリ", "GPE")
    ], "doc2の固有表現は正しくないようです！"
    assert [(ent.text, ent.label_) for ent in doc3.ents] == [
        ("アーカンソー", "GPE"),
        ("パリ", "GPE"),
    ], "doc3の固有表現は正しくないようです！"
    assert [(ent.text, ent.label_) for ent in doc4.ents] == [
        ("ベルリン", "GPE")
    ], "doc3の固有表現は正しくないようです！"

    __msg__.good(
        "Great work! 旅行者のレビューの固有表現抽出の精度が十分よくなったら、"
        "観光地かどうかを判定するルールベースコンポネントを追加できます。"
        "例えばGPEの固有表現をナレッジベースに紐付いたり、観光wikiで検索したり"
        "することで、観光地かどうかを区別できます。"
    )
