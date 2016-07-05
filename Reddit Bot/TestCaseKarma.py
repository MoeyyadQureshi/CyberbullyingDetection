#importing PRAW (Python Reddit API Wrapper) to access Reddit's API
import praw

#user agent is a library to identify device by parsing user agent strings
user_agent = ("PyEng Bot 0.1")
r = praw.Reddit(user_agent = user_agent)

#specifying which subreddit to search
subreddit = r.get_subreddit("twoxchromosomes")

#specifies how many comments to search
#specifies how it sorts the comments to search from
subreddit_comments = subreddit.get_comments(sort = u'controversial', limit = 1000)

#open files to record data
presentReference = open("PresentDataReference.txt","r+")
notPresentReference = open("NotPresentDataReference.txt","r+")
present = open("PresentData.txt","r+")
notPresent = open("NotPresentData.txt","r+")

#writes harmful comments to the appropriate file
#writes non-harmful comments to the appropriate file
for comment in subreddit_comments:
    if all(ord(c) < 128 for c in comment.body):
        if comment.score < -1: #comment is treated as harmful if karma < -1
            presentReference.write('\n'+comment.body +'\n'+'-----')
            present.write(comment.body+'-----')
        elif comment.score >= 5: #comment is treated as non-harmful if karma < 5
            notPresentReference.write('\n'+comment.body+'\n'+'-----')
            notPresent.write(comment.body+'-----')


#closes files
present.close()
notPresent.close()
presentReference.close()
notPresentReference.close()
