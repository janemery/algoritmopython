"""
Section6_exe10

Elabore um algoritmo que dada a idade de um nadador
classifique-o em uma das seguintes categorias:
infantil_a = 5 a 7 anos
infantil_b = 8 a 11 anos
juvenil_a = 12 a 13 anos
juvenil_b = 14 a 17 anos
adultos = maiores de 18 anos
"""

recebe idade
Se 5 <= idade <= 7 então
    imprime "A categoria do nadador é infantil_a"
Se 8 <= idade <= 11 então
    imprime "A categoria do nadador é infantil_b"
Se 12 <= idade <= 13 então
    imprime "A categoria do nadador é juvenil_a"
Se 14 <= idade <= 17 então
    imprime "A categoria do nadador é juvenil_b"
Se idade >= 18 então
    imprime "A categoria do nadador é adulto"
Senão então
    imprime "Este  nadador não está classificado em uma categoria"