#!/usr/bin/python
####### SI 106 Final Project #######
######## import lib here ###########
import urllib2
import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import matplotlib
from matplotlib.finance import candlestick
matplotlib.rcParams.update({'font.size': 12})
########## end of import ###########

eachStock = [ 'TSLA' ]

def movingaverage( values, window ):
  weights = np.repeat( 1.0, window )/window
  smas = np.convolve( values, weights, 'valid' )
  return smas

def graphData( stock, MA1, MA2 ):
  try:
    # stockFile = stock + '.txt'
    try:
      print 'pulling data on ', stock
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


    ( date, closep, highp, lowp, openp, volume ) = \
  		np.loadtxt( stockFile, delimiter=',', unpack=True, \
  		converters={ 0: mdates.strpdate2num('%Y%m%d')})
  	
    x = 0
    y = len( date )
    candleArr = []
    while x < y:
      appendLine = date[x], openp[x], closep[x], highp[x], lowp[x], volume[x]
      candleArr.append( appendLine )
      x += 1

    Av1 = movingaverage( closep, MA1 )
    Av2 = movingaverage( closep, MA2 )

    SP = len( date[ MA2-1:] )

    label1 = str(MA1) + ' SMA'
    label2 = str(MA2) + ' SMA'

    fig = plt.figure( facecolor = '#07000d' )
    ax1 = plt.subplot2grid( (5, 4), (0, 0), rowspan=4, colspan=4, \
                            axisbg='#07000d' )
    # ax1 = plt.subplot( 2, 1, 1 ) # (2,3,1) 2 by 3 position 1
    ## plot the following datas
    candlestick( ax1, candleArr[-SP:], width=0.75, colorup='green', \
                  colordown='red' )

    ax1.plot( date[-SP:], Av1[-SP:], '#5998ff', label=label1, linewidth=1.0, alpha=0.8)
    ax1.plot( date[-SP:], Av2[-SP:], '#5998ff', label=label2, linewidth=1.0, alpha=0.8)



    # ax1.plot( date, openp )
    # ax1.plot( date, highp )
    # ax1.plot( date, lowp )
    # ax1.plot( date, closep )

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

    # plt.figure()
    ax2 = plt.subplot2grid( (5, 4), (4, 0), sharex = ax1, rowspan=1, colspan=4, \
                            axisbg='#07000d' )
    # ax2 = plt.subplot( 2, 1, 2, sharex = ax1 ) # sync with the first graph
    ax2.plot( date, volume, '#00ffe8', linewidth = 0.80 )
    ax2.fill_between( date, volumeMin, volume, facecolor = '#00ffe8', \
                      alpha = 0.50 )
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

    # plot settings
    # plt.subplots_adjust( left=0.1, bottom=0.19, right=0.93, top=0.90,\
    # 					 wspace=0.2 , hspace=0.3)

    plt.xlabel( 'Date', color='w')
    plt.suptitle( stock + ' Stock Price', color='w')
    plt.setp( ax1.get_xticklabels(), visible = False )
    plt.subplots_adjust( left=0.09, bottom=0.14, right=0.95, top=0.94,\
		     wspace=0.20, hspace=0.00 )
    # print date
    plt.show()
    # fig.savefig('example.png', facecolor=fig.get_facecolor())

  except Exception, e:
  	print 'failed main loop', str(e)

while True:
  stockToUse = raw_input( 'Stock to chart: ' ) 
  graphData( stockToUse, 20, 26 )
  # time.sleep(100)  	
