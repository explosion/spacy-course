def test():
    assert (
        'with nlp.disable_pipes("tagger", "parser")' in __solution__
        or 'with nlp.disable_pipes("parser", "tagger")' in __solution__
    ), "Você está usando nlp.disable_pipes com os componentes corretos?"

    __msg__.good(
        "Perfeito! Agora que você já praticou as dicas e truques para melhorar "
        "a performance dos seus projetos, estamos prontos para o próximo capítulo "
        "onde vamos treinar modelos de redes neurais da biblioteca spaCy."
    )
