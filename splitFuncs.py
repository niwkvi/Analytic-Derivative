from tokens import *


def splitBraces(tokenList: list) -> (list, bool):
    if tokenList[0][0] == '(' and tokenList[-1][0] == ')':
        return [('(', None), tokenList[1:-1], (')', None)], True
    return tokenList, False


def splitBinaryOperation(tokenList: list, priority: int) -> (list, bool):
    braceCounter = 0
    for i in range(len(tokenList)):
        if tokenList[i][0] == '(':
            braceCounter += 1
        elif tokenList[i][0] == ')':
            braceCounter -= 1
        elif tokenList[i][0] == 'binary' + str(priority):
            if braceCounter == 0:
                if priority == 1 and i == 0:
                    return [[('number', '0')], tokenList[i], tokenList[i + 1:]], True
                return [tokenList[:i], tokenList[i], tokenList[i + 1:]], True
    return tokenList, False


def splitFunction(tokenList: list) -> (list, bool):
    if tokenList[0][1] in functionDict:
        return [tokenList[0], tokenList[1:]], True
    return tokenList, False


def tokenListToTree(tokenList: list) -> list:
    result, isSplit = splitBinaryOperation(tokenList, 1)
    if isSplit:
        result[0] = tokenListToTree(result[0])
        result[-1] = tokenListToTree(result[-1])
        return result

    result, isSplit = splitBinaryOperation(tokenList, 2)
    if isSplit:
        result[0] = tokenListToTree(result[0])
        result[-1] = tokenListToTree(result[-1])
        return result

    result, isSplit = splitBinaryOperation(tokenList, 3)
    if isSplit:
        result[0] = tokenListToTree(result[0])
        result[-1] = tokenListToTree(result[-1])
        return result

    result, isSplit = splitFunction(tokenList)
    if isSplit:
        result[1] = tokenListToTree(result[1])
        return result

    result, isSplit = splitBraces(tokenList)
    if isSplit:
        result[1] = tokenListToTree(result[1])
        return result

    return result
