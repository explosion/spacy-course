# Import spaCy
import spacy

# Create the German nlp object
nlp = spacy.blank("de")

# Process a text (this is German for: "Kind regards!")
doc = nlp("Liebe Grüße!")

# Print the document text
print(doc.text)
