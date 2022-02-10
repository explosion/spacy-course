import spacy
from spacy.matcher import Matcher

nlp = spacy.load("fr_core_news_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "j'ai téléchargé Fortnite sur mon ordinateur portable et je ne peux pas "
    "du tout lancer le jeu. Quelqu'un pour m'aider ? "
    "donc quand je téléchargeais Minecraft j'ai eu la version de Windows dans "
    "le dossier .zip et j'ai utilisé le programme par défaut pour le "
    "décompresser... est-ce qu'il faut aussi que je télécharge Winzip ?"
)

# Écris un motif qui recherche une forme de "télécharger" suivie d'un nom propre
pattern = [{"LEMMA": "télécharger"}, {"POS": "PROPN"}]

# Ajoute le motif au matcher et applique le matcher au doc
matcher.add("DOWNLOAD_THINGS_PATTERN", [pattern])
matches = matcher(doc)
print("Nombre de correspondances trouvées :", len(matches))

# Itère sur les correspondances et affiche la portion de texte
for match_id, start, end in matches:
    print("Correspondance trouvée :", doc[start:end].text)
