import spacy
from spacy.matcher import Matcher

nlp = spacy.load("es_core_news_sm")
doc = nlp(
    "Cuando pac-man debutó en Tokio, en 1980, nadie podría haber predicho "
    "que se convertiría en el videojuego más exitoso de todos los tiempos. "
    "Hoy, 40 años después, aun sigue sorprendiendo. Su desarrolladora, "
    "Bandai Namco, ha anunciado novedades en el marco del aniversario del "
    "juego. La celebración del 40 aniversario de pac-Man en 2020 incluirá "
    "el debut de una nueva canción temática, compuesta por el famoso artista "
    "japonés de Techno Ken Ishii. Además de estas novedades, Bandai Namco "
    "publicará nuevas versiones del videojuego. La primera será pac-man Live "
    "Studio, en Twitch, en colaboración con Amazon Games."
)

# Crea los patrones
pattern1 = [{"LIKE_NUM": True}, {"POS": "NOUN"}]
pattern2 = [{"LOWER": "pac-man"}, {"IS_TITLE": True}]

# Inicializa el Matcher y añade los patrones
matcher = Matcher(nlp.vocab)
matcher.add("PATTERN1", [pattern1])
matcher.add("PATTERN2", [pattern2])

# Itera sobre los resultados
for match_id, start, end in matcher(doc):
    # Imprime en pantalla el nombre en string del patrón
    # y el texto del span encontrado
    print(doc.vocab.strings[match_id], doc[start:end].text)
