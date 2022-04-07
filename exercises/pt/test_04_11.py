def test():
    assert [(ent.text, ent.label_) for ent in doc1.ents] == [
        ("amsterdem", "GPE")
    ], "Confirme as entidades no primeiro exemplo."
    assert [(ent.text, ent.label_) for ent in doc2.ents] == [
        ("Paris", "GPE")
    ], "Confirme as entidades no segundo exemplo."
    assert [(ent.text, ent.label_) for ent in doc3.ents] == [
        ("Paris", "GPE"),
        ("Arkansas", "GPE"),
    ], "Confirme as entidades no terceiro exemplo."
    assert [(ent.text, ent.label_) for ent in doc4.ents] == [
        ("Berlin", "GPE")
    ], "Confirme as entidades no quarto exemplo."

    __msg__.good(
        "Ótimo trabalho! Uma vez que o modelo obteve um bom resultado ao identificar entidades GPE"
        "nos comentários dos viajantes, você pode agora adicionar um componente"
        "baseado em regras para determinar se a entidade é um destino turístico"
        "neste contexto. Por exemplo, você pode comparar as entidades com uma"
        "base de conhecimento ou consultar uma wiki pública de viagens."
    )

