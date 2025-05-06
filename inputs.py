print("Le solicito sus datos personales")
nombre = input("¿Como te llamas? ")
primer_apellido = input("¿cual es su primer apellido? ")
segundo_apellido = input("¿cual es su segundo apellido ")
año_de_nacimiento = int(input("¿en que año nacistes? "))
año = int(input("¿año acutal?"))
edad = año - año_de_nacimiento
print(" Bienvenid@ " + nombre + " " + primer_apellido + " " + segundo_apellido + "y tienes" + " " + str(edad) + " años.") 