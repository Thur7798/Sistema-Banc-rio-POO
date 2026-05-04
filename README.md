# 🏦 Sistema Bancário - POO com Python

Sistema bancário desenvolvido em Python com foco em **Programação Orientada a Objetos (POO)**, separando responsabilidades em camadas de entidades e serviços.

---

## 📁 Estrutura do Projeto

```
DESAFIO POO/
├── application/
│   └── main.py               # Ponto de entrada da aplicação
└── model/
    ├── entities/
    │   ├── cliente.py         # Classe base Cliente
    │   ├── conta.py           # Classe base Conta
    │   ├── conta_corrente.py  # Conta Corrente (herda de Conta)
    │   └── pessoa_fisica.py   # Pessoa Física (herda de Cliente)
    └── services/
        ├── deposito.py        # Serviço de depósito
        ├── historico.py       # Histórico de transações
        ├── saque.py           # Serviço de saque
        └── transacao.py       # Classe base de transação
```

---

## ⚙️ Funcionalidades

- ✅ Cadastro de usuários (Pessoa Física)
- ✅ Criação de contas bancárias
- ✅ Depósito
- ✅ Saque com validação de saldo
- ✅ Extrato com histórico de transações
- ✅ Listagem de contas cadastradas

---

## 🧠 Conceitos de POO Aplicados

| Conceito | Onde foi aplicado |
|---|---|
| **Herança** | `PessoaFisica` herda de `Cliente`, `ContaCorrente` herda de `Conta`, `Deposito`/`Saque` herdam de `Transacao` |
| **Encapsulamento** | Atributos privados com prefixo `_` em todas as entidades |
| **Properties** | Acesso controlado aos atributos via `@property` |
| **Abstração** | Classe `Transacao` define o contrato para `Deposito` e `Saque` |
| **Separação de responsabilidades** | Camadas `entities` e `services` bem definidas |

---

## ▶️ Como executar

**Pré-requisito:** Python 3.10+

```bash
# Clone o repositório
git clone https://github.com/Thur7798/Sistema-Banc-rio-POO.git

# Acesse a pasta
cd Sistema-Banc-rio-POO

# Execute
python3 application/main.py
```

---

## 🖥️ Exemplo de uso

```
================ MENU ================
[d]     Depositar
[s]     Sacar
[e]     Extrato
[nc]    Nova conta
[lc]    Listar contas
[nu]    Novo usuário
[q]     Sair
=>
```

---

## 🛠️ Tecnologias

- Python 3.10+
- Módulos nativos: `textwrap`, `sys`, `os`

---

## 👨‍💻 Autor

Desenvolvido como parte do **Desafio de POO** do bootcamp de Back-End Python da [DIO](https://www.dio.me/).
