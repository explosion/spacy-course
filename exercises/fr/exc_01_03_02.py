# Importe spacy et crée l'objet nlp français
import ____

nlp = ____

# Traite le texte
doc = ____("La forêt est peuplée de loups gris et renards roux.")

# La portion du Doc pour "loups gris"
loups_gris = ____
print(loups_gris.text)

# La portion du Doc pour "loups gris et renards roux" (sans le ".")
loups_gris_et_renards_roux = ____
print(loups_gris_et_renards_roux.text)
