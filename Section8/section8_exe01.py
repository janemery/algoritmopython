/*
Section8_exe01
faça um algoritmo que carregue um vetor de 5 elementos
inteiros e em seguida armazene em um vetor apenas os 
números pares maiores que zero. no final deve mostrar
os elementos do vetor na tela.
*/

num lista[5]
recebe numero
Se numero % 2 == 0 && numero > 0, Processe
    lista(i) = numero
    i+ = 1
    escreve "Vetor: " + numero
fim se 

correção
vetor = [0, 0, 0, 0, 0]
pares = []
para i = 0, enquanto i < 5 processar
    escrever "Digite um valor: "
    receber vetor[i]
    Se (vetor[i] > 0) and (vetor[i] % 2 == 0) então
        adicionar vetor[i] em pares
    escrever pares
