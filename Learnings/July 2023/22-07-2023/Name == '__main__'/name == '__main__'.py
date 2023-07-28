# Python interpreter sets "special variables", one of which is __name__
# Python wll assign the __name__ variable a value of '__main__' if it's the initial module being run
#
# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules
#
# Basically, "name == '__main__'" is used to see if the user uses the module as standalone program or as an
# imported module used by other modules

import NameMainTest
print(__name__)
print(NameMainTest.__name__)

if __name__ == '__main__':
    print("Running this module directly")
else:
    print("Running other module indirectly")

NameMainTest.hello()

# 22/07/23