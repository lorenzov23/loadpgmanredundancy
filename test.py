# The idea is to create a new library to detect if a system belongs to redundant ones or not.

# The function takes in 2 parameters. One is the list of the red
# Algorithm flux

from pprint import pprint
import logging

# logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger().setLevel(logging.INFO)

PATH = 'redlist.txt'
UAT = 'UATLIST.txt'
ENV_NAME = 'UL9'
COMPONENTS = 'components.txt'



def is_redundant(env_name, path):
    # type: (object, object) -> object
    from pprint import pprint
    result = False
    with open(path) as f:
        for line in f.readlines():
            pprint(line.strip())
            if env_name in line.strip():
                result = True
            if result:
                print("Redundant environment")
            else:
                print("Non redundant environment")
    return result


def get_components_list(path):
    components = []
    with open(path) as f:
        lines = f.readlines()
        if len(lines) < 5:
            logging.error("Not enough lines")
            return components

        for line in lines[4::]:
            parts = line.split()
            if len(parts) is 4:
                logging.debug("This line is good: {}".format(parts))
                components.append(parts[2])
            else:
                logging.warn("This line is garbage: {}".format(parts))

            # pprint(line.strip().split())
    return components


def is_UAT(env_name, uat):

    from pprint import pprint
    result = False
    with open(uat) as f:
        for line in f.readlines():
            pprint(line.strip())
            if env_name in line.strip():
                result = True
            if result:
                print("UAT")
            else:
                print("Non UAT")
    return result

def contain_common_code(components_to_be_loaded):
    # type: (object) -> object
    components_from_file = get_components_list('components.txt')

    for comp in components_to_be_loaded:
        if comp in components_from_file:
            logging.info("Component to be loaded {} is in the list".format(comp))
            return True
    return False


if __name__ == '__main__':
    # is_redundant(ENV_NAME, PATH)
    # pprint(get_components_list('components.txt'))
    pprint(contain_common_code(['compon14', 'balbalaldsfs']))

    #In this part I will consider all the 4 possible cases
    # 1 mixed code (common and alternable) NON REDUNDANT
    # 2 alternable code only NON REDUNDANT
    # 3 mixed code (common and alternable) REDUNDANT
    # 4 alternable code only REDUNDANT
    # In cases 1 the script must warn the user and tell that we are going to load on NON REDUNDANT environment containing common code
    # In case 2 the script must continue its work without any change
    # In case 3 we SHOULD PERFORM REDUNDANT SYSTEMS maintenance
    # In case 4 as in case 2 there is no special thing to do
    # Let's build up all the cases
    a = contain_common_code(get_components_list(COMPONENTS))
    b = is_redundant(ENV_NAME, PATH)
    c = is_UAT(ENV_NAME, UAT)
    if a and not b:

        if c:
            print "WARNING: YOU ARE GOING TO LOAD COMMON CODE ON NON REDUNDANT UAT SYSTEM"


                #check via ssh commands that the environments we are going to load on have been already scheduled for maintenance

    if not a and not b:
            print "I am loading without any issue"

    if a and b:
        #going to execute maintenance operations
        print "Going to execute maintenance operations"
            #first individuate the machtype
            #second read the list of commands to be used to do maintenance
            #perform the commands

    if not a and b:

            print "I am loading without any issue"



























