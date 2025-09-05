class Main: #Task 4 e 5
    def n(animal1):

        animal1 = gato ("amy", 3)
        print(animal1.falar())

class animal:
    def __init__(self, nome, idade):
         
         self.nome = nome
         self.idade = idade

    def falar (self):
        return f"meu nome é {self.nome},tenho {self.idade} anos"
    
        
class gato(animal):
        
        def __init__(self, nome, idade):
              
              super().__init__(nome, idade)

        def falar(self):
            return "miau miau"
        def Idade_gato(idade):
                return f"tenho 3 anos"
        def Nome_gato(nome):
                return f"meu nome é amy"

        
class cachorro(animal):
        def falar(self):
                return f"AUAU AUAU"
        def Idade_cachorro(idade):
                return f"tenho 13 anos"
        def Nome_cachorro(nome):
                return f"meu nome é mel"

#Task 6 irei continuar dps

class Zoologico:
      def __init__(self):
          self.animais = []
      
      def adicionar_animais(self, animal):
            self.animais.append(animal)
      def listar_animais(self):
          return [f""]


