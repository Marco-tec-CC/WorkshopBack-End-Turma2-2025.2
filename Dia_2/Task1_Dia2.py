import math #o import para fazer o calculo

numero = float(input("digite um numero:")) #interação e para definir numero

def Numero (numero): #A função 
    
     raiz_quadrada = math.sqrt(numero) #aqui fica o calculo e toda operação por meio do import

     return f"está aqui a raiz quadrada do {numero}, é {raiz_quadrada}" #Mostragem do resultado

print(Numero (numero))