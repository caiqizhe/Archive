Final Project – README Template
I. Type of project (delete those that do not apply): 
1) API project



II. Brief description of project:
Both Yahoo! Finance and Google Finance APIs are used. 
There’re two options available when launching the application.
(1) python stock.py live
(2) python stock.py hist
The ‘live’ argument provides a simple user interface that renders stock 
price using Google Finance API, which has 0 second delay. However, to make
the plot more informative, time interval is set to 10 second. 
Live market data is available from Mon to Fri after 9:30 AM to 4:00 PM EST.
The ‘hist’ argument provides a sophisticated user interface that renders
historical stock price using Yahoo! Finance API. To make the plot more
informative, volume and two moving averages are plotted on the graph as well.
For both arguments, there will be a option menu printed out. 
Once the plot is closed, another plot can be generated in the terminal.
‘Status’ will return the most queried stocks in one single session.
Yahoo! Finance API is called using REST
Google Finance is called using python API
Please be patient when plotting Live data since the time interval is every 10 seconds.



III. List of files being turned in, with a brief description of each one:
hist-plot.png: historical stock plot example
hist-terminal.png: historical stock terminal example
live-plot.png: live stock plot example
live-terminal.png: live stock terminal example



IV. Python packages/modules that need to be installed (e.g. BeautifulSoup):
urllib2, time, datetime, sys, requests, json, numpy, matplotlib, googlefinance,




V. Instructions for running/using/playing project:
For example:
-- python myproj.py
-- when it asks for a city to search on, enter a three-digit airport code like DTW

python stock.py [ live | hist ]
following option will be printed out
-----------------------------
SI 106 - Final Project
presented to you by ZIJIE KU
-----------------------------
=======================================================
OPTIONS:
'quit': to quit program
'stock <STOCK>': to fetch historical data for <STOCK>
'status': to get current query status
'help': to get list of options
=======================================================
Z.K.> stock GOOG # to plot historical or live data for Google
Z.K.> stock ZZ 
** ERR: Unrecognized stock: ZZ # if any unknown stock, an error message will be printed out
Z.K.> quit # program will exit peacefully




VI. Data sources used (for API projects only):
(1) Google Finance
(2) Yahoo! Finance




VII. Approximate line numbers in main python file to find following components (if they occur in another code file, note this):

Accumulation pattern
# Line 223
To keep currently most queried stocks.

Sort with a key function	
# Line 232
To sort currently most queried stocks by its query counts.

Class definition
# ...etc.
__init__() method for this class	
# Line 20, 136

class stock( object ):
  def __init__( self, stock, MA1=20, MA2=26 ):
    self.stock = stock
    try:
      print 'pulling data on', self.stock 
      urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/' \
                + stock + '/chartdata;type=quote;range=1y/csv'
      stockFile = []
      try:
        sourceCode = urllib2.urlopen(urlToVisit).read()
        splitSource = sourceCode.split('\n')
        for eachLine in splitSource:
          splitLine = eachLine.split(',')
          if len(splitLine) == 6:
            if 'values' not in eachLine:
              stockFile.append( eachLine )
      except Exception, e:
        print str(e), 'failed to organize pulled data'
    except Exception, e:
      print str(e), 'failed to pull price data'

    ( self.date, self.closep, self.highp, self.lowp, self.openp, self.volume ) = \
        np.loadtxt( stockFile, delimiter=',', unpack=True, \
     	converters={ 0: mdates.strpdate2num('%Y%m%d')})

class main( object ):
  def __init__( self ):
    self.status = {}
    self.query = sys.argv[1]
    self.sName = 'Zijie Ku'.upper()
    self.currentStock = ''
    print "-----------------------------"
    print "SI 106 - Final Project"
    print "presented to you by " + self.sName
    print "-----------------------------"


First method for this class	
# checkStock(stock)
# Line 189
To check whether the Stock ticker is valid.
It returns True if Stock is a valid stock, False if it doesn’t

Second method for this class	
# menu()
# Line 155
A while-loop, which keeps prompting the user for inputs. 

Importation of a python module, either built-in or third-party	
matplotlib is the core python module here as it helps to render the data, 
which makes the data useful and interesting to analyst.

Use of this module in the code:	
# Line 85 to 130

Use of list comprehension OR map OR filter	
# Line 261
To get all stock name with the same number to top query counts.
{ ‘GOOG’: 3, ‘FB’:3, ‘EBAY’:1 }
[ ‘GOOG’, ‘FB’ ] should be returned because they have the same top query counts.

Definitions of 5 functions or methods (can include class methods above)	
# 1 option
# 2 menu
# 3 checkStock
# 4 live
# 5 hist
# 6 updateStatus
# 7 getStatus

Test cases for at least three functions or methods	
# 1 please refer to screenshot: test_case_0.png for unrecognized stock
# 2 test1(): test if stock name is successfully initialized.
# 3 test2(): test if stock name is verified against Yahoo! Finance.
# 4 test3(): test if status is updated.




VIII. Rationale for project; why did you do this project? Why do you find it interesting?
I want to do Quant analysis. Python has many powerful lib or APIs. I choose to do this 
final project because python is easy to code and provide GUI to users. It’s interesting 
because once I break the program into different classes and modules, I can start add in 
more features along the way. Other indexes such as RSI can be added by just modifying the 
current code. The basic framework and structure remain untouched.
