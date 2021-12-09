def test():
    assert len(doc1.ents) == 2, "doc1に2つの固有表現が含まれています。"
    assert (
        doc1.ents[0].label_ == "WEBSITE" and doc1.ents[0].text == "Reddit"
    ), "doc1の1番目の固有表現を確認してください"
    assert (
        doc1.ents[1].label_ == "WEBSITE" and doc1.ents[1].text == "Patreon"
    ), "doc1の2番目の固有表現を確認してください"
    assert len(doc2.ents) == 1, "doc2に1つの固有表現が含まれています。"
    assert (
        doc2.ents[0].label_ == "WEBSITE" and doc2.ents[0].text == "YouTube"
    ), "doc2の固有表現を確認してください"
    assert len(doc3.ents) == 1, "doc3に1つの固有表現が含まれています。"
    assert (
        doc3.ents[0].label_ == "WEBSITE" and doc3.ents[0].text == "Reddit"
    ), "doc3の固有表現を確認してください"

    __msg__.good("Nice work!")
