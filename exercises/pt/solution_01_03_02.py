# Importar spaCy e o objeto nlp do Inglês
import spacy
nlp = spacy.blank("en")

# Processar o texto
doc = nlp("I like tree kangaroos and narwhals.")

# Uma partição do Doc para "tree kangaroos"
tree_kangaroos = doc[2:4]
print(tree_kangaroos.text)

# Uma partição do Doc para "tree kangaroos and narwhals" (sem incluir o ".")
tree_kangaroos_and_narwhals = doc[2:6]
print(tree_kangaroos_and_narwhals.text)
