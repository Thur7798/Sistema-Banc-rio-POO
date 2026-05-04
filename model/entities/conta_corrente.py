from conta import Conta
from saque import Saque

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saque=3):
        super().__init__(numero, cliente)
        self.limite=limite
        self.limite_saque=limite_saque

    def sacar(self, valor):
        numero_saque = len(
            [transacao for transacao in self._historico.transacoes
            if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saque >=self.limite_saque

        if excedeu_limite:
            print("\nOperação Falhou ! Valor maior que o limite")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques atingido")
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência: {self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """