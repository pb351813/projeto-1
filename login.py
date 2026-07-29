def login(conta, i):
    
    usuario = str(input('digite o CPF do usuário'))
    usuario_cpf = f"{usuario[0:3]}.{usuario[3:6]}.{usuario[6:9]}-{usuario[9:11]}"
    ver_usuario = False
    
    for j in range (i):
        
        if (conta[j].CPF == usuario_cpf):
            
            ver_usuario = True
            break
        
    login = False
    limite = 0
    
    if (ver_usuario == True):
        
        while ((login == False) and (limite < 3)):
       
            senha_usuario = int(input('digite a senha da conta'))
       
            if (conta[j].senha == senha_usuario):
           
               print('\nsenha correta, acesso autorizado')
               print(f'Nome: {conta[j].nome} {conta[j].sobrenome}')
               print(f'Email: {conta[j].email}')
               print(f'CPF: {conta[j].CPF}')
               print(f'Saldo: {conta[j].saldo:.2f}')
               login = True
               break
           
            elif (conta[j].senha != senha_usuario):
            
                limite += 1
            
                print('senha incorreta, tente novamente')
                print(f'{3-limite} tentativas restantes')
        
    return login, j        