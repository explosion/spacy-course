def test():
    assert (
        "span1.similarity(span2)" or "span1.similarity(span2)" in __solution__
    ), "Vergleichst du die Ähnlichkeit der beiden Spans?"
    assert span1.text == "great restaurant", "Hast du span1 korrekt erstellt?"
    assert span2.text == "really nice bar", "Hast du span2 korrekt erstellt?"
    assert (
        0 <= float(similarity) <= 1
    ), "Der Ähnlichkeitswert muss eine Zahl zwischen 0 und 1 sein. Hast du ihn korrekt berechnet?"
    __msg__.good(
        "Sehr schön! Du kannst gerne noch mehr Objekte vergleichen, wenn du "
        "magst. Ähnlichkeiten sind allerdings nicht immer so eindeutig. Sobald "
        "du es ernst meinst und eine NLP-Anwendung entwickelst, die semantische "
        "Ähnlichkeit einsetzt, solltes du überlegen, ob du nicht deine eigenen "
        "Vektoren anhand deiner eigenen Daten trainieren oder den Ähnlichkeits-"
        "Algorithmus entsprechend anpassen willst."
    )
