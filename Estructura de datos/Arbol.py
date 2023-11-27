class arbol:
    def __init__(self, n):
        self.raiz = n
   
    def imprime(self):
        self.raiz.imprime()    

class nodo:
    def __init__(self, cont="", h=[]):
        self.contenido = cont
        self.hijos = h

    def imprime(self):
        print(self.contenido, end=' ')
        for hijo in self.hijos:
            hijo.imprime()

# Creación del árbol
A = nodo("7", [])
B = nodo("5", [])
C = nodo("+", [A, B])
D = nodo("2", [])
E = nodo("*", [C, D])
F = nodo("1", [])
G = nodo("6", [])
H = nodo("-", [F, G])
I = nodo("9", [])
J = nodo("/", [H, I])
K = nodo("*", [E, J])

# Creación del objeto arbol
arb = arbol(K)

# Recorrido del árbol
arb.imprime()