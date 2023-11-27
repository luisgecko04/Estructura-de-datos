import random as rnd

class almacen:
    def __init__(self, d, a, m, p=None):
        self.dato = d
        self.apuntador = a
        self.memoria = m
        self.prev = p  # Apuntador al nodo anterior

class listaLigada:
    def __init__(self, n=50, ini=None):
        self.almacenes = [None]*n
        self.tamanio = 0
        self.ultimo = -1 if ini is None else rnd.randint(1, n)
        self.ocupados = [] if ini is None else [self.ultimo]
        self.inicio = None if ini is None else almacen(ini, -1, self.ultimo)
        if ini is not None:
            self.almacenes[self.ultimo-1] = self.inicio
            self.tamanio = 1

    def push(self, dato):
        if self.tamanio >= 50:
            print("Error: La lista está llena")
        else:
            prox = rnd.randint(1, 50)
            while prox in self.ocupados:
                prox = rnd.randint(1, 50)
            if self.tamanio == 0:
                self.inicio = almacen(dato, -1, prox)
            else:
                self.almacenes[self.ultimo-1].apuntador = prox
                self.almacenes[prox-1] = almacen(dato, -1, prox, self.ultimo)
            self.ultimo = prox
            self.ocupados.append(prox)
            self.tamanio += 1

    def pop(self):
        if self.tamanio > 0:
            penultimo = self.almacenes[self.ultimo-1].prev
            dato = self.almacenes[self.ultimo-1].dato
            self.almacenes[self.ultimo-1] = None
            if self.tamanio > 1:
                self.almacenes[penultimo-1].apuntador = -1
            self.ultimo = penultimo
            self.ocupados.remove(self.ultimo+1)
            self.tamanio -= 1
            return dato
        else:
            print("Error: No hay elementos en la lista")

    def insert(self, dato, posicion):
        if self.tamanio >= 50:
            print("Error: La lista está llena")
        elif posicion > self.tamanio:
            print("Error: La posición es mayor que el tamaño de la lista")
        else:
            prox = rnd.randint(1, 50)
            while prox in self.ocupados:
                prox = rnd.randint(1, 50)
            nuevo = almacen(dato, self.almacenes[posicion-1].apuntador, prox, posicion-1)
            self.almacenes[posicion-1].apuntador = prox
            self.almacenes[prox-1] = nuevo
            self.ocupados.append(prox)
            self.tamanio += 1

    def remove(self, posicion):
        if self.tamanio == 0:
            print("Error: No hay elementos en la lista")
        elif posicion > self.tamanio:
            print("Error: La posición es mayor que el tamaño de la lista")
        else:
            self.almacenes[self.almacenes[posicion-2].apuntador-1].apuntador = self.almacenes[posicion-1].apuntador
            self.almacenes[posicion-1] = None
            self.ocupados.remove(posicion)
            self.tamanio -= 1