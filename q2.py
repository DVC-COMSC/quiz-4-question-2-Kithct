
# ******************************
# Make your Code
# ******************************
L = []
S = []
while True:
    n = input()
    if n == 'STOP':
        break
    if len(n) > len(L) or L == []:
        L = n
    elif len(n) < len(S) or S == []:
        S = n
print(L, S)
# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
