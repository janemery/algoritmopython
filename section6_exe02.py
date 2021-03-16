/*
Section6_exe02
*/

elabore um algoritmo que leia um número. Se positivo, 
armazene-o em 'a', se for negativo, armazene-o em 'b'.
No final, mostrar o resultado.

Inicio
    Recebe número
    Se número > 0
        número = a
        Imprime "número a = %número%" 
    Se número < 0
        número = b
        Imprime "número b = %número%"   
    Fim
Fim


correção

Inicio
    Recebe número
    Se número > 0 então
        a = número
        imprime "Valor positivo" + " a = " + a
    Se número < 0
        b = número
        imprime "Valor negativo" + " b = " + b
    Fim Se
Fim