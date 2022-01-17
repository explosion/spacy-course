def test():
    assert (
        doc.text == "I like tree kangaroos and narwhals."
    ), "Verifique se você processou o texto corretamente..."
    assert (
        tree_kangaroos == doc[2:4]
    ), "Tem certeza que você selecionou partição correta para tree_kangaroos?"
    assert (
        tree_kangaroos_and_narwhals == doc[2:6]
    ), "Tem certeza que você selecionou partição correta para tree_kangaroos_and_narwhals?"
    assert 'spacy.blank("en")' in __solution__, 'Você está usando spacy.blank("en")?'
    __msg__.good("Bom trabalho!")
