import spacy

# Criar um modelo vazio "en"
nlp = spacy.blank("en")

# Criar um novo identificador de entidades e adicionar ao fluxo de processamento
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)

# Adicionar o rótulo "GADGET" ao identificador de entidades
ner.add_label("GADGET")
