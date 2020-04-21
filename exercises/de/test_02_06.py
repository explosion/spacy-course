def test():
    assert (
        "import Doc, Span" or "import Span, Doc" in __solution__
    ), "Hast du die Klassen Doc und Span korrekt importiert?"
    assert doc.text == "Ich mag David Bowie", "Hast du das Doc richtig erstellt?"
    assert span.text == "David Bowie", "Hast du die Span richtig erstellt?"
    assert span.label_ == "PER", "Hast du das Label PERSON zur Span hinzugefügt?"
    assert "doc.ents =" in __solution__, "Hast du die doc.ents überschrieben?"
    assert len(doc.ents) == 1, "Hast du die Span zu den doc.ents hinzugefügt?"
    assert (
        list(doc.ents)[0].text == "David Bowie"
    ), "Hast du die richtige Span zu den doc.ents hinzugefügt?"
    __msg__.good(
        "Perfekt! Das Erstellen von spaCys Objekten von Hand und das Anpassen "
        "der Entitäten wird sich später als nützlich erweisen, wenn du deine "
        "eigenen Pipelines zum Extrahieren von Informationen erstellst."
    )
