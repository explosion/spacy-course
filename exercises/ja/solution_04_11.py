import spacy
from spacy.tokens import Span

nlp = spacy.blank("ja")

doc1 = nlp("去年アスムテルダムに行った。運河がきれいだった。")
doc1.ents = [Span(doc1, 1, 2, label="GPE")]

doc2 = nlp("人生で一度はパリに行くべきだけど、エッフェル塔はちょっとつまらないな。")
doc2.ents = [Span(doc2, 4, 5, label="GPE")]

doc3 = nlp("アーカンソーにもパリはあるｗ")
doc3.ents = [Span(doc3, 0, 1, label="GPE"), Span(doc3, 3, 4, label="GPE")]

doc4 = nlp("ベルリンは夏が最高！公園がたくさんあって、夜遊びが充実していて、ビールが安い！")
doc4.ents = [Span(doc4, 0, 1, label="GPE")]
