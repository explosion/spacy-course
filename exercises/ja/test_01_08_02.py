def test():
    assert "for ent in doc.ents" in __solution__, "固有表現をイテレートしていますか？"
    assert "print(ent.text, ent.label_)" in __solution__, "文字列とラベルをプリントしましたか？"

    __msg__.good(
        "素晴らしい！ここでは、モデルはすべての例で正しい予測を行いました。" "次の演習では、モデルが予測を誤る例を見ていき、モデルを修正する方法を学びます。"
    )
