def mine():
    
    if (peso<=0) or (altura<=0):
        print ("Revisa tus datos, alguno de ellos es erróneo.")
    else:
        imc= peso/altura**2
        if imc<20:
            print ("PESO BAJO")
        if 20<=imc<25:
            print ("NORMAL")
        if  25<=imc<30:
            print ("SOBREPESO")
        if 30<=imc<40:
            print ("OBESIDAD")
        if imc>=40:
            print ("OBESIDAD MORBIDA")
 
        
peso=float(input("Peso en kg: "))
altura=float(input("Altura en m: "))
mine()