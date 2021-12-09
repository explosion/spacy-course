def test():
    assert (
        "span1.similarity(span2)" in __solution__ or "span2.similarity(span1)" in __solution__
    ), "Are you comparing the similarity of the two spans?"
    assert span1.text == "great restaurant", "Did you generate span1 correctly?"
    assert span2.text == "really nice bar", "Did you generate span2 correctly?"
    assert (
        0 <= float(similarity) <= 1
    ), "The value of similarity needs to be a float. Did you calculate it correctly?"
    __msg__.good(
        "Well done! Feel free to experiment with comparing more objects, if "
        "you like. The similarities are not *always* this conclusive. Once "
        "you're getting serious about developing NLP applications that "
        "leverage semantic similarity, you might want to train vectors on "
        "your own data, or tweak the similarity algorithm."
    )
