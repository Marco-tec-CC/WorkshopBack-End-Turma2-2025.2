import math

def arredondamento(numero: float) -> dict: #uma especie de dicionario
    
    return{
        "piso": math.floor(numero),
        "teto": math.ceil(numero),
        "arredondamento": round(numero)

}

#não consegui fazer isso será APENAS PARA ESTUDOS!!!!