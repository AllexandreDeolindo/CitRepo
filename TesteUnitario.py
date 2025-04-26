
import pytest
from ContaBancaria import ContaPessoaFisica, ContaPessoaJuridica

@pytest.fixture
def conta_pf():
    return ContaPessoaFisica("Carlos José", "123.456.789-00", 1000)

@pytest.fixture
def conta_pj():
    return ContaPessoaJuridica("Empresa", "12.345.678/0001-99", 5000)

def test_deposito(conta_pf):
    conta_pf.depositar(500)
    assert conta_pf._saldo == 1500

def test_saque_valido(conta_pf):
    conta_pf.sacar(300)
    assert conta_pf._saldo == 700

def test_saque_invalido(conta_pf):
    conta_pf.sacar(2000)
    assert conta_pf._saldo == 1000

def test_tipo_conta(conta_pf, conta_pj):
    assert conta_pf.tipo_conta() == "Pessoa Física"
    assert conta_pj.tipo_conta() == "Pessoa Jurídica"

def test_dados_completos(conta_pf, conta_pj):
    assert "CPF" in conta_pf.dados_completos()
    assert "CNPJ" in conta_pj.dados_completos()

#python -m pytest TesteUnitario.py