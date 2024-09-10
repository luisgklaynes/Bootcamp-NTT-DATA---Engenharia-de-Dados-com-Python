from datetime import datetime

saldo_conta = 1500.00
saque_diario = 0
LIMITE_SAQUE = 3
LIMITE_VALOR_SAQUE = 500
menu = ['[1] Deposito','[2] Extrato','[3] Saque','[4] Sair',]
navegacao = ['[V] Voltar','[S] Sim','[N] Não']
extrato = [f'Saldo anterior: R$ {saldo_conta:.2f}']


def operacao_saque():
    global saldo_conta, saque_diario, LIMITE_SAQUE, LIMITE_VALOR_SAQUE
    while True:
        if saque_diario >= LIMITE_SAQUE:
            print(f'Limite de {LIMITE_SAQUE} saques diários foi atingido! Novo saque estará disponível amanhã!')
            break
        else:
            print('--/',menu[2][4:])
            saque = float(input('Informe o valor do saque --> R$ '))

            while saque > saldo_conta:
                saque = float(input('Valor do saque maior que o saldo atual \nInforme um valor válido!'))
                
            while saque > LIMITE_VALOR_SAQUE:
                saque = float(input(f'Limite de R$ {LIMITE_VALOR_SAQUE:.2f} por saque está configurado em sua conta!\nInforme um valor igual ou menor que limite! '))
                break
            dh_saque = datetime.now()
            saque_formatado = f"{saque:.2f}"
            extrato.append((f'{dh_saque.strftime("%d/%m/%Y %H:%M:%S")} - Saque: R$ {saque_formatado}'))
            saque_diario = saque_diario +1
            saldo_conta -= saque
            print(f'{dh_saque.strftime("%d/%m/%Y %H:%M:%S")} - Saque no valor de R$ {saque_formatado} realizado com sucesso !')
            nova_operacao = input(f'Deseja realizar outro saque? \n{navegacao[1]},{navegacao[2]} -->  ')
            if nova_operacao.upper() != 'S':
                break    

def operacao_deposito():
    global saldo_conta
    while True:
        print('--/',menu[0][4:])
        deposito = float(input('Informe o valor para depósito? '))
        while deposito <= 0:
            deposito = float(input( f'Não é possivel depositar R$ {deposito:.2f}, por favor informe um valor válido --> R$ '))
        deposito_formatado = f"{deposito:.2f}"
        dh_deposito = datetime.now() 
        extrato.append((f'{dh_deposito.strftime("%d/%m/%Y %H:%M:%S")} - Depósito: R$ {deposito_formatado}'))
        saldo_conta += deposito
        print(f'{dh_deposito.strftime("%d/%m/%Y %H:%M:%S")} - Depósito no valor de R$ {deposito_formatado} realizado com sucesso !')
        nova_operacao = input(f'Deseja realizar outro depósito? \n{navegacao[1]},{navegacao[2]} -->  ')
        if nova_operacao.upper() != 'S':
            break

def operacao_extrato():
    global saldo_conta
    while True:
        print('--/',menu[1][4:])
        for l in extrato:
            print(l)
        dh_extrato = datetime.now() 
        print(f'{datetime.strftime(dh_extrato, "%d/%m/%Y %H:%M:%S")} - Saldo Atual: R$ {saldo_conta:.2f}')
        break
    
while True:
    for opcao in menu:
        print(opcao)
    operacao = int(input('Informe qual operação deseja realizar '))
    
    match operacao:
    ## CANCELAR OPERAÇÃO
        case 4:
            print('--/',menu[3][4:])
            print('Operação cancelada! Volte sempre!')
            break

        ## OPERAÇÃO DE SAQUE
        case 3:
            operacao_saque()
                        
        ## OPERAÇÃO DE DEPÓSITO
        case 1:
            operacao_deposito()
        
        ## OPERAÇÃO DE EXTRATO
        case 2:
            operacao_extrato()
    