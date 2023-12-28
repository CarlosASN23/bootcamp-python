from models import Pessoas, Usuarios

def insere_pessoas():

    pessoa = Pessoas(nome='Carlos', idade='27')
    print(pessoa)
    pessoa.save()
def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)

def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Carlos').first()
    pessoa.idade = 20
    pessoa.save()

def exclui_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Carlos').first()
    pessoa.delete()

def insere_usuarios(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    insere_usuarios('carlos', '1234')
    insere_usuarios('marina', '123')
    #insere_pessoas()
    #altera_pessoas()
    #exclui_pessoas()
    #consulta_pessoas()
    consulta_todos_usuarios()