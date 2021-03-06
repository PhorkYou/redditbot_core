""" Reddit Bot Core - A standard reddit bot that could be
    used by anyone, and quickly expanded upon by anybody.
    
    Version BETA 4.0.0 Release Candidate 3
"""

# Import standard libraries
import math
import time
import sys
import getpass
import re

# Import Praw (Python Reddit API Wrapper) with error handling
try:
    import praw
    print "PRAW (Python Reddit API Wrapper) has loaded"
except ImportError:
    # Error handling if praw is not installed on users system
    lib = "PRAW"
    print "ImportError: %s is not found on your system" % (lib)
    print "You must install %s to operate this program" % (lib)
    sys.exit()
    
# Useragent
print "Please set bot useragent (short descriptive sentence)"
print "Make sure your useragent includes:"
print "    Bot Name"
print "    Version Number"
print "    Username of botmaster"
useragent = raw_input("Useragent: ")

# Creates praw.reddit object using useragent
r = praw.Reddit(useragent)

# Login
def login():
    """ Login function - login at reddit.com using user specified
    credentials. Contains basic error handling using a loop0 """
    
    # Login loop
    while True:
        try:
        
            # Defines username and password
            print "Please enter the bot's username and password"
            print "Notice: An account at reddit.com is required"
            username = raw_input("    Username: ")
            
            # Password is securely prompted using getpass (no echo)
            print "Your password is blanked out for security reasons"
            print "Continue typing normally"
            password = getpass.getpass("    Password: ")
            
            # Attempts to authenticate with reddit.com
            r.login(username,password)
            if r.is_logged_in():
                print "Login into /u/%s is successful" % (username)
                time.sleep(2)
                break

        # Error handling if login credentials is incorrect
        except praw.errors.InvalidUserPass:
            
            # User is prompted to retry authentication or quit
            print "PrawError: Login as /u/%s has failed" % (username)
            print "Please make sure that:"
            print "    Username/Password combination is correct"
            print "    A internet connection is available"
            print "    reddit.com is online and reachable"
            print "Retry authentication?"
            
            # Retry Authentication Loop
            while True:
            
                # Response is evaluated
                response0 = raw_input("(Y/N): ")
                if response0.upper() == "Y":
                    print "Please wait 30 seconds (Reddit API Rule)"
                    time.sleep(30)
                    break
                
                elif response0.upper() == "N":
                    print "Exiting Reddit Bot Core."
                    time.sleep(2)
                    sys.exit()
                    
                else:
                    print "TypeError: Please respond with 'Y' or 'N'"
        
        # Error handling if user is attempting to login quickly            
        except praw.errors.RateLimitExceeded:
            print "PrawError: Login rate limit has been exceeded"
            print "Login has been attempted multiple times in succession"
            print "Please wait 5 minutes before reattempting login"
            print "Retry authentication in 5 minutes?"
            
            # Retry Authentication in 5 minutes loop
            while True:
                
                # Response is evaluated
                response1 = raw_input("(Y/N): ")
                if response1.upper() == "Y":
                    print "Will retry authentication in 5 minutes"
                    time.sleep(300)
                    break
                
                elif response0.upper() == "N":
                    print "Exiting Reddit Bot Core."
                    time.sleep(2)
                    sys.exit()
                    break
                    
                else:
                    print "TypeError: Please respond with 'Y' or 'N'"
                    
def operation_scope():
    """ Defines the operational scope of the bot. Prompts the user to
    choose between operating in test mode, in community mode, or in
    production (entire reddit.com website) mode. """
    
    # Displays available modes of operation
    print "Please choose the operation mode of your reddit bot."
    print "Currently, there are 3 distinct operation modes available"
    print "    Test Mode - Operates only in /r/test subreddit"
    print "    Community Mode - Operates only in a user defined subreddit"
    print "    Production Mode - Operates in entire reddit.com website"
    
    # User is prompted for response and response is evaluated
    while True:
        response0 = raw_input("(T/C/P): ")
        
        # Response is evaluated
        if response0.upper() == "T":
            print "Test Mode Accepted"
            time.sleep(2)
            return "test"
            
        elif response0.upper() == "C":
            print "Community Mode Accepted"
            time.sleep(2)
            
            # Additionally user is prompted for subreddit name
            print "Please enter a subreddit name (ex: 'AskReddit')"
            subreddit_name = raw_input("/r/")
            return subreddit_name
        
        elif response0.upper() == "P":
            print "Production Mode - Accepted"
            time.sleep(2)
            return "all"
            
        else:
            print "TypeError: Please respond with:"
            print "    'T' for Test mode"
            print "    'C' for Community mode"
            print "    'P' for Production mode"
            
def get_comments(subreddit_name):
    """ Function that uses PRAW to recieve the comments of a subreddit
    defined in operation_scope(). On default, subreddits for Test Mode
    and Production Mode are hardcoded as 'test' and 'all'. """
    
    # Intake variable contains .json of all subreddit comments
    intake = r.get_comments(subreddit_name)
    return intake
    
