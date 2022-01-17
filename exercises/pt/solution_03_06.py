import spacy
from spacy.language import Language

# Defina o componente customizado
@Language.component("length_component")
def length_component_function(doc):
    # Calcule o tamanho do doc
    doc_length = len(doc)
    print(f"This document is {doc_length} tokens long.")
    # Retorne o doc
    return doc


# Carregue o fluxo de processamento pequeno do idioma inglês
nlp = spacy.load("en_core_web_sm")

# Adicione o componente como primeiro do fluxo e imprima o nome dos componentes
nlp.add_pipe("length_component", first=True)
print(nlp.pipe_names)

# Processe um texto
doc = nlp("This is a sentence.")
