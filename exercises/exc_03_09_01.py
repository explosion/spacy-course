from spacy.lang.en import English
from spacy.tokens import Token

nlp = English()

# Register the Token extension attribute 'is_country' with the default value False
____.____(____, ____=____)

# Process the text and set the is_country attribute to True for the token "Spain"
doc = nlp("I live in Spain.")
____ = True

# Print the token text and the is_country attribute for all tokens
print([(____, ____) for token in doc])
