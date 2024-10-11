#Criando um Banco em Python, operação simples.

menu = '''
[d] Depositar 
[s] Sacar
[e] Extrato 
[q] Sair
       '''
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opçao = input(menu)
    
    if opçao == 'd':
        valor = float(input('Digite o valor a ser depositado: '))

        if valor > 0 : # aqui verificamos se o valor para que seja positivo, ou seja o valor não pode ficar negativo em um deposito.
            saldo += valor #aqui conferimos o saldo com deposito para que seja mostrado o valor. 
            extrato += f'Depósito: R$ {valor:.2f}\n'
        
        else:
            print('Operação encerrada! Valor inválido.')

    elif opçao == 's':
        valor = float(input('Digite o valor a ser sacado: '))

        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if valor:
            print('Saque realizado com sucesso!')

        elif excedeu_saldo:
            print(f'Operação falhou! Saldo insuficiente!. ')

        elif excedeu_limite:
            print('Operação falhou! Valor do saque excede o limite permitido.')

        elif excedeu_saques:
            print(f'Operação falhou! Você atingiu o valor de saque permitido. ')

        elif valor > 0: #aqui e para verificar se ele está tentando sacar um valor negativo na conta. se isso acontecer ele cai no else valor invalido.
            saldo -= valor # aqui verificamos o saldo se positivo com o valor sacado. 
            extrato += f'Saque: R${valor:.2f}\n' # registra o historico de movimentação 
            numero_saques += 1 # aqui incrementamos +1 para que não comece do zero, então o usuário pode fazer os 3 saque e no proximo ja não consiga mais fazer pois tera atingindo o limite maximo de 3 saques
            print('Saque realizado com sucesso! Valor sendo entregue.')
        else: 
            print('Operação falhou! Valor informado é invalido.')

    
    elif opçao == 'e':
        print('\n========== EXTRATO ==========')
        print('Não foram feitas movimentações.' if not extrato else extrato) # if ternario, onde verificamos se o extrato está vazio, se tiver sido feito movimentações, exibimos essa movimentação no com o comando abaixo.
        print(f'\nSaldo: R$ {saldo:.2f} ')
        print('===============================')

    elif opçao == 'q':
        print('Operação encerrada!')
        break
    else:
        print('Operação invalida! Por favor, selecione uma operação valida.')
