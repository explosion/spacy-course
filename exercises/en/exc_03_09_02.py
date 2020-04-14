from spacy.lang.en import English
from spacy.tokens import Token

nlp = English()

# Define the getter function that takes a token and returns its reversed text
def get_reversed(token):
    return token.text[::-1]


# Register the Token property extension 'reversed' with the getter get_reversed
____.____(____, ____=____)

# Process the text and print the reversed attribute for each token
doc = nlp("All generalizations are false, including this one.")
for ____ in ____:
    print("reversed:", ____)
