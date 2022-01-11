import spacy
from spacy.matcher import Matcher

nlp = spacy.load("fr_core_news_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "L'appli se distingue par une interface magnifique, la recherche "
    "intelligente, la labellisation automatique et les réponses "
    "vocales fluides."
)

# Écris un motif pour un adjectif suivi d'un ou deux noms
pattern = [{"POS": ____}, {"POS": ____}, {"POS": ____, "OP": ____}]

# Ajoute le motif au matcher et applique le matcher au doc
matcher.add("ADJ_NOUN_PATTERN", [pattern])
matches = matcher(doc)
print("Nombre de correspondances trouvées :", len(matches))

# Itère sur les correspondances et affiche la portion de texte
for match_id, start, end in matches:
    print("Correspondance trouvée :", doc[start:end].text)
