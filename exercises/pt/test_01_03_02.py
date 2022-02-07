def test():
    assert (
        doc.text == "Eu tenho três cachorros e dois gatos."
    ), "Verifique se você processou o texto corretamente..."
    assert (
        tres_cachorros == doc[2:4]
    ), "Tem certeza que você selecionou a partição correta para tres_cachorros?"
    assert (
        tres_cachorros_dois_gatos == doc[2:7]
    ), "Tem certeza que você selecionou a partição correta para tres_cachorros_dois_gatos?"
    assert 'spacy.blank("pt")' in __solution__, 'Você está usando spacy.blank("pt")?'
    __msg__.good("Bom trabalho!")
