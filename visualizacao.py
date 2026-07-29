def visualizacao_individual(conta, i):
    
    busca_CPF = str(input('Digite o CPF do cliente: '))
    busca_CPF = f"{busca_CPF[:3]}.{busca_CPF[3:6]}.{busca_CPF[6:9]}-{busca_CPF[9:11]}"
    
    encontrou = False
    
    for j in range (i):
        
        if (conta[j].CPF == busca_CPF):
            
            print(f'\nCliente: {conta[j].nome} {conta[j].sobrenome}')
            print(f'Email: {conta[j].email}')
            print(f'CPF: {conta[j].CPF}')
            print(f'Saldo: {conta[j].saldo:.2f}')
    
            encontrou = True
        
    if not encontrou:
        
        print(f'Cliente não encontrado')
              
def visualizacao_geral(conta, i):
    
    for j in range (i):
        
        print(f'\nCliente: {conta[j].nome} {conta[j].sobrenome}')
        print(f'Email: {conta[j].email}')
        print(f'CPF: {conta[j].CPF}')
        print(f'Saldo: {conta[j].saldo:.2f}')