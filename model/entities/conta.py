import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from model.services.historico import Historico

class Conta:
    def __init__(self, numero, cliente):
        self._numero=numero
        self._cliente=cliente
        self._saldo=0
        self._agencia="0001"
        self._historico=Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)
    
    @property
    def numero(self):
        return self._numero  
    
    @property
    def saldo(self):
        return self._saldo

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        if valor > self._saldo:
            print("Operação falhou! Saldo insuficiente")
        elif valor>0:
            self._saldo-=valor
            print("Valor sacado com sucesso")
            return True
        else:
            print("Erro! Operação Falhou")

        return False
    
    def depositar(self, valor):
        if valor<0:
            print("Valor inválido")

        elif valor>0:
            self._saldo+=valor
            print("Valor depositado com sucesso")
            return True
        
        else:
            print("Erro! Operação Falhou")
            
        return False

        