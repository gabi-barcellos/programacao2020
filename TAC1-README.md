# programacao2020
Disciplina Biofísica Ufrj 2020

from Bio.Seq import Seq
from Bio import SeqIO


def homopolimeros(letras):
    lista_homopolimeros=[]
    valor_anterior=""
    soma_valores=0
    for x in letras:
      if valor_anterior=="" or valor_anterior == x:
        valor_anterior=x
        soma_valores+=1
      else:
        if soma_valores>=3 and valor_anterior in ('A','C','T','G'):
            tupla=(valor_anterior, soma_valores, letras.index(valor_anterior)+1)
            lista_homopolimeros.append(tupla)
        soma_valores=1
        valor_anterior=x

    if soma_valores>=3 and x in ('A','C','T','G'):
      tupla=(x, soma_valores, letras.index(x)+1)
      lista_homopolimeros.append(tupla)
    print(lista_homopolimeros)
letras=str(input("Digite uma sequencia de letras: "))
letras=Seq(letras.upper())
homopolimeros(letras)
