"""
UNIVERSIDADE FEDERAL DA BAHIA
ALUNO ALEXANDRE CARVALHO DOS SANTOS
Quebra cabeça de 8 peças utilizando busca A

"""

import sys
import copy

sys.setrecursionlimit(3000000)
charger=440 # 9! numero maximo de estados alcançaveis
fronteira=[]
visited=[]
moves=[]

class State:
    def _init_(self):
        self.start = 0
        self.tab = [[0,0,0],[0,0,0],[0,0,0]] #config tabela
        self.heu = [[0,0,0],[0,0,0],[0,0,0]] #tabela heuristica
        self.profundidade = 0
        self.h = 0 #total heuristica
        self.moves=[]#armazena o histórico de movimentos feitos para chegar neste estado

estado_ini = State()
estado_ini.tab = [[0,0,0],[0,0,0],[0,0,0]]
estado_ini.heu = [[0,0,0],[0,0,0],[0,0,0]]
estado_ini.h = 0
estado_ini.moves=[]
estado_ini.profundidade = 0

goal_state = State()
goal_state.tab = [['0','1','2'],['3','4','5'],['6','7','8']]



def convert(x1,x2,x3):  
    res1 = ''.join(x1)
    res2 = ''.join(x2)
    res3 = ''.join(x3)
    res4 =res1+res2+res3
    return(res4) 

def checkgoal(est):
 if est.tab == goal_state.tab:
  return True
 else:
  return False
 
def manhatan(est):
  i=0
  j=0
  for i in range(0,3):
    for j in range(0,3):
      est.heu[i][j]=distancia(est.tab[i][j],i,j)

  i=0
  j=0
  for i in range(0,3):
    for j in range(0,3):
      est.h = int(est.h)+int(est.heu[i][j])
  
  est.h= int(est.h)+int(est.profundidade)

  
def distancia(dado,i,j):
 c=int(dado)
 a=int(nlist[c].x)-i 
 b=int(nlist[c].y)-j
 res = abs(a)+abs(b)
 return res

class Node:
    def __init__(self, data):
        self.data = data
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.x=0
        self.y=0

    def str(self):
        return str(self.data)

class arvore:

  def init(self, data):
    node=Node(data)
    self.root = node

  def buscador(self,node,est):
     global charger
     charger = charger-1
     if checkgoal(fronteira[0]) == True:
      
      moves.append(fronteira[0].acao)
      print("SOLUÇÃO ENCONTRADA PARA O PROBLEMA!")
      print("")
      print("OS "+str(fronteira[0].profundidade)+" MOVIMENTOS NECESSÁRIOS PARA OBTE-LA SÃO:")
      print("")
      print(fronteira[0].moves)
      sys.exit(); 
      
     if checkgoal(fronteira[0]) == False:

      fronteira[0].profundidade=fronteira[0].profundidade+1
      visited.append(convert(fronteira[0].tab[0],fronteira[0].tab[1],fronteira[0].tab[2]))
      #converte a tabela em string para guardar como configuração de  estado visitado
      moves.append(fronteira[0].acao)
      
      if node.left is not None:
          temp=0
          aux = State()
          aux =copy.deepcopy(fronteira[0])
          aux.start = aux.start.left
          aux.h=0
          temp=aux.tab[node.x][node.y]
          aux.tab[node.x][node.y]=aux.tab[node.x][node.y-1]
          aux.tab[node.x][node.y-1]=temp
          seq=convert(aux.tab[0],aux.tab[1],aux.tab[2])
          if seq not in visited :
           manhatan(aux)
           aux.moves.append("esquerda")
           fronteira.append(aux)
          
      if node.right is not None:
          temp=0
          aux = State()
          aux =copy.deepcopy(fronteira[0])
          aux.start = aux.start.right
          aux.h=0

          temp=aux.tab[node.x][node.y]
          aux.tab[node.x][node.y]=aux.tab[node.x][node.y+1]
          aux.tab[node.x][node.y+1]=temp
          seq=convert(aux.tab[0],aux.tab[1],aux.tab[2])
          if seq not in visited :
           manhatan(aux)
           aux.moves.append("direita")
           fronteira.append(aux)
          
      if node.up is not None:
          temp=0
          aux = State()
          aux =copy.deepcopy(fronteira[0])
          aux.start = aux.start.up
          aux.h=0

          temp=aux.tab[node.x][node.y]
          aux.tab[node.x][node.y]=aux.tab[node.x-1][node.y]
          aux.tab[node.x-1][node.y]=temp
          seq=convert(aux.tab[0],aux.tab[1],aux.tab[2])
          if seq not in visited :
           manhatan(aux)
           aux.moves.append("cima")
           fronteira.append(aux)
          
        
            
      if node.down is not None:
          temp=0
          aux = State()
          aux =copy.deepcopy(fronteira[0])
          aux.start = aux.start.down
          aux.h=0

          temp=aux.tab[node.x][node.y]
          aux.tab[node.x][node.y]=aux.tab[node.x+1][node.y]
          aux.tab[node.x+1][node.y]=temp
          seq=convert(aux.tab[0],aux.tab[1],aux.tab[2])
          if seq not in visited :
           manhatan(aux)
           aux.moves.append("baixo")
           fronteira.append(aux)


      fronteira.pop(0)
      fronteira.sort(key=lambda state: state.h, reverse=False)

      if charger<=0:
        print(" O problema nao tem solucao válida")
        sys.exit(); 

      if len(fronteira)>0:
        tree.buscador(fronteira[0].start,fronteira[0])

	    
    
