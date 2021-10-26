import spacy

# Import the Matcher
from spacy.____ import ____

nlp = spacy.load("en_core_web_sm")
doc = nlp("Upcoming iPhone X release date leaked as Apple reveals pre-orders")

# Initialize the Matcher with the shared vocabulary
matcher = ____(____.____)

# Create a pattern matching two tokens: "iPhone" and "X"
pattern = [____]

# Add the pattern to the matcher
____.____("IPHONE_X_PATTERN", ____)

# Use the matcher on the doc
matches = ____
print("Matches:", [doc[start:end].text for match_id, start, end in matches])
