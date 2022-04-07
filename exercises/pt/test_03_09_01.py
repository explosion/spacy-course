def test():
    assert Token.has_extension(
        "is_country"
    ), "Você registrou a extensão no token?"
    ext = Token.get_extension("is_country")
    assert ext[0] == False, "Você definiu o valor padrão corretamente?"
    country_values = [False, False, False, True, False]
    assert [
        t._.is_country for t in doc
    ] == country_values, "Você alterou o valor do token correto?"
    assert (
        "print([(token.text, token._.is_country)" in __solution__
    ), "Você está imprimindo os atributos do token correto?"

    __msg__.good("Muito bom!")
