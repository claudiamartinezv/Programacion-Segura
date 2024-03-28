"""
Aquí estoy realizando mi primer programa en el leguaje de multiparadigma Python
Clase: Introducción a la programación segura.
Fecha: 27-03-2024
"""

print("Hola Mundo!\n") #Mostrar mensaje en consola 

print("Mi nombre es: Claudia Martínez") #Presentación 
print("Tengo: 30 años")
print("Soy Fonoaudióloga y ahora estoy estudiando Analista Programador \n")

#Se pueden utilizar las variables
nombre = "Claudia Martínez"
edad = 30
ocupacion = "Fonoaudióloga y ahora estoy estudiando Analista Programador"

print("Vamos mejorando...") #Presentación con variables 
print("Mi nombre es: ", nombre) #Primera opción de concatenar con ","
print("Edad:",  edad, "años") #Con la "," tira un espacio más por defecto, porque entiende que se puede estar concadenando dos string
print("Soy: " + ocupacion) #Segunda opción de concatenar con "+"

#Estructura condicional ? 🔷
if(edad > 17):
    print("Mensaje de verdad")
else:
    print("Mensaje de falso")

#elif... apoyo a la condición