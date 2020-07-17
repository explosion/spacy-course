def test():
    assert (
        "list(doc.ents) + [span]" in __solution__
    ), "As-tu ajouté le span à doc.ents ?"
    assert (
        "span_root_head = span.root.head" in __solution__
    ), "Obtiens-tu la tête du token racine du span ?"
    assert (
        "print(span_root_head.text" in __solution__
    ), "Affiches-tu le texte de la tête de la racine du span ?"
    ents = [ent for ent in doc.ents if ent.label_ == "GPE"]
    assert len(ents) == 19, "Nombre incorrect d'entités. Attendu 19."
    __msg__.good(
        "Bien joué ! Maintenant que tu as pratiqué la combinaison de "
        "prédictions avec des extractions basées sur des règles, tu es prêt "
        "pour le chapitre 3, qui va tout t'apprendre sur les pipelines de "
        "traitement de spaCy."
    )
