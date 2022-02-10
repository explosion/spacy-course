import spacy
from spacy.language import Language

# Defina o componente customizado
@Language.component("length_component")
def length_component_function(doc):
    # Calcule o tamanho do doc
    doc_length = ____
    print(f"Este documento tem {doc_length} tokens.")
    # Retorne o doc
    ____


# Carregue o fluxo de processamento pequeno do idioma inglês
nlp = spacy.load("en_core_web_sm")

# Adicione o componente como primeiro do fluxo e imprima o nome dos componentes
____.____(____, ____=____)
print(nlp.pipe_names)

# Processe um texto
doc = ____
