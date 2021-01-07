def test():
    assert "for ent in doc.ents" in __solution__, "Você está iterando nas entidades?"
    assert (
        "print(ent.text, ent.label_)" in __solution__
    ), "Você está imprimindo o texto (text) e o marcador (label)?"

    __msg__.good(
        "Ótimo trabalho! Até agora o modelo previu corretamente em todos os casos. "
        "No próximo exercício, você verá o que acontece quando o modelo erra, "
        "e como corrigir a sua previsão."
    )
