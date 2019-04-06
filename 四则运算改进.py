import random
from fractions import Fraction
operation = ['+', '-', '*', '/']   #四则运算的符号
global f

def judge(f, ch):
    p1 = -1        #左括号的左符号
    p2 = -1        #右括号的右符号
    que = []       #判断各组符号是否为有用，False为无用，True为有用
    for k, i in enumerate(ch):
        p = []                      #存储括号中的符号
        if i == '(' and k == 0:    #开始出现括号
            for j in range(1, len(ch)):
                if ch[j] != '(' and ch[j] != ')' and ch[j] >= 0:
                    p.append(ch[j])   #ch[j]为括号中间的符号
                elif ch[j] == ')':
                    for n in range(j + 1, len(ch)):
                        if ch[n] != ')' and ch[n] >= 0:
                            p2 = ch[n]     #右括号的符号
                            break
                        else:
                            continue
                    break
                else:
                    continue
            #分两种情况，判断中间的括号的符号有几个符号
            if len(p) == 1:                            #括号中间只有一个符号时
                if (p[-1] == 0 or p[-1] == 1) and (p2 == 0 or p2 == 1):  #括号中间符号为—或+时，右括号右边为—或+，为无用括号
                    que.append(False)
                elif (p[-1] == 2 or p[-1] == 3):    #括号中间符号为*或/时，为无用括号
                    que.append(False)
                else:                               #其他的情况为有用括号
                    que.append(True)
            if len(p) > 1:                            #括号中间不只符号时
                if p2 == 0 or p2 == 1:   #当右边符号为-或+，为无用符号
                    que.append(False)
                elif (p2 == 3 or p2 == 4) and (0 not in p or 1 not in p):      #当右括号右边的符号为*或/，
                    que.append(False)                                            # 中间括号里没有+或-，则为无用符号
                else:
                    que.append(True)
        # 括号在中间的情况
        if i == '(' and k != 0:
            p1 = ch[k - 1]                 #左括号左边的符号
            for j in range(k + 1, len(ch)):
                if ch[j] != '(' and ch[j] != ')' and ch[j] >= 0:
                    p.append(ch[j])         #中间的符号
                elif ch[j] == ')':
                    if j != len(ch) - 1:    #判断右括号右边是否有符号
                        for n in range(j + 1, len(ch)):
                            if ch[n] != ')' and ch[n] >= 0:
                                p2 = ch[n]    #右括号右边的符号
                                break
                            else:
                                continue
                        break
                    else:
                        p2 = -1          #右括号右边没有符号
                else:
                    continue
            #中间括号只有一个符号的情况
            if len(p) == 1:
                if  p1 == 3:       #左括号左边为/，都为有用括号
                    que.append(True)
                elif p1 == 2 and (0 == p[-1] or 1 == p[-1]):  #左括号为*，中间括号为-或+，为有用括号
                    que.append(True)
                elif p1 == 1 and (0 == p[-1] or 1 == p[-1]): #左括号为-，中间的括号为-或+，为有用括号
                    que.append(True)
                elif p1 == 0 and (0 == p[-1] or 1 == p[-1]) and (p2 == 3 or p2 ==2):
                    que.append(True)                         #左括号为+，中间括号为-或+，右括号为*或/
                else:
                    que.append(False)             #其他情况为无用括号
            #中间括号不只一个的情况
            else:
                if p1 == 3:             #左括号左边为/，都为有用括号
                    que.append(True)
                elif p1 == 1 and (1 in p or 0 in p):        #左括号为-，中间的括号有-或+，为有用括号
                    que.append(True)
                elif p1 == 2 and (0 in p or 1 in p):        #左括号为*，中间括号有-或+，为有用括号
                    que.append(True)
                elif p1 == 0 and (0 in p or 1 in p) and (p2 == 3 or p2 ==2):
                    que.append(True)                         #左括号为+，中间括号有-或+，右括号为*或/
                else:
                    que.append(False)
    return que


