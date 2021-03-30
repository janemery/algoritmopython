"""
exercicio Rodrigo
Section4_exe01

transferencia com saldo bancário
"""

saldo = 100
valor_transf = 30

if(valor_transf > saldo):
    print("Saldo insuficiente")
else:
    print("transferencia realizada")
    saldo = saldo - valor_transf
    #str restante = saldo
    print("O Saldo após a tranferencia é: " + str(saldo))
