"""
Section6_exe07

desenvolva um algoritmo que:
a) Leia 4 numeros;
b) calcule o quadrado de cada um;
c) Se o valor resultante do quadrado do terceiro for >= 1000
imprima e finalize;
Caso contrário, imprima os valores lidos e seus quadrados.
"""

recebe numero 1 e guarde em n1
recebe numero 2 e guarda em n2
recebe numero 3 e guarda em n3
recebe numero 4 e guarda em n4
calcular qn1 = n1 * n1
calcular qn2 = n2 * n2
calcular qn3 = n3 * n3
calcular qn4 = n4 * n4
se qn3 >= 1000 então
    imprimir qn3
senão
    imprimir "número " + n1 " e quadrado " + qn1
    imprimir "número " + n2 " e quadrado " + qn2
    imprimir "número " + n3 " e quadrado " + qn3
    imprimir "número " + n4 " e quadrado " + qn4