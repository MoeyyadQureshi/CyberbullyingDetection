#importing PRAW (Python Reddit API Wrapper) to access Reddit's API
import praw
import nltk

f = open('PresentData.txt','r')
g = open('NotPresentData.txt','r')

present = f.read().translate(None, '!?":;$%*(\'_)#/[.,]\{}-')
notPresent = g.read().translate(None, '!?":;$%*(\'_)#/[.,]\-{}')
wholeText = present + ' ' + notPresent
finalDistribution = []

f.close()
g.close()

presentBi = []
wholeBi = []

h = open('Bigrams.txt','r+')

tokens = nltk.word_tokenize(wholeText)
bgs = nltk.bigrams(tokens)
fdist = nltk.FreqDist(bgs)
for k,v in fdist.items():
    wholeBi += [k,v]

tokens = nltk.word_tokenize(present)
bgs = nltk.bigrams(tokens)
fdist = nltk.FreqDist(bgs)
for k,v in fdist.items():
    presentBi += [k,v]
    freq = wholeBi[wholeBi.index(k)+1]
    ratio = float(v)/float(freq)
    h.write(str(k) + '\n' + str(freq) + '\n' + str(ratio)+'\n')
h.close()
