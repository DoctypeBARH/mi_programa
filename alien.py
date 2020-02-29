aliens=[]
def agragar():
    for numero_alien in range(30):
        nuevo_alien={'color':'verde','puntos':'5','velocidad':'baja'}
        aliens.append(nuevo_alien)

def cambio():
    for alien in aliens[:3]:
        if alien['color']==['verde']:
            alien['color']=['amarillo']
            alien['puntos']=[10]
            alien['velocida']=['media']
#muestra los primeros 5 aliens
def mostrar(cuantos):
    for alien in aliens[:cuantos]:
        print(alien)
        print ("............................")
def contar():
    cantidad=len(aliens)
    print("El numero de alines es", cantidad)

agragar()
cambio()

mostrar(5)
contar()



