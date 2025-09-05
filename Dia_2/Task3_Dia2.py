import math
class FiguraGeometrica:
    @staticmethod #estudar esse staticmethod pq eu não entendi como usar.... e estudar mais função e classe!!
    def area_circulo(raio: float) -> float:
        return math.pi * math.pow(raio, 2)
    
    @staticmethod
    def area_triangulo(base: float, altura: float) -> float:
        return (base + altura) / 2
    
    @staticmethod
    def hipotenusa(cateto: float, cateto2: float) -> float:
        return math.sqrt(math.pow(cateto, 2) + math.pow (cateto2, 2))
    
    #não conseguir fazer!!! IREI APENAS ESTUDAR ISSO!!!!!!!!!!!!