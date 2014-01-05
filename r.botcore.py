# Declaration of importation:
import praw # Main praw api
import math # Math libraries
import time # Time libraries
import os   # system command

# Clears the screen of the terminal
os.system('cls' if os.name=='nt' else 'clear')

# Assigns r as praw.reddit
connecting = True
while connecting:
    print "Attempting to communicate to reddit.com servers"
    r = praw.Reddit("testbot 1.30a by /u/peterpacz1.")
    trying = False
    print "Communication between bot to reddit established"

# Login to reddit function
def login():
    username = raw_input("Please enter username: ")
    password = raw_input("Please enter password: ")
    r.login(username, password)

# Attempts to login
logging = True
while logging
    try:
        # Login successful
        login()
        print "Login successful"
        logging = False
    except praw.errors.InvalidUserPass:
        # Error handling
        print "Unable to login, please try again"
        
# Asks user to choose between a single subreddit or submission, and returns the data
def subreddit_or_submission():

    # First asks the user to choose between a subreddit or submission
    query = raw_input("Do you want to operate in a single submission or subreddit (submission/subreddit): ")
    
    # Specific hotwords 
    hotwords = ["hotword1", "hotword2", "hotword3", "hotword4"]
    
    # List of comments already responded to
    complete = set()
    
    if query == "submission":
        submission_id = raw_input("Enter submission URL: ")
        while True:
            flat_comments = praw.helpers.flatten_tree(r.get_submission(submission_id).comments)
            for comment in flat_comments:
            
                # First checks if the comment contains the hotwords, and if the comment is not already done
                if comment.body in hotwords and comment.id not in complete:
                    comment.reply("response")    # Replies
                    complete.add(comment.id) # Adds the comment id to a list of already done comments
                    print "cycle complete"

    elif query == "subreddit":
        subreddit_id = raw_input("Enter subreddit ID: ")
        
        # Returns the data as subreddit variable
        return subreddit
        
    else:
    # If something breaks
        print "Error: Invalid choice"
        
       
print "All done"
