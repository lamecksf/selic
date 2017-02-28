
version = 'sel 0.1'

<<<<<<< HEAD
idef helper():
	hp = '\n'+'%24s'%'Selic Calculator '+version+' (c) 2017 Lameck\n'
	hp += '%37s'%'https://github.com/lamecksf/selic\n\n'
=======
def helper():
	hp = '\n'+'%24s'%'Selic Calculator '+version+' (c) 2017 Lameck\n'
	hp += '%37s'%'https://github.com/lamecksf/\n\n'
>>>>>>> 344871c552e45c5ba786e42b5f0223f5eb47d97f
	hp += '%39s'%'usage: python selic.py [options]'

	hp += '\n\n'+'%50s'%'##########################################\n'
	hp += '%39s'%'SELIC CALCULATOR:\n'
	hp += '%51s'%'##########################################\n\n'

	hp += '%20s'%'--rate %15s'%'Interest rate per month\n'
	hp += '%19s'%'--inv %15s'%'Investment \n'
	hp += '%21s'%'--month %15s'%'Number of Month \n'
	hp += '%25s'%'--acc <n|y> %15s'%'Accumulative yes or no \n\n'

	hp += '%64s'%'python selic.py --rate 0.5 --inv 570 --month 12 --acc y \n'
	
	
	print hp


