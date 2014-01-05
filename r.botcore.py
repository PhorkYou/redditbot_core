# Declaration of importation:
import praw                   # Main praw api
import math                   # Math libraries
import time                   # Time libraries
import os                     # system command
from collections import deque # deque lists

# Clears the screen of the terminal
os.system('cls' if os.name=='nt' else 'clear')

# Assigns r as praw.reddit
print "Attempting to communicate to reddit.com servers"
r = praw.Reddit("testbot 1.30a by /u/peterpacz1.")
print "Communication between bot to reddit established"

# Login to reddit function
def login():
    username = "bitcointripe"
    print "Username: bitcointripe"
    password = "reddi!H8uE054F/I"
    r.login(username, password)

# Attempts to login
logging = True
while logging:
    try:
        # Login successful
        login()
        if r.is_logged_in() == True:
            print "Login successful"
            logging = False
    except praw.errors.InvalidUserPass:
        # Error handling
        print "Unable to login, please try again"
        
# Hotphrases list
hotword = ["atest", "btest", "ctest", "dtest"]
    
# Response to hot comment
response = "**[BOT]**: Test Response: *12345*"

# Amount of comments proccessed
amount = 1
    
# Active subreddits
subreddit_list = "test"
    
# Banned subreddits:
banned = [
    "testban"
    ]

# Already completed list (limit 300 to prevent memory leak)
complete = deque(maxlen=300)

# Finds out if a post contains the hotwords liste earlier
def is_hot(post_body):
    if post_body in hotword:
        return True
    else:
        return False

# Parses though the comments, and checks if they are hot
def parse_comment():
    # get_comments loop
    while True:
        comments = r.get_comments(subreddit_list)
        for post in comments:
            if post.id not in complete:
                is_hot(post.body)
                complete.append(post.id)
                amount
                if is_hot is True:
                    post.reply(response)
                    print "Contains hotwords"
                else:
                    print "Does not contain hotwords"
                   
parse_comment()
