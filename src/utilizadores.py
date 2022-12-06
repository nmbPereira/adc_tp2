from io_terminal import imprime_lista

nome_ficheiro_lista_de_utilizadores = "lista_de_utilizadores.pk"


def cria_novo_utilizador():
    """ Cria um novo utilizador a partir de inputs

    :return: dicionario de um utilizador na forma
         "nome": <<nome>>, "email": <<email>>
    """

    print("Insira o nome do utilizador.")
    nome = input("> ")
    print("Insira o e-mail do utilizador.")
    email = input("> ")
    return {"nome": nome, "email": email}


def imprime_lista_de_utilizadores(lista_de_utilizadores):
    """ ..."""

    imprime_lista(cabecalho="Lista de Utilizadores", lista=lista_de_utilizadores)
