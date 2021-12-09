import spacy

# Defina o componente customizado
def length_component(doc):
    # Calcule o tamanho do doc
    doc_length = ____
    print(f"This document is {doc_length} tokens long.")
    # Retorne o doc
    ____


# Carregue o modelo pequeno do idioma inglês
nlp = spacy.load("en_core_web_sm")

# Adicione o componente como primeiro do fluxo e imprima o nome dos componentes
____.____(____)
print(nlp.pipe_names)

# Processe um texto
doc = ____
