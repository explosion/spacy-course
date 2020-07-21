# Importe la classe de langue "Français" et crée l'objet nlp
from spacy.lang.fr import French

nlp = French()

# Traite le texte
doc = nlp("La forêt est peuplée de loups gris et renards roux.")

# La portion du Doc pour "loups gris"
loups_gris = doc[5:7]
print(loups_gris.text)

# La portion du Doc pour "loups gris et renards roux" (sans le ".")
loups_gris_et_renards_roux = doc[5:10]
print(loups_gris_et_renards_roux.text)
