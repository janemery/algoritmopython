/*
Section7_exe03

Elabore um programa que gera e escreve os números impares
dos numeros entre 100 e 200. 
*/

numero = 100
recebe numero
para numero <= 200 processe
    numero = numero + 1
Se numero % 2 != 0 então
    imprime numero
fim
______
correção

para numero = 100, enquanto i <=200 processar
    Se (i % 2 != 0) então
        escrever "Impar " + i 

(acho que falta incrementar o  valor de i na correção)