import spacy
from spacy import displacy

# Load the spaCy model
sp = spacy.load('en_core_web_sm')

# Analyze text
sen = sp("I like to play football. I hated it in my childhood though")
print(sen.text)

# Print part-of-speech (POS) tags and explanations
print(sen[7].pos_)
print(sen[7].tag_)
print(spacy.explain(sen[7].tag_))

for word in sen:
    print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')

# Analyze another sentence
sen = sp("Can you google it?")
word = sen[2]
print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')

# Analyze another sentence
sen = sp("Can you search it on google?")
word = sen[5]
print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')

# Finding the number of POS tags
sen = sp("I like to play football. I hated it in my childhood though")
num_pos = sen.count_by(spacy.attrs.POS)

for k, v in sorted(num_pos.items()):
    print(f'{k}. {sen.vocab[k].text:{8}}: {v}')

# Visualizing parts of speech tags
displacy.serve(sen, style='dep', options={'distance': 120})
