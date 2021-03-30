"""
Section6_exe09

A Secretaria de meio ambiente que controla o indice de poluição
mantém 3 grupos de industrias que são altamente poluentes do 
meio ambiente. o indice de poluição aceitável varia de 0,05 até
0,25. Se o índice sobe para 0,3 as industrias do 1 grupo são 
intimadas a suspenderem suas atividades, se o índice crescer para
0,4 as industrias do 1 e do 2 grupo são intimadas a suspenderem 
suas atividades, se o índice atingir 0,5 todos os grupos devem 
ser notificados a paralisarem suas atividades. Faca um algoritmo
que leia o índice de poluição medido e emita a notificação adequada
aos diferentes grupos de empresas
"""

indiceP = 0,25
limiteG1 = 0,3
limiteG2 = 0,4
limiteG3 = 0,5

recebe indiceP
Se indiceP >= 0,5 então
    "O grupo 3 deve suspender suas atividades"
Se indiceP >= 0,4 então
    "O grupo 2 deve suspender suas atividades"
Se indiceP >= 0,3 então
    "O grupo 1 deve suspender suas atividades"
Se indiceP <= 0,25 então
    imprimir "Todas as empresas do grupo podem funcionar"