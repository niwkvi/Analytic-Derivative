def stripOperation(left: list, operator: tuple, right: list):

    if operator[1] == '+' or operator[1] == '-':
        if len(right) == 1 and right[0] == ('number', '0'):
            return left
        elif len(left) == 1 and left[0] == ('number', '0'):
            return [operator, *right]
        else:
            return [*left, operator, *right]

    elif operator[1] == '*':
        if len(left) == 1 and left[0] == ('number', '0') or len(right) == 1 and right[0] == ('number', '0'):
            return [('number', '0')]
        elif len(left) == 1 and left[0] == ('number', '1'):
            return right
        elif len(right) == 1 and right[0] == ('number', '1'):
            return left
        else:
            return [*left, operator, *right]

    elif operator[1] == '/':
        if len(right) == 1 and right[0] == ('number', '0'):
            return None
        elif len(left) == 1 and left[0] == ('number', '0'):
            return [('number', '0')]
        elif len(right) == 1 and right[0] == ('number', '1'):
            return left
        else:
            return [*left, operator, *right]

    elif operator[1] == '^':
        if len(left) == 1 and left[0] == ('number', '1'):
            return ['number', '1']
        elif len(right) == 1 and right[0] == ('number', '0'):
            if len(left) == 1 and left[0] == ('number', '0'):
                return None
            else:
                return [('number', '1')]
        else:
            return [*left, operator, *right]


def findDerivative(tree: list, var: str) -> list:

    if len(tree) == 1 and (tree[0][0] == 'number' or tree[0][0] == 'constant'):
        return [('number', '0')]

    elif len(tree) == 1 and tree[0][0] == 'variable':
        return [('number', '0')] if tree[0][1] != var else [('number', '1')]

    elif len(tree) == 2:
        pass

    elif len(tree) == 3 and tree[1][0] == 'binary1':
        first = findDerivative(tree[0], var)
        second = findDerivative(tree[2], var)
        return stripOperation(first, tree[1], second)

    elif len(tree) == 3 and tree[0][0] == '(' and tree[2][0] == ')':
        inside = findDerivative(tree[1], var)
        return inside if len(inside) == 1 else [tree[0], *inside, tree[2]]

    elif len(tree) == 3 and tree[1][0] == 'binary2':
        pass
