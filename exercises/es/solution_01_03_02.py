# Importa la clase de lenguaje "English" y crea el objeto nlp
from spacy.lang.en import English

nlp = English()

# Procesa el texto
doc = nlp("I like tree kangaroos and narwhals.")

# Un slice del Doc para "tree kangaroos"
tree_kangaroos = doc[2:4]
print(tree_kangaroos.text)

# Un slice del Doc para "tree kangaroos and narwhals" (sin el ".")
tree_kangaroos_and_narwhals = doc[2:6]
print(tree_kangaroos_and_narwhals.text)
