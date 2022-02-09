def test():
    assert (
        doc.text == "Eu gosto de gatos e cachorros."
    ), "Verifique se você processou o texto corretamente..."
    assert first_token == doc[0], "Tem certeza que você selecionou o primeiro token?"
    assert "print(first_token.text)" in __solution__, "Você está imprimindo o texto do token?"
    assert 'spacy.blank("pt")' in __solution__, 'Você está usando spacy.blank com o idioma correto?'
    __msg__.good("Muito bem!")
