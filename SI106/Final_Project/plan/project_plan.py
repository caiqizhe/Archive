#See requirements in the "Final Project Instructions" document in cTools

## Please put your name here!

sname = "Zijie Ku"
print sname # this is a helpful double-check for us when we are grading
print
print "------"

#####Part I. Describe your project #####

# Include:
# a.	What data sources you will use
# b.	How you plan to process the data you will get.
# c.	How you will present the results.
s = """
a. I will use stock data from Google Finance (https://pypi.python.org/pypi/googlefinance) and Yahoo Finace (http://finance.yahoo.com/q?s=) (https://pypi.python.org/pypi/yahoo-finance/1.1.4)
b. I will use json.dumps() to convert data to JSON format for data from Google Finance, which will be merged with data set from Yahoo Finance for detailed trade information. 
c. I will use Matplotlib API for python to render the stock historical data.
"""
print s
print
print "------"

#####Part II: Describe a class you will define ####

# The name of my class will be...
your_name = "Stock"

# Each instance of my class will represent one...
your_inst_represents = "company stock on either NYSE or NASDAQ"

# Each instance of my class will have ... instance variables
your_inst_var_count = 15

# Each instance will have instance variables that keep track of...
your_inst_vars = "Company Name, Stock Symbol, Index, Last Trade Price, Last Trade Time, Yield, ID, Currency, Year High, Year Low, Day High, Day Low" 

# One method of my class, other than __init__, will be named...
your_method_name = "getQuote(), getSymbol(), getHistory(), getPrice()"

# When invoked, that method will...
your_method_description = "getQuote() will return all information available to the stock with last trade price.\
getSymbol() will return the symbol of the stock. getHistory will return the historical price within a time frame.\
getPrice will return current stock price."

print "The name of my class will be %s. Each instance of my class will represent one %s. Each instance will have %d instance variables. The instance variables will keep track of %s. One method of my class, other than __init__, will be named %s. When invoked, that method will %s." % (your_name, your_inst_represents, your_inst_var_count, your_inst_vars, your_method_name, your_method_description)
print
print "----------"

#####Part III (For API projects only): For each API that you will use, provide answers to the following questions, 
##analogous to the answers provided in the document "Using APIs summary table.pdf"

# a.	Modules
print """Modules to use for access to the API
>> requests, json, yql, urllib2, urllib, matplotlib

"""

# b.	Developer key
print """Is developer key needed and how to get one?
>> YQL API key. sign-up on Yahoo! Developer Network and generate one API key.

"""

# c.	Authorization for particular users
print """Is authorization needed for particular users? If so, how is that done?
>> No authentication is required for any user since stock price is publically available.

"""


# d.	Making requests
print """How to make requests
>> Google Finance: [API] getQuotes('GOOG') [REST] http://www.google.com/finance/info?q=NASDAQ:GOOG
>> Yahoo! Finance: [API] https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22BHP.AX%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback= [REST] http://finance.yahoo.com/d/quotes.csv?s=GOOG+AAPL&f=snl1

"""


# e.	Parsing responses
print """How to parse responses
>> Google Finance: json.dumps() <- API output in String
>> Yahoo Finance: json.load() <- API output in JSON format

"""

#####Part IV (For Pyglet projects only): Answer the following questions about the game or visual application you plan to write
# a.	Name
print """Name of your project or application:
>> Quant Trading - GetQuotes

"""

# b.	Description
print """Description of your project or application. If it is a game, how does it work? What is the goal? If it is an application, what is its purpose?
>> The purpose of my application is simply fetch stock trading data by using two APIs. Yahoo! Finance is able to provide more detailed trading information with 15 minutes delay whereas Google Finance provides live streaming data with no delay. By making use of both APIs, I could to produce a data sets for advanced data analysis or machine learning. This could potentially help me in Quant Trading in near future at no cost.

"""

# c.	Visual elements
print """What are the distinct types of visual elements present in your game or application? Describe what each one does, on a high level. 
>> I will be using matplotlib to render different graphs, including stock prices.

"""

# d.	Classes
print """Assuming you are using the pong game as a basic template, which classes will you have to modify, and how on a high level will you have to modify them?
If you are starting from scratch, what are the basic classes you will have to write to make your application work? Describe each one on a high level. 
>> Stock class. This class will be using two APIs to get stock prices and other information. This is the basic classes and the core for my application.

"""

#####Part V (For other kinds of projects only): Answer the following questions about the project you plan to do
# a.	Description
print """Description of your project. What does it do? 
>> Get live and historical data from two APIs and data will be visualized by using matplotlib.

"""

# b.	Impact
print """Why do you think this project is a useful or interesting thing to make?
>> This project is particularly interesting to me as I am interested in Quant trading. It is the first step for builing automated trading strategy. 

"""

# c.	Learning
print """How will this project reflect what we've learned in the class?
>> Mostly likely I will be using RESTful for Google Finance queries. I am still deciding. But API outputs will be in JSON format. Also, there're a couple of ways to get data from Yahoo! Finance, one of them is by getting elements in a csv file. All those data structures are relevent to class. 

"""

# d.	Code
print """ What are the basic components of your project going to be? This could be classes, but it could also be just chunks of code that do different things, or modules. 
Describe each component and how it works, on a high level.  
>> For each stock variable will be an instance of Stock class. I will be taking advantage of both Yahoo! Finance [getHistory()] and Google Finance [getPrice] for historical data and live data respectively. There'll be a global method called plot() which takes an instance of stock and render it graphically. Historical data set will be stored in a list and last traded price will be stored in a single variable.

"""


