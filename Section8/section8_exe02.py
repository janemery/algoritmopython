/*
Section8_exe02

escreva um algoritmo que leia dois vetores de 10 posições e 
faça a soma dos elementos de mesmo indice, colocando o resultado
 em um terceiro vetor. Mostre o vetor resultante.
*/
solução:
vetor1 = [1, 2, 3, 4, 5, 6, 7. 8, 9, 10]
vetor2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
vetor_res = []

para i = 0, enquanto i <= 10 processe
    recebe vetor1
    recebe vetor2
    vetor_res[i] = vetor1[i] + vetor2[i]
    i = i + 1
escreve "O Vetor resultante é: " + vetor_res

correção

vetor1 = []
vetor2 = []
vetor_res = []

para i = 0, enquanto i < 10 processar
    escrever "Digite um valor para o primeiro vetor: "
    recebe valor1
    escrever "Digite um valor para o segundo vetor: "
    recebe valor2
    vetor1[i] = valor1
    vetor2[i] = valor2
    vetor_res[i] = valor1 + valor2
    
para i = 0, enquanto i < 10 processar
escrever vetor_res

