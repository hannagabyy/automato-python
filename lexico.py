import re
palavras_reservadas = ['program', 'if', 'then', 'else', 'while', 'double', 'until',
                           'repeat', 'int', 'do', 'char', 'case', 'switch',
                           'end', 'procedure', 'function', 'for', 'begin']

def lexico():  
    arquivo = open('texto.txt')
    texto = arquivo.read()
    global cadeia, estado,linha

    i = 0
    linha = 0
    zeraEstadoeCadeia() 

    while i <= len(texto):

         
        # se for o ultimo caractere do arquivo
        if i == len(texto):
          if(cadeia != ""):
            tokenIsValido()
          break

        # if texto[i] == '\n':
        #   linha+=1 
       
      

####################### estado 0 ####################################
        if estado == 0:
          if re.search(r"[a-z]", texto[i]) is not None :
            mudaEstado(1, texto[i])
            i+=1
            
            # print(cadeia)
          elif texto[i] in '>:+': 
            mudaEstado(4, texto[i])
            i+=1
          elif texto[i] == '-':
            mudaEstado(12,texto[i])
            i+=1  
            # print(cadeia)

          elif texto[i] in (';,.*(){}='):
            mudaEstado(6, texto[i])
            i+=1
            
          elif texto[i] == '<':
            mudaEstado(7, texto[i])
            i+=1

          elif texto[i].isdigit():
            mudaEstado(9, texto[i])
            i+=1
          elif texto[i] == '@':
            mudaEstado(13,texto[i])
            i+=1
          elif texto[i] == '/':
            mudaEstado(16,texto[i])
            i+=1
          elif texto[i] == ' ' or texto[i] == '\n':
            i+=1
          else:
            cadeia = texto[i]
            
            tokenIsValido()
            break
            # i+=1
            # print(f'[ [ERRO] {cadeia} ->  token inválido]')
            # break 

####################### estado 1 ####################################
        elif estado == 1:
          if texto[i] == '_' or texto[i] == '-':
            mudaEstado(2, texto[i])
            i+=1
            # print(cadeia)
          elif re.search(r"[a-z]", texto[i]) is not None or texto[i].isdigit():
            mudaEstado(3, texto[i])
            i+=1
            # print(cadeia)
          else:    
            i+=1     
            tokenIsValido()
            zeraEstadoeCadeia()      
            
####################### estado 2 ####################################
        elif estado == 2:
            if re.search(r"[a-z]", texto[i]) is not None or texto[i].isdigit():
                mudaEstado(3, texto[i])
                i+=1
            # print(cadeia)
            else:
            # texto[i]isvalido()
              
              tokenIsValido()
              zeraEstadoeCadeia()
                
                

####################### estado 3 ####################################                  
        elif estado == 3:
            if re.search(r"[a-z]", texto[i]) is not None or texto[i].isdigit():
                mudaEstado(3, texto[i])
                i+=1
            # print(cadeia)
            else:
            
              tokenIsValido()
              zeraEstadoeCadeia()
              
                                
######################## estado 4 ####################################
        elif estado == 4:
          if texto[i] == '=':
            mudaEstado(5, texto[i])
            i+=1
            # print(cadeia)
          else:
            
            tokenIsValido()
            zeraEstadoeCadeia()
            
# ####################### estado 5 e 6 e 15####################################
        elif estado == 5 or estado == 6 or estado == 15 or estado == 8:  
            tokenIsValido()
            zeraEstadoeCadeia()

# ####################### estado 7 ####################################              
        elif estado == 7:
          if texto[i] == '>' or texto[i] == '=':
            mudaEstado(8, texto[i])
            i+=1
          else:
            
            tokenIsValido()
            zeraEstadoeCadeia()

# ####################### estado 9 ####################################              
        elif estado == 9:
          if texto[i] == ',':
            mudaEstado(10, texto[i])
            i+=1
          elif texto[i].isdigit():
            mudaEstado(9,texto[i])
            i+=1
          else:
            
            tokenIsValido()
            zeraEstadoeCadeia()
            
####################### estado 10 ####################################
        elif estado == 10:
            if texto[i].isdigit():
                mudaEstado(11, texto[i])
                i+=1
            else:
                # tokenIsValido()
                zeraEstadoeCadeia()
                                

