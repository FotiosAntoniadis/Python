# Module = a file containing python code. May contain function, slasses, etc.
# used with modular programming, which is to separate a program into parts

# 1st Way
import Modules_Test as mdlt

mdlt.Hello()

mdlt.Bye()

print("------------------------------------------")

# 2nd Way
from Modules_Test import Hello, Bye

Hello()
Bye()

print("------------------------------------------")

# 3rd Way
from Modules_Test import *
#                        ^
#                 * = all modules

Hello()
Bye()

print("------------------------------------------")

# List of pre-fixed modules on Python

help("modules")

#03/07/23