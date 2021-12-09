def test():
    assert (
        len(doc1.ents) == 2 and len(doc2.ents) == 2 and len(doc3.ents) == 2
    ), "各docに2つの固有表現が含まれています。"
    assert any(
        e.label_ == "PERSON" and e.text == "ピューディパイ" for e in doc2.ents
    ), "doc2のPERSONのスパンを確認してください"
    assert any(
        e.label_ == "PERSON" and e.text == "アレクシス・オハニアン" for e in doc3.ents
    ), "doc3のPERSONのスパンを確認してください"

    __msg__.good(
        "Good job！新しいラベルであるWEBSITEのデータと、すでにあったPERSONのデータを用意したので、モデルの性能はもっとよくなるでしょう。"
    )
