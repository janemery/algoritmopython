/*
Section7_exe04

construa um algoritmo que leia 10 valores inteiros
e positivos e:
a) Encontre o maior valor
b) Encontre o menor valor
c) Calcule a média dos números lidos
*/

correção

maior = -999
menor = 999
soma = 0
para i=0, enquanto i <= 10 processar
    receber valor
    enquanto valor < 0 processar
        receber valor
        se valor > maior então
            maior = valor
        se valor < menor então
            menor = valor
        soma  = soma + valor
escrever "Maior " + maior
escrever "Menor " + menor
escrever "Média " + (soma / 10)
