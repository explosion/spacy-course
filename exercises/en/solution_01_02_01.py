import os

try:
    import spacy
except ImportError:
    os.system("python3 -m pip install --upgrade pip")
    print("installing spacy...")
    os.system("pip install spacy")
    print("installed spacy.")
    import spacy

try:
    import en_core_web_sm
except ImportError:
    os.system("python -m spacy download en")

# Create the English nlp object
nlp = spacy.blank("en")

# Process a text
doc = nlp("This is a sentence.")

# Print the document text
print(doc.text)
