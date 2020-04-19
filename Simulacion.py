
import imageio
import numpy as np
import matplotlib.pyplot as plt
from conjunto import conjunto
from parciales import Gausiana_2d,Act_Temperatura

import time
t0 = time.time()
# Importacion de la imagen inicial
print('Cargando imagen y clasificando regiones ...')

img_path = "tortuga.png"      # <-----------------------------------------------IMAGEN A ANALIZAR
img =  imageio.imread(img_path)
mancha = conjunto(img)

print('Genrando mapa de color del estado inicial...')

tamaño = mancha.tamaño
Temp = np.zeros(tamaño, dtype= np.float32)
#Temp = np.array([[float(0) for x in range(tamaño[0])] for y in range(tamaño[1])] )
Temp_inicial = Temp
for r in mancha.conjunto:
    Temp[r[0],r[1]] = 30 + Gausiana_2d(r[0],r[1],500,(130,130),(25,25))
    

# Inicio de la simulación 

h = 0.008
alpha = 23 # 23 para el acero, en mm cuadrados. 


n = 2000  
for i in range(n  + 1):
    
    if i%200 == 0:        
        fig, ax = plt.subplots()
        ax.set_xlabel('milímetros') ; ax.set_ylabel('milímetros')
        c = ax.pcolormesh(Temp,cmap = 'magma', vmin=0, vmax=500) 
        cb = fig.colorbar(c, ax=ax)
        cb.set_label("Temperatura °C")
        plt.title('Material : Acero ' + '\n' + 'Tiempo: ' + str(round(h*i,2)) + 's')
       
        plt.savefig(str(i) + '.png')
        print("Paso:",i,"  ;  Progreso :",str(int(100*i/n))+'%')
        
    
    Temp = Act_Temperatura(mancha,Temp,h,alpha)
    i = i + 1 
 
t1 = time.time()
print("Tiempo ejecucion",t1-t0,"s")
