capacidad=10
elementos=[0] * capacidad
tope= -1
print("teclea elementos de la pila (termina con -1)")

x=0
CLAVE=-1

while x != CLAVE:
    entrada=input()
    if entrada.isdigit():
        x=int(entrada)
        if tope<capacidad -1:
            tope += 1
            elementos[tope] = x
        else:
            print("Excepcion: pila llena ")
            break
    else:
            print("excepcion: Entrada NO valida")
            
    if tope>=0:
        print("elementos de la pila:",end ="")
        while tope>=0:
            x = elementos [tope]
            tope -= 1
            print(x, end="")
        else:
            print("pila vacia")
        