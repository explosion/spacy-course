def test():
    assert "for ent in doc.ents" in __solution__, "Iterierst du über die Entitäten?"
    assert (
        "print(ent.text, ent.label_)" in __solution__
    ), "Druckst du den Text und das Label?"

    __msg__.good(
        "Gute Arbeit! Bisher lag das Modell jedes Mal richtig. In der nächsten "
        "Übung siehst du, das passiert, wenn das Modell einmal daneben liegt, "
        "und wie du es anpassen kannst."
    )
