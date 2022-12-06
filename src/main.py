"""
Menu principal da aplicação de venda de bilhetes

:Date: 6 Dez 2022
:Version: 0.1
:Authors: Nuno Pereira, Daniel Fordham, Lourenço Albuquerque
"""

from espetaculos import (
    nome_ficheiro_lista_de_espetaculos,
    imprime_lista_espetaculos,
    criar_espetaculo
)
from utilizadores import (
    cria_novo_utilizador,
    nome_ficheiro_lista_de_utilizadores,
    imprime_lista_de_utilizadores
)
from io_ficheiros import (
    ler_ficheiro,
    guardar_ficheiro
)


def menu():
    """ Menu principal da aplicação"""

    lista_de_bilhetes = []
    lista_de_espetaculos = []
    lista_de_utilizadores = []

    while True:
        print("""
        ==================================
        QUE ESPETÁCULO - Venda de Bilhetes                     
        ==================================
        ne - novo espetáculo       
        nu - novo utilizador      
        nb - novo bilhete         
        le - listar espetáculos
        lu - listar utilizadores
        lb - listar bilhetes
        cb - comprar bilhete
        
        g - guardar dados
        c - carregar dados
        x - sair
        ==================================
        """)
        print("Comando?")
        op = input("> ").lower()

        if op == "x":
            exit()
        elif op == "ne":
            novo_espetaculo = criar_espetaculo()
            lista_de_espetaculos.append(novo_espetaculo)
        elif op == "nu":
            novo_utilizador = cria_novo_utilizador()
            lista_de_utilizadores.append(novo_utilizador)
        elif op == "nb":
            # todo - criar novo bilhete
            pass
        elif op == "le":
            imprime_lista_espetaculos(lista_de_espetaculos)
        elif op == "lu":
            imprime_lista_de_utilizadores(lista_de_utilizadores)
        elif op == "lb":
            # todo - listar bilhetes
            pass
        elif op == "g":
            guardar_dados(lista_de_espetaculos, lista_de_utilizadores)
            pass
        elif op == "c":
            lista_de_espetaculos, lista_de_utilizadores = carregar_dados()
        elif op == "cb":
            # todo - associar um bilhetes a um utilizador
            pass
        elif op == "al":
            pass
            # todo - imprime_lista_de_compras()


def carregar_dados():
    """ Carrega os dados de espetáculos e utilizadores a partir de um ficheiro local

    :return: o conteúdo de ambos ficheiro (depende dos dados guardados)
    """
    lista_de_espetaculos = ler_ficheiro(nome_ficheiro_lista_de_espetaculos)
    lista_de_utilizadores = ler_ficheiro(nome_ficheiro_lista_de_utilizadores)
    return lista_de_espetaculos, lista_de_utilizadores


def guardar_dados(lista_de_espetaculos, lista_de_utilizadores):
    """ Guarda os dados da sessão para carregar numa sessão futura.

    :param lista_de_espetaculos: lista de espetáculos da sessão
    :param lista_de_utilizadores: lista de utilizadores da sessão
    """

    op = input("Os dados nos ficheiros serão sobrepostos. Continuar (S/n)?")
    if op in ['s', 'S', '']:
        guardar_ficheiro(nome_ficheiro_lista_de_utilizadores, lista_de_utilizadores)
    else:
        print("Cancelada.")


if __name__ == "__main__":
    menu()
