/*
Section7_exe06

desenvolva um gerador de tabuada, capaz de gerar
a tabuada de qualquer número inteiro entre 1 e 10.
o usuário deve informar de qual numero ele deseja 
ver a tabuada. A saída deve ser conforme o exemplo
abaixo:

Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
*/

escrever "Qual o número que você deseja ver a tabuada?"
receber numero
escrever "Tabuada de " + numero
para (i=0, i <= 10, i=1+)
    resultado = numero * i 
    escrever numero + " X " + i " = " + resultado 