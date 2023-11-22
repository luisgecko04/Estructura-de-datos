import random as rnd
class almacen:
    def __init__(self,d,a,m):
        self.dato=d
        self.memoria=m
        self.apuntador=a

class listaLigada:
    def __init__(self,n=50,ini=None):
        self.almacenes=[]
        self.tamanio = 0
        for i in range(n):
            self.almacenes+=[None]
        if(ini==None):
            self.ultimo=-1
            self.ocupados=[]
            self.inicio = None
        else:
            self.ultimo=rnd.randint(1, n)
            self.ocupados=[self.ultimo]
            self.inicio=almacen(ini,-1,self.ultimo)
            self.almacenes[self.ultimo-1]=self.inicio
            self.tamanio=1
   
   
    def push(self,dato):
        if(self.tamanio>=50):
            print("Error: La lista está llena")
        else:
            if(self.tamanio==0):
                self.ultimo=rnd.randint(1, 50)
                self.ocupados=[self.ultimo]
                self.inicio=almacen(dato,-1,self.ultimo)
                self.almacenes[self.ultimo-1]=self.inicio
            else:
                prox=rnd.randint(1, 50)
                while(prox in self.ocupados):
                    prox=rnd.randint(1, 50)
                self.almacenes[self.ultimo-1].apuntador = prox
                self.ultimo = prox        
                self.ocupados+=[self.ultimo]
                self.almacenes[self.ultimo-1]=almacen(dato,-1,self.ultimo)
            self.tamanio+=1
   
    def pop(self):
        if(self.tamanio>1):
            penultimo=self.ocupados[-2]
            self.ocupados=self.ocupados[:-1]
            dato = self.almacenes[self.ultimo-1].dato
            self.almacenes[self.ultimo-1]=None
            self.almacenes[penultimo-1].apuntador=-1
            self.ultimo=penultimo
            self.tamanio-=1
            return dato
        elif(self.tamanio==1):
            self.ocupados=[]
            dato = self.almacenes[self.ultimo-1].dato
            self.almacenes[self.ultimo-1]=None
            self.inicio=None
            self.ultimo=-1
            self.tamanio-=1
            return dato
        else:
            print("Error: No hay elementos en la lista")