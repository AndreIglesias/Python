def genPascal(n, first=True):
    if first: n +=1; first = False
    if n == 1: return [1]
    row = [1]
    lastRow = genPascal(n-1, first)
    row += list(map(lambda x: lastRow[x]+lastRow[x+1],range(len(lastRow)-1)))
    row.append(1)
    return row

def printPascal(n, number=0):
    if number == n: return
    print("\n{0} -->".format(number), " "*(n-number),end="") 
    exec(str(genPascal(number)).replace("[", "print(").replace("]", ", sep=' ')"))
    printPascal(n, number+1)


def BinoExpansion(Eq):
    """
    type param Eq: str
    param Eq: (a+b)^n
    """
    finalEq = ""
    exponent = ""
    ab = ""
    for i in range(len(Eq)-1, -1, -1):
        try:
            int(Eq[i])
            exponent = Eq[i]+exponent
            ab = Eq[:i]
        except:
            exponent = int(exponent)
            break
    ab = eval(ab.replace("+","','").replace("(","['").replace(")","']").replace("^",""))
    a = ab[0]
    b = ab[1]
    coeff = list(map(lambda x: str(x), genPascal(exponent)))
    for i in range(len(coeff)):
        expoA = "^"+str(len(coeff)-i-1)
        expoB = "^"+str(i)
        if expoA == "^1": expoA = ""
        if expoB == "^1": expoB = ""
        A = a+expoA
        B = b+expoB
        coef = coeff[i]
        if expoA == "^0": A = ""
        if expoB == "^0": B = ""
        if coef == "1": coef = ""

        finalEq += coef+A+"*"+B+"+"
    finalEq = finalEq[:-1]
    try: return finalEq, eval(Eq.replace("^","**"))
    except: return finalEq, None

print(BinoExpansion("(x+3)^5"))
