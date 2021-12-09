def test():
    import spacy.matcher

    assert isinstance(
        matcher, spacy.matcher.Matcher
    ), "Você está inicializando o Comparador corretamente?"
    assert (
        "Matcher(nlp.vocab)" in __solution__
    ), "Você está inicializando o Comparador corretamente com o vocabulário compartilhado?"
    assert (
        len(pattern) == 2
    ), "A expressão deve descrever dois tokens (dois dicionários)."
    assert isinstance(pattern[0], dict) and isinstance(
        pattern[1], dict
    ), "Cada item da expressão deve conter um dicionário."
    assert (
        len(pattern[0]) == 1 and len(pattern[1]) == 1
    ), "Cada item na expressão deve conter apenas uma chave."
    assert any(
        pattern[0].get(key) == "iPhone" for key in ["text", "TEXT"]
    ), "Você está fazendo a comparação com o texto do token?"
    assert any(
        pattern[1].get(key) == "X" for key in ["text", "TEXT"]
    ), "Você está fazendo a comparação com o texto do token?"
    assert (
        'matcher.add("IPHONE_X_PATTERN"' in __solution__
    ), "Você está adicionando a expressão corretamente?"
    assert (
        "matches = matcher(doc)" in __solution__
    ), "Você está chamando o Comparador passando o doc como parâmetro?"

    __msg__.good(
        "Parabéns! Você identificou uma correspondência com sucesso: dois tokens "
        "em doc[1:3] que correspondem a partição 'iPhone X'. "
    )