def search_setup():
    """ Allows a user defined 'hotword' to be set, which would be searched
    against in the comments from get_comments() """
    
    # Prompts user for search term
    print "Reddit Bot Core must be configured to look for a search term"
    print "that it will reply to. This term would be searched for in the"
    print "comments, and the bot will reply a phrase to all matches"
    print "Please make sure that the term is not too generic"
    
    # Ensures term is not empty
    while True:
        term = raw_input("    Search Term: ")
        if term == "":
            print "TypeError: Please make sure search term is not empty"
        else:
            print "Accepted %s as search term" % (term)
            break
    
    return term

def reply_setup():
    """ Allows a user defined reply to be set which would be sent as an
    reply to all comments that matches the search term defined above """
    
    # Prompts user for search term
    print "A reply must be configured for the search term that is defined"
    print "earlier. This would be sent as a reply to all comments that"
    print "matches the term defined above."
    print "Please make sure to follow reddiquette, especially for a bot"
    
    # Ensures reply is not empty
    while True:
        reply = raw_input("    Reply Message: ")
        if reply == "":
            print "TypeError: Please make sure reply message is not empty"
        else:
            print "Accepted '%s' as reply message" % (reply)
            return reply
            
def footer_setup():
    return True
    """ Prompts the user to choose a footer, which would be automatically
    added to the end of every comment the bot will post. The footer can
    be configured to have contact information, and details about the bot """
    
    # Prompts user about footer configuration
    print "Do you want to configure a footer? A footer is a short message"
    print "attached to the end of a comment posted by the bot."
    print "The footer will contain:"
    print "    Botmaster username - in case bot becomes disruptive/broken"
    print "    Custom message - general info about the robot"
    
    # Querys user to enable footer or not
    while True:
        response0 = raw_input("    Enable Footer? (Y/N): ")
        if response0.upper() == "Y":
        
            # Prompts the user with information about the contact info
            print "Please enter your main reddit account as the botmaster"
            print "Moderators and Admins can contact you via this account"
            print "in case the bot becomes rogue"
            username = raw_input("    /u/")
            
            # Removes section if contactinfo is blank
            if username == "":
                print "No contact information will be given"
            else:
                print "Botmaster will be set as /u/%s" % (username)
                
            # Prompts the user with information about the custom message
            print "If you wish, you can enter a optional message to be"
            print "included with your footer. It must be less than 64 "
            print "characters long. To skip, simply have a blank message"
            
            # Checks if message is < 64 char, and formats it as footer
            while True:
                message = raw_input("    Message: ")
                if len(message) > 64:
                    print "TypeError: The message is longer than 64 char"
                    print "Try again?"
                    response1 = raw_input("    (Y/N): ")
                    if response1.upper() == "Y":
                        pass
                    elif response1.upper() == "N":
                        print "Message will be skipped"
                        break
                    else:
                        print "TypeError: Please respond with 'Y' or 'N'"
                else:
                    loop1 = False
                break
            # Formats the footer using reddit markup
            message.split(" ")
            newmessage = ""
            for w in message:
                newmessage = newmessage + "^^" + w + " "
            
            break
        
        elif response0.upper() == "N":
            break
        
        else:
            print "TypeError: Please respond with 'Y' or 'N'"
    
    # Footer is created and passed on to comment_parser()
    footer = "\n \n" + "---" + "\n \n" + "^^This ^^is ^^a ^^bot ^^by ^^/u/" + username + " ^^| " + newmessage
    return footer
    
def comment_parser(term, message, footer, scope):
    """ Main comment parser function goes through all comments that are
    found by get_comments() and checks if post.body contains the search
    terms determined by search_setup(). Replys reply and also footer """
    
    # Informs user that the bot is now successfully running
    print "All configuration complete. The bot is now running"
    print "Exit by Ctrl + C in terminal"
    
    # Competed comments set (to prevent replying multiple times to a comment
    complete = set()
    
    # Main parser loop
    loop0 = True
    
    # Misc statistics variables
    parse_term = 0
    parse_noterm = 0
    while loop0:
        intake = get_comments(scope)
        for post in intake:
            if post.body == term and post.id not in complete:
                post.reply(message) # + footer)
                parse_term += 1
                print "%s comment(s) search has term from %s processed" % (parse_term, parse_noterm)
                
                # Adds parsed comment to completed set
                complete.add(post.id)
            else:
                parse_noterm += 1
                print "%s comment(s) search has term from %s processed" % (parse_term, parse_noterm)

        print "Sleeping 30 seconds (reddit API rule)"
        time.sleep(30)

def startup():
    """ Starts the entire program up by calling all functions in correct
    order and sequence. """

    # Logs in using login function which sets useragent
    login()
    
    # Calls comment_parser, which calls all required functions when needed
    comment_parser(search_setup(), reply_setup(), footer_setup(), operation_scope())

# Starts program
startup()
