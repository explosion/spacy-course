import spacy
from spacy.matcher import Matcher

nlp = spacy.load("es_core_news_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "descargué Fortnite en mi computadora, pero no puedo abrir el juego. "
    "Ayuda? Cuando estaba descargando Minecraft, conseguí la versión de Windows "
    "donde tiene una carpeta '.zip' y usé el programa por defecto para "
    "descomprimirlo…así que también tengo que descargar Winzip?"
)

# Escribe un patrón que encuentre una forma de "descargar" más un nombre propio
pattern = [{"LEMMA": ____}, {"POS": ____}]

# Añade el patrón al matcher y usa el matcher sobre el documento
matcher.add("DOWNLOAD_THINGS_PATTERN", None, pattern)
matches = matcher(doc)
print("Total de resultados encontrados:", len(matches))

# Itera sobre los resultados e imprime el texto del span
for match_id, start, end in matches:
    print("Resultado encontrado:", doc[start:end].text)
