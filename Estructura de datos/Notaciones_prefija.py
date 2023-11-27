def infija_a_sufija(expresionInfija):
    precedencia = {}
    precedencia["*"] = 3
    precedencia["/"] = 3
    precedencia["+"] = 2
    precedencia["-"] = 2
    precedencia["("] = 1
    pilaOperadores = Pila()
    listaSufija = []
    listaSimbolos = expresionInfija.split()

    for simbolo in listaSimbolos:
        if simbolo in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or simbolo in "0123456789":
            listaSufija.append(simbolo)
        elif simbolo == '(':
            pilaOperadores.incluir(simbolo)
        elif simbolo == ')':
            simboloTope = pilaOperadores.extraer()
            while simboloTope != '(':
                listaSufija.append(simboloTope)
                simboloTope = pilaOperadores.extraer()
        else:
            while (not pilaOperadores.estaVacia()) and \
               (precedencia[pilaOperadores.inspeccionar()] >= \
                precedencia[simbolo]):
                  listaSufija.append(pilaOperadores.extraer())
            pilaOperadores.incluir(simbolo)

    while not pilaOperadores.estaVacia():
        listaSufija.append(pilaOperadores.extraer())
    return " ".join(listaSufija)

def evaluarPostfija(expresionPostfija):
    operandos = Pila()
    tokenLista = expresionPostfija.split()

    for token in tokenLista:
        if token in "0123456789":
            operandos.incluir(int(token))
        else:
            operando2 = operandos.extraer()
            operando1 = operandos.extraer()
            resultado = hacerOperacion(token, operando1, operando2)
            operandos.incluir(resultado)
    return operandos.extraer()

def hacerOperacion(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
    
expresionInfija = "( A + B ) * C - ( D - E ) * ( F + G )"
expresionPostfija = infija_a_sufija(expresionInfija)
resultado = evaluarPostfija(expresionPostfija)
print(resultado)