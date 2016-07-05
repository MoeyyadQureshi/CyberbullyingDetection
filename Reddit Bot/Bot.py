#importing PRAW (Python Reddit API Wrapper) to access Reddit's API
import praw
import nltk

#user agent is a library to identify device by parsing user agent strings
user_agent = ("StupidName 0.1")
r = praw.Reddit(user_agent = user_agent)

##### IMPORTANT NOTICE #####
#Replace the below line of code with valid login info #
#Log into reddit account
r.login = ('ReneLevesque_', 'bdt123')


wholeBi = []
x = ''

#specifying which subreddit to search
subreddit = r.get_subreddit("relationships")

#specifies how many comments to search
subreddit_comments = subreddit.get_comments(limit = 100)
f = open('Bigrams.txt','r')
bigrams = f.read().strip().split('\n')
g = open('UserWatchlist.txt','r+')
userWarning = g.read().strip().split()
h = open('CommentPermalinks.txt','r+')

#scans through reddit comments that the bot retrieves
ratio = 0.0
for comment in subreddit_comments:
    if all(ord(c) < 128 for c in comment.body):
        x = str(comment.body)
        x = x.translate(None,'.!?#$%&()[]{}/') #removes any characters that might crash the program

        #retrives the bigrams of the comment
        tokens = nltk.word_tokenize(x)
        bgs = nltk.bigrams(tokens)
        fdist = nltk.FreqDist(bgs)
        count = 0

        #compares the comment to the learning data of harmful and non-harmful messages
        for k,v in fdist.items():
            wholeBi += [str(k),v]
            if str(k) in bigrams:
                if float(bigrams[bigrams.index(str(k))+2]) > ratio: 
                    ratio = float(bigrams[bigrams.index(str(k))+2])

                #if the comment is deemed to be harmful
                if ratio > 0.5: #and float(bigrams[bigrams.index(str(k))+1]) > 1:
                    
                    #checks if the user behind the comment has made other harmful comments
                    if (str(comment.author) in userWarning): 
                        if int(userWarning[userWarning.index(str(comment.author))+1]) >= 2:
                            h.write(str(comment.permalink)+'\n')                       
                    else:
                        userWarning.append(str(comment.author))
                        userWarning.append(str(0))
                    userWarning[userWarning.index(str(comment.author))+1] = str(int(userWarning[userWarning.index(str(comment.author))+1])+1)
                    break
                        
g.close()
g = open('UserWatchlist.txt', 'w')

#writes updated user information to a file                        
for line in userWarning:
    g.write(str(line)+'\n')

f.close()
g.close()
h.close()
                
                
            


