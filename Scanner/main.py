mport string
from functions import *
from Scanner import *



ruta_archivo = readTxt('lenguaje.txt')

ruta_archivo = comentario(ruta_archivo)
ruta_archivo = borrarEspacios(ruta_archivo)
objeto = Scanner(ruta_archivo)
objeto.scan()
objeto.prinToken()
