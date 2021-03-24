/*
Section8_exe03
Faça um programa que carregue um vetor com 10 numeros
inteiros. mostre o vetor na ordem inversa ao que foi digitado.

*/
solução:

vetor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

para i = 0, enquanto i < 10 processe
    escreva "digite o valor: "
    recebe valor
    vetor[i] = valor

correção:

vetor = []
para i = 0, enquanto i <= 10, processar
    escrever "Digite um valor: "
    receber valor
    vetor[i] = valor

i = 9
enquanto i >= 0 processar
    escrever vetor[i]
    i = i - 1