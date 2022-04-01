def braceStrip(tokenList: list):
    tempTokenList = tokenList[:]
    while True:
        if tempTokenList[0][0] == '(' and tempTokenList[-1][0] == ')':
            tempTokenList = tempTokenList[1:-1]
        else:
            return tempTokenList


def splitBinaryOperation(tokenList: list, priority: int) -> (list, bool):
    braceCounter = 0
    for i in range(len(tokenList)):
        if tokenList[i][0] == '(':
            braceCounter += 1
        elif tokenList[i][0] == ')':
            braceCounter -= 1
        elif tokenList[i][0] == 'binary' + str(priority):
            if braceCounter == 0:
                left = braceStrip(tokenList[:i])
                right = braceStrip(tokenList[i + 1:])
                return [left, tokenList[i], right], True
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

    return result
