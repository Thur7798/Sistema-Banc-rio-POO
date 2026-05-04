import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from model.entities.cliente import Cliente


class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._dataNascimento = data_nascimento
    
    @property
    def cpf(self):
        return self._cpf    
    
    @property
    def nome(self):
        return self._nome
    
    