# Scope = The region that a variable is recognised
# A variable is only available from inside the region it is created
# A global and locally scoped versions of a variable can be created

def disp_name():
    name = "Deez"
    print(name)
# The variable works only in this function (Local Scope)

disp_name()

# print(name)
# If I were to try the above, I would get an error

# ----------------------------------------------------------

name2 = "Nuts"
print(name2)
# This variable is available both inside and outside function (Global Scope)

#29/06/23