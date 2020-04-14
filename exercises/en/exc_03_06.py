import spacy

# Define the custom component
def length_component(doc):
    # Get the doc's length
    doc_length = ____
    print("This document is {} tokens long.".format(doc_length))
    # Return the doc
    ____


# Load the small English model
nlp = spacy.load("en_core_web_sm")

# Add the component first in the pipeline and print the pipe names
____.____(____)
print(nlp.pipe_names)

# Process a text
doc = ____
