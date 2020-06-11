import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "Features of the app include a beautiful design, smart search, automatic "
    "labels and optional voice responses."
)

# Écris un motif pour un adjectif suivi d'un ou deux noms
pattern = [{"POS": "ADJ"}, {"POS": "NOUN"}, {"POS": "NOUN", "OP": "?"}]

# Ajoute le motif au matcher et applique le matcher au doc
matcher.add("ADJ_NOUN_PATTERN", None, pattern)
matches = matcher(doc)
print("Nombre de correspondances trouvées :", len(matches))

# Itère sur les correspondances et affiche la portion de texte
for match_id, start, end in matches:
    print("Correspondance trouvée :", doc[start:end].text)
