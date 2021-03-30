"""
Section6_exe08

Faça um algoritmo que leia um número inteiro e mostre
uma mensagem indicando se esse número é par ou impar,
se é positivo ou negativo;
"""

receba o numero
se numero / numero == 1 então
    numero válido
        Se numero % 2  == 0 && numero > 0 então
            imprimir numero + " número é par e positivo"
        Se numero % 2  == 0 && numero < 0 então
            imprimir numero + " número é par e negativo"
        Se numero % 2  =! 0 && numero > 0 então
            imprimir numero + " número é impar e positivo"
        Se numero % 2  =! 0 && numero < 0 então
            imprimir numero + " número é impar e negativo"
senão
    número inválido
Fim se

correção

recebe numero n1
se n1 % 2 == 0
    escreva "Número par"
senão
    escreva "Número impar"
se (n1 > 0)
    escreva "Número maior que zero"
senão
    escreva "Número menor que zero"