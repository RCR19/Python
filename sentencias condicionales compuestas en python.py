print("sistema para calcular el promedio de un alumno")

nombre = str(input("para comenzar, ¿cual es tu nombre?: "))

materia_1 = float(input(nombre + "¿cual es tu calificacion en matematicas?: "))

materia_2 = float(input(nombre + "¿cual es tu calificacion en español?: "))

materia_3 = float(input(nombre + "¿cual es tu calificacion en ingles?: "))

operacion = (materia_1 + materia_2 + materia_3) /3

if operacion >= 80:
    print(nombre, "felicidades aprovaste con un promedio de: ", round(operacion,2))
else:
    print(nombre, "lo sentimos has reprobado con un promedio de: ", round(operacion,2))

print("fin.")
