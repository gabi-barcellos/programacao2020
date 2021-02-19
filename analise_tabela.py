#Autora: gabriela
#data:18/02/2021

import csv
from estatisticas_script import valor_maximo, valor_minimo, media_valores
caminho = input('Escreva o caminho do arquivo desejado: ')
coluna_media = int(input('Digite o número da coluna que você deseja calcular a média: '))
coluna_valor_maximo = int(input('Digite o número da coluna que você deseja calcular o valor máximo: '))
coluna_valor_minimo = int(input('Digite o número da coluna que você deseja calcular o valor mínimo: '))
#numero_linha=int(input('Digite o número da coluna com o identificador das linhas: '))
#valor_coluna_01 = int(input('Digite o numero da 1 coluna: '))
#valor_coluna_02 = int(input('Digite o numero da 2 coluna: '))
listavalormax = []
listavalormin = []
listavalormedio = []


with open(caminho) as entrada:
    if caminho in 'tsv':
        reader = csv.reader(entrada, demiliter="\t")
    else:
        reader = csv.reader(entrada)
    next(reader)  # Descarta o cabeçalho
    for line in reader:
        listavalormax.append(line[coluna_valor_maximo])
        listavalormin.append(line[coluna_valor_minimo])
        listavalormedio.append(line[coluna_media])




    val_minimo = valor_minimo(listavalormin)
    val_maximo = valor_maximo(listavalormax)
    val_medio  = media_valores(listavalormedio)


    #val_razao = razao_valores(numero_linha, valor_coluna_01, valor_coluna_02, reader)

    print('Esse é o valor maximo {}'.format(val_maximo))
    print('Esse é o valor minimo {}'.format(val_minimo))
    print('Essa é a media dos valores {}'.format(val_medio))
    #print('Essa foi a linha {}, essa a coluna1 {} e a coluna2 {}'.format(numero_linha,valor_coluna_01,valor_coluna_02 ))