if __name__ == '__main__':

  tree = arvore()

  print("")
  print("FORMATO DO ESTADO OBJETIVO (com o zero no inicio):")
  print("")
  print(goal_state.tab[0])
  print(goal_state.tab[1])
  print(goal_state.tab[2])
  print("")

  print("Digite a configuracao do estado inicial, linha por linha:")
  print("")
  print("Digite os valores da primeira linha:")

  n0 = Node(input())
  n0.x=0
  n0.y=0

  n1 = Node(input())
  n1.x=0
  n1.y=1
  
  n2 = Node(input())
  n2.x=0
  n2.y=2
  
  print("Digite os valores da segunda linha:")  
  n3 = Node(input())
  n3.x=1
  n3.y=0

  n4 = Node(input())
  n4.x=1
  n4.y=1
  
  n5 = Node(input())
  n5.x=1
  n5.y=2
  
  print("Digite os valores da terceira linha:")
  print("")
  n6 = Node(input())
  n6.x=2
  n6.y=0
  
  n7 = Node(input())
  n7.x=2
  n7.y=1
  
  n8 = Node(input())
  n8.x=2
  n8.y=2
  
  nlist = [n0,n1,n2,n3,n4,n5,n6,n7,n8]
  
  n0.down = n3
  n0.right = n1
  n2.down = n5
  n2.left = n1
  n6.up = n3
  n6.right = n7
  n8.up = n5
  n8.left = n7
  n1.down = n4
  n1.left = n0
  n1.right = n2
  n3.up = n0
  n3.right = n4
  n3.down = n6
  n5.up = n2
  n5.left = n4
  n5.down = n8
  n7.up = n4
  n7.left = n6
  n7.right = n8
  n4.up = n1
  n4.left = n3
  n4.right = n5
  n4.down = n7

  z=0
  for z in range(0,9):
  	if nlist[z].data == '0':
  		tree.root = nlist[z]

  
estado_ini.tab[0][0] = n0.data
estado_ini.tab[0][1] = n1.data
estado_ini.tab[0][2] = n2.data
estado_ini.tab[1][0] = n3.data
estado_ini.tab[1][1] = n4.data
estado_ini.tab[1][2] = n5.data  
estado_ini.tab[2][0] = n6.data
estado_ini.tab[2][1] = n7.data
estado_ini.tab[2][2] = n8.data
estado_ini.start=tree.root
estado_ini.acao=""

print("ESTADO INICIAL INSERIDO POR VOCÊ:")
print("")
print(estado_ini.tab[0])
print(estado_ini.tab[1])
print(estado_ini.tab[2])
print("")

manhatan(estado_ini)
fronteira.append(estado_ini)

tree.buscador(fronteira[0].start,fronteira[0])