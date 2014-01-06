""" Reddit automated program core version 1.50a by /u/peterpacz1
    otherwise known as Shen Zhou Hong. No warrenties nor liabilities
    implied whatsoever. Open source, feel free to copy but accreddit """



""" Post excecution background work. Imports libraries and
    assigns core functions such as praw.reddit """
# Declaration of importation:
import praw                   # Main praw api
import math                   # Math libraries
import time                   # Time libraries
import os                     # system command
from collections import deque # deque lists

# Assigns r as praw.reddit
print "Attempting to communicate to reddit.com servers"
r = praw.Reddit("testbot 1.50a by /u/peterpacz1.")
print "Communication between bot to reddit established"



""" List of all user defined functions, in order of usage:
    Special thanks to stackoverflow for clearscreen() """
def clearscreen():
    """ Uses the newly imported misc. os commands to
    clear the terminal output screen in PC and mac """
    os.system('cls' if os.name=='nt' else 'clear')
    return True

def auth():
    """ Autheticates with reddit.com and attempts
    to login using default reddit account. """
    # Sets username and password
    username = "bitcointripe"
    password = raw_input("Password: ")
    print "Username: bitcointripe"
    # Logs in using variables defined above
    r.login(username, password)
    return True
def login():
    """ Actual login function. Uses auth() info to
    attempt to login, and tries again if fail """
    # Starts logging loop that attempts logins to reddit.com
    logging = True
    while logging:
        try:
            # Summons auth() to attempt to login to reddit.com
            auth()
            # If reddit replies back with True = login accepted
            if r.is_logged_in():
                print "Login successful"
                # Turns off loop after login succeeds.
                logging = False
        except praw.errors.InvalidUserPass:
        # If r.login replies back with the error above, user is informed
            print "Unable to login, please try again"
            # Goes back to loop, and attempts login again
    
def is_hot(post_body):
    """ Finds out if a post is hot and contains hotwords.
    if contains hotwords returns true. Small function """
    # If the post_body matches any words in hotword list
    if post_body in hotword:
        # Returns true
        return True
    else:
        # If the post doesn't match, returns false
        return False

def parse_comment():
    """ gets comments from specified list of subreddits in
    subreddit_list and uses is_hot() to check if hot, and
    responds using hot_responder(comments) """
    # Crawls the comments using this loop
    while True:
        # Comments = list of comments from subreddits in subreddit_list
        comments = r.get_comments(subreddit_list)
        # Summons hotresponder(comments) with comments as comments argument
        hot_responder(comments)
        
def hot_responder(comments):
    """ Responds to hot comments. First checks if the post.id
    is not in complete (etc not done before) and responds with
    a defined response, and prints affirmation to terminal """
    for post in comments:
        # Checks if post.id is not in a already completed list
        if post.id not in complete:
            # Uses is_hot() to check if post is hot or not
            is_hot(post.body)
            # If is_hot() returns True:
            if is_hot:
                # Adds post.id of proccessed comment to complete list
                complete.append(post.id)
                # Replies, and prints affirmation on terminal
                post.reply(response)
                print "Contains hotwords"
            else:
                # If not, loops to the next comment and tries again
                print "Does not contain hotwords"



""" Single variables declaration zone. """
# Hotphrases list: Bot will respond to comments containing these words:
hotword = ["f100", "f200", "f300", "f400"]
    
# Response to hotcomments: Bot replies this string to reddit.com
response = "**[BOT]**: Test Response: *12345*"

# Subreddits list: Bot will crawl comments in the subreddits below (LIST):
subreddit_list = "test"
    
# Already completed list: (limit 300 to prevent memory leak)
complete = deque(maxlen=300)

 
""" Functions excecution zone """
# Clears the terminal screen before calling any functions
clearscreen()
# Logs in to reddit
login()
# Runs core bot
parse_comments()
