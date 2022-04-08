# from math import *
from splitFuncs import *
from tokens import *
from derivative import *


f = open("input.txt")

function = stringToTokens(f.readline().replace(' ', ''))

tree = tokenListToTree(function)

derivative = findDerivative(tree, 'x')
