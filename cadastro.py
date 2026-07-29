def cadastro(conta, i):
    
    
    conta[i].nome = str(input("digite o nome:"))
    conta[i].sobrenome = str(input("digite o sobrenome:"))
                
    conta[i].email = str(input("digite o email:"))
    
    k = 0
    
    while (k < i):
            
        if (conta[k].email == conta[i].email):
                
            print(f'Email ja cadastrado')
            print(f'escolha outro email')
                
            conta[i].email = str(input("digite o email:"))
            
            k = 0
            
        else:
            
            k += 1
            
    CPF = str(input('digite o numero do CPF:'))
    
    while (len(CPF) != 11):
    
        CPF = str(input('digite um CPF válido'))
    
    conta[i].CPF = f"{CPF[0:3]}.{CPF[3:6]}.{CPF[6:9]}-{CPF[9:11]}"
    k = 0
    
    while (k < i):
                  
        if (conta[k].CPF == conta[i].CPF):
            
            print(f'CPF ja cadastrado')
            CPF = str(input('digite um CPF válido:'))
            k = 0
            
            while (len(CPF) != 11):
            
                CPF = str(input('digite um CPF válido'))
                k = 0
            
            conta[i].CPF = f"{CPF[0:3]}.{CPF[3:6]}.{CPF[6:9]}-{CPF[9:11]}"
            
        else:
            
            k += 1
                    
    conta[i].senha = int(input('defina uma senha de 4 digitos'))
        
    conta[i].saldo = float(input('digite o saldo inicial da conta:'))
                
    return i+1