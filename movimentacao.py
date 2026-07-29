def transferencia(conta, i):
    
    from login import login
    
    login, j = login(conta, i)
    operacao = 0    
    
    while (operacao != 4):
        
        if (login == True):
            
            print('\nESCOLHA UMA OPERAÇÃO\n')
            print('1-realizar uma transferência')
            print('2-realizar um deposito')
            print('3-excluir a conta')
            print('4-realizar logout')
            operacao = int(input(''))
            
            match operacao:
                
                case 1:
                    
                    ver_remetente = False
                    k = 0
                    
                    while ((ver_remetente == False) or (k < i)):
                            
                        remetente = str(input('digite o email do remetente'))
                            
                        if (conta[k].email == remetente):
                                
                            print(f'Remetente: {conta[k].nome} {conta[k].sobrenome}')
                            ver_remetente = True
                            break
                                    
                            
                        else:
                                
                            k += 1
                            
                    print(f'\nSaldo disponível: {conta[j].saldo:.2f}\n')
                                        
                    valor = float(input('digite o valor da operação:'))
                    restante = conta[j].saldo - valor
                    
                    if (restante < 0):
                        
                        while (restante < 0):
                        
                            print('valor do saldo excedido, digite novo valor')
                            valor = float(input('digite o novo valor'))
                            restante = conta[j].saldo - valor
                                        
                    elif (restante >= 0):
                                        
                        conta[j].saldo = conta[j].saldo - valor
                        conta[k].saldo = conta[k].saldo + valor
                            
                        
                case 2:
                    
                    valor = float(input('digite o valor do depósito'))
                    conta[j].saldo += valor
                    
                    print(f'Saldo atual: {conta[j].saldo:.2f}')
                            
                case 3:     
                                
                                
                    senha = int(input('digite a senha'))
                    ver_senha = False
                    
                    while (ver_senha == False):
                                            
                        if (senha == conta[j].senha):
                            
                            print('senha correta, excluindo a conta')
                            
                            conta[j].nome = None
                            conta[j].sobrenome = None
                            conta[j].email = None
                            conta[j].CPF = None
                            conta[j].saldo = None
                            conta[j].senha = None
                        
                        elif (senha != conta[j].senha):
                            
                            senha = int(input('digite a senha correta'))