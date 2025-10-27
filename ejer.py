#Autor: Daniel Salcedo 
def matrizmag():
    def esmatriz(matriz):
        n = len(matriz)
        refe = sum(matriz[0])
        for fila in matriz:
            if sum(fila) != refe:
                return False
        for j in range(n):
            if sum(matriz[i][j] for i in range(n)) != refe:
                return False
        if sum(matriz[i][i] for i in range(n)) != refe:
            return False
        if sum(matriz[i][n - 1 - i] for i in range(n)) != refe:
            return False
        return True

    matriz_ejemplo = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    print("¿La matriz es mágica?:", esmatriz(matriz_ejemplo))

def uno():
    def ordval(diccionario):
        valores = list(diccionario.values())
        valores.sort()
        return valores

    dic1 = {"a": 5, "b": 2, "c": 9, "d": 1}
    print("Valores ordenados:", ordval(dic1))

def dos():
    def verif(dic1, dic2):
        for clave, valor in dic1.items():
            if clave not in dic2 or dic2[clave] != valor:
                return False
        return True

    dicA = {"x": 10, "y": 20}
    dicB = {"x": 10, "y": 20, "z": 30}
    print("¿El diccionario A está contenido en diccionario B?:", verif(dicA, dicB))


def tres():
    def mix(dic1, dic2):
        resultado = dic2.copy()
        resultado.update(dic1)
        return resultado

    dic1 = {"a": 1, "b": 2}
    dic2 = {"b": 3, "c": 4}
    print("Diccionarios mezclados:", mix(dic1, dic2))

def cuatro():
    def age(lista_personas, edad_min, edad_max):
        for persona in lista_personas:
            if edad_min <= persona["edad"] <= edad_max:
                print(f"{persona['nombres']} {persona['apellidos']} ({persona['edad']} años)")

    personas = [
        {"nombres": "Pedro Julio", "apellidos": "Tristán Merchán", "edad": 101},
        {"nombres": "Ana María", "apellidos": "Pérez López", "edad": 30},
        {"nombres": "Carlos", "apellidos": "García", "edad": 45}
    ]

    print("\nPersonas entre 25 y 50 años:")
    age(personas, 25, 50)

def main():
    #matrizmag()
    uno()
    #dos()
    #tres()
    #cuatro()
