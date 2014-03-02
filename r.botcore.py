""" 
    Reddit automated program (bot). Connects to www.reddit.net
    servers and automatically parses though comments and responds
    to them if they fit a certain criteria. Created by /u/
    peterpacz1/Shen Zhou Hong. Copyright 2014
    
    VERSION 2.60 BETA 
"""
""" Post excecution background work. Imports libraries and
    assigns core functions such as praw.reddit """
# Declaration of importation:
# Items of significance: deque lists, and system hooks
import praw
import math
import time
import os #depreciated
from collections import deque

""" User notice that praw has to be installed """
print "Notice: Python Reddit API Wrapper must be installed"
time.sleep(4)

# Assigns useragent
print "Attempting to communicate to reddit.com servers"
time.sleep(2)
print "Please set bot useragent"
print "A good useragent contains the author, the version"
print "and a short description of what the bot does. "
useragent = raw_input("useragent: ")

# Creates praw.reddit object and sends useragent over
r = praw.Reddit(useragent)
time.sleep(2)
print "Communication between bot to reddit established"

# Now listing all defined functions:

def version():
    """Displays version number"""
    print "Reddit Bot Core: Version 2.60 Beta"
    
def auth():
    """ Autheticates with reddit.com and attempts
    to login using default reddit account. """
    # Sets username and password
    print "Login with reddit.com account"
    username = raw_input("....Username: ")
    password = raw_input("....Password: ")
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
            print "Unable to login to reddit (bad username/password?)"
            print "Will retry to login in 60 seconds, please wait..."
            
            # Pauses the program for 60 seconds to prevent shell overflow
            # suggested by /u/manueslapera
            time.sleep(60)
            # Goes back to loop, and attempts login again
        
def subreddit_only():
    """ Allows the user to choose if the bot operates only in an
    subreddit, or in the entire reddit.com. """
    # Prints the available options to choose from
    print "Please choose operation mode"
    print "....A subreddit"
    print "....B reddit"

    # First loop allows users to enter the choice, or try again
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
    """Operating the reddit bot in a single subreddit mode.
    gets comments, and returns them """
    # Allows users to set the subreddit name
    intake = r.get_comments(subreddit_name)
    return intake
    
def reddit_mode():
    """Operating the reddit bot in entire reddit.com mode.
    CAUTION: if bot runs wild, bans may happen. Same as
    subreddit mode except uses /r/all """
    # Uses praw to get comments as intake from /r/all
    intake = r.get_comments("all")
    return intake

def hotword_setup():
    """Hotwords setup. Allows the user to set a certain
    hotword to search for in the comments """
    print "Please set up hotword to search for:"
    hotword = raw_input()
    return hotword
    
def response_setup():
    """Response setup. Allows the user to set a response
    to the comments if the hotword is found """
    print "Please set up the response to the hotword:"
    response = raw_input()
    return response
    
def comment_parser(hotword, response):
    """Main function that does all the work. Uses the previous
    functions to check if it's operating in subreddit only or not
    and parses comments depending on the conditions, than replies
    to them using user specified hotword/responses """
    
    # the "done" set - keeps list of completed comments
    done = set()
    
    # Sets trying to True in order to prepare for the loops
    trying = True
    
    # Checks to see if the bot's operating in a subreddit only
    if subreddit_only():
        subreddit_name = raw_input("Please enter subreddit name: ")
        # First loop, parses though comments and replies to them
        while trying:
            for post in subreddit_mode(subreddit_name):
                if post.body == hotword and post.id not in done:
                    post.reply(response)
                    # Adds to the list of completed comments
                    done.add(post.id)
                    print "Contains hotwords"
                else:
                    print "Does not contain hotwords"
            # Now waits 30 seconds before looping again
            print "Sleeping"
            time.sleep(30)
    else:
        # If operating in the entire reddit.com same code as above
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
                
# Starts program
def startup(arg):
    """Startup function. Call this in order to start the program"""
    if arg:
        #Checks if argument is true   
        version()
        login()
        comment_parser(hotword_setup(), response_setup())
    else:
        #If argument not true:
        print: "Error: Set startup() arg to True"

startup(True)
