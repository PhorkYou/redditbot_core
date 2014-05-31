""" Cleverbot Reddit bot, made by Shen Zhou Hong.
    Version alpha 0.0.1 - all rights reserved 
"""
    
# Begin importing standard libraries (included on default)
import math
import time
import sys

# defines ImportError handler function
def import_handler(library):
    """ Error handler function that tells the user to install
    any missing libraries, and what to do to install them """
    
    print "ImportError: You must install %s" % (library)
    print "In order to install %s you must do" % (library)
    print "# pip install %s" % (library)
    print "assuming you have pip installed"
    time.sleep(2)
    sys.exit()
# Begin importing non standard libraries with error handling
try:
    import praw
    print "Successfully loaded praw"
except ImportError:
    import_handler("praw")

# Sets useragent
print "Please set bot useragent (short descriptive sentence)"
useragent = raw_input("    useragent: ")
# Creates praw.reddit object and sends useragent over
r = praw.Reddit(useragent)
print "Communication between bot to reddit established"

# Starts authenication function
def login():
    """ Login function - a loop with error handling tat
    provides an easy authentication experiance that
    allows the user to log in with a bot reddit account """
    
    # Login loop
    logging = True
    while logging:
        try:
            # Starts defining username and password from user
            print "Please enter reddit.com login credentials"
            username = raw_input("    Username: ")
            password = raw_input("    Password: ")
            
            # Uses username and password to login via Praw
            r.login(username, password)
            # Successful authentication
            if r.is_logged_in():
                print "Login into %s account is successful" % (username)
                logging = False
                
            else:
                pass
                
        except praw.errors.InvalidUserPass:
            # If the login failed
            retrying = True
            while retrying:
                print "Login Failure, bad username/password?"
                print "Do you want to retry in 30 seconds?"
                
                # Evaluates user response
                response = raw_input("(Y/N): ")
                if response.upper() == "Y":
                    retrying = False
                    # Retrys login in 30 seconds
                    print "Ok, please wait..."
                    time.sleep(30)
                elif response.upper() == "N":
                    print "Program will exit"
                    time.sleep(2)
                    retrying = False
                    sys.exit()
                else:
                    print "Please respond with 'Y' or 'N'"
            
def version():
    """Displays version number"""
    print "Reddit Bot Core: Version 3.00 RC1"

def subreddit_only():
    """ Allows the user to choose if the bot operates only in an
    subreddit, or in the entire reddit.com. """
    # Prints the available options to choose from
    print "Please choose operation mode (A/B):"
    print "    A - subreddit mode only"
    print "    B - entire reddit.com mode"

    # First loop allows users to enter the choice, or try again
    trying = True
    while trying:
        choice = raw_input("Enter your choice: ")
            
        if choice.upper() == "A":
            print "OK - single subreddit mode"
            trying = False
            return True
        elif choice.upper() == "B":
            print "OK - entire reddit.com mode"
            trying = False
            return False
        else:
            print "Please enter 'A' or 'B' as a response"

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
    
def footer_setup():
	"""Allows user to set up the footer, a small piece of
	text that can contain contact information, etc.
	Right now only supports contact information """
	print "Please enter your main reddit account as the"
	print "contact information (in case anything goes wrong"
	contactinfo = raw_input("/u/")
	footer = "^^Note: ^^This ^^post ^^is ^^made ^^by ^^a ^^bot. ^^Contact ^^/u/%s ^^for ^^more ^^info" % (contactinfo)
	return footer
	
    
def comment_parser(hotword, response, footer):
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
    	print "Please enter the name of the subreddit:"
        subreddit_name = raw_input("    /r/")
        # First loop, parses though comments and replies to them
        while trying:
            for post in subreddit_mode(subreddit_name):
                if post.body == hotword and post.id not in done:
                    post.reply(response + "\n\n" + "---" + "\n\n" + footer)
                    # Adds to the list of completed comments
                    done.add(post.id)
                    print "Contains hotwords"
                else:
                    print "Does not contain hotwords"
            # Now waits 30 seconds before looping again
            print "Sleeping (reddit API rule)"
            time.sleep(30)
    else:
        # If operating in the entire reddit.com same code as above
        print "Will operate in entire reddit.com website"
        print "Warning - if bot runs wild, bans may happen"
        while trying:
            for post in reddit_mode():
                if post.body == hotword and post.id not in done:
                    post.reply(response)
                    done.add(post.id)
                    print "Contains hotwords"
                else:
                    print "Does not contain hotwords"
            print "Sleeping (reddit API rule)"
            time.sleep(30)
                
# Starts program
def startup(arg):
    """Startup function. Call this in order to start the program"""
    if arg:
        #Checks if argument is true   
        version()
        login()
        comment_parser(hotword_setup(), response_setup(), footer_setup())
    else:
        #If argument not true:
        print "Error: Set startup() arg to True"

startup(True)
                
