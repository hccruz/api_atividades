from models import Pessoas, Usuarios


# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Renata', idade=44)
    print(pessoa)
    pessoa.save()


# consulta dados na tabela pessoa
def consulta_pessoa():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Renata').first()
    #print(pessoa.idade)


# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Heraldo').first()
    pessoa.nome = 'Giovane'
    pessoa.idade = 17
    pessoa.save()


# Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Renata').first()
    pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consulta_todos_usuarios():
    usuario = Usuarios.query.all()
    print(usuario)


if __name__ == '__main__':
    #insere_usuario('heraldo', '1234')
    #insere_usuario('giovane', '5678')
    consulta_todos_usuarios()
    #insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    #consulta_pessoa()
