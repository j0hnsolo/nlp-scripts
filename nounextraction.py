import nltk

File = open("filename.txt") 
lines = File.read() 
sentences = nltk.sent_tokenize(lines) 
nouns = [] #empty to array to hold all nouns

for sentence in sentences:
     for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
         if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
             nouns.append(word)

print(nouns)
nouns1 = " ".join(nouns)

f = open("john.txt","w")
f.write(nouns1)
f.close()
