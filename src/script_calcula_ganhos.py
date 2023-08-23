from manager import AnalisaPedidos

if __name__ == '__main__':
    teste = AnalisaPedidos()
    teste.carrega_dados_json()
    teste.escolhe_motoboy()
    teste.gera_relatorio()