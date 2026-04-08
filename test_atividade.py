from atividade import login
from atividade import cadastrar_cliente
import pytest

def test_login_sucesso():
    assert login("Nicolas", "0511") == "Login realizado com sucesso"

def test_senha_incorreta():
    assert login("Nicolas", "errada") == "Senha incorreta"

def test_usuario_inexistente():
    assert login("Vinicios", "1234") == "Usuário não cadastrado"

def test_campos_vazios():
    assert login("", "") == "Algum campo obrigatório está vazio"


def test_cadastro_sucesso():
    assert cadastrar_cliente("Nicolas", "12345678901", "teste@gmail.com", "41999999999") == "Cadastro realizado com sucesso"

def test_nome_vazio():
    assert cadastrar_cliente("", "12345678901", "teste@gmail.com", "41999999999") == "Nome obrigatório"

def test_cpf_invalido():
    assert cadastrar_cliente("Nicolas", "123", "teste@gmail.com", "41999999999") == "CPF inválido"

def test_email_invalido():
    assert cadastrar_cliente("Nicolas", "12345678901", "testegmail.com", "41999999999") == "E-mail inválido"

def test_telefone_vazio():
    assert cadastrar_cliente("Nicolas", "12345678901", "teste@gmail.com", "") == "Campo telefone está em branco"

    