# This test file only runs internally when you test the course with pytest.
# It can be used to ensure that results the course depend on are accurate, e.g.
# when updating to a new version of spaCy. This especially includes predictions
# that some examples assume or depend on.
import spacy
from spacy.matcher import Matcher
import pytest


@pytest.fixture
def nlp():
    return spacy.load("de_core_news_sm")


def test_01_08_02_predictions(nlp):
    text = "Apple wurde 1976 von Steve Wozniak, Steve Jobs und Ron Wayne gegründet."
    doc = nlp(text)
    ents = [(ent.text, ent.label_) for ent in doc.ents]
    assert len(ents) == 4
    assert ents[0] == ("Apple", "ORG")
    assert ents[1] == ("Steve Wozniak", "PER")
    assert ents[2] == ("Steve Jobs", "PER")
    assert ents[3] == ("Ron Wayne", "PER")


def test_01_09_predictions(nlp):
    text = "Apple: Neues Modell iPhone SE kommt im Sommer"
    doc = nlp(text)
    ents = [(ent.text, ent.label_) for ent in doc.ents]
    assert len(ents) == 1
    assert ents[0] == ("Apple", "ORG")
    assert doc[4].ent_type == 0
    assert doc[5].ent_type == 0


def test_slides_01_03(nlp):
    doc = nlp("Ich mochte Hunde, aber ich mag Katzen jetzt lieber.")
    pattern = [{"LEMMA": "mögen", "POS": "VERB"}, {"POS": "NOUN"}]
    matcher = Matcher(nlp.vocab)
    matcher.add("TEST", None, pattern)
    matches = [doc[start:end].text for _, start, end in matcher(doc)]
    assert matches == ["mochte Hunde", "mag Katzen"]


def test_03_16_02_predictions(nlp):
    text = (
        "Die McDonald’s Corporation ist ein Betreiber und Franchisegeber von "
        "weltweit vertretenen Schnellrestaurants."
    )
    doc = nlp(text)
    assert [ent.text for ent in doc.ents] == ["McDonald’s Corporation"]
