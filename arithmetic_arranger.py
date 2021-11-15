import re

def arithmetic_arranger(problems, answer = False):

    # Error checking

    if len(problems) < 1: return 'Error: No problem found'
    if len(problems) > 5: return 'Error: Too many problems.'

    for item in problems:

        matchtest1 = re.fullmatch('\s*.+\s*\+\s*.+\s*', item)
        matchtest2 = re.fullmatch('\s*.+\s*-\s*.+\s*', item)

        if matchtest1 != None or matchtest2 !=  None: pass
        else: return "Error: Operator must be '+' or '-'."

        if '+' in item:
            numbers = item.split('+')
            for number in numbers:
                number = number.strip()
                if not number.isdigit():
                    return 'Error: Numbers must only contain digits.'
                if len(number) > 4:
                    return 'Error: Numbers cannot be more than four digits.'
        else:
            numbers = item.split('-')
            for number in numbers:
                number = number.strip()
                if not number.isdigit():
                    return 'Error: Numbers must only contain digits.'
                if len(number) > 4:
                    return 'Error: Numbers cannot be more than four digits.'

    # Formatting starts from here

    firstproblem = True
    for question in problems:
        if '+' in question:
            op = '+'
            pieces = question.split('+')
        else:
            op = '-'
            pieces = question.split('-')
        num1 = pieces[0].strip()
        num2 = pieces[1].strip()
        no1 = int(num1)
        no2 = int(num2)
        if op == '+': ans = str(no1 + no2)
        else: ans = str(no1 - no2)

        width = max(len(num1), len(num2))

        if firstproblem == True:
            row1 = num1.rjust(width + 2)
            row2 = op + ' ' + num2.rjust(width)
            row3 = '-' * (width + 2)
            if answer == True: row4 = ans.rjust(width + 2)
            firstproblem = False
        else:
            row1 += num1.rjust(width + 6)
            row2 += '    ' + op + ' ' + num2.rjust(width)
            row3 += '    ' + '-' * (width + 2)
            if answer == True: row4 += ans.rjust(width + 6)

    if answer == True: return row1 + '\n' + row2 + '\n' + row3 + '\n' + row4
    return row1 + '\n' + row2 + '\n' + row3
