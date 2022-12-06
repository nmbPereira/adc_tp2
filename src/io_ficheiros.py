"""
Funções de i/o de ficheiros

:Date: 6 Dez 2022
:Version: 0.1
:Authors: Nuno Pereira, Daniel Fordham, Lourenço Albuquerque
"""

import pickle

def ler_ficheiro(ficheiro):
    """ Lê os dados de um ficheiro

    :param ficheiro: nome do ficheiro para ler
    :return: o conteúdo do ficheiro (depende dos dados guardados)
    """
    with open(ficheiro, "rb") as f:
        return pickle.load(f)


def guardar_ficheiro(ficheiro, dados):
    """ Guardar os dados num ficheiro

    :param ficheiro: nome do ficheiro onde vai guardar os dados
    :param dados: dados para guardar
    """
    with open(ficheiro, "wb") as f:
        pickle.dump(dados, f)
