import spacy

nlp = spacy.load("en_core_web_sm")

text = "New iPhone X release date leaked as Apple reveals pre-orders by mistake"

# Process the text
doc = ____

# Iterate over the entities
for ____ in ____.____:
    # Print the entity text and label
    print(____.____, ____.____)

# Get the span for "iPhone X"
iphone_x = ____

# Print the span text
print("Missing entity:", iphone_x.text)
