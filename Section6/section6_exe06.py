"""
Section6_exe06

elabore um algoritmo que leia as variáveis 'c' e 'n', respectivamente
código e número de horas trabalhadas de um operário. Calcule o salário
sabendo que ele ganha R$ 10,00 por hora. Quando o número de horas 
exceder a 50 calcule o excesso de pagamento armazenando-a na variável
'e' (excesso). Caso contrário zerar tal variável. A hora excedente
de trabalho vale R$ 20,00. No final do processamento imprimir o 
salário total e o salário excedente.
"""

c = código
n = numero
h = 10
e = 20
st = salário total
se = salário excedente

receber o código do operário 'c'
receber o numero de horas trabalhadas para este 'n'
Se n <=50
    calcule n * 10
    guarde o valor em st
    imprimir "O valor de salário é " + st
Se n > 50
    calcule 50 * 10
    guarde o valor em st
    calcule (n - 50) * 20
    guarde o valor em se
    imprimir "O valor de salário total é " + st + " e o valor de salário excedente é " + se
    
_____________
correção:

e = 0
receber c 
receber n 
se n > 50 então
    e = (n - 50)
    n = n - e
extra = e * 20
salario = n * 10
escreva "Salário " + salario
escreva "Extra " + extra
