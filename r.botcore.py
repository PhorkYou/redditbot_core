""" 
    Reddit automated program (bot). Connects to www.reddit.net
    servers and automatically parses though comments, and responds
    to them if they fit a certain criteria. Created by /u/
    peterpacz1/Shen Zhou Hong. Copyright 2014
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
print "Communication between bot to reddit established"

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
    print "Password:"
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

def op_parm():
    """ Operation parameters. Function allows user to choose
    between having the bot operate in a single submission, a
    single subreddit, or the entirety of reddit.net itself """
    
    # Limited user interface
    print "Welcome, please choose the operation zone of this bot"
    print "... A single submission? (Enter 1)"
    print "... A single subreddit? (Enter 2)"
    print "... The whole reddit.com? (Enter 3)"
    choice = raw_input("Enter your choice please: ")
    
    #Detects the choice that the user makes
    str(choice)
    trying = True
    while trying:
        if choice == "1":
            print "Ok - single submission mode"
            trying = False
            return 1
        
        elif choice == "2":
            print "Ok - single subreddit mode"
            trying = False
            return 2
        elif choice == "3":
            print "Ok - entire reddit.com mode"
            trying = False
            return 3
        else:
            print "Please enter 1, 2, or 3. Try again"

def submission_mode():
    """ Operating bot in single submission mode Gets comments as
    intake, and flattens them. """
    
    #Finds submission ID and flattens comment tree
    submission_id = raw_input("Please enter submission ID: ")
    intake = r.get_submission(submission_id)
    print "got " + str(len(intake)) + " comments"
    flat_intake = praw.helpers.flatten_tree(intake.comments)
    
    #Returns the flattened comment tree
    return flat_intake
    
def subreddit_mode():
    """ Operating bot in single subreddit. Gets comments as
    intake, and flattens them. """
    
    #Finds the subreddit name, and flattens comment tree
    subreddit_name = raw_input("Please enter subreddit name: ")
    intake = r.get_comments(subreddit_name)
    print "got " + str(len(intake)) + " comments"
    flat_intake = praw.helpers.flatten_tree(intake.comments)
    
    #Returns the flattened comment tree
    return flat_intake
    
def reddit_mode():
    """Operating bot in the entire reddit.com website. Gets
    comments as intake, and flattens them. Same code for
    subreddit mode, except /r/all is used. """
    
    #Returns flattened comments from /r/all
    intake = r.get_comments("all")
    print "got " + str(len(intake)) + " comments"
    flat_intake = praw.helpers.flatten_tree(intake.comments)
    
    #Returns the flattened comment tree
    return flat_intake

def comment_parser():
    """Parses though the comments and replies to them if they
    contain the 'hotwords' that are specified by the user"""
    
    # NOT FINISHED YET
    
# NOT FINISHED YET
login()
if op_parm() == 1:
    submission_mode()
elif op_parm() == 2:
    subreddit_mode()
elif op_parm() == 3:
    reddit_mode()
    
    

