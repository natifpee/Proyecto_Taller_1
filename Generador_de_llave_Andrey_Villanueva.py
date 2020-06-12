def decimal_a_binario(n):
    if n<2:
        return n
    else:
        return (n%2)+(10*(decimal_a_binario(n//2)))
print(decimal_a_binario(111))

def lista(n):
    digito=n%10
    if n==0:
        listado.append(0)
        listado.reverse()
        return listado
    else:
        listado.append(digito)
        return lista(n//10)

listado=[]

print(lista(decimal_a_binario(111)))

def xor(listado,a,b,c,e,f):
    if len(listado)==9:       
        
        return listado
        
    else:
        if a==1:
            return xor(listado,a-10,b,c,e+1,f)
        if a==0 or a==2:
            return xor(listado,a-10,b,c,e,f)
        if b+e==1:
            return xor(listado,a-10,b-10,c,e,f+1)
        if b+e==0 or b+e==2:
            return xor(listado,a-10,b-10,c,e,f)
        if c+f==1:
            listado.insert(0,1)
            return xor(listado,a-10,b-10,c,e,f)
        if c+f==0 or c+f==2:
            listado.insert(0,0)
            return xor(listado,a-10,b-10,c,e,f)



a= listado[7]+listado[5]
b= listado[3]
c= listado[2]
e=0
f=0

print(xor(listado,a,b,c,e,f))

resultado = xor(listado,a,b,c,e,f)

listado.pop(8)

print(listado)

def conjunto(listado):
    conjunto="".join(map(str,listado))
    entero=int(conjunto)
    return entero

print(conjunto(listado))

def convertir_decimal(pNum,pBase=2, pExpo=0):
    if pNum < pBase :
        return pNum*pBase**pExpo
    else:
        return (pNum%10*pBase**pExpo + convertir_decimal(pNum//10,pBase, pExpo+1))

print(convertir_decimal(conjunto(listado)))

#Andrey Villanueva Aguilar Carnet:2020097733
