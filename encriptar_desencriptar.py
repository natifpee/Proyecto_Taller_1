#ENCRIPTACION
def encriptar(string, llave):
    #Se verifica que sea un string y un numero
    if(isinstance(string, str) and isinstance(llave, int) and llave != 0 and string != ""):
        encriptar_aux(string, llave, 0, "", [])
    else:
        print("Alguno de los valores ingresados no es correcto.")
        
def encriptar_aux(string, llave, i, nuevoString, listallaves):
    #Verifica si revisó toda la palabra
    if(i == len(string)):
        print(nuevoString)
        return desencriptar(nuevoString, listallaves)
    else:
        
        listallaves.append(llave)
        
        #Lista estática
        lista1 = ["a","b","c","d","e","f","g","h","i","j","k","l",
                  "m","n","ñ","o","p","q","r","s","t","u","v","w",
                  "x","y","z", "A", "B", "C", "D", "E", "F", "G", "H",
                  "I", "J", "K", "L", "M", "N","Ñ","O","P","Q","R","S",
                  "T", "U", "V", "W", "X", "Y" ,"Z"]
        
        #Lista dinámica
        lista2 = ["a","b","c","d","e","f","g","h","i","j","k","l",
                  "m","n","ñ","o","p","q","r","s","t","u","v","w",
                  "x","y","z", "A", "B", "C", "D", "E", "F", "G", "H",
                  "I", "J", "K", "L", "M", "N","Ñ","O","P","Q","R","S",
                  "T", "U", "V", "W", "X", "Y" ,"Z"]

        #Obtiene la letra de la palabra
        letra = string[i]

        if(letra == " "):
            return encriptar_aux(string, llave, i+1, nuevoString + " ", listallaves)

        #Rota la lista
        if(llave<=54):
            lista2 = lista2[-llave:] + lista2[:-llave]
        if(llave>54 and llave<=81):
            llave1 = llave-54
            lista2 = lista2[-llave1:] + lista2[:-llave1]
        if(llave>81 and llave<=108):
            llave1 = llave-54
            lista2 = lista2[-llave1:] + lista2[:-llave1]
        if(llave>108 and llave<=135):
            llave1 = llave-108
            lista2 = lista2[-llave1:] + lista2[:-llave1]
        if(llave>135 and llave<=162):
            llave1 = llave-135
            lista2 = lista2[-llave1:] + lista2[:-llave1]
        if(llave>162 and llave<=189):
            llave1 = llave-162
            lista2 = lista2[-llave1:] + lista2[:-llave1]
        if(llave>189 and llave<=216):
            llave1 = llave-189
            lista2 = lista2[-llave1:] + lista2[:-llave1]
        if(llave>216 and llave<=243):
            llave1 = llave-216
            lista2 = lista2[-llave1:] + lista2[:-llave1]
        if(llave>243 and llave<=255):
            llave1 = llave-243
            lista2 = lista2[-llave1:] + lista2[:-llave1]
        
        #Obtiene la posición de la letra en la primera lista
        posicion = lista1.index(letra)

        #Obtiene la letra de la segunda lista con la posicíon de la primera
        letranueva = lista2[posicion]

        nuevallave = crearNuevaLlave(llave)
        
        #Recursivo
        encriptar_aux(string, nuevallave, i+1, nuevoString + letranueva, listallaves)

        

def desencriptar(string, listallaves):
    #Se verifica que sea un string y un numero

    desencriptar_aux(string, 0, "", listallaves, len(listallaves)-1)


def desencriptar_aux(string, i, palabrafinal, listallaves, j):
    if(i == len(string)):
        print(palabrafinal)
    else:
        #Lista estática
        lista1 = ["a","b","c","d","e","f","g","h","i","j","k","l",
                  "m","n","ñ","o","p","q","r","s","t","u","v","w",
                  "x","y","z", "A", "B", "C", "D", "E", "F", "G", "H",
                  "I", "J", "K", "L", "M", "N","Ñ","O","P","Q","R","S",
                  "T", "U", "V", "W", "X", "Y" ,"Z"]
            
        #Lista dinámica
        lista2 = ["a","b","c","d","e","f","g","h","i","j","k","l",
                  "m","n","ñ","o","p","q","r","s","t","u","v","w",
                  "x","y","z", "A", "B", "C", "D", "E", "F", "G", "H",
                  "I", "J", "K", "L", "M", "N","Ñ","O","P","Q","R","S",
                  "T", "U", "V", "W", "X", "Y" ,"Z"]

        stringback = string[::-1]
        
        llave = listallaves[j]
        
        letra = stringback[i]

        if(letra == " "):
            return desencriptar_aux(string, i+1, " " + palabrafinal, listallaves, j-1)

        #Rota la lista
        if(llave<=54):
            lista2 = lista2[-llave:] + lista2[:-llave]
        if(llave>54 and llave<=81):
            llave1 = llave-54
            lista2 = lista2[-llave1:] + lista2[:-llave1]
        if(llave>81 and llave<=108):
            llave1 = llave-54
            lista2 = lista2[-llave1:] + lista2[:-llave1]
        if(llave>108 and llave<=135):
            llave1 = llave-108
            lista2 = lista2[-llave1:] + lista2[:-llave1]
        if(llave>135 and llave<=162):
            llave1 = llave-135
            lista2 = lista2[-llave1:] + lista2[:-llave1]
        if(llave>162 and llave<=189):
            llave1 = llave-162
            lista2 = lista2[-llave1:] + lista2[:-llave1]
        if(llave>189 and llave<=216):
            llave1 = llave-189
            lista2 = lista2[-llave1:] + lista2[:-llave1]
        if(llave>216 and llave<=243):
            llave1 = llave-216
            lista2 = lista2[-llave1:] + lista2[:-llave1]
        if(llave>243 and llave<=255):
            llave1 = llave-243
            lista2 = lista2[-llave1:] + lista2[:-llave1]
        
        posicion = lista2.index(letra)
        
        letranueva = lista1[posicion]
        
        desencriptar_aux(string, i+1, letranueva + palabrafinal, listallaves, j-1)

#CREACION DE LA LLAVE     

def crearNuevaLlave(llave):
    binario = decimal_a_binario(llave)
    numbin = []
    listabin = lista(binario, numbin)

    a = listabin[7]
    b = listabin[5]
    c = listabin[3]
    d = listabin[2]

    resultado = (((a^b)^c)^d) #XOR

    listabin[0] = resultado
    listabin.pop(8)
    nuevallave = convertir_decimal(conjunto(listabin))
    return nuevallave

def decimal_a_binario(n):
    if n<2:
        return n
    else:
        return (n%2)+(10*(decimal_a_binario(n//2)))

def lista(n, numbin):
    digito=n%10
    if n==0:
        tamaño = len(numbin)
        if(tamaño<=8):
            listafinal = fill(numbin, 8-tamaño, 0)
        listafinal.append(0)
        listafinal.reverse()
        return listafinal
    else:
        numbin.append(digito)
        return lista(n//10, numbin)

def fill(numbin, cant, i):
    if(i == cant):
        return numbin
    else:
        numbin.append(0)
        return fill(numbin, cant, i+1)

def conjunto(listado):
    conjunto="".join(map(str,listado))
    entero=int(conjunto)
    return entero

def convertir_decimal(pNum,pBase=2, pExpo=0):
    if pNum < pBase :
        return pNum*pBase**pExpo
    else:
        return (pNum%10*pBase**pExpo + convertir_decimal(pNum//10,pBase, pExpo+1))

print (encriptar("Hola Mundo",2))