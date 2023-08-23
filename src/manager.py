import json
from models import LojasList, PedidosList, MotoboyList, Lojas, Pedidos, Motoboy
class GerenciaDados:

    def __init__(self):
        self.lojas = None
        self.pedidos = None
        self.motoboys = None

    def carrega_dados_json(self):
        with open("dados/lojas.json", 'r', encoding='utf-8') as file:
            lojas_json = json.load(file)
        with open("dados/pedidos.json", 'r', encoding='utf-8') as file:
            pedidos_json = json.load(file)
        with open("dados/motoboys.json", 'r', encoding='utf-8') as file:
            motoboys_json = json.load(file)

        self.lojas = LojasList(lojas=[Lojas(**loja) for loja in lojas_json])
        self.pedidos = PedidosList(pedidos=[Pedidos(**pedido) for pedido in pedidos_json])
        self.motoboys = MotoboyList(motoboys=[Motoboy(**motoboy) for motoboy in motoboys_json])

    def carrega_dados_sqlite(self):
        pass

class AnalisaPedidos(GerenciaDados):

    def __init__(self):
        super().__init__()
        self.motoboy = None

    def escolhe_motoboy(self):
        print("Escolha um motoboy: ")
        for i, motoboy in enumerate(self.motoboys.motoboys):
            print(f"{i+1} - {motoboy.name}")
        motoboy = int(input("Digite o número correspondente ao motoboy: "))
        self.motoboy = self.motoboys.motoboys[motoboy]

    def gera_relatorio(self):
        print(f"\nMotoboy: {self.motoboy.name}")
        print(f"Motoboy atende as lojas: ")
        for loja in self.motoboy.lojas:
            print(f"  - {loja['name']}")
        print(f"Pedido(s) do motoboy: ")
        comissao = 0
        frete = 0
        for pedido in self.pedidos.pedidos:
            if {"name": pedido.loja} in self.motoboy.lojas:
                print(f"  - Pedido: {pedido.name} - Loja: {pedido.loja} - Preço: {pedido.price}")
                loja = self.lojas.get_loja_by_name(pedido.loja)
                comissao += pedido.price * loja.per_cent_motoboy
                frete += self.motoboy.fixed_cost
        print(f"O Motoboy irá ganhar")
        print(f"  - Valor: R$ {comissao + frete}")
