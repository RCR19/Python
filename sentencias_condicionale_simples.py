print("sistema para calcular el promedio de un alumno.")

nombre =(input("¿cual es tu nombre?: "))

matematicas = int(input(nombre + " ¿cual es tu calificacion en matematicas?: "))
español = int(input(nombre + " ¿cual es tu calificacion en español?: "))
quimica = int(input(nombre + " ¿cual es tu calificacion en quimica?: "))

promedio = (matematicas + quimica + español)  / 3 
promedio = int (promedio)

if promedio >= 60:
       print('felicidades ' + nombre + ' "aprobaste" con un promedio de: ' , promedio)

print("fin.")


       

