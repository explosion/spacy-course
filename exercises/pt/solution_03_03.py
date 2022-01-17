import spacy

# Carregue o fluxo de procesamento en_core_web_sm
nlp = spacy.load("en_core_web_sm")

# Imprima o nome dos componentes do fluxo
print(nlp.pipe_names)

# Imprima as informações das tuplas (name, component)
print(nlp.pipeline)
