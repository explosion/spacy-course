# Importar spaCy e o objeto nlp do Português
import ____
nlp = ____

# Processar o texto
doc = ____("Eu tenho três cachorros e dois gatos.")

# Uma partição do Doc para "três cachorros"
tres_cachorros = ____
print(tres_cachorros.text)

# Uma partição do Doc para "três cachorros e dois gatos" (sem incluir o ".")
tres_cachorros_dois_gatos = ____
print(tres_cachorros_dois_gatos.text)
