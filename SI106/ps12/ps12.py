###################
import facebook
import json
import test106 as test

## Please put your name here!

sname = "Zijie Ku"
print sname # this is a helpful double-check for us when we are grading

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

# This code makes lists of positive words and negative words, saving them in the variables pos_ws and neg_ws.
pos_ws = []
f = open('positive-words.txt', 'r')

for l in f.readlines()[35:]:
    pos_ws.append(unicode(l.strip()))
f.close()

neg_ws = []
f = open('negative-words.txt', 'r')
for l in f.readlines()[35:]:
    neg_ws.append(unicode(l.strip()))
f.close()

### Now begins the graded problems.

# [PROBLEM 1] 
    # Fill in the definition of the class Post to hold information about one post that you've made on Facebook.
    # Add to the __init__ method additional code to set the instance variables comments and likes. 
    # More instructions about that follow, in the code below.
    # You need to pull out the appropriate data from the json representation of a single post. 
    # You can find a sample in the file samplepost.txt. 
    # There are tests that check whether you've pulled out the right data.
    
class Post():
    """object representing status update"""
    def __init__(self, post_dict={}):
        if 'message' in post_dict:
            self.message = post_dict['message']
        else:
            self.message = ""
        # [PROBLEM 1A] if the post dictionary has a 'comments' key, set an instance variable self.comments
        # to the list of comment dictionaries you extract from post_dict. 
        # Otherwise, set self.comments to be an empty list: []

        # Something similar has already been done for the contents (message) of the original post, 
        # which is the value of the 'message' key in the dictionary, when it is present 
        # (photo posts don't have a message). See above for that code, which you can model the rest after!

        # But, pulling out the list of dictionaries from a post_dict 
        # where each dictionary represents a comment from a post_dict 
        # is a little harder. You have to go one level deeper in the data structure
        # Take a look at the sample of what a post_dict looks like
        # in the file samplepost.txt to figure out where to find information.

        self.comments = []
        if 'comments' in post_dict:
            self.comments = post_dict['comments']['data']
        else:
            self.comments = []
        
        # [PROBLEM 1B] Now, similarly, if the post dictionary has a 'likes' key, set self.likes to
        # the list of likes dictionaries from the corresponding likes dictionary.  
        # Otherwise, if there are no 'likes', set self.likes to an empty list: []
        self.likes = []
        if 'likes' in post_dict:
            self.likes = post_dict['likes']['data']
        else:
            self.likes = []

    # [PROBLEM 2] In the Post class, fill in three methods:
    # -- positive() returns the number of words in the message that are in the list of positive words pos_ws (provided in our code)
    # -- negative() returns the number of words in the message that are in the list of negative words neg_ws (provided in our code)
    # -- emo_score returns the difference between positive and negative scores
    # The beginnings of these functions are below -- fill in the rest of the method code!
    # There are tests of these methods later on.
        
    def positive(self):
        pos_ws_count = 0
        for wd in self.message.split():
            if wd in pos_ws:
                pos_ws_count += 1
        return pos_ws_count
                   
    def negative(self):
        neg_ws_count = 0
        for wd in self.message.split():
            if wd in neg_ws:
                neg_ws_count += 1
        return neg_ws_count

    def emo_score(self):
        return self.positive() - self.negative()
        

# [PROBLEM 3] Add comments for these lines of code explaining what is happening in them.
sample = open('samplepost.txt').read()
sample_post_dict = json.loads(sample)

p = Post(sample_post_dict)

# use the next lines of code if you're having trouble getting the tests to pass.
# they will help you understand what a post_dict contains, and what
# your code has actually extracted from it and assigned to the comments 
# and likes instance variables.
#print pretty(sample_post_dict)
#print pretty(p.comments)
#print pretty(p.likes)

# Here are tests for instance variables set in your __init__ method
print "-----PROBLEM 1 tests"
try:
    test.testEqual(type(p.comments), type([]))
    test.testEqual(len(p.comments), 4)
    test.testEqual(type(p.comments[0]), type({}))
    test.testEqual(type(p.likes), type([]))
    test.testEqual(len(p.likes), 4)
    test.testEqual(type(p.likes[0]), type({}))
except:
    print "One or more of the test invocations is causing an error,\nprobably because p.comments or p.likes has no elements..."

# Here are some tests of the positive, negative, and emo_score methods.
print "-----PROBLEM 2 tests"
p.message = "adaptive acumen abuses acerbic aches for everyone" # this line is to use for the tests, do not change it
test.testEqual(p.positive(), 2)
test.testEqual(p.negative(), 3)
test.testEqual(p.emo_score(), -1)        
    
