from time import sleep
print('Bem vindo ao \033[35m Banco Djovan \033[m')
print('\033[:36m==\033[m' * 14 )
print('Aguarde o nosso sistema fazer todas as otimizações...')
sleep(3)
print('\033[:36m==\033[m' * 14)
nome = str(input('Digite o seu nome '))
print('Bom te ver novamente \033[:35m{}\033[m!. =)'.format(nome))
print('\n')
p1 = input('Deseja fazer um novo empréstimo? Digite \033[:32mSim\033[m ou\033[:31m Não\033[m ')
if p1 == 'Sim':
    valor = float(input('\033[:33mDigite em R$, o valor da casa que deseja financiar:\033[m '))
    sleep(2)
    salario = float(input('\033[:33mAgora, também em R$, digite o valor do seu salário: \033[m '))
    sleep(2)
    prestacao = salario * .3
    tempo = int(input('\033[:33mPor fim, digite em anos, o tempo que você irá pagar:\033[m '))
    parcela = valor / tempo
    print('\033[:36m==\033[m' * 14)
    sleep(3)
    print('\033[:36m==\033[m' * 14)
    sleep(1)
    if parcela > prestacao:
        print('\033[:31m====EMPRÉSTIMO NEGADO====\033[m')
        info = bool(input('Deseja ter mais informações? Digite \033[:32m(1)\033[m para \033[:32mSIM\033[m e \033[:31m(0)\033[m para NÃO '))
        if info == True:
            print('\033[:36m{}\033[m, seu empréstimo foi \033[:31mnegado\033[m pois a prestação de \033[:32mR${:.3f}\033[m, excedeu \033[:33m30%\033[m do seu salário \033[:31m(R${:.3f})\033[m'.format(nome, parcela, prestacao))
            print('Tente novamente mais tarde!')
        else:
            print('Ok, obrigado pela preferência e até mais!')
    else:
        print('\033[:34m====EMPRÉSTIMO ACEITO!====\033[m')
        print('Agora que seu empréstimo foi aceito, tenha atenção para as informações a seguir:')
        sleep(3)
        print('Seu emprestimo foi aceito: As parcelas serão feitas em \033[:32mR${:.3f}\033[m por mês, até \033[:34m{} anos.'.format(parcela, tempo))
else:
    print('Ok, até mais!')

print('\033[1:97:45mObrigado por usar o BANCO DJOVAN\033[m')
