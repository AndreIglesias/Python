a = ((list(filter(lambda p: ((2**(p-1))%p==1) or p==2, range(1,978)))))
f = lambda x, y: print(x) if (y + 1) % 8 == 0 else print(x, end="\t")
[f(a[x],x) for x in range(len(a))]
