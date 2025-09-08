#Atividade 1 fácil:

#print("Olá, mundo!"#

#O problema está na falta de um parêntese#

print("Hello World!") #versão corrigida!!#

#Atividade 2 fácil:

#print(nome)#

#O problema está em definir a variavel "nome" que no exemplo a cima não está sendo definida.#

nome = 10

print(nome) #versão corrigida!!#

#Atividade 3 mediana:

#def somar(a, b):
#    return a + b

#resultado = somar(10, "5")
#print(resultado)

#o problema está em aspas exatamente no 5 que considera ele apartir de que use aspas se torne str e dara erro por conta que não da para somar sting com numero

def somar(a, b):
    return a + b

resultado = somar(10, 5) #versão corrigida!!!
print(resultado)

#atividade 4 Difícil:

#dados = {
    #"nome": "Isaac ",
    #"idade": 25,
    #"cidade": "São Paulo"
#}

#chave = input("Digite a chave que deseja acessar: ")

#print(f"O valor da chave '{chave}' é: {dados[chave]}") 

#o problema se envolta todos na variavel "chave"

dados = { 
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo",

}

chave = input("Digite a chave que deseja acessar: ")

try:

    print(f"O valor da chave '{chave}' é: {dados[chave]}") #Versão corrigida!!

except KeyError:
    print(f"A chave não existe no dicionario")

valor = dados.get(chave)

print(valor)