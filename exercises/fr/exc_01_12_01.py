import spacy
from spacy.matcher import Matcher

nlp = spacy.load("fr_core_news_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "Après avoir effectué la mise à jour d'iOS vous ne constaterez pas de "
    "renouveau radical : rien de commun avec le bouleversement que nous "
    "avions connu avec iOS 7. Globalement iOS 11 reste très semble à iOS 10. "
    "Mais vous découvrirez quelques changements en approfondissant un peu."
)

# Écris un motif des versions complètes d'iOS ("iOS 7", "iOS 11", "iOS 10")
pattern = [{"TEXT": ____}, {"IS_DIGIT": ____}]

# Ajoute le motif au matcher et applique le matcher au doc
matcher.add("IOS_VERSION_PATTERN", [pattern])
matches = matcher(doc)
print("Nombre de correspondances trouvées :", len(matches))

# Itère sur les correspondances et affiche la portion de texte
for match_id, start, end in matches:
    print("Correspondance trouvée :", doc[start:end].text)
