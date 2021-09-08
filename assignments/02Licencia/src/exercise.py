def mine():
    
    if edad <18:
      print ('no cuentas con la edad')  
    elif edad>=18:
   
      print('¿cuentas con identificacion?: (s/n)')
      opcion=str(input())
    if opcion =='s':
      print ('solicitud aceptada')
    elif opcion=='n':
     print('no cuentas con los requisitos necesarios')
    
print ('ingresa tu edad')
edad=int(input())
mine ()