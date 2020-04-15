from spacy.lang.en import English
from spacy.tokens import Span

nlp = English()

# Define the method
def to_html(span, tag):
    # Wrap the span text in a HTML tag and return it
    return "<{tag}>{text}</{tag}>".format(tag=tag, text=span.text)


# Register the Span property extension 'to_html' with the method to_html
____.____(____, ____=____)

# Process the text and call the to_html method on the span with the tag name 'strong'
doc = nlp("Hello world, this is a sentence.")
span = doc[0:2]
print(____)
