def test():
    assert "token_texts" not in __solution__, "Você removeu a variável token_texts?"
    assert "pos_tags" not in __solution__, "Você removeu a variável pos_tags?"
    assert (
        "token.pos_ ==" in __solution__
    ), "Você está verificando se a classe gramatical do token é um substantivo próprio?"
    assert (
        "token.i + 1" in __solution__ or "1 + token.i" in __solution__
    ), "Você está usando o atributo index do token para verificar o proximo token?"
    __msg__.good(
        "Ótimo trabalho! Enquanto essa solução funciona corretamente para este exemplo, "
        "ainda há espaço para melhorias. Se do doc terminar com um substantivo próprio, "
        "doc[token.i + 1] retornará erro. Para ter certeza que este código está robusto," 
        "você deve primeiro verificar se token.i + 1 < len(doc). "
    )
