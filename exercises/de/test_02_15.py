def test():
    assert (
        "list(doc.ents) + [span]" in __solution__
    ), "Hast du die span zu den doc.ents hinzugefügt?"
    assert (
        "span_root_head = span.root.head" in __solution__
    ), "Greifst du auf den Kopf-Token des Root-Tokens der Span zu?"
    assert (
        "print(span_root_head.text" in __solution__
    ), "Druckst du den Text des Kopf-Tokens?"
    ents = [ent for ent in doc.ents if ent.label_ == "LOC"]
    assert len(ents) == 9, "Leider die falsche Anzahl an Entitäten – erwartet sind 9."
    __msg__.good(
        "Gut gemacht! Jetzt wo du das Kombinieren von Vorhersagen und "
        "regelbasierter Informationsextraktion geübt hast, bist du bereit für "
        "Kapitel 3. Dort dreht sich alles um spaCys Pipelines für Textverarbeitung."
    )
