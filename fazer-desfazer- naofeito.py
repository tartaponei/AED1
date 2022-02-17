# implementar algoritmo de pilha
# FAZER DEPOIS NÃO É ESSA A RESPOSTA!!!!!!!!!!!!!!

class pilha():
    def __init__(self, n):
        self.n = n #n = capcidade da pilha
        
        self.a = [] #cria lista vazia
        self.topo = 0

def empilha(x, p):
        if p.topo == p.n:
            print("pilha cheia")
        else:
            p.topo = p.topo + 1
            p.a.append(x)

def desempilha(p):
    if p.topo == 0:
        print("pilha vazia")
    else:
        v = p.a[p.topo-1]
        del(p.a[p.topo-1])
        p.topo = p.topo - 1
        return v

p = pilha(5)

for i, item in enumerate(range(10, 13)):
    p.a.append(item) #[1, 2, 3]
    p.topo = i+1 

print(p.a)
print("topo: ", p.topo)

print("\n")

empilha(4, p)
print(p.a)
print("topo:", p.topo)

print("\n")

desempilha(p)
print(p.a)
print("topo:", p.topo)