import spacy
from spacy.tokens import Span

nlp = spacy.blank("en")

# Definir a função
def to_html(span, tag):
    # Envolva o texto com uma tag HTML e retorne como resultado
    return f"<{tag}>{span.text}</{tag}>"


# Definir o método extendido para a partição (Span) "to_html" com a função to_html
____.____(____, ____=____)

# Processar o texto e chamar o método to_html para a partição span passando o argumento "strong" 
doc = nlp("Olá mundo, essa é uma frase.")
span = doc[0:2]
print(____)
