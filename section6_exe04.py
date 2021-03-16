/*
Section6_exe04
*/

tendo como dados de entrada a altura e o sexo de uma pessoa,
construa um algoritmo que calcule seu peso ideal, utilizando
as seguinntes formulas:
para homens: (72.7 * altura) - 58
para mulheres: (62.1 * altura) - 44.7

receba o sexo da pessoa = Sx 
receba a altura da pessoa = Al 

Inicio
Se Sx = F ou f 
    Pid = (62.1 * altura) - 44.7
Se Sx = M ou m
    Pid = (72.7 * altura) - 58
    fim Se
imprimir o valor de Pid
fim