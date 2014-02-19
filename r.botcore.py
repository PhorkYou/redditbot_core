""" 
    Reddit automated program (bot). Connects to www.reddit.net
    servers and automatically parses though comments and responds
    to them if they fit a certain criteria. Created by /u/
    peterpacz1/Shen Zhou Hong. Copyright 2014
    
    VERSION 1.80a
"""

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
r = praw.Reddit("testbot 1.60a by /u/peterpacz1.")
time.sleep(1)
print "Communication between bot to reddit established"

def auth():
    """ Autheticates with reddit.com and attempts
    to login using default reddit account. """
    # Sets username and password
    username = "bitcointripe"
    print "Username: bitcointripe"
    password = raw_input("Password: ")
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
        # If r.login replies back with the error, user is informed
            print "Unable to login, please try again"
            # Goes back to loop, and attempts login again

def subreddit_only():
    """ Allows the user to choose if the bot operates only in an
    subreddit, or in the entire reddit.com. """
    print "Please choose operation mode"
    print "....A subreddit"
    print "....B reddit"

    # Loop 
    trying = True
    while trying:
        choice = raw_input("Enter your choice: ")
            
        if choice == "A":
            print "OK - single subreddit mode"
            trying = False
            return True
        elif choice == "B":
            print "OK - entire reddit.com mode"
            trying = False
            return False
        else:
            print "Error - Please try again"

def subreddit_mode(subreddit_name):
    """ Operating bot in single subreddit. Gets comments as
    intake, and flattens them. """
    
    #Finds the subreddit name, and flattens comment tree
    trying = True
    while trying:
        intake = r.get_comments(subreddit_name)
        return intake
    
def reddit_mode():
    """Operating bot in the entire reddit.com website. Gets
    comments as intake, and flattens them. Same code for
    subreddit mode, except /r/all is used. """
    
    #Returns flattened comments from /r/all
    trying = True
    while trying:
        intake = r.get_comments("all")
        return intake

def hotword_setup():
    print "Please set up hotword to search for:"
    hotword = raw_input()
    return hotword
    
def response_setup():
    print "Please set up the response to the hotword:"
    response = raw_input()
    return response
    
def comment_parser(hotword, response):
    trying = True
    done = set()
    if subreddit_only():
        subreddit_name = raw_input("Please enter subreddit name: ")
        while trying:
            for post in subreddit_mode(subreddit_name):
                if post.body == hotword and post.id not in done:
                    post.reply(response)
                    done.add(post.id)
                    print "Contains hotwords"
                else:
                    print "Does not contain hotwords"
            print "Sleeping"
            time.sleep(30)
    else:
        while trying:
            for post in reddit_mode():
                if post.body == hotword and post.id not in done:
                    post.reply(response)
                    done.add(post.id)
                    print "Contains hotwords"
                else:
                    print "Does not contain hotwords"
            print "Sleeping"
            time.sleep(30)
                

login()
comment_parser(hotword_setup(), response_setup())
