def test():
    assert (
        "token_text = token.text" in __solution__
    ), "Você está atribuindo o texto to token corretamente?"
    assert (
        "token_pos = token.pos_" in __solution__
    ), "Você está atribuindo a classe gramatical do token corretamente? Lembre-se de usar o atributo com sublinhado (underscore)."
    assert (
        "token_dep = token.dep_" in __solution__
    ), "Você está atribuindo o termo sintático do token corretamente? Lembre-se de usar o atributo com sublinhado (underscore)."
    __msg__.good("Perfeito!")
