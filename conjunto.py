# Felos, 19 de Febrero del 2020
# Version optimizada del proyecto equilibrium


"""
Para llamar a la clase de entrada necesita una variable que contenga una
imagen cargada de la libreria imageio

Al cargar un objeto de esta clase automaticamente se clasifica los puntos donde
se ve a hacer la simulacion en el conjunto en si, su interior y su frontera
todos como  numpy arrays

"""
import numpy as np

class conjunto:
    """Define el conjunto de pixeles sobre los que se va a simular"""
    def __init__(self,img):
        def conjunto(img):
            """ Toma de input una imagen (png) y devuleve las coordenadas de los pixeles
            que no son blancos """
            conjunto = []
            for x in range( img.shape[0] - 1):
                for y in range( img.shape[1] - 1):
                    if list(img[x,y]) != [255,255,255,255]:
                        conjunto.append([self.tamaño[0] - x , y])
            return(conjunto)
     
        def frontera(conjunto,img):
            """Devulve la frontera del dibujo en la imagen"""
            frontera = []
            for r in conjunto:
                alrededores = [[r[0] + 1 , r[1] + 0],
                               [r[0] - 1 , r[1] + 0],
                               [r[0] + 1 , r[1] - 1],
                               [r[0] + 1 , r[1] + 1],
                               [r[0] + 0 , r[1] + 1],
                               [r[0] + 0 , r[1] - 1],
                               [r[0] - 1 , r[1] + 1],
                               [r[0] - 1 , r[1] - 1]]
                
                for R in alrededores:
                    if list( img[ self.tamaño[0] - R[0],R[1] ] ) != [255,255,255,255]:
                        pass
                    else:
                        frontera.append(r)
                        break
            return(frontera)
        
        def interior(conjunto,frontera):
            """Obtierne el ineterior de un conjunto"""
            interior = [r for r in conjunto if r not in frontera]
            return(interior)
        
        # Atributo y clasificacion del conjunto. 
        self.tamaño = (img.shape[0],img.shape[1])
        
        self.conjunto = np.array( conjunto(img) , dtype = np.int16 )
        self.frontera = np.array( frontera(self.conjunto,img) , dtype = np.int16)
        self.interior = np.array( interior(self.conjunto,self.frontera) , dtype = np.int16)
