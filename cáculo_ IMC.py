nome=(input("digite seu nome:"))
peso = float (input ("digite seu peso em kg:"))
altura = float (input ("digite sua altura:"))
imc= peso/(altura*altura)
if imc <18.5:
    print ("imc abaixo do peso!")
elif imc >=18.5 and imc <=24.9:
    print ("imc peso normal!")
elif imc >=25.0 and imc <=29.9:
    print("imc sobrepeso!")
else:
    print("imc obesidade!")
    




    
    

 