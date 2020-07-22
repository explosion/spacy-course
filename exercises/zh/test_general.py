# This test file only runs internally when you test the course with pytest.
# It can be used to ensure that results the course depend on are accurate, e.g.
# when updating to a new version of spaCy. This especially includes predictions
# that some examples assume or depend on.
import spacy
import pytest


@pytest.fixture
def nlp():
    return spacy.load("zh_core_web_sm")


def test_01_08_02_predictions(nlp):
    text = "写入历史了：苹果是美国第一家市值超过一万亿美元的上市公司。"
    doc = nlp(text)
    ents = [(ent.text, ent.label_) for ent in doc.ents]
    assert len(ents) == 3
    assert ents[0] == ("美国", "GPE")
    assert ents[1] == ("第一", "ORDINAL")
    assert ents[2] == ("一万亿美元", "MONEY")


def test_01_09_predictions(nlp):
    text = "苹果公布了预购细节，泄露了即将到来的iPhone X的发布日期。"
    doc = nlp(text)
    ents = [(ent.text, ent.label_) for ent in doc.ents]
    assert len(ents) == 0
    assert doc[1].ent_type == 0
    assert doc[2].ent_type == 0
