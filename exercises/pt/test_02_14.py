def test():
    assert (
        "from spacy.matcher import PhraseMatcher" in __solution__
    ), "Você importou corretamente o PhraseMatcher?"
    assert (
        "PhraseMatcher(nlp.vocab)" in __solution__
    ), "Você inicializou corretamente o PhraseMatcher?"
    assert "matcher(doc)" in __solution__, "Você chamou o Comparador passando o doc como parâmetro?"
    assert len(matches) == 2, "Quantidade incorreta de correspondências. Esperado: 2."
    __msg__.good("Bom! Vamos usar este Comparador e adicionar algumas entidades personalizadas.")
