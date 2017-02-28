import locale

#GLOBAL
rate = ""
inv = ""
year = ""
month = ""
day = ""
verbose = ""




#SETTERS
def setRate(rt):
	global rate 
	rate = rt

def setInv(iv):
	global inv 
	inv = iv

def setYear(yr):
	global year
	year = yr

def setMonth(mo):
	global month
	month = mo

def setDay(dy):
	global day
	day = dy

def setVerbose(vb):
	global verbose
	verbose = vb



#GETTERS
def getRate():
	return rate

def getInv():
	return inv

def getYear():
	return year

def getMonth():
	return month

def getDay():
	return day

def getAll():
	return rate+" - "+inv+" - "+day+" - "+month+" - "+year

def getVerbose():
	return verbose


#FUNCTIONS
def Selic(opt):
	ret = ""	
	count = 0
	poupanca = getInv()
	dia = 1
	mes = 1
	ano = 0

	locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

	if opt == 'n':
		

		while count < int(getMonth()):

			ret = "Ano: "+str(ano)+" | Mes: "+str(mes)+" --- "
			ret += "Poupanca: "+poupanca+" | "
			juros = round((float(poupanca) * float(getRate()))/100,2)
			ret += "juros: "+str(juros)
			poupanca = str(round(float(poupanca) + juros,2))
								
			if mes == 13:
				ano = ano + 1
				mes = 1

			mes = mes + 1

			print ret
			count = count + 1
		else:
			print "\n--------------------------------------------------------"
			print "[valor nao acumulado]"
			FS = locale.currency(float(getInv()), grouping=True, symbol=None)
			DF = locale.currency(float(poupanca) - float(getInv()), grouping=True, symbol=None)
			printElse(ano,mes,poupanca,FS,DF)
	

	if opt == 'y':
		
		while count < int(getMonth()):

			ret = "Ano: "+str(ano)+" | Mes: "+str(mes)+" --- "
			ret += "Poupanca: "+poupanca+" | "
			juros = round((float(poupanca) * float(getRate()))/100,2)
			ret += "juros: "+str(juros)
			poupanca = str(round(float(poupanca) + juros,2)+float(getInv()))
								
			if mes == 13:
				ano = ano + 1
				mes = 1

			mes = mes + 1

			print ret
			count = count + 1
		else:
			print "\n--------------------------------------------------------"			
			print "[valor acumulativo]"
			FS = "["+getInv()+"*"+getMonth()+"] : R$ "+locale.currency((float(getInv())*int(getMonth())), grouping=True, symbol=None)
			DF = locale.currency((float(poupanca) - ( float(getInv())*int(getMonth()) ) ), grouping=True, symbol=None)
			printElse(ano,mes,poupanca,FS,DF)

	
def printElse(ano,mes,poupanca,FS,DF):
	
	p = "Em "+str(ano)+" anos e "+str(mes-1)+" meses\n"
	p += "\nInvestimento: R$ "+locale.currency(float(getInv()), grouping=True, symbol=None)
	p += "\nRendimento: R$ "+locale.currency((float(poupanca) - float(getInv())), grouping=True, symbol=None)	   		
	p += "\nTotal: R$ "+locale.currency(float(poupanca), grouping=True, symbol=None)
	p += "\n\nFora da selic "+FS
	p += "\nCom a selic: R$ "+locale.currency(float(poupanca), grouping=True, symbol=None)
	p += "\nDiferenca : R$ "+DF
	
	print p
