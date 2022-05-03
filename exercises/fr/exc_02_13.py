import spacy
from spacy.matcher import Matcher

nlp = spacy.load("fr_core_news_sm")
doc = nlp(
    "Twitch Prime, le programme pour les membres d'Amazon destiné aux "
    "fans de jeux vidéos, arrête l'une de ses fonctionnalités les plus "
    "appréciées de cette offre tout-compris : l'absence de publicité. "
    "La nouvelle ne concerne pas les fans d'Amazon Music ni le programme "
    "pour enfants Amazon Kids. Mais cette décision montre à quel point "
    "l'intérêt des offres tout-compris peut rapidement évoluer quand les "
    "services proposés viennent à être modifiés."
)

# Crée les motifs de correspondance
pattern1 = [{"LOWER": "Amazon"}, {"IS_TITLE": True}]
pattern2 = [{"POS": "NOUN"}, {"LOWER": "tout"}, {"TEXT": "-"}, {"LOWER": "compris"}]

# Initialise le Matcher et ajoute les motifs
matcher = Matcher(nlp.vocab)
matcher.add("PATTERN1", [pattern1])
matcher.add("PATTERN2", [pattern2])

# Itère sur les correspondances
for match_id, start, end in matcher(doc):
    # Affiche le nom de la chaine et le texte de la portion en correspondance
    print(doc.vocab.strings[match_id], doc[start:end].text)
