
import math
import numpy as np


# Util para generar una distribuicion inicial de temperatura. 
def Gausiana_2d(x,y,Amplitud,centro,var):
    """Función Gaussiana en dos dimenciones """
    a = pow((x-centro[0]),2) / ( 2*pow(var[0],2) )
    b = pow((y-centro[1]),2) / ( 2*pow(var[1],2) )
    return( float(Amplitud*math.exp( -(a + b) ) ))


def axx(Temp,img):    
    """
    Obtiene las  dobles parciales de x de las temperaturas.
    input: Temp = Array de mapa de temperatura inicial , img = clase conjunto
    output: Array con la dobleParcial en x. 
    
    """
    interior = img.interior
    frontera = img.frontera
    tamaño = img.tamaño
    
    axx = np.zeros(tamaño, dtype= np.float64)    
    #axx = np.array([[float(0) for x in range(tamaño[0])] for y in range(tamaño[1])] )
       
    for r in interior:
        axx[r[0],r[1]] = Temp[r[0]+1, r[1] ] + Temp[ r[0]-1,r[1] ] - 2*Temp[r[0],r[1]]
    
    for r in frontera:
       if Temp[r[0]+1,r[1]] == 0:
           Temp[r[0]+1,r[1]] = Temp[r[0],r[1]]
       if Temp[r[0]-1,r[1]] == 0:
           Temp[r[0]-1,r[1]] = Temp[r[0],r[1]]
       
       axx[r[0],r[1]] = Temp[r[0]+1, r[1] ] + Temp[ r[0]-1,r[1] ] - 2*Temp[r[0],r[1]]
    return axx   
       
           
def ayy(Temp,img):
    """
    Analogo a la funcion axx
    
    """
    
    interior = img.interior
    frontera = img.frontera
    tamaño = img.tamaño
    
    ayy = np.zeros(tamaño, dtype= np.float64)   
    #ayy = np.array([[float(0) for x in range(tamaño[0])] for y in range(tamaño[1])] )
        
    for r in interior:
        ayy[r[0],r[1]] = Temp[r[0], r[1]+1 ] + Temp[ r[0],r[1]-1 ] - 2*Temp[r[0],r[1]]
    
    for r in frontera:
       if Temp[r[0],r[1]+1] == 0:
           Temp[r[0],r[1]+1] = Temp[r[0],r[1]]
       if Temp[r[0],r[1]-1] == 0:
           Temp[r[0],r[1]-1] = Temp[r[0],r[1]]
       
       ayy[r[0],r[1]] = Temp[r[0], r[1]+1 ] + Temp[ r[0],r[1]-1 ] - 2*Temp[r[0],r[1]]
    return ayy


def Act_Temperatura(conjunto,Temp,dt,alpha):
    """
    Genera un nuevo paso en el timepo con  metodo numerico generando, un 
    nuevo mapa de temperaturas. 
    
    """
    a = alpha # Abreviar 
    tamaño = conjunto.tamaño
    Axx = axx(Temp,conjunto)
    Ayy = ayy(Temp,conjunto)
    # Nueva temperatura
    N_Temp =  np.zeros(tamaño, dtype= np.float64) 
    #N_Temp = np.array([[float(0) for x in range(tamaño[0])] for y in range(tamaño[1])] )
    
    # Operaciones con numpy arrays. (Metodo numerico para el tiempo)
    #N_Temp = Temp + a*(Axx + Ayy)*dt
    for r in conjunto.conjunto:        
        c = Temp[ r[0],r[1] ] + a*(Axx[r[0],r[1]] + Ayy[r[0],r[1]])*dt
        N_Temp[r[0],r[1]] = c 
    
    return N_Temp



            