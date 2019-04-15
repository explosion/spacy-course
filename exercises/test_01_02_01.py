import spacy.lang
import spacy.tokens


def test(solution):
    exec(solution)
    # assert English == spacy.lang.en.English
    assert nlp
    assert isinstance(nlp, English)
    assert doc
    assert isinstance(doc, spacy.tokens.Doc)
    assert "print(doc.text)" in solution
