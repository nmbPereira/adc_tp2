"""
Funções de espetáculos

:Date: 6 Dez 2022
:Version: 0.1
:Authors: Nuno Pereira, Daniel Fordham, Lourenço Albuquerque
"""

from io_terminal import imprime_lista

nome_ficheiro_lista_de_espetaculos = "lista_de_espetaculos.pk"


def criar_espetaculo():
    """ Cria um novo espetáculo a partir de inputs do utilizador

    :return: dicionario de um espetáculo na forma
        "nome": <<nome>>, "artista": <<artista>>, "local": <<local>>
    """

    print("Insira o nome do espetáculo.")
    nome = input("> ")
    print("Insira o/a artista.")
    artista = input("> ")
    print("Insira a localização.")
    local = input("> ").upper()
    return {"nome": nome, "artista": artista, "local": local}


def imprime_lista_espetaculos(lista_de_espetaculos):
    """ Imprime a lista de espetáculos.

    :param lista_de_espetaculos:
    :return:
    """

    imprime_lista(cabecalho="Lista de Espetáculos", lista=lista_de_espetaculos)
