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
import subprocess
import requests
import string



reddit = praw.Reddit(client_id='redacted',
client_secret='redacted',
password='redacted',
user_agent='mac:Taylor_Swift_Is_Lord:v1.0',
username='Taylor_Swift_Is_Lord',

)

comment_text = 'Hello!' 

comment_text += '\n \n' 

comment_text += 'As a r/tumblr user, you should have clear expectations about the r/tumblr moderation (at least according to Reddit admins lolol). The only active moderator (u/taytay_is_god) was recently demodded and permanently suspended after supporting the protests. As far as your experience will be, it is most relevant that:' 

comment_text += '\n \n' 

comment_text += '1. The words queer, autistic and curated (in reference to r/CuratedTumblr) are now banned again, unless u/IranianGenius and Reddit admins have decided to no longer be bigots.' 

comment_text += '\n \n' 

comment_text += '2. There will be a lot more bot posts now. u/taytay_is_god was the only person with the code to catch the bots.' 

comment_text += '\n \n' 

comment_text += '3. The subreddit will most likely be unmoderated, so do not expect responses to modmail or reports.' 

comment_text += '\n \n'

comment_text += 'For the inside dirt, please look here: https://imgur.com/a/XqbucPw.'

counter=0
for line in open("Tumblr_Users_ND.txt", "r"):

    new_comment_text = comment_text + ' It was nice knowing you, '

    new_comment_text += line

    #print(new_comment_text)

    #print(comment_text)

    try:
        reddit.redditor(line).message('update on r/tumblr moderation',new_comment_text)
        reddit.subreddit("Tumblr").banned.add(line, ban_reason="fuck u/spez")

    except:

        print(line)

    counter+=1

    time.sleep(30)

    print(counter)

