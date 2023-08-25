import json
import pytest
from manager import GerenciaDados, AnalisaPedidos

lojas_mock = [{
    "name": "LojaA",
    "per_cent_motoboy": 0.1
}]

pedidos_mock = [{
    "name": "Pedido1",
    "loja": "LojaA",
    "price": 100
}]

motoboys_mock = [{
    "name": "Motoboy1",
    "lojas": [{"name": "LojaA"}],
    "fixed_cost": 50
}]


def mock_open_read(file_name, mode='r', encoding=None):
    class MockFile:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

        def read(self):
            if "lojas.json" in file_name:
                return json.dumps(lojas_mock)
            if "pedidos.json" in file_name:
                return json.dumps(pedidos_mock)
            if "motoboys.json" in file_name:
                return json.dumps(motoboys_mock)

    return MockFile()


@pytest.fixture
def gerencia_dados(mocker):
    mocker.patch('builtins.open', side_effect=mock_open_read)
    gd = GerenciaDados()
    gd.carrega_dados_json()
    return gd


def test_carrega_dados_json(gerencia_dados):
    assert len(gerencia_dados.lojas.lojas) == 1
    assert len(gerencia_dados.pedidos.pedidos) == 1
    assert len(gerencia_dados.motoboys.motoboys) == 1

    assert gerencia_dados.lojas.lojas[0].name == "LojaA"
    assert gerencia_dados.pedidos.pedidos[0].name == "Pedido1"
    assert gerencia_dados.motoboys.motoboys[0].name == "Motoboy1"


def test_escolhe_motoboy(mocker, gerencia_dados):
    analise = AnalisaPedidos()
    analise.lojas = gerencia_dados.lojas
    analise.pedidos = gerencia_dados.pedidos
    analise.motoboys = gerencia_dados.motoboys

    mocker.patch("builtins.input", return_value="0")
    analise.escolhe_motoboy()

    assert analise.motoboy.name == "Motoboy1"


def test_gera_relatorio(capfd, gerencia_dados):
    analise = AnalisaPedidos()
    analise.lojas = gerencia_dados.lojas
    analise.pedidos = gerencia_dados.pedidos
    analise.motoboys = gerencia_dados.motoboys
    analise.motoboy = analise.motoboys.motoboys[0]

    analise.gera_relatorio()

    captured = capfd.readouterr()
    assert "Motoboy: Motoboy1" in captured.out
    assert "Pedido: Pedido1 - Loja: LojaA - Preço: 100" in captured.out
    assert "Valor: R$ 60.0" in captured.out

