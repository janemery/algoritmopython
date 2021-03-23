/*
Section7_exe05

Faça um programa que leia um nome de usuário e a sua
senha e não aceite a senha igual ao nome de usuário,
mostrando uma mensagem de erro e voltando a pedir as 
informações
*/

escrever "Informe o nome"
receber nome
escrever "Informe a senha"
receber senha
    Se senha == nome então
        escrever "senha inválida"
    sair
    Senão
        escrever "Senha foi salva com sucesso"