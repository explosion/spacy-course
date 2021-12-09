def test():
    assert (
        doc.text == "I like tree kangaroos and narwhals."
    ), "Verifique se você processou o texto corretamente..."
    assert first_token == doc[0], "Tem certeza que você selecionou o primeiro token"
    assert "print(first_token.text)" in __solution__, "Você está imprimindo o texto do token?"
    __msg__.good("Muito bem!")
