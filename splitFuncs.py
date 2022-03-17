def braceStrip(expression: str):
    expressionLocal = expression
    while True:
        if expressionLocal[0] == '(' and expressionLocal[-1] == ')':
            expressionLocal = expressionLocal.lstrip('(')
            expressionLocal = expressionLocal.rstrip(')')
        else:
            return expressionLocal


def splitPlusMinus(expression: str):
    braceCounter = 0
    for i in range(len(expression)):
        match expression[i]:
            case '(':
                braceCounter += 1
            case ')':
                braceCounter -= 1
            case ('+'|'-'):
                if braceCounter == 0:
                    left = braceStrip(expression[:i])
                    right = braceStrip(expression[i + 1:])
                    return [left, expression[i], right]
    return expression


def splitMulDiv(expression: str):
    braceCounter = 0
    for i in range(len(expression)):
        match expression[i]:
            case '(':
                braceCounter += 1
            case ')':
                braceCounter -= 1
            case ('*' | '/'):
                if braceCounter == 0:
                    left = braceStrip(expression[:i])
                    right = braceStrip(expression[i + 1:])
                    return [left, expression[i], right]
    return expression


def split(expression: str):
    result = splitPlusMinus(expression)
    if type(result) == list:
        result[0] = split(result[0])
        result[-1] = split(result[-1])
        return result

    result = splitMulDiv(expression)
    if type(result) == list:
        result[0] = split(result[0])
        result[-1] = split(result[-1])
        return result

    return result
