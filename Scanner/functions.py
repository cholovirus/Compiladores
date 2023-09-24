def readTxt(ruta):
  ruta_archivo = ruta
  contenido = ""
  try:
    with open(ruta_archivo, 'r') as archivo:
      contenido = archivo.read()
  except FileNotFoundError:
    print(f"No se pudo encontrar el archivo en la ruta: {ruta_archivo}")
  except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {str(e)}")

  return contenido

def borrarEspacios(text):
  textTemp = ""
  for i in range(len(text)):
    if (text[i] == '\n' or text[i] == ' '):
      continue
    textTemp += text[i]

  return textTemp

def comentario(text):
  flag = False
  flag2 = False
  cont = 0
  textTemp = ""
  for i in range(len(text)):
    if (text[i] == "$"):
      flag = True
      continue
    elif (flag):
      if (text[i] == '\n' ):
          flag = False
      continue

    
    if( text[i] == "#" ):
      flag2 = True
      cont +=1
      if(cont ==2):
        flag2 = False
        cont =0
      continue
      
    elif (flag2):

      continue
    textTemp += text[i]

  return textTemp

