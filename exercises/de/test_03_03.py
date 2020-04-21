def test():
    assert nlp.meta["name"] == "core_news_sm", "Lädst du das richtige Modell?"
    assert (
        "print(nlp.pipe_names)" in __solution__
    ), "Druckst du die Namen der Komponenten?"
    assert "print(nlp.pipeline)" in __solution__, "Druckst du die komplette Pipeline?"

    __msg__.good(
        "Super! Wenn du dir mal nicht sicher bist, wie deine Pipeline genau "
        "aussieht, kannst du sie inspizieren, indem du nlp.pipe_names oder "
        "nlp.pipeline druckst."
    )
