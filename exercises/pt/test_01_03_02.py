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
    __msg__.good("Bom tranalho!")
