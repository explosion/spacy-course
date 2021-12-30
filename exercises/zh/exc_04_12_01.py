import spacy
from spacy.tokens import Span

nlp = spacy.blank("zh")

doc1 = nlp("哔哩哔哩与阿里巴巴合作为博主们建立社群")
doc1.ents = [
    Span(doc1, ____, ____, label="WEBSITE"),
    Span(doc1, ____, ____, label="WEBSITE"),
]

doc2 = nlp("李子柒打破了Youtube的记录")
doc2.ents = [Span(doc2, ____, ____, label="WEBSITE")]

doc3 = nlp("阿里巴巴的创始人马云提供了一千万购物优惠券")
doc3.ents = [Span(doc3, ____, ____, label="WEBSITE")]

# And so on...
