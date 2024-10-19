def acceso():
    print("Favor de introducir usuario y contraseña:")
    usuario_correcto= "Lcepeda"
    contraseña_correcta= "Santiago"

    usuario= input("introduce usuario:")
    contraseña= input("introduce contraseña:")
    if usuario == usuario_correcto and contraseña == contraseña_correcta:
      print("usuario correcto")
      print("Bienvenido Lcepeda")
    else:
     print("usuario incorrecto: usuario y contraseña no coinciden.")
     print("Acceso denegado")

num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese un numero: "))
suma = num1 + num2
print("el resultado es", num1 + num2)

acceso()

