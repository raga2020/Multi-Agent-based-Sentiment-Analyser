import nltk
from nltk.corpus import stopwords

f = open("sample.txt","r")
text = f.readline()
smpl =[]
while text:
    print "\n"+text
    smpl = (nltk.word_tokenize(text))
    print "\ntokens are:\n%s"%(smpl)
    text = f.readline()

    smpl = [w.lower() for w in smpl]
    print "\nafter lowercasing:\n%s"%(smpl)

    smpl = [w for w in smpl if w.isalpha()]
    print "\nafter punct removal:\n%s"%(smpl)

    stopwords = nltk.corpus.stopwords.words('english')
    smpl = [w for w in smpl if w not in stopwords]
    print "\nafter stopwords removal:\n%s"%(smpl)

    porter = nltk.PorterStemmer()
    smpl = [porter.stem(t) for t in smpl]
    print "\nafter stemming:\n%s"%(smpl)

f.close()