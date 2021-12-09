# Import spaCy
import spacy

# Create the Spanish nlp object
nlp = spacy.blank("es")

# Process a text (this is Spanish for: "How are you?")
doc = nlp("¿Cómo estás?")

# Print the document text
print(doc.text)
