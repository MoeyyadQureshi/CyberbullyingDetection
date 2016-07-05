#Present cases
f = open('PresentData.txt','r')
present_string = f.read().lower().strip().translate(None, '!?":;$%*(\'_)#/[.,]\{}')
present_string.replace('\n',' ')
present = present_string.split()
f.close()

#Not present cases
f = open('NotPresentData.txt','r')
notPresent_string = f.read().lower().strip().translate(None, '!?":;$%*(\'_)#/[.,]\{}')
notPresent_string.replace('\n',' ')
notPresent=notPresent_string.split()
f.close()

#Present cases
f1 = open('PresentData.txt','r')
present_string1 = f1.read().lower().strip().translate(None, '!?":;$%*(\'_)#/[.,]\{}')
present_string1.replace('\n',' ')
present1 = present_string1.split('-----')
f1.close()

#Not present cases
f1 = open('NotPresentData.txt','r')
notPresent_string1 = f1.read().lower().strip().translate(None, '!?":;$%*(\'_)#/[.,]\{}')
notPresent_string1.replace('\n',' ')
notPresent1=notPresent_string1.split('-----')
f1.close()


#Open stats maker
g = open('stats.txt','r+')

whole = present + notPresent
whole1 = present1 + notPresent1

words = list(set(list(whole)))
presWords = list(set(list(present)))

for word in words:
    g.write(word + ' ')
    g.write(str(whole.count(word))+' ')
    g.write(str(float(present.count(word))/float(whole.count(word)))+'\n')

present_pair = []
for i in range(len(presWords)-1):
    for j in range(i+1, len(presWords)):
        present_pair.append([presWords[i],presWords[j]])


print present1
print whole1


count = 0


for j in range(len(presWords)-1):
    for k in range(j+1,len(presWords)):
        for i in range(len(present1)):
            if (presWords[j] in present1[i]) and (presWords[k] in present1[i]):
                count = count + 1
        present_pair[present_pair.index([presWords[j],presWords[k]])].append(count)
        count = 0
                            
count = 0
print present_pair


for j in range(len(presWords)-1):
    for k in range(j+1,len(presWords)):
        for i in range(len(whole1)):
            if (presWords[j] in whole1[i]) and (presWords[k] in whole1[i]):
                count+=1
        for l in range(len(present_pair)):
            if (presWords[j] and presWords[k]) in present_pair[l]:
                present_pair[l].append(count)
                
        count = 0

g.close()
