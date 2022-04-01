functionDict = {'sin', 'cos', 'tan', 'cot', 'sec', 'csc',
                'sinh', 'cosh', 'tanh', 'coth', 'sech', 'csch',
                'asin', 'acos', 'atan', 'acot', 'asec', 'acsc',
                'asinh', 'acosh', 'atanh', 'acoth', 'asech', 'acsch',
                'ln', 'log', 'exp', 'sqrt'}


def stringToTokens(expression: str) -> list | None:
   tokenList = []
   i = 0
   while i < len(expression):
      if expression[i] in ['(', ')']:
         tokenList.append((expression[i], None))
         i += 1
      elif expression[i] in ['+', '-']:
         tokenList.append(('binary1', expression[i]))
         i += 1
      elif expression[i] in ['*', '/']:
         tokenList.append(('binary2', expression[i]))
         i += 1
      elif expression[i] == '^':
         tokenList.append(('binary3', expression[i]))
         i += 1
      elif expression[i].isalpha():
         j = i + 1
         while j < len(expression) and expression[j].isalpha():
            j += 1
         word = expression[i:j]
         if word in ['e', 'pi']:
            tokenList.append(('constant', word))
         elif len(word) == 1:
            tokenList.append(('parameter', word))
         elif word in functionDict:
            tokenList.append(('function', word))
         else:
            return None
         i = j
      elif expression[i].isdigit():
         j, flag = i + 1, False
         while j < len(expression):
            if expression[j].isdigit():
               j += 1
            elif expression[j] == '.' and not flag:
               j += 1
               flag = True
            elif expression[j] == '.' and flag:
               return None
            else:
               break
         word = expression[i:j]
         tokenList.append(('number', word))
         i = j
   return tokenList
