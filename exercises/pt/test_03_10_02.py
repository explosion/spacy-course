def test():
    assert Span.has_extension("to_html"), "Você registrou a extensão na partição?"
    ext = Span.get_extension("to_html")
    assert ext[1] is not None, "Você definiu o método corretamente?"
    assert "method=to_html" in __solution__, "Você atribuiu to_html como sendo o método?"
    assert (
        'span._.to_html("strong")' in __solution__
    ), "Você está acessando o atributo personalizado?"
    assert (
        span._.to_html("strong") == "<strong>Olá mundo</strong>"
    ), "Parece que o método está retornando o valor errado."

    __msg__.good(
        "Perfeito! No próximo exercício você combinará atributos personalizados "
        "com componentes personalizados do fluxo de processamento (pipeline)."
    )
