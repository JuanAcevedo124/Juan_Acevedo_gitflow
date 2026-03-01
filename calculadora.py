booleanito = True
while booleanito == True:
   

    print('BIenvenido a la caluladora')
    print('que funcion desea realizar')
    print('1- suma: ')
    print('2- resta:  ')
    print('3- multiplicacion: ')
    print('4- division: ')
    print('5- salir: ')

    opcion_usuario = int(input(''))
    if opcion_usuario == 1:
        a = float(input('Ingrese el primer digito' ))
        b = float(input('Ingrese el segundo digito' ))
        suma_total = (a + b)
        print(suma_total)

    elif opcion_usuario == 2:
        a = float(input('Ingrese el primer digito' ))
        b = float(input('Ingrese el segundo digito' ))
        resta_total = (a - b)
        print(resta_total)

    elif opcion_usuario == 3:
        a = float(input('Ingrese el primer digito' ))
        b = float(input('Ingrese el segundo digito' ))
        multiplicacion_total = (a * b)
        print(multiplicacion_total)

    elif opcion_usuario == 4:
        a = float(input('Ingrese el primer digito' ))
        b = float(input('Ingrese el segundo digito' ))
        division_total = (a / b)
        print(division_total)

    elif opcion_usuario == 5: 
        print('gracias por usar nuestra calculador')
    booleanito = False