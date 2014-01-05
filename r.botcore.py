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
    password = raw_input("Password: ")
    r.login(username, password)

# Attempts to login
logging = True
while logging:
    try:
        # Login successful
        login()
        print "Login successful"
        logging = False
    except praw.errors.InvalidUserPass:
        # Error handling
        print "Unable to login, please try again"
        
# Hotphrases list
hotword = [
    "testa"
    "testb"
    "testc"
    "testd"
    ]
    
# Active subreddits
subreddit_list = "test"
    
# Banned subreddits:
banned = [
    "testban"
    ]

# Already completed list (limit 300 to prevent memory leak)
complete = deque(maxlen=300)

def parse_comment():
        subreddit = r.get_subreddit(subreddit_list)
        sub_comments = subreddit.get_comments()
        
parse_comment()
print "All done"
