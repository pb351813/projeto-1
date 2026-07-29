from cadastro import cadastro
from visualizacao import visualizacao_geral
from visualizacao import visualizacao_individual
from movimentacao import transferencia

class cliente:
    
    nome = None
    sobrenome = None
    email = None
    saldo = None
    senha = None
    CPF = None
    
i = 0
conta = [cliente() for i in range (50)]
     

opcao = 0

while opcao != 5:
    
    print('\nESOLHA UMA OPÇÃO\n')
    print('1-cadastro de uma conta')
    print('2-visualizar uma conta')
    print('3-vizualizar todas as contas')
    print('4-realizar o login')
    print('5-finalizar processo\n')
    
    opcao = int(input(''))
    
    match opcao:
        
        case 1:
            
            i = cadastro(conta, i)
                
        case 2:
            
            visualizacao_individual(conta, i)
        
        case 3:
            
            visualizacao_geral(conta, i)
        
        case 4:
            
            transferencia(conta, i)
            
        