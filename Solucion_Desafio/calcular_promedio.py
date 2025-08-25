nombre = input ("Ingrese su nombre")
print(f'{nombre} a continuación ingresa tus 5 notas de la materia por favor')

nota1 = float(input("Ingresa la primera nota:  "))
nota2 = float(input("Ingresa la segunda nota:  "))
nota3 = float(input("Ingresa la tercera nota:  "))
nota4 = float(input("Ingresa la cuarta nota:  "))
nota5 = float(input("Ingresa la quinta nota:  "))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print(f'El promedio de las calificaciones es {promedio}')

if promedio >= 60:
    print("Estado actual: Aprobado!")

elif promedio >= 40:
    print("Estado actual: En recuperación")

else:
    print ("Estado actual: Reprobado") 