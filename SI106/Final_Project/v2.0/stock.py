#!/usr/bin/python
####### SI 106 Final Project #######
######## import lib here ###########
import urllib2, time, datetime, sys
import requests, json, numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import matplotlib
import matplotlib.animation as animation
from googlefinance import getQuotes
from matplotlib.finance import candlestick
matplotlib.rcParams.update({'font.size': 12})
import test106 as test
########## end of import ###########

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

class stock( object ):
  stock = None
  livePrice = None
  lastDateTime = None

  def __init__( self, stock, MA1=20, MA2=26 ):
    self.MA1 = MA1
    self.MA2 = MA2
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

  def movingAverage( self, values, window ):
    weights = np.repeat( 1.0, window ) / window
    smas = np.convolve( values, weights, 'valid' )
    return smas

  def animate( self, i ):
    try:
      print 'animating data on', self.stock 
      self.liveStock = getQuotes( self.stock )[0]
      self.livePrice = self.liveStock['LastTradePrice']
      self.lastDateTime = self.liveStock['LastTradeDateTime']
      print self.stock, self.livePrice, self.lastDateTime
    except Exception, e:
      print str(e), 'failed to pull price data'
    self.xarr.append( i )
    self.yarr.append( float(getQuotes( self.stock )[0]['LastTradePrice']) )
    self.liveAx1.clear()
    self.liveAx1.plot( self.xarr, self.yarr )
    plt.ylabel( 'Stock price' )
    plt.suptitle( self.stock + ' Stock Price' )

  def graphData( self, live=False ):
    try:
      x = 0
      y = len( self.date )
      candleArr = []
      while x < y:
        appendLine = self.date[x], self.openp[x], self.closep[x], \
                     self.highp[x], self.lowp[x], self.volume[x]
        candleArr.append( appendLine )
        x += 1

      Av1 = self.movingAverage( self.closep, self.MA1 )
      Av2 = self.movingAverage( self.closep, self.MA2 )

      SP = len( self.date[ self.MA2-1:] )

      label1 = str( self.MA1 ) + ' SMA'
      label2 = str( self.MA2 ) + ' SMA'

      fig = plt.figure( facecolor = '#07000d' )
      ax1 = plt.subplot2grid( (5, 4), (0, 0), rowspan=4, colspan=4, axisbg='#07000d' )
      candlestick( ax1, candleArr[-SP:], width=0.75, colorup='green', colordown='red' )

      ax1.plot( self.date[-SP:], Av1[-SP:], '#5998ff', label=label1, linewidth=1.0, alpha=0.8 )
      ax1.plot( self.date[-SP:], Av2[-SP:], '#5998ff', label=label2, linewidth=1.0, alpha=0.8 )

      ax1.grid( True, color = 'w' )
      ax1.xaxis.set_major_locator( mticker.MaxNLocator(10) ) # maximum 10 days show up
      ax1.xaxis.set_major_formatter( mdates.DateFormatter('%Y-%m-%d') )
      ax1.yaxis.label.set_color( 'w')
      ax1.spines['bottom'].set_color( '#5998ff' )
      ax1.spines['top'].set_color( '#5998ff' )
      ax1.spines['left'].set_color( '#5998ff' )
      ax1.spines['right'].set_color( '#5998ff' )
      ax1.tick_params( axis='y', colors='w')
      plt.ylabel( 'Stock price', color='w' )
      plt.legend( loc=3, fancybox=True, prop={'size':7} )

      volumeMin = 0

      ax2 = plt.subplot2grid( (5, 4), (4, 0), sharex = ax1, rowspan=1, colspan=4, axisbg='#07000d' )
      # ax2 = plt.subplot( 2, 1, 2, sharex = ax1 ) # sync with the first graph
      ax2.plot( self.date, self.volume, '#00ffe8', linewidth = 0.80 )
      ax2.fill_between( self.date, volumeMin, self.volume, facecolor = '#00ffe8', alpha = 0.50 )
      ax2.axes.yaxis.set_ticklabels([])
      ax2.grid( False )
      ax2.spines['bottom'].set_color( '#5998ff' )
      ax2.spines['top'].set_color( '#5998ff' )
      ax2.spines['left'].set_color( '#5998ff' )
      ax2.spines['right'].set_color( '#5998ff' )
      ax2.tick_params( axis='x', colors='w')
      ax2.tick_params( axis='y', colors='w')

      plt.ylabel( 'Volume', color='w')
      # for label in ax1.xaxis.get_ticklabels():
      # label.set_rotation( 45 ) # rotate label by 45 degree; easier to see
      for label in ax2.xaxis.get_ticklabels():
        label.set_rotation( 45 ) # rotate label by 45 degree; easier to see

      plt.xlabel( 'Date', color='w')
      plt.suptitle( self.stock + ' Stock Price', color='w')
      plt.setp( ax1.get_xticklabels(), visible = False )
      plt.subplots_adjust( left=0.09, bottom=0.14, right=0.95, top=0.94, wspace=0.20, hspace=0.00 )
      # print date
      plt.show()
      # fig.savefig('example.png', facecolor=fig.get_facecolor())
    except Exception, e:
      print 'failed main loop', str(e)

  def __str__( self ):
    print '------------'
    print 'Stock Info'
    print '------------'
    if self.stock == None:
      print 'No Stock Selected'
    else:
      print 'Stock name:', self.stock
    if self.livePrice == None:
      print 'No Last Live Stock Price'
    else:
      print 'Last Live Stock Price:', self.livePrice
    if self.lastDateTime == None:
      print 'No Last Live Query Time'
    else:
      print 'Last Live Query Time', self.lastDateTime

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

  def option( self ):
    print '======================================================='
    print 'OPTIONS:'
    print '\'quit\': to quit program'
    print '\'stock <STOCK>\': to fetch historical data for <STOCK>'
    print '\'status\': to get current query status'
    print '\'help\': to get list of options'
    print '\'test\': to test basic test cases'
    print '======================================================='

  def menu( self ):
    self.option()
    while True:
      try:
        line = raw_input('Z.K.> ')
        com = line.strip()
        if len( com ) == 0: continue
        elif com == 'quit': break
        elif com.split()[0] == 'stock':
          if len( com.split() ) != 2:
            print '** Usage: stock'
            sys.exit(1)
          else:
            if self.checkStock( com.split()[1] ):
              self.updateStatus( com.split()[1] )
            else:
              print '** ERR: Unrecognized stock: ', com.split()[1].upper()
              continue
            self.currentStock = com.split()[1].upper()
            if self.query == 'live':
              self.live()
            elif self.query == 'hist':
              self.hist()
            else:
              print '** ERR: Unrecognized command!'
        elif com == 'help': self.option()
        elif com == 'status': self.getStatus()
        elif com == 'test': self.test()
        else:
          print '** Unrecognized command:', com
      except EOFError:
        break
      except Exception, e:
        print 'ERR:', type(e), str(e)

  def checkStock( self, stock ):
    url_parameters = {'format': 'json'}
    baseurl = 'http://finance.yahoo.com/webservice/v1/symbols/'
    ending = '/quote?'
    fullurl = baseurl + stock + ending
    yahoo_finance_response = requests.get(fullurl, params=url_parameters)
    yahoo_finance_data = yahoo_finance_response.json()
    if len( yahoo_finance_data['list']['resources'] ) == 0:
      return False
    else:
      self.stock = stock
      return True
    return False

  def live( self ):
    print 'fetching live data for', self.stock
    currentStock = stock( self.currentStock )
    currentStock.liveFig = plt.figure( )
    currentStock.liveAx1 = currentStock.liveFig.add_subplot( 1, 1, 1 )
    currentStock.liveAx1.grid( True, color = 'b' )
    currentStock.xarr = []
    currentStock.yarr = []
    plt.ylabel( 'Stock price' )
    plt.suptitle( self.stock + ' Stock Price' )
    ani = animation.FuncAnimation( currentStock.liveFig, currentStock.animate, interval = 10000 )
    plt.show()
    return

  def hist( self ):
    print 'fetching historical data for', self.stock
    currentStock = stock( self.currentStock )
    currentStock.graphData()
    return

  def updateStatus( self, stock ):
    if stock in self.status:
      self.status[stock] += 1
    else:
      self.status[stock] = 1
  
  def getStatus( self ):
    top = []
    topCount = 0
    sortedStatus = sorted( self.status, key = self.status.get, reverse=True )
    if len( sortedStatus ) != 0:
      topCount = self.status[sortedStatus[0]]
      itemizedStatus = self.status.items()
      top = [ s[0] for s in itemizedStatus if s[1] == topCount ]
      # for stock in self.status:
      #   if self.status[stock] == topCount:
      #     top.append( stock )

    elif len( sortedStatus ) == 0:
    	print 'No query yet!'
    	return

    top = sorted( top )
    print 'Mostly queried stocks are:'
    print top
    print 'Total query count: ', topCount

  def __str__( self ):
    print 'Current Status:'
    getStatus()
    return

  def test( self ):
    self.test1()
    self.test2()
    self.test3()
    return

  def test1( self ):
    currentStock = stock( 'FB' )
    test.testEqual( currentStock.stock, 'FB', '** OK. test if stock name is correctly initialized.')
    return

  def test2( self ):
    test.testEqual( self.checkStock('ZZ'), False, '** OK. test if stock name is valid.' )
    return

  def test3( self ):
    self.updateStatus( 'GOOG' )
    test.testEqual( len( self.status ), 1, '** OK. test if status is updated.' )
    return

#--  Main  ---------------------------------------------------------------------

if __name__ == '__main__':
  args = sys.argv[1:]
  if len( args ) != 1:
    print '** Please read usage of stock.py: stock.py [ live | hist ]'
    sys.exit(1)
  if sys.argv[1] == 'live':
    main().menu()
  elif sys.argv[1] == 'hist':
    main().menu()
  else: 
    print '** Please read usage of stock.py: stock.py [ live | hist ]'
    sys.exit(1)
  
