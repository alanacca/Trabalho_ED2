import argparse
import time
from grafo import Grafo
import algoritmosDeOrdenacao as ai
from utils import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("Resposta", type=str)
    parser.add_argument("vertices", type=str)
    parser.add_argument("ordenacao",type=str)

    args = parser.parse_args()

    ordenacao = args.ordenacao

    if(ordenacao.lower()=='insert'):
        algoritimoDeOrdenacao = ai.Insert_SortAux()
    elif(ordenacao.lower()  =='quick'):
        algoritimoDeOrdenacao = ai.Quicksort()
    elif(ordenacao.lower()=='quickp'):
        algoritimoDeOrdenacao = ai.Quicksort_InsertP()
    elif(ordenacao.lower()=='quickf'):
        algoritimoDeOrdenacao = ai.Quicksort_InsertF()
    elif(ordenacao.lower()=='merge'):
        algoritimoDeOrdenacao = ai.Mergesort()
    elif(ordenacao.lower()=='mergep'):
        algoritimoDeOrdenacao = ai.Mergesort_InsertP()
    elif(ordenacao.lower()=='mergef'):
        algoritimoDeOrdenacao = ai.Mergesort_InsertF()
    
    cTime = time.time()
    

    resp = args.Resposta
    arquivoSaidaAux = resp+".txt"
    arquivoJson = args.vertices+"vertices.json"
    arquivoDeSaida = arquivoSaidaAux

    grafo = Grafo()
    grafo.estabelecerAlgoritmoDeOrdencao(algoritimoDeOrdenacao)
    grafo.carregarGrafo(arquivoJson)

    arvoreGeradoraMinima =  grafo.executarKruskal() 
    SalvarArvoreGeradoraMinimaEmArquivo(arquivoDeSaida, arvoreGeradoraMinima)

    fTime = time.time()

    tempo = fTime-cTime
    print("Execucao: ",tempo)