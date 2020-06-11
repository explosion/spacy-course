# Importe la classe de langue "English" et crée l'objet nlp
from spacy.lang.en import English

nlp = English()

# Traite le texte
doc = nlp("I like tree kangaroos and narwhals.")

# La portion du Doc pour "tree kangaroos"
tree_kangaroos = doc[2:4]
print(tree_kangaroos.text)

# La portion du Doc pour "tree kangaroos and narwhals" (sans le ".")
tree_kangaroos_and_narwhals = doc[2:6]
print(tree_kangaroos_and_narwhals.text)
