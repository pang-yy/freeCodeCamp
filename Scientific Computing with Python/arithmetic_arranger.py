def arithmetic_arranger(problems, calculate=False):
    # check number of problems
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        first_num = []
        operator =[]
        last_num = []
        for problem in problems:
            l = problem.split(' ')
            first_num.append(l[0])
            operator.append(l[1])
            last_num.append(l[2])
        # check operator
        for o in operator:
            if o != '+' and o != '-':
                return "Error: Operator must be '+' or '-'."
        # check number
        for num in (first_num+last_num):
            if num.isdigit():
                if len(num) > 4:
                    return "Error: Numbers cannot be more than four digits."
            else:
                return "Error: Numbers must only contain digits."
        
        # process
        first_line = '' # num 1
        second_line = '' # operator, num 2
        third_line = '' # dash
        forth_line = '' # answer (optional)
        space = 0
        for i in range(len(first_num)):
            space = len(str(max(int(first_num[i]), int(last_num[i])))) + 2

            first_line += ' '*(space-len(first_num[i])) + first_num[i] + ' '*4
            second_line += operator[i] + ' '*(space-1-len(last_num[i])) + last_num[i] + ' '*4
            third_line += '-'*space + ' '*4

            if calculate == True:
                if operator[i] == '+':
                    ans = str(int(first_num[i]) + int(last_num[i]))
                else:
                    ans = str(int(first_num[i]) - int(last_num[i]))
                forth_line += ' '*(space-len(ans)) + ans + ' '*4
        
        return (first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + third_line.rstrip() + '\n' + forth_line.rstrip()).rstrip()



arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

