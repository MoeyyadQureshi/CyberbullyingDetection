#Present cases
f = open('PresentData.txt','r')
present_string = f.read().lower().strip().translate(None, '!?":;$%*(\'-_)#/[.,]\{}')
present_string.replace('\n',' ')
present = present_string.split()
f.close()

#Not present cases
f = open('NotPresentData.txt','r')
notPresent_string = f.read().lower().strip().translate(None, '!?":;$%*(\'-_)#/[.,]\{}')
notPresent_string.replace('\n',' ')
notPresent=notPresent_string.split()
f.close()


#Open stats maker
g = open('stats.txt','r+')

whole = present + notPresent
words = list(set(list(whole)))
presWords = list(set(list(present)))

for word in words:
    g.write(word + '\n')
    g.write(str(whole.count(word))+'\n')
    g.write(str(float(present.count(word))/float(whole.count(word)))+'\n')

g.close()
