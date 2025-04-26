from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    def __init__(self, titular, saldo=0):
        self._titular = titular
        self._saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self._saldo:.2f}")

    @abstractmethod
    def tipo_conta(self):
        pass

    # Método protegido
    def _informacoes_basicas(self):
        return f"Titular: {self._titular}, Saldo: R${self._saldo:.2f}"

    # Método privado
    def __log_transacao(self, operacao, valor):
        print(f"LOG: {operacao} de R${valor:.2f} para {self._titular}")

class ContaPessoaFisica(ContaBancaria):
    def __init__(self, titular, cpf, saldo=0):
        super().__init__(titular, saldo)
        self.__cpf = cpf

    def tipo_conta(self):
        return "Pessoa Física"

    def dados_completos(self):
        return f"{self._informacoes_basicas()}, CPF: {self.__cpf}"

class ContaPessoaJuridica(ContaBancaria):
    def __init__(self, titular, cnpj, saldo=0):
        super().__init__(titular, saldo)
        self.__cnpj = cnpj

    def tipo_conta(self):
        return "Pessoa Jurídica"

    def dados_completos(self):
        return f"{self._informacoes_basicas()}, CNPJ: {self.__cnpj}"