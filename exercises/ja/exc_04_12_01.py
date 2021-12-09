import spacy
from spacy.tokens import Span

nlp = spacy.blank("ja")

doc1 = nlp("クリエーターのコミュニティづくりを支援するため、RedditはPatreonと提携している")
doc1.ents = [
    Span(doc1, ____, ____, label="WEBSITE"),
    Span(doc1, ____, ____, label="WEBSITE"),
]

doc2 = nlp("ピューディパイはYouTubeの記録を打ち破った")
doc2.ents = [Span(doc2, ____, ____, label="WEBSITE")]

doc3 = nlp("Redditの創業者であるアレクシス・オハニアンは、メタリカのチケットを2枚、ファンにプレゼントした")
doc3.ents = [Span(doc3, ____, ____, label="WEBSITE")]

# などなど
