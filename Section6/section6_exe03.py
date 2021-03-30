"""
Section6_exe03

ler um número e verificar se ele é par ou impar. quando for 
par, armazene esse valor em 'p' e quando for impar armazená-lo em 'i'.
exibir 'p' e 'i' no final do processo.
"""

Inicio
Receber um número
    Se número for par
        número = p 
    Se número for impar 
        numero = i
    fim se
imprimir "O valor de p é " + p + " e o valor de i é " + i "."
Fim
    
/*
correção
*/

p = 0
i = 0

Inicio
Receber um número
    Se (número / 2 == 0) então
        p = número 
    Senão 
        i = numero
    fim
imprimir "O valor de p é " + p + " e o valor de i é " + i "."