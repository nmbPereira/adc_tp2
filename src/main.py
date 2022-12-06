
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
            # todo - criar novo espetáculo
            pass
        elif op == "nu":
            # todo - criar novo utilizador
            pass
        elif op == "nb":
            # todo - criar novo bilhete
            pass
        elif op == "le":
            # todo - listar espetaculos
            pass
        elif op == "lu":
            # todo - listar utilizadores
            pass
        elif op == "lb":
            # todo - listar bilhetes
            pass
        elif op == "g":
            # todo - guardar dados
            pass
        elif op == "c":
            # todo - carregar dados
            pass
        elif op == "cb":
            # todo - associar um bilhetes a um utilizador
            pass
        elif op == "al":
            pass
            # todo - imprime_lista_de_compras()

def carregar_dados():
    # todo
    pass


def guardar_dados(lista_de_veiculos, lista_de_utilizadores):
    # todo
    pass


if __name__ == "__main__":
    menu()
