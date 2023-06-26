#!python


import argparse
import logging
import os
import pdb
import re
import praw
import requests
import sys
import time
import traceback
import requests
import string



from praw.models import MoreComments



reddit = praw.Reddit(client_id='redacted',
client_secret='redacted',
password='redacted',
user_agent='redacted',
username='redacted',

)



subreddit = reddit.subreddit("Tumblr")





for submission in subreddit.new(limit=1000):
    with open("Tumblr_Users.txt", "a") as f:
        f.write(str(submission.author) + "\n" )
    for comment in submission.comments:
        with open("Tumblr_Users.txt", "a") as f:
            if isinstance(comment, MoreComments):
                continue
            f.write(str(comment.author) + "\n" )

    




    
