## EECS388 Homework 2
## question 1:	breaking vigenere cipher 
## method:		kasiski
## assumption:	assuming the plain text is in English
 
## useful library
from sets import Set
from collections import Counter
import re

## define function that finds the factors of an integer
def factor(x):
	factorList = [];
	for i in range(2, x + 1):
	   if ( x % i == 0 ):
	   	factorList.append(i);
	return factorList;

# reset letter count
def reset():
	# letter count
	letterCount = { 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 
					'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 
					'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 
					'Y': 0, 'Z': 0 };
	return letterCount;

# shift letters l by i position
def shift( l, i ):
	LETTER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
	return LETTER[ (LETTER.find(l) + ( i % 26) ) % 26 ];


LETTER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';



# use English letter frequency in part 2
letter_dist = { 'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253, 'E': 0.12702, 
				'F': 0.02228, 'G': 0.02015, 'H': 0.06094, 'I': 0.06996, 'J': 0.00153, 
				'K': 0.00772, 'L': 0.04025, 'M': 0.02406, 'N': 0.06749, 'O': 0.07507, 
				'P': 0.01929, 'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056, 
				'U': 0.02758, 'V': 0.00978, 'W': 0.02360, 'X': 0.00150, 'Y': 0.01974, 
				'Z': 0.00074 };


## assign ciphertext
ciphertext = "GERGHDEVNIYMXQXUXGFPAXVVVOCBWGNUMDDXRVYBXOYRLWCGQIPNISRMQZNEWRYXVHEWCR"\
			"LRIISHCRPXFTIFMEWGOGRMRLTOAJIQTUJTPWNKZSHKSEXXSCCVNECMXRMFTSCJRGBGJHGS"\
			"GGBEUPLHNGRZNXMAZGFDRSPHCGIFEGHMSGASZXKVTGRSELSCAIBYRRKCVFTIWTQEAWNVXA"\
			"LNKVFTJEGXUHDTEEBFIHYWCXTHHGRVGWCGKEGBFBHCGHKZHNQYPARGSYXNVFBUGHRGKWPJ"\
			"MGRUOIYMAMVUGGXLTLHWCRGBTOIGSATERCMREXGISGEGBFBBMHRKEQGWTGHXFPNLLBEHTP"\
			"WRVKGIFIQBJQXNPVGVGDDQNMYSBYXVVJQDKTHMVFHAMRGTSPLHREVQIPMPTCSCEMAXVFXL"\
			"KZHUSGLGERGHDEVNIYMXQLRTMWAWFNLVRDLQNMYSBYXVVRZIFIBKPOCBGBFGIICVFVZSCA"\
			"ICKRQIGGRVIMERSTKRDWGGNEXCGGXUFJOGCHRLZUCCHNKFICBGBFGIIYXVHEOAFEEWESHQ"\
			"EFLLAERMBGJAPIMAZJIRFEYZFFXRLZLYOGBXBUISPIMAIIORRMPXSMPLCNWMSGQEERZHXQ"\
			"XUXFFTRMPTCZNNSFLZPACXBUISPIWHVYOHWWGXDPJRMGBJWCDINLZPACXBWFGDZCNGPYCM"\
			"AAIIORRMPTCATYRFVIMERSYHXMGCPNMVRICGUGFZDECUTJFPGWRWRBJKFRKFTACKNEZGHS"\
			"IFMYSTJIPMICCGGSKFBIGIEYFICBEGBFBLYWVGMCATIQBEORYWRBEHWCYABKSSQXNMVGLF"\
			"MPAHITQXVHESSULRMYSGPIDNZFXLKFNJDTAXRWTFXKMATCGIMTEHMWSCXUXZFSCGERGHXM"\
			"RXXPGIMPNPVBUMVPXDSCRMFNEQDLWGBKIIGSATCHWCISYRFVSIQMYOIRLVLZGPTMBERHXM"\
			"RBYKVTPMTAKCULSGUVWCEJBKTSSRSVGTFXKMATKSDLIFXCTPQKVOVBXLXUXWWURLNFVBSK";
## print ciphertext
# print(ciphertext);

## get the maximum possible length of key length
## maximum key length is the length of the cipher text
ciphertext_len = len(ciphertext);
# print(ciphertext_len);

