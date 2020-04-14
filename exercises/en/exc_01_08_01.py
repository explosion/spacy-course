import spacy

nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# Process the text
doc = ____

for token in doc:
    # Get the token text, part-of-speech tag and dependency label
    token_text = ____.____
    token_pos = ____.____
    token_dep = ____.____
    # This is for formatting only
    print("{:<12}{:<10}{:<10}".format(token_text, token_pos, token_dep))
