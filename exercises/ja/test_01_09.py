def test():
    assert "in doc.ents" in __solution__, "固有表現をイテレートしましたか？"
    assert mihonomatsubara.text == "三保の松原", "mihonomatsubara変数は正しいスライスですか？"

    __msg__.good(
        "完璧です！もちろん、いつもこのように手動でやる必要はありません。"
        "次の演習では、単語やフレーズを探すためのルールベースのmatcherについて学んでいきます。"
    )
