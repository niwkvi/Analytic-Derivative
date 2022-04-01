# from math import *
from splitFuncs import *
from tokens import *

f = open("input.txt")

function = stringToTokens(f.readline().replace(' ', ''))

print(tokenListToTree(function))
