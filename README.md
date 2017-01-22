# Cyberbullying Detection

**Description**

This project seeks to combat cyberbullying in social media, through computer automated detection and prevention of cyberbullying. Through analyzing the monogram and bigram frequencies of harmful messages, a machine learning algorithm will be used to determine if an inputted Reddit comment is harmful or not. This is done through a bot that scans through Reddit comments.

A preventative system will be implemented based on the Rethink System of cyberbullying prevention. See the below link for more information about this system:

[https://www.googlesciencefair.com/projects/en/2014/f4b320cc1cedf92035dab51903bdd95a846ae7de6869ac40c909525efe7c79db]

**Technologies**

- PRAW (Python Reddit API Wrapper)
- NLTK (Natural Language Tool Kit)
- Python 2.7.11

**Research**

This project was developed for research purposes. The research report can be found directly below:

https://1drv.ms/b/s!ArYmmazjqJUssDulBBpNNEllisZk

The software development report can be found directly below:

https://1drv.ms/b/s!ArYmmazjqJUssDzsgZP9ygfXY7d4

**Notes**

This project is in its very early stages. Currently this is the third model of a cyberbullying detection program that I've developed, and more models are planned which add/refine:

- Consistency checking features to ensure that checks if longer comments include instances of cyberbullying throughout. This will reduce the number of false positives
- Context checking the surrounding comments to see if any hostility/negativity was already present
- A More reliable data gathering system from the program to learn from
- Using cython to be able to handle larger sets of data to learn from
- Incorporating natural language processing into the detection algorithm using SyntaxNet and Tensorflow
- Using Facebook/Twitter API so this program can detect more than just Reddit comments

**Instructions**

1. Delete anything in the text files
2. Run TestCaseKarma.py
3. Run nGrams.py
4. Run Bot.py
5. Run Replier.py

Warning: Some of the code my need to be updated with valid Reddit Login credentials.
