import math

inicio="a"
destino="o"

valores={
    "a":[math.inf,""],
    "b":[math.inf,""],
    "c":[math.inf,""],
    "d":[math.inf,""],
    "e":[math.inf,""],
    "f":[math.inf,""],
    "g":[math.inf,""],
    "h":[math.inf,""],
    "i":[math.inf,""],
    "j":[math.inf,""],
    "k":[math.inf,""],
    "l":[math.inf,""],
    "m":[math.inf,""],
    "n":[math.inf,""],
    "ñ":[math.inf,""],
    "o":[math.inf,""],
    "p":[math.inf,""]
}

caminos=[
    ["a","b",8],
    ["a","d",15],
    ["b","c",5],
    ["b","d",3],
    ["d","c",12],
    ["d","e",8],
    ["e","m",14],
    ["m","j",8],
    ["m","k",2],
    ["m","l",5],
    ["l","k",12],
    ["k","j",1],
    ["e","n",9],
    ["n","ñ",1],
    ["n","o",5],
    ["n","p",6],
    ["p","o",13],
    ["o","ñ",10],
    ["e","f",11],
    ["f","g",4],
    ["f","h",7],
    ["f","i",9],
    ["g","h",18],
    ["h","i",12],
]
 
def actualizarValores(origen,destino,valor):
    if valor<valores[destino][0]:
        valores[destino][0]=valor 
        valores[destino][1]=origen
        return True
    return False
 
valores[inicio][0]=0
 
while True:
    cancelar=True
    for i in caminos:
        if actualizarValores(i[0],i[1],valores[i[0]][0]+i[2]):
            cancelar=False
        if actualizarValores(i[1],i[0],valores[i[1]][0]+i[2]):
            cancelar=False
    if cancelar:
        break
 
camino=[destino]
 
while True:
    if camino[-1]==inicio:
        break
    camino.append(valores[camino[-1]][1])
 
print("El camino mas corto desde el punto '{}' y el punto '{}' es: {}".format(inicio, destino, camino[::-1]))