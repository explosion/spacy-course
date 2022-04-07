import spacy
from spacy.language import Language

# Defina o componente customizado
@Language.component("length_component")
def length_component_function(doc):
    # Calcule o tamanho do doc
    doc_length = len(doc)
    print(f"Este documento tem {doc_length} tokens.")
    # Retorne o doc
    return doc


# Carregue o fluxo de processamento pequeno do idioma inglês
nlp = spacy.load("pt_core_news_sm")

# Adicione o componente como primeiro do fluxo e imprima o nome dos componentes
nlp.add_pipe("length_component", first=True)
print(nlp.pipe_names)

# Processe um texto
doc = nlp("Esta é uma frase.")
