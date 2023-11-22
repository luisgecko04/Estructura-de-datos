datos = [5,7,18,9,8,79,5,6,3,4,2,8,10,1]


for j in range(len(datos)):
    for i in range(len(datos)-1-j):
        if(datos[i]>datos[i+1]):
            aux=datos[i]
            datos[i]=datos[i+1]
            datos[i+1]=aux


print(datos)