# ####################### estado 11 ####################################              
        elif estado == 11:
          if texto[i].isdigit():
            mudaEstado(11, texto[i])
            i+=1
          else:
            tokenIsValido()
            zeraEstadoeCadeia()
                                   
# ####################### estado 12 ####################################              
        elif estado == 12:
          if texto[i] == '=':
            mudaEstado(5, texto[i])
            i+=1
          elif texto[i].isdigit():
            mudaEstado(9,texto[i])
            i+=1 
          else:
            tokenIsValido()
            zeraEstadoeCadeia()

# ####################### estado 13 ####################################              
        elif estado == 13:
          if texto[i] == '@':
            mudaEstado(14, texto[i])
            i+=1
          else:
            
            tokenIsValido()
            zeraEstadoeCadeia()
                 
# ####################### estado 14 ####################################              
        elif estado == 14:
          if texto[i] == "\n":
            estado = 15
          else:
            mudaEstado(14, texto[i])
            i+=1         

                          
# ####################### estado 16 ####################################              
        elif estado == 16:
          if texto[i] == '/':
            mudaEstado(17, texto[i])
            i=i+1 

          elif texto[i] == '*':
            mudaEstado(21, texto[i])
            i=i+1                  
          else:
            
            tokenIsValido() 
            zeraEstadoeCadeia()
            
# # ####################### estado 17 ####################################              
        elif estado == 17:
          mudaEstado(18, texto[i])
          i = i+1 
           

# # ####################### estado 18 ####################################              
        elif estado ==18:
          if texto[i] == '/':
            mudaEstado(19, texto[i])
            i = i+1 
          else:
            mudaEstado(18, texto[i])
            i=i+1
# # ####################### estado 19 ####################################              
        elif estado == 19:
          if texto[i] == '/':
            mudaEstado(20, texto[i])  
          else:
            mudaEstado(18, texto[i])
            i = i+1
# # ####################### estado 21 ####################################              
        elif estado == 20:
          tokenIsValido()
          zeraEstadoeCadeia()
          i+=1
          
# # ####################### estado 21 ####################################              
        elif estado == 21:
            mudaEstado(22, texto[i])
            i = i+1 
          
# # ####################### estado 22 ####################################              
        elif estado == 22:
          if texto[i] == '*':
            mudaEstado(23, texto[i])
            i = i+1 
          else:
            mudaEstado(22, texto[i])
            i=i+1                

# # ####################### estado 23 ####################################              
        elif estado == 23:
          if texto[i] == '/':
            mudaEstado(24, texto[i])  
          else:
            mudaEstado(22, texto[i])
            i = i+1          
          
# # ####################### estado 24 ####################################              
        elif estado == 24:
          tokenIsValido()
          zeraEstadoeCadeia()
          i+=1

def notComentario(estado):
  if (estado in [21, 22, 23, 17, 18, 19, 14]) == False:
    return True
  

def zeraEstadoeCadeia():#zera estado e cadeia
  global estado, cadeia
  estado = 0
  cadeia = ""

def mudaEstado(novoEstado, caracter):
  global estado, cadeia
  estado = novoEstado
  cadeia += caracter

def tokenIsValido():
    if estado == 3 and cadeia in palavras_reservadas:
      print(f'[ {cadeia} -> PALAVRA RESERVADA]')
    elif (estado == 3 or estado == 1):
      print(f'[ {cadeia} -> IDENTIFICADOR]') 
    elif( estado == 4 or estado == 5 or estado ==6 or estado == 7 or estado == 8 or estado == 12 or estado ==13 or estado == 16) :
      print(f'[ {cadeia} -> SIMBOLO ESPECIAL]')
    elif(estado == 9 or estado == 11) :
      print(f'[ {cadeia} -> DÍGITO]') 
    elif(estado == 15 or estado == 20 or estado == 24):
      pass     
    else:
      print(f'[ [ERRO] na linha : {linha}] ]')
      print(f'[ [ERRO] {cadeia} -> Token inválido] ]')
           
lexico()
# Verificar o erro no comentario e printar 