# [PROBLEM 4] (SOLUTION PROVIDED, Just need to un-comment)
# Get a json-formatted version of your last 100 posts on Facebook. 
# (Hint: use the facebook module, as presented in class, and use https://developers.facebook.com/tools/explorer 
# to get your access token.
# Every couple hours you will need to get a new token.)
# This is almost the same as the Facebook code example you saw in class.

# uncomment the next three lines. Fill in your access token (in quotes, because it's a string) 
# in the code if you don't want
# to have to paste it every time you run the program
access_token = None
if access_token == None:
    access_token = raw_input("\nCopy and paste token from https://developers.facebook.com/tools/explorer\n>  ")
graph = facebook.GraphAPI( access_token )
feed = graph.get_object("1683212485235313/feed", limit = 100, verify=False)


## If you do not have a Facebook account with any feed posts,
## you can use our group: replace the "me" with this id string: "1683212485235313"
## Note that you will need to get the user_groups permission with your access token, as discussed in class on Monday

# [PROBLEM 5]
# For each of those posts in the feed you get back,
    # -- create an instance of your class Post.
    # (Note that this should fill in attributes for:
        #-- the message if it exists
        #-- the comments data if it exists
        #-- the likes data if it exists)
    # Save all the post instances in a list called post_insts.
    # If you passed the tests above, all this should work just fine if you create one instance per post.

# Write code to do that here.
# print( pretty( feed['data'] ) )
post_insts = []
for post in feed['data']:
    post_insts.append( Post( post ) )

try:
    print "testing whether the list post_insts exists and is the right kind of thing"
    test.testEqual(type(post_insts), type([]))
    test.testEqual(len(post_insts) > 0, True)
    test.testEqual(type(post_insts[0]),type(Post()))
except:
    print "failed tests for problem 5 or there is another error"


# [PROBLEM 6] 
# Write code to compute the top three likers and commenters on your posts overall,
# and save them in lists called top_likers and top_commenters.
# So top_likers should contain 3 names of people who made the most likes on all your Facebook posts,
# and top_commenters should contain 3 names of people who made the most comments on all your Facebook posts.
# Hint: making dictionaries and sorting may both be useful here!
top_commenters = []
top_likers = []

commenters = {}
likers = {}

for post in post_insts:
    for comment in post.comments:
        if comment['from']['name'] in commenters:
            commenters[ comment['from']['name'] ] += 1
        else:
            commenters[ comment['from']['name'] ] = 1

for post in post_insts:
    for like in post.likes:
        if like['name'] in likers:
            likers[ like['name'] ] += 1
        else:
            likers[ like['name'] ] = 1

# print( likers )
# print( '===================' )
# print( commenters )

top_commenters = sorted( commenters, key = commenters.get, reverse = True )[:3]
top_likers = sorted( likers, key = likers.get, reverse = True )[:3]

 
### Code to help test whether problem 6 is working correctly
try: 
    print "Top commenters:"
    print top_commenters
    for p in range(len(top_commenters)):
        print p, top_commenters[p]

    print "Top likers:"
    print top_likers
    for p in range(len(top_likers)):
        print p, top_likers[p]
except:
    print "Problem 6 not correct.\ntop_commenters and/or top_likers has not been defined or is not the correct type."

# [PROBLEM 7] 
# Write code to find out: were there more unique commenters or more unique likers? 
# (Each person should only get counted once among commenters, and once among likers.)
#    (Note that this is not the same as looking at whether there were more comments or likes!)
# If there were more unique commenters, write code to print "There were more unique commenters."
# If there were more unique likers, write code to print "There were more unique likers."
if len( commenters ) > len( likers ):
    print( "There were more unique commenters." )
else:
    print( "There were more unique likers." )   
  
# [PROBLEM 8] 
# Output a .csv file that lets you make scatterplots (in Excel or Google sheets) showing 
# net positivity on x-axis and comment-counts and like-counts on the y-axis. 
# Each row should represent one post and have: emo score, comment counts, and like counts.
# Post a screenshot of your scatterplot to our facebook group!
import csv
f = open( 'result.csv', 'w' )
file_write = csv.writer( f )
data = []
data.append( [ 'emo_score', 'comment_counts', 'like_counts'] )

for post in post_insts:
    data.append( [ str( post.emo_score() ), str( len( post.comments ) ), str( len( post.likes ) ) ] )
file_write.writerows(data)
f.close()

# You can see what the scatterplot might look like
# in emo_scores.xlsx. (In the example case, there's not an obvious
# correlation between positivity and how many comments or likes. There may not be,
# but you find that out by exploring the data!)

# Can you see any trend in whether your friends are more likely 
# to respond to positive vs. negative posts? That question is not graded, but something to think about.
'''Likes are more normally distributed where as comments counts are more clustered in interval [ 0 .. 5 ]
