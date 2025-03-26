import sys
import numpy as np

'''Função para tranformar o instância(de um grafo) lido em uma matriz, utiliza a função 
loadtxt da biblioteca numpy, que le de forma mais veloz arquivos simplesmente formatados. 
A função retorna um ndarray.'''
def transform_into_matrix(arq_name):
  filepath="./Datasets/"+arq_name+".txt"
  matrix=np.loadtxt(filepath,dtype="int32")
  return matrix

'''Função utilizada para guardar os dados retirados da instância em um arquivo .txt
os dados retirados serão, nome da instancia e as dimensões do ndarray gerado.'''
def save_result(dataset_name,lines,columns):
  archive = open("results.txt","a+")
  archive.write(f"{dataset_name}.txt {lines} {columns} \n")
  archive.close()


def main(dataset_name):
  matrix=transform_into_matrix(dataset_name)
  lines,columns=np.shape(matrix)
  save_result(dataset_name,lines,columns)
  print(dataset_name,np.shape(matrix))

'''Esta condição verifica se o script está sendo executado diretamente pelo 
interpretador Python ou se está sendo importado como um módulo em outro script.'''
if __name__ == "__main__":
  main(sys.argv[1])






