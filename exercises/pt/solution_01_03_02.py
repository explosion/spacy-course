# Importar a classe da língua inglesa (English) e criar um objeto nlp
from spacy.lang.en import English

nlp = English()

# Processar o texto
doc = nlp("I like tree kangaroos and narwhals.")

# Uma partição do Doc para "tree kangaroos"
tree_kangaroos = doc[2:4]
print(tree_kangaroos.text)

# Uma partição do Doc para "tree kangaroos and narwhals" (sem incluir o ".")
tree_kangaroos_and_narwhals = doc[2:6]
print(tree_kangaroos_and_narwhals.text)
