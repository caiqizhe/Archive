#Author: Brandon Mendrick and Zijie Ku
#Produced for EECS 388 project 3

import sys, dpkt

def tcpFlags(flag): #returns 1 if it is SYN, 2 if SYN+ACK, 0 otherwise
	syn_flag = (flag & dpkt.tcp.TH_SYN) != 0
	ack_flag = (flag & dpkt.tcp.TH_ACK) != 0

	if syn_flag and not ack_flag:
		return 1
	if syn_flag and ack_flag:
		return 2

	return 0
	
def ipDecode(r): #decodes an ip address into ascii characters
	return ".".join(["%d" % ord(x) for x in str(r)])
	#I am using this class as is from bytes.com
	
class tcpStruct(): #struct used for storing ip's (name makes no sense for some reason?)
	def __init__(self, source, scount, acount):
		self.source = source
		self.scount = scount
		self.acount = acount

#START OF CODE
f = open(str(sys.argv[1])) #opening the pcap file
pcap = dpkt.pcap.Reader(f) #using dpkt to read the file

#setting up a list for later
sources = []

#iterating through all packets in the pcap file
for ts, buf in pcap:
	try:
		valid = 0
		eth = dpkt.ethernet.Ethernet(buf)
		ip = eth.data
		tcp = ip.data
		
		#checking if the source ip has already been seen
		#if so then we increment the appropraite variables if needed
		for i in sources:
			if ip.src == i.source and tcpFlags(tcp.flags) == 1:
				i.scount = i.scount + 1
				valid = 1
				break
			if ip.dst == i.source and tcpFlags(tcp.flags) == 2:
				i.acount = i.acount + 1
				valid = 1
				break
		
		#case in which the source ip has not been seen before
		#we simply define a new member to the source list
		if valid == 0 and tcpFlags(tcp.flags) != 0:
			if tcpFlags(tcp.flags) == 1:
				sources.append(tcpStruct(ip.src, 1, 0))
			else:
				source.append(tcpStruct(ip.dst, 0, 1))
		
	except:
		continue
		
#determining/printing the sources meeting the requirements
for ele in sources:
	if ele.acount == 0 and ele.scount != 0:
		print ipDecode(ele.source)
		continue
	if (ele.scount/ele.acount) > 3.0:
		print ipDecode(ele.source)

f.close()
