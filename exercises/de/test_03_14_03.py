def test():
    assert (
        "patterns = list(nlp.pipe(people))" in __solution__
    ), "Verwendest du nlp.pipe in einer Liste?"

    __msg__.good(
        "Gut gemacht! Als nächstes schauen wir uns ein praktisches Beispiel "
        "an, das nlp.pipe verwendet, um Dokumente mit zusätzlichen Metadaten "
        "zu verarbeiten."
    )
