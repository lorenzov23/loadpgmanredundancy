

#The idea is to create a new library to detect if a system belongs to redundant ones or not.

#The function takes in 2 parameters. One is the list of the red
#Algorithm flux

ENV_NAME = "UL1"


fil = open("redlist.txt","r")
appoggio = ''
uscita = False
while(fil.readline()!=""):
	appoggio = fil.readline()
	print appoggio
	if (appoggio == ENV_NAME):
		uscita = True
	appoggio = ""
fil.close()    
if(uscita==True):
	print("Redundant environment")
else:
	print("Non redundant environment")

exit 







