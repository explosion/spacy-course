import spacy
from spacy.language import Language

# Define the custom component
@Language.component("length_component")
def length_component_function(doc):
    # Get the doc's length
    doc_length = ____
    print(f"This document is {doc_length} tokens long.")
    # Return the doc
    ____


# Load the small English pipeline
nlp = spacy.load("en_core_web_sm")

# Add the component first in the pipeline and print the pipe names
____.____(____, ____=____)
print(nlp.pipe_names)

# Process a text
doc = ____
