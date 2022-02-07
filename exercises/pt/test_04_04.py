def test():
    assert (
        'spacy.blank("en")' in __solution__
    ), "Você inicializou um fluxo de processamento em Inglês vazio?"
    assert "DocBin(docs=docs)" in __solution__, "Você criou o DocBin corretamente?"
    assert "doc_bin.to_disk(" in __solution__, "Você utilizou o método to_disk?"
    assert "train.spacy" in __solution__, "Você criou um arquivo com o nome correto?"

    __msg__.good("Muito bem! Tudo certo por aqui.")
