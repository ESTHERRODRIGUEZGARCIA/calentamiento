#dinero inicial, 2000. 
#satisfecho: entre 85 y 100% -> True
#precio inicial del helado, 100; cada vez que compres otro aumenta 20%
#si tienes x años, tienes x% de hambre


dinero = 2000
hambre = 17
if dinero >= 1700 and dinero <= 2000:
    print ("no tengo hambre")
precio_helado = 0.17 * 100

def compro_helado():
     dinero -= precio_helado
     print("el precio del helado es, ", str(precio_helado))

#algo no va