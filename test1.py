

#The idea is to create a new library to detect if a system belongs to redundant ones or not.

#The function takes in 2 parameters. One is the list of the red
#Algorithm flux

ENV_NAME = "UL3"
#definition of the array containing components to be loaded
array('Comp1','Comp2','Comp3','Comp4')

from pprint import pprint

fil = open("redlist.txt","r")
result = False

with open('redlist.txt') as f:
	for line in f.readlines():
		pprint(line.strip())
		if ENV_NAME in line.strip():
			result = True
if result:
	print("Redundant environment")
else:
	print("Non redundant environment")
exit
















