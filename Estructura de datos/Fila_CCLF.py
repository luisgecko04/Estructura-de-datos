class Pila:
    def __init__(self, tamaño_maximo=None):
        self.cuerpo = []
        self.tamaño_maximo = tamaño_maximo

    def push(self, elemento):
        if self.tamaño_maximo is None or len(self.cuerpo) < self.tamaño_maximo:
            self.cuerpo.append(elemento)
        else:
            raise Exception("La pila está llena")

    def pop(self):
        if len(self.cuerpo) == 0:
            raise Exception("La pila está vacía")
        return self.cuerpo.pop()

    def peek(self):
        if len(self.cuerpo) == 0:
            raise Exception("La pila está vacía")
        return self.cuerpo[-1]

    def es_vacia(self):
        return len(self.cuerpo) == 0

    def tamaño(self):
        return len(self.cuerpo)
