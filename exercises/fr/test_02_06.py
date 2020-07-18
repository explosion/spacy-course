def test():
    assert (
        "import Doc, Span" or "import Span, Doc" in __solution__
    ), "As-tu correctement importé Doc et Span ?"
    assert doc.text == "I like David Bowie", "As-tu correctement créé le Doc ?"
    assert span.text == "David Bowie", "As-tu correctement créé le span ?"
    assert span.label_ == "PERSON", "As-tu ajouté le label PERSON au span?"
    assert "doc.ents =" in __solution__, "As-tu réécrit doc.ents?"
    assert len(doc.ents) == 1, "As-tu ajouté le span à doc.ents ?"
    assert (
        list(doc.ents)[0].text == "David Bowie"
    ), "As-tu ajouté le span à doc.ents ?"
    __msg__.good(
        "Parfait ! Savoir créer manuellement des objets de spaCy et modifier "
        "les entités sera utile plus tard quand tu créeras tes propres "
        "pipelines d'extraction d'informations."
    )
