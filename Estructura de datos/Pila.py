class Pila:
    def __init__(self,t):
        self.cuerpo=[]
        for i in range(t):
            self.cuerpo.append(None)
        self.tamanio = t
        self.ultimo = 0
    def vacia(self):
        if(self.ultimo==0):
            return True
        else:
            return False
    def llena(self):
        if(self.ultimo==self.tamanio):
            return True
        else:
            return False
    def push(self,a):
        if(not self.llena()):
            self.cuerpo[self.ultimo]=a
            self.ultimo+=1
        else:
            print("Pila llena")
    def pop(self):
        if(not self.vacia()):
            porquex=self.cuerpo[self.ultimo-1]
            self.cuerpo[self.ultimo-1]=None
            self.ultimo-=1
            return porquex
        else:
            print("La pila está vacía")