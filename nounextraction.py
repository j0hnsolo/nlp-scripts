import nltk
import csv
import sys
import time

# nouns = [] #empty array to hold all nouns
start = time.time()

f = open("outputfile.txt","w")
csv.field_size_limit(sys.maxsize)

with open("originalfile.csv") as csvfile: 
	lines = csv.reader(csvfile, delimiter=',')
	for row in lines: 
		sentences = nltk.sent_tokenize(row[1]) 
		for sentence in sentences:
			nouns = []
			for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
				if (pos == 'NN'  or pos == 'NNS'):
					nouns.append(word)
			nouns1 = " ".join(nouns)
			f.write(nouns1) 
			f.write(" ")

f.close()
end = time.time()
print(end-start)
