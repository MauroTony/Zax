from manager import AnalisaPedidos

if __name__ == '__main__':
    analise = AnalisaPedidos()
    analise.carrega_dados_json()
    analise.escolhe_motoboy()
    analise.gera_relatorio()