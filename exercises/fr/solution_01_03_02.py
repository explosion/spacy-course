# Importe spacy et crée l'objet nlp français
import spacy

nlp = spacy.blank("fr")

# Traite le texte
doc = nlp("La forêt est peuplée de loups gris et renards roux.")

# La portion du Doc pour "loups gris"
loups_gris = doc[5:7]
print(loups_gris.text)

# La portion du Doc pour "loups gris et renards roux" (sans le ".")
loups_gris_et_renards_roux = doc[5:10]
print(loups_gris_et_renards_roux.text)
