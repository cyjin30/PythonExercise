
import re

def myCalculate(mystr):
    if (mystr.__contains__("(")):
        start = mystr.rindex("(")
        lstr = mystr[0:start]
        tmpstr = mystr[start + 1:]
        end = tmpstr.index(")")
        rstr = tmpstr[end + 1:]
        nowstr = tmpstr[0:end]
        newstr = lstr + str(myCalculate(nowstr)) + rstr
        return myCalculate(newstr)
    else:
        return calcNoSym(mystr)


def calcNoSym(string):
    if (string.__contains__("*")):
        string = getNewStr(string, "*")
        return calcNoSym(string)
    if (string.__contains__("/")):
        string = getNewStr(string, "/")
        return calcNoSym(string)
    if (string.__contains__("+")):
        string = getNewStr(string, "+")
        return calcNoSym(string)
    if (string.__contains__("-")):
        string = getNewStr(string, "-")
        return calcNoSym(string)
    return string


def getNewStr(string, op):
    start = string.index(op)
    lstr = string[0:start]
    rstr = string[start + 1:]
    lnum = re.search('\d+$', lstr).group()
    rnum = re.search('\d+', rstr).group()
    newstr = lstr.rstrip(lnum) + str(calcs(lnum, rnum, op)) + rstr.lstrip(rnum)
    return newstr


def calcs(num1, num2, op):
    if (op == "+"):
        return int(num1) + int(num2)
    elif (op == "-"):
        return int(num1) - int(num2)
    elif (op == "*"):
        return int(num1) * int(num2)
    elif (op == "/"):
        return int(num1) / int(num2)
    else:
        raise "error"


string = "11*22*3/4"

print(myCalculate(string))
sexp = "512+((112+212)*2-312)"
print(myCalculate(sexp))