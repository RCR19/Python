#conjuncion
print("conjuncion 'and'")
num_1 = int(input("Escribe un numero mayor a 2 y menor a 5: "))

if num_1 > 2 and num_1 < 5:
    print("El numero", num_1, " cumple con la condicon.\n")
else:
    print("El numero", num_1, " no cumple con la condicon.\n")

#disyuncion

print("disyuncion 'or'")

palabra = input("para cumplir la condicion escribe 'si' o 'yes': ")

if palabra == "si" or palabra == "yes":
    print("\n la condicon se ha cumplido.\n")
else:
    print("\n la condicon no se ha cumplido.\n")

#negacion

print("negacion 'not'")

num_uno = int(input("ingresa un numero igaul a 5: "))

if not num_uno == 5:
            print("\n el numero es diferente y si cumple la funcion.\n")
else:
    print("\n el numero es igual a cinco y no cumple la funcion.\n")
          

          