## based on the theory on 
## http://www.cs.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-Kasiski.html
## suppose:
## 			1. k is the keyword length, then k must be a factor of the cipthertext_len
##			2. g is the distance between two matching substring, then g is a multiple of k

factorList = factor( ciphertext_len );

## Find repeating sequences and store distance
print	"Computing potential key length..." + \
		"It will take a while, please be patient...";
spaces_sequences = {};

## reference: http://inventwithpython.com/hacking/chapter21.html

# search for repeated string with length 3 and max factors of k
# almost brute force on guessing key length
# but not necessary as it's unlikely to have key length = length of the ciphertext
for k_prime in range(3, factorList[-1]):
    # iterate over each position of the ciphertext
    for sequence_start in range( 0, ciphertext_len - k_prime):
        # temporarily store substring
        substring = ciphertext[sequence_start : sequence_start + k_prime];
        # count number of times a substring appear in the ciphertext
        count = ciphertext.count( substring );
        # only calculate the distance if it appears more than once
        # ignore non-repeated terms
        if ( count > 1 ):
		        # search for the next matching substring in the ciphertext
		        for i in range(sequence_start + k_prime, ciphertext_len - k_prime):
		            if (ciphertext[i : i + k_prime] == substring):
		                # add entry for new sequence
		                if( substring not in spaces_sequences ):
		                	spaces_sequences[substring] = [];
		                # append the corresponding distance to the sequence spaces
		                spaces_sequences[substring].append(i - sequence_start);

# for substring, distance in spaces_sequences.items():
#     print "[+] Sequence: %s, Distance: %s" % (substring, str(distance))

# Calculate factors of distances
list_of_factors = {}
test = [];
for substring, list_of_distances in spaces_sequences.items():
    for distance in list_of_distances:
    	# obtained all distance of repeated substrings
        for factor in range(2, factorList[-1]):
        	# check if the distnace of repeated substrings is also a factor of the ciphertext
            if distance % factor == 0:
                if substring not in list_of_factors:
                    list_of_factors[substring] = [];
                # store factors
                # list_of_factors[substring].append(factor);
                test.append(factor);

# for substring, factors in list_of_factors.items():
    # print "[+] Sequence: %s, factors: %s" % (substring, str(factors))
counter = Counter(test);
k = counter.most_common(3)[0][0];

print "Possible key length: %d" % k;


## reference: http://www.cs.umd.edu/~waa/class-pubs/vigenere_ex1.txt
## reference: https://www.bucknell.edu/Documents/Engineering/MattBerntsen-thesis.pdf
print "Calculating possible key...";

## using regular expression to break ciphertext every 7 letters
ciphertext_formatted = re.findall('.......', ciphertext);
temp = '';
keyword = '';

# guess letter for each keyword
for z in range(0, k):
	for cf in ciphertext_formatted:
		temp = temp + cf[z];
		# print chr(ord('a'));

	# print temp;
	# print shift('Z', 25);
	letter = reset();

	# create a variance which takes only 0 - 1
	# get the shift number with optimal value
	var = 2.0;
	temp_var = 0.0;
	optimized_shift = 0;

	for j in range(0, 26):
		for i in LETTER:
			letter[i] = temp.count(shift(i,j))/(temp.__len__()*1.0);
			# print i + ' ' + str(letter[i]);
		for i in LETTER:
			temp_var = temp_var + (letter[i] - letter_dist[i]) ** 2;
		temp_var = temp_var / 26;
		# print temp_var;
		if ( temp_var < var ):
			var = temp_var;
			optimized_shift = j;
		temp_var = 0.0;

	keyword = keyword + LETTER[optimized_shift];
	temp = '';

print "The guessed keyword: %s " % keyword;


## ================== TESTS =================
# # a = Set();
# # a.add('b');
# # a.add('c');
# # a.add('b');
# for x in repeated_substring:
# 	print x;

# print( C[0:3] );
# print( C.count("GER") );
# print( C.find("GER") );

# for i in range(1, ciphertext_len):
# 	print("The factors of",ciphertext_len,"are:")
# 	factor(ciphertext_len);	

# 
# print(C.find('KZ'));
# print( C.count(C[:3],3) );