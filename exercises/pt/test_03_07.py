def test():
    assert (
        'after="ner"' in __solution__
    ), "Você está adicionando o componente explicitamente depois do identificador de entidades?"
    assert (
        nlp.pipe_names[6] == "animal_component"
    ), "Você adicionou o componente depois do indentificador de entidades?"
    assert len(doc.ents) == 2, "Você adicionou as entidades corretamente?"
    assert all(
        ent.label_ == "ANIMAL" for ent in doc.ents
    ), "Você atribuiu o marcador ANIMAL?"

    __msg__.good(
        "Bom trabalho! Você construiu seu primeiro componente do fluxo de processamento para "
        "a identificação de entidades baseada em regras."
    )
