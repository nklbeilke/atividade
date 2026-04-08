def login(usuario, senha):
    usuarios = {
        "Nicolas": "0511",
    }

    if not usuario or not senha:
        return "Algum campo obrigatório está vazio"

    if usuario not in usuarios:
        return "Usuário não cadastrado"

    if usuarios[usuario] != senha:
        return "Senha incorreta"

    return "Login realizado com sucesso"



def cadastrar_cliente(nome, cpf, email, telefone):

    if not nome:
        return "Nome obrigatório"

    if not cpf or len(cpf) != 11 or not cpf.isdigit():
        return "CPF inválido"

    if "@" not in email:
        return "E-mail inválido"

    if not telefone:
        return "Campo telefone está em branco"

    return "Cadastro realizado com sucesso"

