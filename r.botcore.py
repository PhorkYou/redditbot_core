# Declaration of importation:
import praw # Main praw api
import math # Math libraries
import time # Time libraries
import os   # system command

# Clears the screen of the terminal
os.system('cls' if os.name=='nt' else 'clear')

print "Attempting to communicate to reddit.com servers"
# Code body begins
# Assigns "r" as praw.reddit for praw functions to only require a single r. in front of them rather than praw.
r = praw.Reddit( """testbot 1.00 beta by /u/peterpacz1.
                Did I break anything? Please punish me with a
                ban on this version, and I will try to behave
                better in the next version."""
               )
print "Communication between bot to reddit established"

# Login and subreddit finder.
def login():
    # Asks for login information to login bot account.
    username = raw_input("Please enter username: ")
    password = raw_input("Please enter password: ")
    
    # Logs in bot account using information gathered above.
    r.login(username, password)
    
    #Tells the client everything is well.
    print "Login completed."

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
                has_hot = any(string in flat_comments for string in hotwords)
                if has_hot and comment.id not in complete:
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
        
        
# Activates the login function to log the bot in (see above).
login() 
subreddit_or_submission()

print "All done"
