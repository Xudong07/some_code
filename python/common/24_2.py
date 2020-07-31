from  itertools import permutations
dict_char_2_num={'A': '1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', '10':'10', 'J':'11', 'Q':'12','K':'13'}
def compare(op1, op2):
    """
    比较两个运算符的优先级,乘除运算优先级比加减高
    op1优先级比op2高返回True，否则返回False
    """
    return op1 in ["*", "/"] and op2 in ["+", "-"]
 
def getvalue(num1, num2, operator):
    """
    根据运算符号operator计算结果并返回
    """
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    else:  # /
        return num1 / num2
 
 
def process(data, opt):
    """
    opt出栈一个运算符，data出栈两个数值，进行一次计算，并将结果入栈data
    """
    operator = opt.pop()
    num2 = data.pop()
    num1 = data.pop()
    if isinstance(num2, str):
        num2 = int(dict_char_2_num[num2])
    if isinstance(num1, str):
        num1 = int(dict_char_2_num[num1])
    data.append(getvalue(num1, num2, operator))

 
 




def calculate(s):
    """
    计算字符串表达式的值,字符串中不包含空格
    """

    data = []  # 数据栈
    opt = []  # 操作符栈
    i = 0  # 表达式遍历索引
    while i < len(s):
        if s[i].isdigit() or s[i] in ['A', 'K', 'J', 'Q']:  # 数字，入栈data
            data.append(s[i])  # i为最后一个数字字符的位置
        elif not opt:  # 操作符栈为空，或者操作符栈顶为左括号，操作符直接入栈opt
            opt.append(s[i])
        else:  # 优先级不比栈顶操作符高时，opt出栈同时data出栈并计算，计算结果如栈data
            while opt:
                process(data, opt)
            opt.append(s[i])
        i += 1  # 遍历索引后移
    while opt:
        process(data, opt)
    return data.pop()
 





def is_24(num1,obj):
    opt_list = ['+','-','*',"/"]
    if 'joker' in num1 or 'JOKER' in num1:
        return "ERROR"
    #new_num = [dict_char_2_num[num1[i]] for i in range(len(num1))]
    num_all = list(permutations(num1, len(num1)))
    for num in num_all:
        for op1 in opt_list:
            for op2 in opt_list:
                for op3 in opt_list:
                    s = num[0]+op1+num[1]+op2+num[2]+op3+num[3]
                    finv = calculate(s)
                    if(abs(finv-obj)<1.0e-12):
                        return s
    return 'NONE'



try:
    while(True):
        num = input()
        if not num:
            break
        num =num.split()
        print(is_24(num,24.0))
except:
    pass