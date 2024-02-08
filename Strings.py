mensaje = "Hola"
mensaje += " "
mensaje += "Ernesto"
print(mensaje)

print("concatenacio:")

mensaje = "Hola"
espacio = " "
nombre = "Ernesto"
print(mensaje + espacio + nombre)

print("busqueda:")

mensaje = "Hola Ernesto"
buscar_subcadena = mensaje.find("Ernesto")
print(buscar_subcadena)

print("extraccion:")

mensaje = "hola ernesto"
extrae_subcadena = mensaje[1:8]
print(extrae_subcadena)

print("comparacion:")

mensaje_uno = "hola"
mensaje_dos = "hola"
print(mensaje_uno == mensaje_dos)
