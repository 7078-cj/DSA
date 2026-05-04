def fib_topdown(n):
    mem = {0:0,1:1}
    
    
    def fib(x):
        if x in mem:
            return mem[x]
        
        else:
            r = fib(x-2) + fib(x-1)
            mem[x] = r
    
            return mem[x] 
        
    return fib(n)

def fib_bottomup(n):#tabulation
    if n == 0:
        return 0
    if n == 1:
        return 1
        
    
    tab = [0] * (n+1)
    tab[1] = 1
    for i in range(2,n+1):
        tab[i] = tab[i-1] + tab[i-2]
    
    return tab[n]

if __name__ =='__main__':
    
    r = fib_topdown(3)
    
    print(r)
    
    print()
    
    b = fib_bottomup(6)
    print(b)