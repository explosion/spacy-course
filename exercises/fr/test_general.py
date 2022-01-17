# This test file only runs internally when you test the course with pytest.
# It can be used to ensure that results the course depend on are accurate, e.g.
# when updating to a new version of spaCy. This especially includes predictions
# that some examples assume or depend on.
import spacy
from spacy.matcher import Matcher
import pytest


@pytest.fixture
def nlp():
    return spacy.load("fr_core_news_sm")


def test_01_08_02_predictions(nlp):
    text = "Apple a été créée en 1976 par Steve Wozniak, Steve Jobs et Ron Wayne."
    doc = nlp(text)
    ents = [(ent.text, ent.label_) for ent in doc.ents]
    assert len(ents) == 4
    assert ents[0] == ("Apple", "ORG")
    assert ents[1] == ("Steve Wozniak", "PER")
    assert ents[2] == ("Steve Jobs", "PER")
    assert ents[3] == ("Ron Wayne", "PER")


def test_01_09_predictions(nlp):
    text = "Apple : le nouveau modèle X Pro attendu pour l'été."
    doc = nlp(text)
    ents = [(ent.text, ent.label_) for ent in doc.ents]
    assert len(ents) == 1
    assert ents[0] == ("Apple", "ORG")
    assert doc[5].ent_type == 0
    assert doc[6].ent_type == 0


def test_slides_01_03(nlp):
    doc = nlp(
        "Avant elle photographiait les fleurs. Désormais elle photographiera les oiseaux."
    )
    pattern = [
        {"LEMMA": "photographier", "POS": "VERB"},
        {"POS": "DET"},
        {"POS": "NOUN"},
    ]
    matcher = Matcher(nlp.vocab)
    matcher.add("TEST", [pattern])
    matches = [doc[start:end].text for _, start, end in matcher(doc)]
    assert matches == ["photographiait les fleurs", "photographiera les oiseaux"]


def test_03_16_02_predictions(nlp):
    text = (
        "Le groupe aéronautique Airbus construit des avions et des "
        "hélicoptères vendus dans le monde entier. Le siège opérationnel du "
        "groupe est situé en France à Toulouse dans la région Occitanie."
    )
    doc = nlp(text)
    assert [ent.text for ent in doc.ents] == [
        "Airbus",
        "France",
        "Toulouse",
        "Occitanie",
    ]
