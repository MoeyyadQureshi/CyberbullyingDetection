#imports Reddit API
import praw

#IMPORTANT NOTICE: REPLACE LOGIN WITH VALID INFO
#logs into reddit account
r = praw.Reddit('commentor')
r.login('ReneLevesque_', 'bdt123')

#Checks the file with links to harmful messages
#Comments on harmful messages with a reminder to treat others with respect
f = open('CommentPermalinks.txt', 'r+')
linksList = f.read().strip().split('\n')
for link in linksList:
    s = r.get_submission(link)
    comment = s.comments[0]
    comment.reply('Please be nice') ###CHANGE MESSAGE
    
f.close()
f = open('CommentPermalinks.txt', 'w') #Clears the file with links so the file can be reused
f.close()
