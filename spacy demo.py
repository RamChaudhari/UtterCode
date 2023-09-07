import spacy

nlp = spacy.load('en_core_web_sm')

text = ("I am Manish. I am 19 years old. I love India. My brother's name is Ankush")
doc = nlp(text)

name = [token.lemma_ for token in doc if token.pos_ == "PROPN"]

print(type(name[0]))