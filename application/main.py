import textwrap
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from model.entities.pessoa_fisica import PessoaFisica
from model.entities.conta import Conta
from model.services.deposito import Deposito
from model.services.saque import Saque

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def encontrarUsuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario.cpf == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def encontrarConta(cliente):
    if len(cliente.contas)==0:
        print("Cliente não possui conta")
    else:
        return cliente.contas[0]

def registrarCliente(usuarios):
    cpf = input("Digite o CPF do cliente: ")
    if encontrarUsuario(cpf, usuarios):
        print("\nUsuário ja registrado\n")
    else:
        endereco = input("Digite o endereço do cliente: ")
        nome = input("Digite o nome do cliente: ")
        data_nascimento = input("Digite a data de nascimento do cliente: ")
        cliente = PessoaFisica(endereco, cpf, nome, data_nascimento)

        print("Usuario registrado com sucesso ! ")
        usuarios.append(cliente)
        
def registrarConta(usuarios, numero_conta, contas):
    cpf = input("Digite o cpf do cliente: ")
    usuario = encontrarUsuario(cpf, usuarios)
    
    if(usuario):
        conta = Conta(numero_conta, usuario)
        
        print("Conta criada com sucesso!")
        usuario.adicionar_conta(conta)
        contas.append(conta)
        
    else:
        print("Operação cancelada! Usúario não encontrado")
        
def listarContas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta.agencia}
            C/C:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
        
def depositar(usuarios):
    cpf = input("Digite o cpf do cliente: ")
    cliente = encontrarUsuario(cpf, usuarios)
    
    
    if not cliente:
        print("Cliente não encontrado")
        return
    conta = encontrarConta(cliente)
    if(conta):
        valor = float(input("Digite o valor de depósito: "))
            
        transacao = Deposito(valor)
            
        cliente.realizar_transacao(conta, transacao)
            
      
    
def sacar(usuarios):
    cpf = input("Digite o cpf do cliente: ")
    cliente = encontrarUsuario(cpf, usuarios)
   
    
    if not cliente:
        print("Cliente não encontrado")
        return
    
    conta = encontrarConta(cliente)
    if(conta):
        valor = float(input("Digite o valor: "))
            
        transacao = Saque(valor)
            
        cliente.realizar_transacao(conta, transacao)
            
def extrato(usuarios):
    cpf = input("Digite o cpf do cliente: ")
    cliente = encontrarUsuario(cpf, usuarios)
    
    if not cliente:
        print("Cliente não encontrado")
        return
    
    conta = encontrarConta(cliente)
    
    if conta:
        print("===== EXTRATO =====")
        transacoes = conta.historico.transacoes
        
        extrato=""
        if not transacoes:
            print("Nenhuma transação realizada")
        else:
            for transacao in transacoes:
                extrato += f"\n{transacao["tipo"]}:\n\tR${transacao['valor']:.2f}"
            print(extrato)
        
        
        print(f"\nSaldo: R${conta.saldo:.2f}")     
    
    
    
def main():
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if (opcao == "d"):
            depositar(usuarios)
        
        elif (opcao == "s"):
            sacar(usuarios)
            
        elif (opcao == "e"):
            extrato(usuarios)       
        elif(opcao == "nc"):
            
            numero_conta = len(contas) + 1
            registrarConta(usuarios, numero_conta, contas)
        
        elif(opcao == "lc"):
            listarContas(contas)
            
        elif(opcao == "nu"):
            
            registrarCliente(usuarios)
            
        elif (opcao == "q"):
            print("Encerrando o programa...")
            break
        
        else:
            print("Opção Inválida! Tente novamente")
        
        
            
            
        
            
main()



