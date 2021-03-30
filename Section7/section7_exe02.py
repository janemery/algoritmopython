"""
Section7_exe02

Faça um algoritmo que conte de 1 a 100 e a cada 
múltiplo de 10 emita uma mensagem: "Múltiplo de 10". 
"""

número = 1
recebe número
para número <= 100 processe
    escrever i
    número = número + 1
    Se número % 10 == 1 então
        imprimir número + " é múltiplo de 10"
    fim se
fim