def result_integer(f, m, kh):
    try:
        n = eval(f)
        n = Fraction('{}'.format(n)).limit_denominator()  # 把表达式的结果转成分数
        if n > 0:  # 判断结果是否大于0，否则重新产生表达式
            que = judge(f, kh)
            place = []      #存储无用括号的位置
            zid = []        #存储所有左括号的位置
            yid = []        #存储所有右括号的位置
            zkh = []        #存储无用左括号的位置
            ykh = []        #存储无用右括号的位置
            for k, i in enumerate(que):
                if i == False:
                    place.append(k)
            for k,i in enumerate(f):
                if i == '(':
                    zid.append(k)
                if i == ')':
                    yid.append(k)
            for i in place:
                zkh.append(zid[i])
                ykh.append(yid[i])
            f1 = ''
            for k, j in enumerate(f):
                if k in zkh or k in ykh:
                    continue
                else:
                    f1 += j
            zhi = eval(f1)       #去掉无用括号重新计算表达式的值
            zhi = Fraction('{}'.format(zhi)).limit_denominator()
            if zhi > 0:
                print(f1,'=')
                print('请输入你的答案：')
                x = Fraction('{}'.format(eval(input()))).limit_denominator()
                if x == zhi:
                    print('√')
                else:
                    print('×')
                    print('正确的答案为：', zhi)
            else:
                integer()
        else:
            integer()
    except:
        integer(m)
def func_integer(number):
    f = ''
    ch = []
    rand = random.randint(0, 1)  #选择内嵌或外嵌括号
    if number != 1:         #避免一个表达式也产生括号
        if rand == 0:
            ch.append('(')
            op = operation[random.randint(0, 3)]
            ch.append(random.randint(1, 10))
            ch.append(op)
            ch.append(random.randint(1, 10))
            ch.append(')')
        else:
            op = operation[random.randint(0, 3)]
            if op == '/':
                a = random.randint(1, 10)
                ch.append(a)
                ch.append(op)
                ch.append(random.randint(a, 10))
            else:
                ch.append(random.randint(1, 10))
                ch.append(op)
                ch.append(random.randint(1, 10))
    else:
        op = operation[random.randint(0, 3)]
        if op == '/':
            a = random.randint(1, 10)
            ch.append(a)
            ch.append(op)
            ch.append(random.randint(a, 10))
        else:
            ch.append(random.randint(1, 10))
            ch.append(op)
            ch.append(random.randint(1, 10))
    for i in ch:       #把产生表达式当成一个整体
        f += str(i)
    return f
def integer():
    ch = []                               #存储表达式
    number = random.randint(1, 5)        #随机产生表达式的数量
    for i in range(number):
        rand = random.randint(0, 1)       #随机产生0和1 判断是否使用括号
        a = func_integer(number)          #调用表达式产生函数，产生表达式
        if rand == 0:
            op = operation[random.randint(0,3)]    #产生*，/来连接有括号的表达式，避免产生+，—
            rand = random.randint(0, 1)            #随机产生0和1 判断是否使用内嵌括号或外嵌括号
            if i != number - 1:                    #避免开始和结尾用无意义的括号
                if rand == 0:
                    ch.append('(')
                    ch.append(a)
                    ch.append(op)
                    ch.append(random.randint(1,10))
                    ch.append(')')
                    ch.append(operation[random.randint(0, 3)])
                else:
                    ch.append(a)
                    ch.append(operation[random.randint(0, 3)])
            else:
                ch.append(a)
                ch.append(operation[random.randint(0, 3)])
        else:
            ch.append(a)
            ch.append(operation[random.randint(0, 3)])

    kuohao = []
    f = ''
    for k,i in enumerate(ch):             #把列表中的所有值用f一个个连起来
        if k != len(ch)-1:
            f += str(i)
    for i in f:
        if i.isdigit() == False:
            if i == '+':
                kuohao.append(0)
            elif i == '-':
                kuohao.append(1)
            elif i == '*':
                kuohao.append(2)
            elif i == '/':
                kuohao.append(3)
            else:
                kuohao.append(i)
    result_integer(f, ch, kuohao)

if __name__ == '__main__':
    while True:
        print('输入你想做几道题目')
        n = int(input())
        for i in range(n):
            print('第{}题：'.format(i + 1))
            integer()
        print('是否继续做题（0退出，1继续）：')
        m = int(input())
        if m == 0:
            exit()