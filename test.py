

#The idea is to create a new library to detect if a system belongs to redundant ones or not.

#The function takes in 2 parameters. One is the list of the red
#Algorithm flux
from xmlrpclib import boolean

PATH = 'redlist.txt'
ENV_NAME = 'UL1'


def is_redundant(ENV_NAME, PATH):
   from pprint import pprint
   fil = open(PATH,"r")
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
   return result

if __name__ == '__main__':

    if(is_redundant(ENV_NAME, PATH)):
        print 'ridondante'
    else:
        print 'non ridondante'

exit








#parse the txt file containing the list of components in such a way to manage it line by line.
















