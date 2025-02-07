# This test file only runs internally when you test the course with pytest.
# It can be used to ensure that results the course depend on are accurate, e.g.
# when updating to a new version of spaCy. This especially includes predictions
# that some examples assume or depend on.
import spacy
import pytest

import spacy
from spacy.matcher import Matcher
import pytest


@pytest.fixture
def nlp():
    return spacy.load("es_core_news_sm")


def test_01_08_02_predictions(nlp):
    text = "De acuerdo con la revista global de negocios Fortune, Apple fue la empresa más admirada en el mundo entre 2008 y 2012."
    doc = nlp(text)
    ents = [(ent.text, ent.label_) for ent in doc.ents]
    assert len(ents) == 2
    assert ents[0] == ("Fortune", "ORG")
    assert ents[1] == ("Apple", "ORG")


def test_01_09_predictions(nlp):
    text = "Los Olímpicos de Tokio 2020 son la inspiración para la nueva colección de zapatillas adidas zx."
    doc = nlp(text)
    ents = [(ent.text, ent.label_) for ent in doc.ents]
    assert len(ents) == 2
    assert ents[0] == ('Olímpicos', 'LOC')
    assert ents[1] == ('Tokio', 'LOC')
    assert doc[14].ent_type == 0
    assert doc[15].ent_type == 0


def test_slides_01_03(nlp):
    doc = nlp("Camila prefería comer sushi. Pero ahora está comiendo espaguetis.")
    pattern = [{"LEMMA": "comer", "POS": "VERB"}, {"POS": "NOUN"}]
    matcher = Matcher(nlp.vocab)
    matcher.add("TEST", [pattern])
    matches = [doc[start:end].text for _, start, end in matcher(doc)]
    assert matches == ["comer sushi", "comiendo espaguetis"]


def test_03_16_02_predictions(nlp):
    text = (
        "Chick-fil-A es una cadena de restaurantes de comida rápida "
        "americana con sede en la ciudad de College Park, Georgia, "
        "especializada en sándwiches de pollo."
    )
    doc = nlp(text)
    assert [ent.text for ent in doc.ents] == ["Chick-fil-A", "College Park", "Georgia"]
    
