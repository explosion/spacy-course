def test():
    assert [(ent.text, ent.label_) for ent in doc1.ents] == [
        ("amsterdem", "GPE")
    ], "Double-check the entities in the first example."
    assert [(ent.text, ent.label_) for ent in doc2.ents] == [
        ("Paris", "GPE")
    ], "Double-check the entities in the second example."
    assert [(ent.text, ent.label_) for ent in doc3.ents] == [
        ("Paris", "GPE"),
        ("Arkansas", "GPE"),
    ], "Double-check the entities in the third example."
    assert [(ent.text, ent.label_) for ent in doc4.ents] == [
        ("Berlin", "GPE")
    ], "Double-check the entities in the fourth example."

    __msg__.good(
        "Great work! Once the model achieves good results on detecting GPE "
        "entities in the traveler reviews, you could add a rule-based "
        "component to determine whether the entity is a tourist destination in "
        "this context. For example, you could resolve the entities types back "
        "to a knowledge base or look them up in a travel wiki."
    )
