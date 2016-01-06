#!/usr/bin/python
####### SI 106 Final Project #######
######## import lib here ###########
import urllib2
import time
import datetime
########## end of import ###########

#### Please put your name here! ####
sname = "Zijie Ku"
print sname # this is a helpful double-check for us when we are grading
print 

stocksToPull = [ 'AAPL', 'GOOG', 'MSFT', 'CMG', 'AMZN', 'EBAY', 'TSLA' ]

def pullData( stock ):
  try:
   #  ### First version
   #  fileLine = stock + '.txt'
   #  # include the basisc url
   #  urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/' \
		 # + stock + '/chartdata;type=quote;range=1y/csv'
   #  # visit the site and get all data
   #  sourceCode = urllib2.urlopen(urlToVisit).read()
   #  # split data by newline
   #  splitSource = sourceCode.split('\n')
    
   #  for eachLine in splitSource:
   #    splitLine = eachLine.split(',')
   #    if len(splitLine) == 6:
   #      if 'values' not in eachLine:
   #      # append data to the file not write to it
   #        saveFile = open(fileLine, 'a')
   #        lineToWrite = eachLine + '\n'
   #        saveFile.write( lineToWrite )
   #  print 'Pulled', stock
   #  print 'Done.... sleeping'
   #  time.sleep(1)

    print 'Currently pulling', stock
    # print str( datetime.datetime.fromtimestamp( time.time() ).strftime('%Y-%m-%d %H:%M:%S') )
    urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/' \
                + stock + '/chartdata;type=quote;range=1y/csv'
    saveFileLine = stock + '.txt'

    try:
      # fail if the file does not exist
      readExistingData = open( saveFileLine, 'r' ).read()
      splitExisting = readExistingData.split('\n')
      mostRecentLine = splitExisting(-2)
      lastUnix = mostRecentLine.split(',')[0]
    except Exception, e:
      # print str(e)
      # time.sleep(1)
      lastUnix = 0

    saveFile = open( saveFileLine, 'a' )
    sourceCode = urllib2.urlopen( urlToVisit ).read()
    splitSource = sourceCode.split('\n')

    for eachLine in splitSource:
      if 'values' not in eachLine:
        splitLine = eachLine.split(',')
        if len( splitLine ) == 6:
          if int( splitLine[0] ) > int( lastUnix ):
            lineToWrite = eachLine + '\n'
            saveFile.write( lineToWrite )

    saveFile.close()

    print 'Pulled', stock
    print str( datetime.datetime.fromtimestamp( time.time() ).strftime('%Y-%m-%d %H:%M:%S') )

    
  except Exception, e:
    print 'main loop', str(e)

while True:
  for eachStock in stocksToPull:
    pullData( eachStock )
  print 'sleep....'
  time.sleep( 300 ) # 5 minutes
