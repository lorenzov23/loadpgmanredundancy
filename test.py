# The idea is to create a new library to detect if a system belongs to redundant ones or not.

# The function takes in 2 parameters. One is the list of the red
# Algorithm flux
from xmlrpclib import boolean

from pprint import pprint
import logging

# logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger().setLevel(logging.INFO)

PATH = 'redlist.txt'
ENV_NAME = 'UL9'


def is_redundant(env_name, path):
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


def contain_common_code(components_to_be_loaded):
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

