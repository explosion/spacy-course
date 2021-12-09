import spacy
from spacy.tokens import Span

nlp = spacy.blank("ja")

doc1 = nlp("クリエーターのコミュニティづくりを支援するため、RedditはPatreonと提携している")
doc1.ents = [
    Span(doc1,  9, 10, label="WEBSITE"),
    Span(doc1, 11, 12, label="WEBSITE"),
]

doc2 = nlp("ピューディパイはYouTubeの記録を打ち破った")
doc2.ents = [Span(doc2, 0, 1, label="PERSON"), Span(doc2, 2, 3, label="WEBSITE")]

doc3 = nlp("Redditの創業者であるアレクシス・オハニアンは、メタリカのチケットを2枚、ファンにプレゼントした")
doc3.ents = [Span(doc3, 0, 1, label="WEBSITE"), Span(doc3, 6, 9, label="PERSON")]

# などなど
