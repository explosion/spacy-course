import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("David Bowie is a PERSON")

# Look up the hash for the string label "PERSON"
person_hash = ____.____.____[____]
print(person_hash)

# Look up the person_hash to get the string
person_string = ____.____.____[____]
print(person_string)
