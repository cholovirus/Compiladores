import string

from tabulate import tabulate

class Scanner:
  #ID, alfabeto
  letras_mayusculas = list(string.ascii_uppercase)
  letras_minusculas = list(string.ascii_lowercase)
  numeros = [str(i) for i in range(10)]
  letter = letras_mayusculas + letras_minusculas
  iD = letras_mayusculas +letras_minusculas + numeros
  
  
  keyWords= ["False","True", "Y",   
  "break","def","simon","resimon","queda","for","llega","nel","O","result","while", "null"]
  operadores ={
    '=':'Asignacion',
    '==':'Igual', 
    '<=':'MenorI', 
    '>=':'MayorI',
    '!=':'Diferente',
    '>':'Mayor', 
    '<':'Menor', 
    '/':'Division',
     '-':'Menos',
    '+':'Mas', 
    '*':'Multi',
    '&&':'And', 
    '||':'Or',
    '~':'Not',
    '%':'Mod',
}
  delimitadores = { 
    '.':'PUNTO',
    ':':'2PUNTOS', 
    ';':'PUNTOCOMA', 
    ',':'COMA',
    '[':'Lcol', 
    ']':'Rcol',
    '{':'Lkey', 
    '}':'Rkey',
    '(':'Lbrack', 
    ')':'Rbrack',
}
  literales= {'bool': 'BOOLEAN',
    'int': 'INTEGER',
    'INT': 'INTEGER',
    'float': 'FLOAT',
    'FLOAT': 'FLOAT',         
}
  coment = {"$,##"}

  def __init__(self, input_string):
        self.input_string = input_string+"$"
        self.pointer = 0
        self.pointerInicio = 0
        self.inputLen = len(input_string)
        self.token = []
  
  def getchar(self,text,i):
    self.pointer+=1
    return text[i]
  
  
  def peekchar(self,text,i):
    if(len(text)< i+1 or text[i]=='$'):
      return 0
    else:
      return text[i+1]


  def ID(self,stack,nToken):
    flag = False

    for i in self.keyWords:
      if(stack == i):
        return False

    for i,d in self.literales.items():
      if(stack == i):
        return False
        
    for i in self.letter:
      if (stack[0]==i):
        flag = True
    
    for i in self.iD:
      if (nToken == i):
        return flag

    return False

    
  def num(self,stack,nTok):
    flag = False
    for i in self.numeros:
      if (stack[0]==i):
        flag = True

    for i in self.numeros:
      if (nTok == i):
        return flag
    return False
  def getToken(self,stack):

    
    for key in self.keyWords:
      if (stack== key):
        tokenTemp = ["DEBUG SCAN","KeyWord - ", stack,self.pointerInicio,self.pointer]
        self.token.append(tokenTemp)
        return True

    
    for op , description in self.operadores.items():
      if (stack== op):
        tokenTemp = ["DEBUG SCAN",description, stack,self.pointerInicio,self.pointer]
        self.token.append(tokenTemp)
        return True

    for delimites , description in self.delimitadores.items():
      if (stack== delimites):
        tokenTemp = ["DEBUG SCAN", description, stack,self.pointerInicio,self.pointer]
        self.token.append(tokenTemp)
        return True

    for liter , description in self.literales.items():
      if (stack== liter):
        tokenTemp = ["DEBUG SCAN", description , stack ,self.pointerInicio,self.pointer]
        self.token.append(tokenTemp)
        return True

    tokenTemp = ["DEBUG SCAN","ID", stack ,self.pointerInicio,self.pointer]
    self.token.append(tokenTemp)
    return True
    
  def scan(self):
    stack = ""
    nextToken =""
    flag = False
    for i in range(self.inputLen):
      if(flag):
        flag = False
        continue
      stack += self.getchar(self.input_string,i)
      nextToken = self.peekchar(self.input_string,i)
     
      if(nextToken==0):
        break
    
      if(self.ID(stack,nextToken)):
        continue
      if(self.num(stack,nextToken)):
        continue
      sTemp = stack+nextToken
      for j,d in self.operadores.items():
        if(sTemp == j):
          stack=sTemp
          self.pointer+=1
          flag = True
          continue 

      if(self.getToken(stack)):
        
        stack = ""
        self.pointerInicio=self.pointer
     
  
  def prinToken(self):
  
    print("INFO SCAN - Start scanning. . .")
    
    headers = ["DEBUG SCAN","TypeToken", "Token", "Inicio","Fin"]
    print(tabulate(self.token, headers, tablefmt="grid"))
  
