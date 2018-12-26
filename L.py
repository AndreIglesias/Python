
# Recursive chio
def chio(matriz, multiplo = None):
    if multiplo is None: multiplo = 1
    if len(matriz) == 2:
        return multiplo*(matriz[0][0]*matriz[1][1]-matriz[0][1]*matriz[1][0])
    else:
        ordenCuadrado = len(matriz[0])
        pivote = 0
        for i in matriz[0]:
            if i != 0:
                pivote = i
                break
        if pivote == 0: return 0
        else:
            multiplo *= -(1/(pivote**(ordenCuadrado-2))) if matriz[0].index(pivote)%2 != 0 else 1/(pivote**(ordenCuadrado-2))
            nueva = []
            for i in range(len(matriz)):
                if i != 0:
                    filanueva = []
                    for j in range(len(matriz[0])):
                        if j != matriz[0].index(pivote):
                            filanueva.append(pivote*matriz[i][j]-matriz[0][j]*matriz[i][matriz[0].index(pivote)])
                    nueva.append(filanueva)
            return int(chio(nueva, multiplo))


#-------------------------------------------------------
n=2 # Linear recurrence order 2
coeff = []
pC = eval("("+input("Initial Condition n,a(n): ")+")")
sC = eval("("+input("Initial Condition n,a(n): ")+")")
for i in range(n):
    coeff.append(float(input("Coefficient of a(n-{0}): ".format(i+1))))

D = (coeff[0]**2+4*coeff[1])**(1/2)
r1 = 0.5*(coeff[0]-D)
r2 = 0.5*(coeff[0]+D)

if(r1!=r2):
    Det = chio([[r1**pC[0],r2**pC[0]],[r1**sC[0],r2**sC[0]]])
    a = chio([[pC[1], r2**pC[0]],[sC[1], r2**sC[0]]])/Det
    b = chio([[r1**pC[0], pC[1]],[r1**sC[0], sC[1]]])/Det

    print("a(n) = {0}({1}^n) + {2}({3}^n)".format(a, r1, b, r2))
else:
    Det = chio([[r1**pC[0],pC[0]*r2**pC[0]],[r1**sC[0],sC[0]*r2**sC[0]]])
    a = chio([[pC[1], pC[0]*r2**pC[0]],[sC[1], sC[0]*r2**sC[0]]])/Det
    b = chio([[r1**pC[0], pC[1]],[r1**sC[0], sC[1]]])/Det
    print("a(n) = {0}({1}^n) + {2}n({3}^n)".format(a, r1, b, r2))
