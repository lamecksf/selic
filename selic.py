#!/usr/bin/python
#SELIC CALCULATOR

import sys, getopt, os
import mInit
import data

def main(argv):

	#os.system("clear")
	

	try:
		opts, args = getopt.getopt(argv,'i:h', [
												'h',
												'help',			
												'rate=',
												'inv=',
												'month=',
												'acc=',												
												])
	except getopt.GetoptError as err:
		print err
		sys.exit(2)


	for opt, arg in opts:

		if opt in ('-h','--help'):
			mInit.helper()
			sys.exit()
		
		elif opt in ('--rate'):
			data.setRate(arg)			

		elif opt in ('--inv'):
			data.setInv(arg)						

		elif opt in ('--month'):
			data.setMonth(arg)

		elif opt in ('--acc'):
			data.Selic(arg)
			

if __name__ == "__main__":
   main(sys.argv[1:])
