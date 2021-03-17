/*
Section6_exe05
*/
/*
João da Silva, pescador, comprou um microcomputador para controlar 
o rendimento diário de seu trabalho. Toda vez que ele traz um peso
peixes maior que o estabelecido pelo regulamento de pesca do estado
de SP (50KG) deve pagar uma multa de R $4 por quilo excedente;
joão precisa que você faça um algoritimo que leia a variavel 'p' 
(peso de peixes) e verifique se há excessos. Se houver, gravar
na variável 'e' (excesso) e na variavel 'm' o valor de multa que 
joão deverá pagar. Caso contrário mostrar tais variáveis com o 
conteudo 'zero'.
*/

e = 0
m = 0

recebe p 
Se p for menor ou igual a 50
   imprime "P =" + p "e e=zero e m=zero"
Se p for maior que 50
   calcular quantos quilos a mais que 50 ele trouxe e = p - 50
   multiplicar o excedente por 4. m = e * 4
   imprime "P = 'p'" e "e='e' e m = 'm''"

correção

e = 0
m = 0
p = peso
recebe p
Se p for maior que 50 então
   calcular quantos quilos a mais que 50 ele trouxe e = p - 50
   multiplicar o excedente por 4. m = e * 4
   imprime "P = " + p + ", e= " + e + "e m= " + m 
Se p for menor ou igual a 50
   imprime "P = " + p + "e e=zero e m=zero"
