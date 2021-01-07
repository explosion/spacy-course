def test():
    assert "in doc.ents" in __solution__, "Você está iterando nas entidades?"
    assert iphone_x.text == "iPhone X", "Verifique se iphone_x aponta para o intervalo de tokens correto."

    __msg__.good(
        "Perfeito! É claro que você não precisa fazer tudo isso manualmente. No "
        "próximo exercício, você vai conhecer o comparador baseado em regras da spaCy, "
        "que poderá ajudá-lo a encontrar determinadas palavras e frases em um texto."
    )
