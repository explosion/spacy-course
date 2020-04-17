# This test file only runs internally when you test the course with pytest.
# It can be used to ensure that results the course depend on are accurate, e.g.
# when updating to a new version of spaCy. This especially includes predictions
# that some examples assume or depend on.
import spacy
import pytest


@pytest.fixture
def nlp():
    return spacy.load("en_core_web_sm")


def test_01_08_02_predictions(nlp):
    text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"
    doc = nlp(text)
    ents = [(ent.text, ent.label_) for ent in doc.ents]
    assert len(ents) == 4
    assert ents[0] == ("Apple", "ORG")
    assert ents[1] == ("first", "ORDINAL")
    assert ents[2] == ("U.S.", "GPE")
    assert ents[3] == ("$1 trillion", "MONEY")


def test_01_09_predictions(nlp):
    text = "Upcoming iPhone X release date leaked as Apple reveals pre-orders"
    doc = nlp(text)
    ents = [(ent.text, ent.label_) for ent in doc.ents]
    assert len(ents) == 1
    assert ents[0] == ("Apple", "ORG")
    assert doc[1].ent_type == 0
    assert doc[2].ent_type == 0
