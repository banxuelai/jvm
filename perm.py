res = []

def make(n, level):
    if n == level:
        print(res)
        return
        
    for i in range(1, n+1):
        if i not in res:
            res.append(i)
            make(n, level+1)
            res.pop()
            
make(4, 0)